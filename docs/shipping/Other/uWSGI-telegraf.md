---
id: uWSGI-data
title: uWSGI
overview: uWSGI is a software application that aims at developing a full stack for building hosting services. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/uwsgi-logo1.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



uWSGI is a software application that aims at developing a full stack for building hosting services. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format uWSGI metrics to Logz.io, you need to add the **inputs.uwsgi** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher on the same maching as uWSGI

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.uwsgi plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the uWSGI data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.uwsgi]]
  ## List with urls of uWSGI Stats servers. Url must match pattern:
  ## scheme://address[:port]
  ##
  ## For example:
  ## servers = ["tcp://localhost:5050", "http://localhost:1717", "unix:///tmp/statsock"]
  servers = ["tcp://127.0.0.1:1717"]

  ## General connection timeout
  # timeout = "5s"
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/uwsgi/README.md)
::: 
 

#### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
