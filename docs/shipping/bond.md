---
id: Bond
title: Bond
overview: This integration allows you to collects metrics from all bond interfaces in your network. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/bond-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


This integration allows you to collects metrics from all bond interfaces in your network. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Bond metrics to Logz.io, you need to add the **inputs.bond** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.bond plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Bond data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.bond]]
  ## Sets 'proc' directory path
  ## If not specified, then default is /proc
  host_proc = "/proc"

  ## By default, telegraf gather stats for all bond interfaces
  ## Setting interfaces will restrict the stats to the specified
  ## bond interfaces.
  bond_interfaces = ["bond0", "bond1"]
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/bond/README.md)
:::
 

#### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
