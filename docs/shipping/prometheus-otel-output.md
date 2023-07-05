---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
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


 




