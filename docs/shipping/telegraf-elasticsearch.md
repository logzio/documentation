---
id: Elasticsearch
title: Elasticsearch
sidebar_position: 1
overview: Elasticsearch is a search engine based on the Lucene library. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



## Overview

Elasticsearch is a search engine based on the Lucene library. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Elasticsearch metrics to Logz.io, you need to add the **inputs.elasticsearch** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Add the inputs.elasticsearch plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Elasticsearch data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.elasticsearch]]
  ## specify a list of one or more Elasticsearch servers
  ## you can add username and password to your url to use basic authentication:
  ## servers = ["http://user:pass@localhost:9200"]
  servers = ["http://localhost:9200"]

  ## Timeout for HTTP requests to the elastic search server(s)
  http_timeout = "5s"

  ## When local is true (the default), the node will read only its own stats.
  ## Set local to false when you want to read the node stats from all nodes
  ## of the cluster.
  local = true

  ## Set cluster_health to true when you want to obtain cluster health stats
  cluster_health = false

  ## Adjust cluster_health_level when you want to obtain detailed health stats
  ## The options are
  ##  - indices (default)
  ##  - cluster
  # cluster_health_level = "indices"

  ## Set cluster_stats to true when you want to obtain cluster stats.
  cluster_stats = false

  ## Only gather cluster_stats from the master node. To work this require local = true
  cluster_stats_only_from_master = true

  ## Indices to collect; can be one or more indices names or _all
  ## Use of wildcards is allowed. Use a wildcard at the end to retrieve index names that end with a changing value, like a date.
  indices_include = ["_all"]

  ## One of "shards", "cluster", "indices"
  ## Currently only "shards" is implemented
  indices_level = "shards"

  ## node_stats is a list of sub-stats that you want to have gathered. Valid options
  ## are "indices", "os", "process", "jvm", "thread_pool", "fs", "transport", "http",
  ## "breaker". Per default, all stats are gathered.
  # node_stats = ["jvm", "http"]

  ## HTTP Basic Authentication username and password.
  # username = ""
  # password = ""

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false

  ## Sets the number of most recent indices to return for indices that are configured with a date-stamped suffix.
  ## Each 'indices_include' entry ending with a wildcard (*) or glob matching pattern will group together all indices that match it, and ## sort them by the date or number after the wildcard. Metrics then are gathered for only the 'num_most_recent_indices' amount of most ## recent indices.
  # num_most_recent_indices = 0
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/elasticsearch/README.md).
:::
 

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
