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


This project helps you configure the OpenTelemetry collector to send your logs to Logz.io.

### Sending OpenTelemetry Logs to Logz.io

#### Download OpenTelemetry collector

:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the relevant OpenTelemetry collector for your host operating system.

Create a configuration file `config.yaml`.



#### Configure Receivers

Ensure your `config.yaml` file includes the necessary receivers to collect your logs.

#### Configure Exporters

Add the following to the exporters section of your `config.yaml`:


```yaml
exporters:
  logzio/logs:
    account_token: <<LOGS-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-logs
```

#### Configure Service Pipeline

In the service section of your `config.yaml`, add:


```yaml
service:
  pipelines:
    logs:
      receivers: [<<YOUR-LOG-RECEIVER>>]
      exporters: [logzio/logs]
```

* Replace `<<YOUR-LOG-RECEIVER>>` with the name of your log receiver.

#### Start the Collector

Run:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to config, adjust the name in the command accordingly.

#### View your logs

Allow some time for data ingestion, then open Logz.io to view your logs.



## Metrics


This project helps you configure the OpenTelemetry collector to send your metrics to Logz.io.


### Sending OpenTelemetry Metrics to Logz.io

#### Download OpenTelemetry collector
  
:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the relevant [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) for your host operating system.

Create a configuration file `config.yaml`.

#### Configure receivers
  
Ensure your `config.yaml` file includes the necessary receivers for your source.

#### Configure exporters

Add the following to the `exporters` section of your `config.yaml`:
  
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

#### Configure service pipeline
  
In the `service` section of your `config.yaml`, add:
  
```yaml
service:
  pipelines:
    metrics:
      receivers: [<<YOUR-RECEIVER>>]
      exporters: [prometheusremotewrite]
```
* Replace `<<YOUR_RECEIVER>>` with the name of your receiver.



#### Start the collector

Run:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

#### View your metrics


Allow some time for data ingestion, then open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).




## Traces

This project helps you configure the OpenTelemetry collector to send your traces to Logz.io.



## Manual configuration

On deployment, your OpenTelemetry instrumentation captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

**Before you begin, you'll need**:

* An active Logz.io account

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  
 

### Download and configure OpenTelemetry collector

Create a directory on your application's host and download the relevant [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) for your host operating system

Create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

{@include: ../../_include/tracing-shipping/tail-sampling.md}


If you already have an OpenTelemetry installation, add the following to the configuration file of your existing OpenTelemetry collector:

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

Example configuration file:

{@include: ../../_include/tracing-shipping/collector-config.md}

### Optional: Configure Span Metrics Collection

Span metrics collection is disabled by default. To enable it, add & modify the following sections in the `config.yaml` OpenTelemetry configuration.
Replace `<<ENV-ID>>` with the envrionment for filteration in App360, `<<LISTENER-HOST>>` with the Logz.io metrics listener URL and `<<METRICS-SHIPPING-TOKEN>>` with your Logz.io SPM metrics account token.
```yaml
  connectors:
    spanmetrics:
      aggregation_temporality: AGGREGATION_TEMPORALITY_CUMULATIVE
      dimensions:
      - name: rpc.grpc.status_code
      - name: http.method
      - name: http.status_code
      - name: cloud.provider
      - name: cloud.region
      - name: db.system
      - name: messaging.system
      - default: <<ENV-ID>>
        name: env_id
      dimensions_cache_size: 100000
      histogram:
        explicit:
          buckets:
          - 2ms
          - 8ms
          - 50ms
          - 100ms
          - 200ms
          - 500ms
          - 1s
          - 5s
          - 10s
      metrics_expiration: 5m
      resource_metrics_key_attributes:
      - service.name
      - telemetry.sdk.language
      - telemetry.sdk.name
    servicegraph:
      latency_histogram_buckets: [2ms, 8ms, 50ms, 100ms, 200ms, 500ms, 1s, 5s, 10s]
      dimensions:
        - env_id
      store:
        ttl: 5s
        max_items: 100000
  processors:
    # Rename metrics and labels to match Logz.io's requirements
    metricstransform/metrics-rename:
      transforms:
      - include: ^duration(.*)$$
        action: update
        match_type: regexp
        new_name: latency.$${1} 
      - action: update
        include: calls
        new_name: calls_total
    metricstransform/labels-rename:
      transforms:
      - action: update
        include: ^latency
        match_type: regexp
        operations:
        - action: update_label
          label: span.name
          new_label: operation
      - action: update
        include: ^calls
        match_type: regexp
        operations:
        - action: update_label
          label: span.name
          new_label: operation  
  exporters:
    prometheusremotewrite/spm-logzio:
      endpoint: https://<<LISTENER-HOST>>:8053
      headers:
        Authorization: Bearer <<METRICS-SHIPPING-TOKEN>> # Metrics account token for span metrics
        user-agent: "logzio-opentelemetry-apm"
      timeout: 30s
      add_metric_suffixes: false
  service:
    pipelines:
      extensions: [health_check, pprof, zpages]
      traces:
        receivers: [otlp]
        processors: [tail_sampling, batch]          
        exporters: [logzio/traces, servicegraph, spanmetrics]
      metrics/spm-logzio:
        receivers: [spanmetrics, servicegraph]
        processors: [metricstransform/metrics-rename, metricstransform/labels-rename, batch]
        exporters: [prometheusremotewrite/spm-logzio]
```
### Instrument the application

If your application isn't instrumented, begin by downloading the OpenTelemetry agent or library specific to your programming language. Logz.io supports popular open-source instrumentation libraries, including OpenTracing, Jaeger, OpenTelemetry, and Zipkin. Attach the agent, set up the necessary configuration options, and start your application. The agent will automatically instrument your application to capture telemetry data.



### Start the collector

Run:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

And run the application to generate traces.


### View your traces

Allow some time for data ingestion, then open your [Tracing](https://app.logz.io/#/dashboard/jaeger) account.


## Configure OpenTelemetry with a Containerized Collector

**Before you begin, you'll need**:

* An active Logz.io account


#### Instrument the application

If your application isn't instrumented, begin by downloading the OpenTelemetry agent or library specific to your programming language. Logz.io supports popular open-source instrumentation libraries, including OpenTracing, Jaeger, OpenTelemetry, and Zipkin. Attach the agent, set up the necessary configuration options, and start your application. The agent will automatically instrument your application to capture telemetry data.

{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the application to generate traces.


### View your traces

Allow some time for data ingestion, then open your [Tracing](https://app.logz.io/#/dashboard/jaeger) account.



{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}
