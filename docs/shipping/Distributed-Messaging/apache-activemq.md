---
id: Apache-ActiveMQ
title: Apache ActiveMQ
overview: Apache ActiveMQ is an open source message broker with a Java Message Service client. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from various sources.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/activemq-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



Apache ActiveMQ is an open source message broker written in Java together with a full Java Message Service client. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format ActiveMQ metrics to Logz.io, you need to add the **inputs.activemq** and **outputs.http** plug-ins to your Telegraf configuration file.

## Configure Telegraf to send your metrics data to Logz.io

 

### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

### Add the inputs.activemq plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the ActiveMQ data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.activemq]]
  ## ActiveMQ WebConsole URL
  url = "http://127.0.0.1:8161"

  ## Required ActiveMQ Endpoint
  ##   deprecated in 1.11; use the url option
  # server = "192.168.50.10"
  # port = 8161

  ## Credentials for basic HTTP authentication
  # username = "admin"
  # password = "admin"

  ## Required ActiveMQ webadmin root path
  # webadmin = "admin"

  ## Maximum time to receive response.
  # response_timeout = "5s"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/activemq/README.md).
:::
 

### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
