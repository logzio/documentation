---
id: Synproxy
title: Synproxy
overview: Synproxy is a TCP SYN packets proxy. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/linux.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


Synproxy is a TCP SYN packets proxy. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Synproxy metrics to Logz.io, you need to add the **inputs.synproxy** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}


##### Add the inputs.Synproxy plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Synproxy data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.synproxy]]
  # no configuration
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/synproxy/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

### Start Telegraf  
  
**Linux (sysvinit and upstart installations)**

```shell
sudo service telegraf start
```

**Linux (systemd installations)**

```shell
systemctl start telegraf
```  
  
### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
