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

Aerospike is a flash-optimized and in-memory open source distributed key value NoSQL database. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Aerospike metrics to Logz.io, you need to add the **inputs.aerospike** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.aerospike plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Aerospike data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.aerospike]]
  ## Aerospike servers to connect to (with port)
  ## This plugin will query all namespaces the aerospike
  ## server has configured and get stats for them.
  servers = ["localhost:3000"]

  # username = "telegraf"
  # password = "pa$$word"

  ## Optional TLS Config
  # enable_tls = false
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## If false, skip chain & host verification
  # insecure_skip_verify = true

  # Feature Options
  # Add namespace variable to limit the namespaces executed on
  # Leave blank to do all
  # disable_query_namespaces = true # default false
  # namespaces = ["namespace1", "namespace2"]

  # Enable set level telemetry
  # query_sets = true # default: false
  # Add namespace set combinations to limit sets executed on
  # Leave blank to do all sets
  # sets = ["namespace1/set1", "namespace1/set2", "namespace3"]

  # Histograms
  # enable_ttl_histogram = true # default: false
  # enable_object_size_linear_histogram = true # default: false

  # by default, aerospike produces a 100 bucket histogram
  # this is not great for most graphing tools, this will allow
  # the ability to squash this to a smaller number of buckets
  # To have a balanced histogram, the number of buckets chosen 
  # should divide evenly into 100.
  # num_histogram_buckets = 100 # default: 10
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/aerospike/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
