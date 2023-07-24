---
id: Youtube
title: Youtube
sidebar_position: 1
overview: Youtube is an online video sharing and social media platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



## Overview

Youtube is an online video sharing and social media platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Youtube metrics to Logz.io, you need to add the **inputs.youtube** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on a machine dedicated to collect your Youtube metrics

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.youtube plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Youtube data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.youtube]]
  ## List of channels to monitor.
  channels = [
    "UCBR8-60-B28hp2BmDPdntcQ",
    "UCnrgOD6G0y0_rcubQuICpTQ"
  ]

  ## YouTube API key.
  # api_key = ""
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/master/CHANGELOG.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
