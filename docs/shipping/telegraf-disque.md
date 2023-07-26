---
id: Disque
title: Disque
overview: Disque is a distributed message broker. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/disque-telegraf.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



## Overview

Disque is a distributed message broker. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Disque metrics to Logz.io, you need to add the **inputs.disque** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Add the inputs.disque plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Disque data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.disque]]
  ## An array of URI to gather stats about. Specify an ip or hostname
  ## with optional port and password.
  ## ie disque://localhost, disque://10.10.3.33:18832, 10.0.0.1:10000, etc.
  ## If no servers are specified, then localhost is used as the host.
  servers = ["localhost"]
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/disque/README.md).
:::
 

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
