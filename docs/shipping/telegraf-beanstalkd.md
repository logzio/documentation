---
id: Beanstalkd
title: Beanstalkd
overview: Beanstalkd is a simple, fast work queue. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/beanstalk-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


## Overview

Beanstalkd is a simple, fast work queue. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Beanstalkd metrics to Logz.io, you need to add the **inputs.beanstalkd** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the relevant server

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.beanstalkd plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Beanstalkd data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.beanstalkd]]
  ## Server to collect data from
  server = "localhost:11300"

  ## List of tubes to gather stats about.
  ## If no tubes specified then data gathered for each tube on server reported by list-tubes command
  tubes = ["notifications"]
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/beanstalkd/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
 

 
