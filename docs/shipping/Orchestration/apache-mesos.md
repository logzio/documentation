---
id: Apache-Mesos-orchestration
title: Apache Mesos
overview: Apache Mesos is an open-source project to manage computer clusters.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mesos-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Apache Mesos is an open-source project to manage computer clusters. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Apache Mesos metrics to Logz.io, you need to add the **inputs.mesos** and **outputs.http** plug-ins to your Telegraf configuration file.

## Configure Apache Mesos to send metrics to Logz.io

 

### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}

### Add the inputs.mesos plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Apache Mesos data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.mesos]]
  ## Timeout, in ms.
  timeout = 100

  ## A list of Mesos masters.
  masters = ["http://localhost:5050"]

  ## Master metrics groups to be collected, by default, all enabled.
  master_collections = [
    "resources",
    "master",
    "system",
    "agents",
    "frameworks",
    "framework_offers",
    "tasks",
    "messages",
    "evqueue",
    "registrar",
    "allocator",
  ]

  ## A list of Mesos slaves, default is []
  # slaves = []

  ## Slave metrics groups to be collected, by default, all enabled.
  # slave_collections = [
  #   "resources",
  #   "agent",
  #   "system",
  #   "executors",
  #   "tasks",
  #   "messages",
  # ]

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/mesos/README.md).
::: 
 

### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
