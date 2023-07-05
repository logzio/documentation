---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---



## Overview

RavenDB is an open source document-oriented NoSQL designed especially for the .NET/Windows platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format RavenDB metrics to Logz.io, you need to add the **inputs.ravendb** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the Ravendb server

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.Ravendb plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the RavenDB data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.ravendb]]
  ## Node URL and port that RavenDB is listening on
  url = "https://localhost:8080"

  ## RavenDB X509 client certificate setup
  tls_cert = "/etc/telegraf/raven.crt"
  tls_key = "/etc/telegraf/raven.key"

  ## Optional request timeout
  ##
  ## Timeout, specifies the amount of time to wait
  ## for a server's response headers after fully writing the request and 
  ## time limit for requests made by this client
  # timeout = "5s"

  ## List of statistics which are collected
  # At least one is required
  # Allowed values: server, databases, indexes, collections
  #  
  # stats_include = ["server", "databases", "indexes", "collections"]

  ## List of db where database stats are collected
  ## If empty, all db are concerned
  # db_stats_dbs = []

  ## List of db where index status are collected
  ## If empty, all indexes from all db are concerned
  # index_stats_dbs = []
  
  ## List of db where collection status are collected
  ## If empty, all collections from all db are concerned
  # collection_stats_dbs = []
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/ravendb/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
