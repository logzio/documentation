---
id: OpenLLMetry-data
title: OpenLLMetry
overview: OpenLLMetry by Traceloop is an open source set of OpenTelemetry instrumentations for LLM applications. Use it to send traces of your LLM and vector database calls - prompts, completions, token usage and latency - to Logz.io.
product: ['tracing','metrics','logs']
os: ['windows', 'linux', 'mac']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/traceloop.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

OpenLLMetry instruments your LLM application with OpenTelemetry and emits standard OTLP data. To send it to Logz.io, point the Traceloop SDK at an OpenTelemetry collector and configure the collector with the Logz.io exporters.

**Before you begin, you'll need**:

* An LLM application (OpenAI, Anthropic, LangChain, LlamaIndex, and [more](https://www.traceloop.com/docs/openllmetry/introduction))
* An active Logz.io account
* Port `4318` available on the collector host

## Instrument your application

Follow the Traceloop installation guide for your language:

| Language | Guide |
|---|---|
| Python | [Getting started with Python](https://www.traceloop.com/docs/openllmetry/getting-started-python) |
| Node.js | [Getting started with Node.js](https://www.traceloop.com/docs/openllmetry/getting-started-ts) |
| Next.js | [Getting started with Next.js](https://www.traceloop.com/docs/openllmetry/getting-started-nextjs) |
| Go | [Getting started with Go](https://www.traceloop.com/docs/openllmetry/getting-started-go) |
| Ruby | [Getting started with Ruby](https://www.traceloop.com/docs/openllmetry/getting-started-ruby) |

## Point the SDK at your collector

Set the following environment variables for your application:

```shell
export TRACELOOP_BASE_URL=http://<<COLLECTOR-HOST>>:4318
```

If your SDK supports it, you can also send prompts and completions as log events:

```shell
export TRACELOOP_LOGGING_ENABLED=true
```

* Replace `<<COLLECTOR-HOST>>` with the hostname of the OpenTelemetry collector, for example `localhost`.
* The service name shown in Logz.io comes from the SDK's `app_name` (`appName` in Node.js) initialization option. See the [Traceloop configuration options](https://www.traceloop.com/docs/openllmetry/configuration).


## Download and configure the OpenTelemetry collector

Create a dedicated directory on the collector host and download the [OpenTelemetry collector contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases) for your operating system.

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::

Create a `config.yaml` file with the following content:

```yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        },
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }
      ]

exporters:
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-traces
  logzio/logs:
    account_token: <<LOG-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-logs
  prometheusremotewrite/logzio:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
      user-agent: logzio-opentelemetry-metrics
    target_info:
      enabled: false

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [logzio/logs]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheusremotewrite/logzio]
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.md}
* Replace `<<LOG-SHIPPING-TOKEN>>` with the [log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping) of the account you want to ship to.
* Replace `<<LISTENER-HOST>>` with the Logz.io listener URL [for your region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).
* Replace `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` with a [token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/) for the metrics account you want to ship to.

:::tip
Not every OpenLLMetry SDK emits all three signals. Check your SDK's guide and the [Traceloop configuration options](https://www.traceloop.com/docs/openllmetry/configuration) for what it exports, and remove any pipeline you don't need.
:::

#### Tail sampling

{@include: ../../_include/tracing-shipping/tail-sampling.md}

## Start the collector

{@include: ../../_include/tracing-shipping/collector-run.md}

To run the collector in Docker instead, mount the configuration file:

```shell
docker run \
-p 4318:4318 \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
otel/opentelemetry-collector-contrib:0.111.0
```

* Replace `<PATH-TO>` with the path to the `config.yaml` file on your system.

{@include: ../../_include/tracing-shipping/collector-run-note.md}

## View your data in Logz.io

Run your LLM application to generate some data, then give it time to process:

* **Traces** appear in your [Tracing](https://app.logz.io/#/dashboard/jaeger) dashboard. Each LLM call is a span, with the model, prompt, completion and token usage as span attributes.
* **Metrics** appear in your [Metrics](https://app.logz.io/#/dashboard/metrics/) dashboard, under metric names starting with `gen_ai.` and `db.`.
* **Logs** appear in [Explore](https://app.logz.io/#/dashboard/explore).
