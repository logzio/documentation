---
id: Prometheus-Te;egraf
title: Prometheus metrics over Telegraf
sidebar_position: 1
overview: This project lets you configure a Telegraf agent to send your collected Prometheus-format metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
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

#### Configuring Telegraf to send your metrics data to Logz.io



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




