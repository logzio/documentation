---
id: Jaeger-data
title: Jaeger
overview: Jaeger is an open-source software that can help you monitor and troubleshoot problems on microservices. Integrate Jaeger with Logz.io to gain more observability into your data, identify if and when issues occur, and resolve them quickly and easily. 
product: ['tracing']
os: ['windows', 'linux']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/jaeger.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Manual configuration

Logz.io recommends that you use OpenTelemetry to gather trace transaction data from your system. Because of its versatility, OpenTelemetry has been widely adopted as the industry standard: OpenTelemetry can be equipped with many additional functionalities, one of which is collecting aggregated trace data. Beyond that, [OpenTelemetry](https://github.com/open-telemetry) is set to be the best production-ready solution going forward.


This integration includes:

* Installing the OpenTelemetry collector with Logz.io exporter on your application host
* Configuring the collector to receive traces from your Jaeger installation and send them to Logz.io

On deployment, your Jaeger instrumentation captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.


### Set up your locally hosted Jaeger installation to send traces to Logz.io

**Before you begin, you'll need**:

* An application instrumented with Jaeger
* An active account with Logz.io


#### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  

After downloading the collector, create a configuration file `config.yaml` with the following parameters:

```yaml
receivers:
  jaeger:
    protocols:
      thrift_compact:
        endpoint: "0.0.0.0:6831"
      thrift_binary:
        endpoint: "0.0.0.0:6832"
      grpc:
        endpoint: "0.0.0.0:14250"
      thrift_http:
        endpoint: "0.0.0.0:14268"



exporters:
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    
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


extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [jaeger]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
{@include: ../../_include/tracing-shipping/tail-sampling.md}

#### Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

#### Run the application

Run the application to generate traces.


#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).

## Troubleshooting

{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}
