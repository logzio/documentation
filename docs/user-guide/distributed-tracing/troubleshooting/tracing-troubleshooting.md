---
sidebar_position: 1
title: Distributed Tracing Troubleshooting
description: Common questions and use cases when setting up your Logz.io tracing account
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, trace dashboard, dashboard, troubleshoot, logs, observability, distributed tracing]
slug: /distributed-tracing/troubleshooting/tracing-troubleshooting/
---


Setting up a Distributed Tracing account might require some additional help. In this doc, we'll walk through troubleshooting some common issues. 

## Post install troubleshooting

There are a few common issues that may prevent data from reaching Logz.io. Use the following checklist to validate your setup:

**1. No traces showing in the UI**

Even if installation succeeded, you might not see any trace data. To troubleshoot:

* Confirm that your application is sending traces to the correct collector endpoint.

* Check the collector/agent logs for connection errors or dropped spans.

* Ensure that the correct token is configured for the tracing account.

**2. Missing service or operation names**

If the UI doesn’t show services or operations in the dropdown menus:

* Restart the collector to re-send metadata (especially in OTEL setups).

* Verify that your instrumentation sets the service.name resource attribute.

* Search for recent trace logs in Open Search Dashboards to confirm data is reaching Logz.io.

**3. Metrics dashboards showing "No data"**

If you’re using Service Performance Monitoring and dashboards show no results:

* Make sure your metrics account is configured to receive tracing-related metrics (like `calls_total`).

* Confirm that the collector is configured to export metrics as well as traces.

**4. Use debug mode to test setup**

If you’re still unsure whether trace data is being collected:

* Temporarily enable a debug exporter in your collector config to log incoming spans locally.

* Run a trace from your application and check the collector output.

This can help confirm that data is generated and received before reaching Logz.io.

**5. Missing data after installing the chart**

If you've installed the Logz.io Helm chart for tracing but no data appears in the UI:

* Check that the collector pods are running and healthy.

* Ensure your instrumented applications are correctly configured to send traces to the OTLP endpoint exposed by the chart (e.g., `otel-collector.monitoring.svc.cluster.local:4317`).

* Verify that your token and endpoint are set correctly in your app’s environment variables.

* Use the debug exporter to confirm data is reaching the collector.

## Routing data to the collector

When Tracing data doesn't appear in your account, one of the most common root causes is misconfigured instrumentation or data not reaching the collector. Before diving into deeper debugging steps, it’s important to verify that your application is correctly set up to export tracing data.

Your instrumented application needs to send telemetry data (traces, metrics, or logs) to the OpenTelemetry Collector using the OTLP protocol.

Set environment variables to configure the destination collector and other tracing options.

If your collector runs on the same host or as a sidecar, set the OTLP endpoint to localhost:

```shell
ENV OTEL_TRACES_SAMPLER=always_on
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
ENV OTEL_RESOURCE_ATTRIBUTES="service.name=<SERVICE_NAME>"
```

If you're running your app on ECS, define the environment variables in your task definition:

```json
"environment": [
  {
    "name": "OTEL_TRACES_SAMPLER",
    "value": "always_on"
  },
  {
    "name": "OTEL_EXPORTER_OTLP_ENDPOINT",
    "value": "http://localhost:4317"
  },
  {
    "name": "OTEL_RESOURCE_ATTRIBUTES",
    "value": "service.name=<SERVICE_NAME>"
  }
]
```

Replace <SERVICE_NAME> with the name you want to appear in the Tracing UI.


If the collector runs in another service or namespace, set the OTLP endpoint to its DNS or internal IP:

```shell
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector.monitoring.svc.cluster.local:4317"
```

Make sure the collector is reachable and exposes the OTLP receiver on that port.


## Debug mode for instrumentation and collector

To enable debug mode for Opentelemetry Operator, add the `OTEL_LOG_LEVEL` environment variable with value `DEBUG`.

### Enable debug mode for a single pod
To enable debug mode for a specific pod, add the following environment variable directly to its spec:

```yaml
spec:
  template:
    spec:
      containers:
        - name: "<CONTAINER_NAME>"
          env:
          - name: OTEL_LOG_LEVEL
            value: "debug"
```

### Enable debug mode for all instrumented pods
To apply debug mode to all pods instrumented by the OpenTelemetry Operator, update your Logz.io Helm chart with the following configuration, replacing <APP_LANGUAGE> with your application's programming language:

```yaml
instrumentation:
  <APP_LANGUAGE>:
    extraEnv:
    - name: OTEL_LOG_LEVEL
      value: "debug"
```

:::tip
`<APP_LANGUAGE>` can be one of `dotnet`, `java`, `nodejs` or `python`.
:::

:::caution
Enabling debug mode generates highly verbose logs. It is recommended to apply it per pod and not for all pods.
:::

