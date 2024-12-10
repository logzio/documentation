---
sidebar_position: 4
title: Traces in Explore
description: View and investigate distributed traces directly in Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, trace, traces, explore, traces in explore, log analysis, observability]
---


Trace View lets you to view and analyze distributed traces directly in Explore, offering a comprehensive understanding of your system's activity. It helps correlate logs with traces to identify bottlenecks, pinpoint errors, and understand your application's complete execution path. 

## Configure Trace view

To enable Trace View in Explore, you’ll need:

* An active Logz.io Tracing account.
* A `traceID` or `trace_id` value for all traces. Most OpenTelemetry compliant tracing libraries automatically include traceID or trace_id. Use Logz.io’s collector to send your traces.
* A `trace_id` value for all **logs correlated with traces**. Most OpenTelemetry compliant logging libraries automatically include trace context feature to populate it. Use Logz.io’s SDKs to send your trace context propagated logs.


:::note
Logs and traces are correlated using the `traceID`or `trace_id` fields. Make sure these fields have the same value in both logs and traces for proper integration with trace context.
:::

After configuring your logs and traces, expand a log entry in Explore to verify that the Trace tab displays the associated trace data.

Supported integrations for Trace context:

* [.NET](https://docs.logz.io/docs/shipping/Code/dotnet/#add-trace-context-1)
* [Python](https://docs.logz.io/docs/shipping/Code/Python/#trace-context)

Additional integrations will be available in future updates.


## Viewing Traces in Explore

Navigate to [Explore](https://app.logz.io/#/dashboard/explore) and select accounts that include tracing data.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/tracing-account-dec9.png" alt="tracing-accounts" width="500"/>

Expand a log entry. The Trace tab will appear alongside the Log tab. If the log is correlated with a trace, the Trace tab displays trace data, including spans, service names, and durations. Click on a span within the trace to view the corresponding log data directly within the same interface.

![open trace view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/trace-view-dec9.png)


## Best practices for using Trace view

* **Maintain Consistent Trace IDs**: Ensure trace_id is propagated consistently across all services.

* **Optimize Logging**: Avoid logging excessive trace data to minimize noise.

* **Validate Regularly**: Periodically confirm that logs and traces are correctly linked in the Trace View tab.


For further assistance, contact our [support team](mailto:help@logz.io).