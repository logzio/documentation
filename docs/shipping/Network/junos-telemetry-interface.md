---
id: junos-telemetry-interface
title: Junos Telemetry Interface
overview: Junos Telemetry Interface (JTI) is a push mechanism to collect operational metrics for monitoring the health of a network that has no scaling limitations. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['logs']
os: ['windows', 'linux']
filters: ['Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/juniper.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---



Junos Telemetry Interface (JTI) is a push mechanism to collect operational metrics for monitoring the health of a network that has no scaling limitations. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format JTI OpenConfig Telemetry metrics to Logz.io, you need to add the **inputs.jti_openconfig_telemetry** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configuring Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.jti_openconfig_telemetry plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the JTI OpenConfig Telemetry data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.jti_openconfig_telemetry]]
  ## Type of JTI OpenConfig Telemetry-IP interface.
  ## Can be either "tunnel" or "router".
  # service_type = "tunnel"

  ## Address of the JTI OpenConfig Telemetry-IP interface.
  service_address = "localhost:3671"

  ## Measurement definition(s)
  # [[inputs.jti_openconfig_telemetry.measurement]]
  #   ## Name of the measurement
  #   name = "temperature"
  #   ## Datapoint-Type (DPT) of the JTI OpenConfig Telemetry messages
  #   dpt = "9.001"
  #   ## List of Group-Addresses (GAs) assigned to the measurement
  #   addresses = ["5/5/1"]

  # [[inputs.jti_openconfig_telemetry.measurement]]
  #   name = "illumination"
  #   dpt = "9.004"
  #   addresses = ["5/5/3"]
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/jti_openconfig_telemetry/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
