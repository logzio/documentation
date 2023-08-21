---
id: MarkLogic
title: MarkLogic
overview: MarkLogic is a NoSQL database platform that is used in publishing, government, finance and other sectors, with hundreds of large-scale systems in production. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Database']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/marklogic.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



MarkLogic is a NoSQL database platform that is used in publishing, government, finance and other sectors, with hundreds of large-scale systems in production. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format MarkLogic metrics to Logz.io, you need to add the **inputs.marklogic** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.marklogic plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the MarkLogic data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.marklogic]]
  ## Base URL of the MarkLogic HTTP Server.
  url = "http://localhost:8002"

  ## List of specific hostnames to retrieve information. At least (1) required.
  # hosts = ["hostname1", "hostname2"]

  ## Using HTTP Basic Authentication. Management API requires 'manage-user' role privileges
  # username = "myuser"
  # password = "mypassword"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/marklogic/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
