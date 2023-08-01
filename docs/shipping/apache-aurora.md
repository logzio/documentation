---
id: Apache-Aurora
title: Apache Aurora
overview: Collect Aurora metrics using Telegraf
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aurora-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

Apache Aurora is a Mesos framework for long-running services and cron jobs. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Apache Aurora metrics to Logz.io, you need to add the **inputs.aurora** and **outputs.http** plug-ins to your Telegraf configuration file.

## Configuring Telegraf to send your metrics data to Logz.io


### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

### Add the inputs.aurora plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Apache Aurora data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.aurora]]
  ## Schedulers are the base addresses of your Aurora Schedulers
  schedulers = ["http://127.0.0.1:8081"]

  ## Set of role types to collect metrics from.
  ##
  ## The scheduler roles are checked each interval by contacting the
  ## scheduler nodes; zookeeper is not contacted.
  # roles = ["leader", "follower"]

  ## Timeout is the max time for total network operations.
  # timeout = "5s"

  ## Username and password are sent using HTTP Basic Auth.
  # username = "username"
  # password = "pa$$word"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/aurora/README.md)
:::
 

### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
