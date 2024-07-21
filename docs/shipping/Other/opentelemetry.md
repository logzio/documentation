---
id: OpenTelemetry-data
title: OpenTelemetry
overview: OpenTelemetry is a collection of APIs, SDKs, and tools to instrument, generate, collect, and export telemetry data, including logs, metrics, and traces. Logz.io helps you identify anomalies and issues in the data so you can resolve them quickly and easily. 
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/opentelemetry-icon-color.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2Q2f3D9WiUgMIyjlDXi0sA']
metrics_alerts: []
drop_filter: []
---


## Logs


This project lets you configure the OpenTelemetry collector to send your collected logs to Logz.io.

### Configuring OpenTelemetry to send your log data to Logz.io

#### Download OpenTelemetry collector

:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the OpenTelemetry collector that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml`.

#### Configure the Receivers

Open the configuration file and ensure it contains the receivers required to collect your logs.

#### Configure the Exporters

In the same configuration file, add the following to the exporters section:

```yaml
exporters:
  logzio/logs:
    account_token: <<LOGS-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-logs
```

#### Configure the Service Pipeline

In the service section of the configuration file, add the following configuration:

```yaml
service:
  pipelines:
    logs:
      receivers: [<<YOUR-LOG-RECEIVER>>]
      exporters: [logzio/logs]
```

* Replace `<<YOUR-LOG-RECEIVER>>` with the name of your log receiver.

#### Start the Collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to config, adjust the name in the command accordingly.

#### Check Logz.io for Your Logs

Give your data some time to get from your system to ours, then log in to your Logz.io account, and open the appropriate tab or dashboard to view your logs.

## Metrics


This project lets you configure the OpenTelemetry collector to send your collected Prometheus-format metrics to Logz.io.


#### Configuring OpenTelemetry to send your metrics data to Logz.io

##### Download OpenTelemetry collector
  
:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml`.

##### Configure the receivers
  
Open the configuration file and make sure that it states the receivers required for your source.

##### Configure the exporters

In the same configuration file, add the following to the `exporters` section:
  
```yaml  
exporters:
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
      user-agent: logzio-opentelemetry-metrics
    target_info:
        enabled: false
```
  
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

##### Configure the service pipeline
  
In the `service` section of the configuration file, add the following configuration
  
```yaml
service:
  pipelines:
    metrics:
      receivers: [<<YOUR-RECEIVER>>]
      exporters: [prometheusremotewrite]
```
* Replace `<<YOUR_RECEIVER>>` with the name of your receiver.



##### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


## Traces

Deploy this integration to send traces from your OpenTelemetry installation to Logz.io.

## Manual configuration

This integration includes:

* Configuring the OpenTelemetry collector to receive traces from your OpenTelemetry installation and send them to Logz.io

On deployment, your OpenTelemetry instrumentation captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

### Set up your locally hosted OpenTelemetry installation to send traces to Logz.io

**Before you begin, you'll need**:

* An active account with Logz.io

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


#### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

{@include: ../../_include/tracing-shipping/tail-sampling.md}


If you already have an OpenTelemetry installation, add the following parameters to the configuration file of your existing OpenTelemetry collector:

* Under the `exporters` list

```yaml
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-traces
```

* Under the `service` list:

```yaml
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

An example configuration file looks as follows:

{@include: ../../_include/tracing-shipping/collector-config.md}

#### Instrument the application

If your application is not yet instrumented, instrument the code as described in our [tracing documents](https://docs.logz.io/shipping/#tracing-sources).


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

### Set up your OpenTelemetry installation using containerized collector to send traces to Logz.io

**Before you begin, you'll need**:

* An active account with Logz.io


#### Instrument the application

If your application is not yet instrumented, instrument the code as described in our [tracing documents](https://docs.logz.io/shipping/#tracing-sources).


{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

#### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the application to generate traces.


#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


### Troubleshooting

{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

