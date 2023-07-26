---
id: ZFS
title: ZFS
overview: ZFS combines a file system with a volume manager. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['File Systems', 'Storage Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/zfs-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



## Overview

ZFS combines a file system with a volume manager. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format ZFS metrics to Logz.io, you need to add the **inputs.zfs** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the same machine as ZFS

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.zfs plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the ZFS data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.zfs]]
  ## ZFS kstat path. Ignored on FreeBSD
  ## If not specified, then default is:
  # kstatPath = "/proc/spl/kstat/zfs"

  ## By default, telegraf gather all zfs stats
  ## Override the stats list using the kstatMetrics array:
  ## For FreeBSD, the default is:
  # kstatMetrics = ["arcstats", "zfetchstats", "vdev_cache_stats"]
  ## For Linux, the default is:
  # kstatMetrics = ["abdstats", "arcstats", "dnodestats", "dbufcachestats",
  #     "dmu_tx", "fm", "vdev_mirror_stats", "zfetchstats", "zil"]

  ## By default, don't gather zpool stats
  # poolMetrics = false

  ## By default, don't gather dataset stats
  # datasetMetrics = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/zfs/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
