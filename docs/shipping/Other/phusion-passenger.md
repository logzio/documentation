---
id: Phusion-Passenger-data
title: Phusion Passenger
overview: Phusion Passenger is a free web server and application server with support for Ruby, Python and Node.js. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/phfusion-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



## Overview

Phusion Passenger is a free web server and application server with support for Ruby, Python and Node.js. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Phusion Passenger metrics to Logz.io, you need to add the **inputs.passenger** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configure Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the Passanger server

{@include: ../../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.Phusion Passenger plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Phusion Passenger data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.passenger]]
  ## Path of passenger-status.
  ##
  ## Plugin gather metric via parsing XML output of passenger-status
  ## More information about the tool:
  ##   https://www.phusionpassenger.com/library/admin/apache/overall_status_report.html
  ##
  ## If no path is specified, then the plugin simply execute passenger-status
  ## hopefully it can be found in your PATH
  command = "passenger-status -v --show=xml"
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/passenger/README.md)
::: 
 

##### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
