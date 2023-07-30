---
id: Telegraf-Windows-services
title: Telegraf Windows Services
overview: Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows']
filters: ['Monitoring Tools', 'Data Collection']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


## Overview

Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Windows Services metrics to Logz.io, you need to add the **inputs.win_services** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

```shell
wget https://dl.influxdata.com/telegraf/releases/telegraf-1.19.2_windows_amd64.zip
```

After downloading the archive, extract its content into `C:\Program Files\Logzio\telegraf\`.

The configuration file is located at `C:\Program Files\Logzio\telegraf\`.
  
##### Add the inputs.win_services plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Windows Services data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.win_services]]
  ## Names of the services to monitor. Leave empty to monitor all the available services on the host. Globs accepted.
  service_names = [
    "LanmanServer",
    "TermService",
    "Win*",
  ]
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/win_services/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

```shell
telegraf.exe --service start
```

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
