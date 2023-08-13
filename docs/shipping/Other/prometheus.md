---
id: Prometheus
title: Prometheus
overview: This project lets you send Prometheus-format logs, metrics and traces to Logz.io.
product: ['metrics', 'logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mascot-telegraf.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['32X5zm8qW7ByLlp1YPFkrJ']
metrics_alerts: []
---



This project lets you configure a Telegraf agent to send your collected Prometheus-format metrics to Logz.io.

## Overview

Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

To send your Prometheus-format metrics to Logz.io, you add the **outputs.http** plug-in to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["32X5zm8qW7ByLlp1YPFkrJ"] -->

#### Configure Telegraf to send your metrics data to Logz.io



##### Set up Telegraf v1.17 or higher:

**Ubuntu & Debian**

```shell
sudo apt-get update && sudo apt-get install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**RedHat and CentOS**

```shell
sudo yum install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**SLES & openSUSE**

```shell
# add go repository
zypper ar -f obs://devel:languages:go/ go
# install latest telegraf
zypper in telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**FreeBSD/PC-BSD**

```shell
sudo pkg install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.
##### Add the outputs.http plug-in

After you create a config file for Telegraf, configure the output plug-in to enable your data to be sent to Logz.io in Prometheus-format and add the following code to the configuration file:


``` yaml
[[outputs.http]]
  url = "https://<<LISTENER-HOST>>:8053"
  data_format = "prometheusremotewrite"
  [outputs.http.headers]
     Content-Type = "application/x-protobuf"
     Content-Encoding = "snappy"
     X-Prometheus-Remote-Write-Version = "0.1.0"
     Authorization = "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
```

{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

:::note
The full list of data scraping and configuring options can be found [here](https://docs.influxdata.com/telegraf/v1.18/plugins/).
:::



##### Check Logz.io for your metrics

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["32X5zm8qW7ByLlp1YPFkrJ"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}





To send your Prometheus application metrics to a Logz.io Infrastructure Monitoring account, use remote write to connect to Logz.io as the endpoint. Your data is formatted as JSON documents by the Logz.io listener.


:::note
**Multiple server environments:**  If you have multiple Prometheus server instances, you'll have to add Logz.io as an endpoint for each instance.
:::



#### Configuring Remote Write to Logz.io



{@include: ../_include/p8s-shipping/remotewrite-syd-userguide-tokens-lookup.html}

##### Add a remote_write url


Configure your Prometheus yaml file or use a Helm chart:

###### To configure a Prometheus yaml file

Add the following parameters to your Prometheus yaml file:

| Environment variable | Description |Required/Default|
|---|---|---|
{@include: ../_include/p8s-shipping/p8s_logzio_name.md}||
{@include: ../_include/p8s-shipping/remotewrite-syd-userguide-values-not-to-show-in-app.html}


```yaml
global:
  external_labels:
    p8s_logzio_name: <labelvalue>
remote_write:
  - url: https://<<LISTENER-HOST>>:8053
    bearer_token: <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    remote_timeout: 30s
    queue_config:
      batch_send_deadline: 5s  #default = 5s
      max_shards: 10  #default = 1000
      min_shards: 1
      max_samples_per_send: 500 #default = 100
      capacity: 10000  #default = 500

```

###### To configure a Helm chart

For [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) Helm chart users:

Edit your chart `values.yaml` file in the following sections:

+ remote write:

```yaml
remoteWrite:
    - url: https://<<LISTENER-HOST>>:8053  # The Logz.io Listener URL for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic.
      bearerToken: <<PROMETHEUS-METRICS-SHIPPING-TOKEN>> # The Logz.io Prometheus metrics account token
      remoteTimeout: 30s
      queueConfig:
        batchSendDeadline: 5s  #default = 5s
        maxShards: 10  #default = 1000
        maxSamplesPerSend: 500 #default = 100
        capacity: 10000  #default = 500
```

+ externalLabels:

```yaml
externalLabels:
  p8s_logzio_name: <labelvalue>
```


##### Verify the remote_write configuration

+ **Run a query**: If you are scraping Prometheus metrics, you can check that the remote_write configuration is working properly by doing one of the following and verifying that the result is greater than zero (n > 0) for the url:

  * Run a query on your local Prometheus interface for the metric `prometheus_remote_storage_samples_in_total`.

  * Check for the metric in the `/metrics` endpoint on your Prometheus server.

+ **Check via Metrics Explore**: To verify that metrics are arriving to Logz,io:
  1. Open Metrics **Explore** via the compass icon in the left menu bar.

  2. Examine the **Metrics** dropdown list below the **Explore** heading in the upper left of the pane. <br />
    An empty list or the text _no metrics_ indicates that the remote write configuration is not working properly.
    ![Verify Prometheus metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/select-metric-query.png)

##### Open Metrics Explore

Once you've verified that your data is available in Logz.io, [explore your Prometheus metrics.](https://docs.logz.io/user-guide/infrastructure-monitoring/metrics-explore-prometheus/)


After your metrics are flowing, [import your existing Prometheus and Grafana dashboards](https://docs.logz.io/user-guide/infrastructure-monitoring/prometheus-importing-dashbds.html) to Logz.io Infrastructure Monitoring as JSON files.



### Performance tips


* **Reduce tagging**: By default, all the metrics from your Prometheus server(s) are sent to Logz.io. To drop or send specific metrics, add Prometheus labeling _before_ enabling the remote write, or as part of the remote write configuration.  Learn more about Prometheus [relabeling tricks here.](https://medium.com/quiq-blog/prometheus-relabeling-tricks-6ae62c56cbda)


* **Metrics metadata dashboards**: If you have both Prometheus & Grafana, you can activate a dashboard as part of the remote write configuration that will show you the queue size and how many metrics you're sending. If your queue size increases, it might be necessary to open an additional channel. _(currently in development)_

* **Tune the remote write process**: Learn more about Prometheus [remote write tuning here.](https://prometheus.io/docs/practices/remote_write/)


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


 