### Debugging with the Collector

To troubleshoot data routing issues in your OpenTelemetry Collector, you can use the built-in debug exporter. This exporter prints telemetry data directly to the console or logs, making it easy to validate what the collector is receiving.

To enable it, add this to your Collector config:

```yaml
exporters:
  debug:
    verbosity: detailed  # or: basic, normal
    sampling_initial: 5
    sampling_thereafter: 200
```

Then attach it to the relevant pipeline:

```yaml
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [debug]
```

With verbosity: `detailed`, you'll get full trace/span info, which is useful to check attributes like `service.name`, `trace ID`, `span.kind`, and verify routing logic.

This debug output is for local validation only and not intended for production.

For more, see [OpenTelemetry Collector Debug Exporter](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.111.0/exporter/debugexporter/README.md).


## Distributed Tracing is not showing data in Service/Operations dropdown lists

You’ve logged into your Distributed Tracing search screen, and you can’t see any data in Service and Operation lists.

![No service or operation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/no-service-or-operation.png)

Several scenarios can cause this:


### Account token misconfiguration in OTEL collector

Distributed Tracing spans are sent to Logz.io and indexed in a Distributed Tracing account the same way as logs. If the spans are sent as expected, you should be able to see them in Open Search Dashboards, the same way you search for logs.

To troubleshoot this issue, you first need to verify that the Tracing account has indexed the data.

Navigate to [Open Search Dashboards](https://app.logz.io/#/dashboard/osd) > Choose the **Tracing account you’re trying to troubleshoot**, and hit the Refresh button on the right side of the screen.

![Logs showing tracing data](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace-and-refresh-in-logs.png)

If there are no results and you can't see any logs, you’ll need to ensure the correct token is used to send the spans.

Head over to **[Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) > [Data shipping tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) > [Tracing](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing)**. Copy the token of the Tracing account you’re troubleshooting, re-configure your collector or make sure it matches, and restart the collector.

Head back to **[Open Search Dashboards](https://app.logz.io/#/dashboard/osd)** and check whether you can now see logs in the Tracing account you're trying to troubleshoot.

If you still can't see any logs, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.

Once your logs appear in Open Search Dashboards, navigate to **Distributed Tracing > [Search](https://app.logz.io/#/dashboard/jaeger/)**.

If there's no data in the Service/Operation dropdown lists, continue to the next step:

### Lost Service and Operation data

Service and Operation data reach Logz.io separately from your spans. That's why you might see data in your Tracing account in Open Search Dashboards (as explained in the previous step), but you won't be able to see data in your Service and Operation lists.

**Restart your collector** to recover this lost data and make sure spans are flowing into your account.

After restarting the collector, navigate back to **Distributed Tracing > [Search](https://app.logz.io/#/dashboard/jaeger/)** and verify that you can see the data in both the Service and Operation dropdown lists.

If you still can't see data in the Service and Operation lists, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.

### Distributed Tracing Search screen not showing search results

When you're trying to search any combination of parameters in **[Distributed Tracing > Search](https://app.logz.io/#/dashboard/jaeger/),** and the search screen does not yield any results, follow these steps to resolve the issue:

**1.** Make sure only **Service**, **Loopback**, and **Limit Results** fields have values, while Tags, Max Duration, and Min Duration are empty.
  ![Service field value](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/just-these-fields-jaeger.png)

**2.** If you still can't see any results, navigate to **[Open Search Dashboards](https://app.logz.io/#/dashboard/osd)** > Choose the **Tracing account you’re trying to troubleshoot**, and check whether you can see logs in the Tracing account you're trying to troubleshoot.

**3.** If you can't see any logs, follow the previous steps to check the token configuration. 

**4.** If you can see logs, make sure their indicated type is jaegerSpan:

  ![Trace logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace-fields-log.png)

**5.** If you still can’t see any search results after following all of these steps, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.



## Service Performance Monitoring dashboard showing no data

Your Service Performance Monitoring dashboard shows a **No Data** message across all elements in your dashboard.

![Query of Metrics account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/spm-no-data-showing.png)

This occurs when the Metrics account attached to the Tracing data is not receiving any data. It’s possible you have not completed the collector configuration changes required to operate your Service Performance Monitoring dashboard.

Let's verify this. Navigate to **[Metrics](https://app-uk.logz.io/#/dashboard/metrics) > [Explore](https://app.logz.io/#/dashboard/metrics/explore)** and choose the relevant data source connected to your Service Performance Monitoring dashboard from the dropdown list.

To confirm that the data is available and accessible, type `calls_total` and run the query.

![Query of calls total](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/calls-total-tracing.png)


If you can see the query's results, but the data is not visible in your Service Performance Monitoring dashboard, contact the [Logz.io Support team](mailto:help@logz.io) for additional help.