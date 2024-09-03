---
id: bCache-memory
title: bCache
overview: bCache is a cache in the Linux kernel's block layer, which is used for accessing secondary storage devices. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Memory Caching']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/linux.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


bCache is a cache in the Linux kernel's block layer, which is used for accessing secondary storage devices. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format bCache metrics to Logz.io, you need to add the **inputs.bcache** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher
  
Install Telegraf on the Linux server that you need to collect the bCache metrics from.

{@include: ../../_include/metric-shipping/telegraf-setup.md}


#### Add the inputs.bcache plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the bCache data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.bcache]]
  ## Bcache sets path
  ## If not specified, then default is:
  bcachePath = "/sys/fs/bcache"

  ## By default, Telegraf gather stats for all bcache devices
  ## Setting devices will restrict the stats to the specified
  ## bcache devices.
  bcacheDevs = ["bcache0"]
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/bcache/README.md)
::: 
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
