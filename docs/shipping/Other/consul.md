---
id: Hashicorp-Consul-data
title: Hashicorp Consul
overview: This project lets you configure the OpenTelemetry collector to send your Prometheus-format metrics from Hashicorp Consul to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/consul-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


This project lets you configure the OpenTelemetry collector to send your Prometheus-format metrics from Hashicorp Consul to Logz.io.

**Before you begin, you'll need**:

* Consul installed on your host
* Golang



### Update Consul configuration

1. Navigate to the Consul server and create a new file called `prometheus.json` under the Consul config library at `/etc/consul.d.`

2. Add the following telemetry stanza to the `prometheus.json`:

   ```json
   {
     "telemetry": {
       "disable_hostname": true,
       "prometheus_retention_time": "72h"

     }
   }
   ```

### Check the Consul server’s metrics format

Check that the Consul server’s metrics are in Prometheus format at this endpoint:

```
http://127.0.0.1:8500/v1/agent/metrics?format=prometheus
```


### Download OpenTelemetry collector

:::note
If you already have OpenTelemetry, proceed to the next step.
:::


Create a dedicated directory on your host and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml`.

### Configure the receivers

Open the configuration file and make sure that it states the receivers required for your source:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'consul-metrics'
          scrape_interval: 15s
          metrics_path: "/v1/agent/metrics"
          static_configs:
            - targets: ['localhost:8500']
  hostmetrics:
    collection_interval: 1m
    scrapers:
      cpu: ##All execpt Mac
      disk: ##All execpt Mac
      load:
      filesystem:
      memory:
      network:
      process: ##Linux & Windows
```

### Configure the processors


In the same configuration file, add the following to the `processors` section:

```yaml
processors:
  resourcedetection/system:
    detectors: ["system"]
    system:
      hostname_sources: ["os"]
```


### Configure the exporters

In the same configuration file, add the following to the `exporters` section:

```yaml
exporters:
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    target_info:
        enabled: false
``` 

{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Configure the service pipeline

In the `service` section of the configuration file, add the following configuration

```yaml
service:
  pipelines:
    metrics:
      receivers: [prometheus,hostmetrics]
      processors: [resourcedetection/system]
      exporters:
        - prometheusremotewrite
  telemetry:
    logs:
      level: "debug"
```



### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

### Check Logz.io for your metrics

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["4E7r0H6dqvzzCDsbhO4Yi4", "4iO9XKgTZZhzy2tU9Z84Pj", "7pbQAcavNuZXhT3ab9DxIs"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

{@include: ../../_include/log-shipping/otel-filter.md}







