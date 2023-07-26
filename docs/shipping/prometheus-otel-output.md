---
id: Prometheus OpenTelemetry
title: Prometheus-OpenTelemetry
overview: This project lets you configure the OpenTelemetry collector to send your collected Prometheus-format metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/opentelemetry-icon-color.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


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
```
  
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

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


 




