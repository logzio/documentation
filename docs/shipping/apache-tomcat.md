---
id: Apache-Tomcat
title: Apache Tomcat
overview: test
product: ['metrics']
os: ['windows', 'linux']
filters: ['Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/tomcat-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ["1QIverGwIdtlC5ZbKohyvj", "6J2RujMalRK3oC4y0r88ax"]
metrics_alerts: []
---


## Overview

Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Apache Tomcat metrics to Logz.io, you need to add the **inputs.tomcat** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["1QIverGwIdtlC5ZbKohyvj", "6J2RujMalRK3oC4y0r88ax"] -->

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.tomcat plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Apache Tomcat data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.tomcat]]
  ## URL of the Tomcat server status
  # url = "http://127.0.0.1:8080/manager/status/all?XML=true"

  ## HTTP Basic Auth Credentials
  # username = "tomcat"
  # password = "s3cret"

  ## Request timeout
  # timeout = "5s"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/tomcat/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}
  
##### Check Logz.io for your metrics

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1QIverGwIdtlC5ZbKohyvj", "6J2RujMalRK3oC4y0r88ax"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 

 
