---
id: apache-couchdb 
title: Apache CouchDB 
overview: Apache CouchDB is an open-source document-oriented NoSQL database, implemented in Erlang. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/couchdb.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


## Overview

Apache CouchDB is an open-source document-oriented NoSQL database, implemented in Erlang. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format CouchDB metrics to Logz.io, you need to add the **inputs.couchdb** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Add the inputs.couchdb plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the CouchDB data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.couchdb]]
  ## Works with CouchDB stats endpoints out of the box
  ## Multiple Hosts from which to read CouchDB stats:
  hosts = ["http://localhost:8086/_stats"]

  ## Use HTTP Basic Authentication.
  # basic_username = "telegraf"
  # basic_password = "p@ssw0rd"
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/couchdb/README.md).
:::
 

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
