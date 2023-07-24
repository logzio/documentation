---
id: Telegraf-tengine
title: Telegraf Tengine
sidebar_position: 1
overview: Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---


## Overview

Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Tengine Web Server metrics to Logz.io, you need to add the **inputs.tengine** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

**Ubuntu & Debian**

```shell
sudo apt-get update && sudo apt-get install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**RedHat and CentOS**

```shell
sudo yum install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**SLES & openSUSE**

```shell
# add go repository
zypper ar -f obs://devel:languages:go/ go
# install latest telegraf
zypper in telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**FreeBSD/PC-BSD**

```shell
sudo pkg install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.
  
  
##### Add the inputs.Tengine Web Server plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Tengine Web Server data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.tengine]]
  ## An array of Tengine reqstat module URI to gather stats.
  urls = ["http://127.0.0.1/us"]

  ## HTTP response timeout (default: 5s)
  # response_timeout = "5s"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/tengine/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

**Linux (sysvinit and upstart installations)**

```shell
sudo service telegraf start
```

**Linux (systemd installations)**

```shell
systemctl start telegraf
```

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
