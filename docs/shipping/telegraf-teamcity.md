---
id: TeamCity
title: TeamCity
overview: TeamCity is a general-purpose CI/CD solution that allows the most flexibility for all sorts of workflows and development practices.  Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/TeamCity-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1mdHqslZMi4gXaNCLZo9G1']
metrics_alerts: []
---



## Overview

TeamCity is a general-purpose CI/CD solution that allows the most flexibility for all sorts of workflows and development practices.  Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format TeamCity metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["1mdHqslZMi4gXaNCLZo9G1"] -->

#### Configuring Telegraf to send your metrics data to Logz.io



##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.prometheus plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the TeamCity data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.prometheus]]

  urls = ["https://<TeamCity_server_URL>/app/metrics?experimental=true"]

  ## Optional HTTP Basic Auth Credentials
  username = “<YOUR-USERNAME>”
  password = “<YOUR-PASSWORD>”
```

* Replace `<TeamCity_server_URL>` with the URL of your TeamCity server.
* Replace `<YOUR-USERNAME>` with the user name to your TeamCity server.
* Replace `<YOUR-PASSWORD>` with the password to your TeamCity server.


##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1mdHqslZMi4gXaNCLZo9G1"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}


