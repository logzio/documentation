---
id: ClickHouse
title: ClickHouse
overview: ClickHouse is a fast open-source column-oriented database management system that allows generating analytical data reports in real-time using SQL queries. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Database']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/clickhouse.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


ClickHouse is a fast open-source column-oriented database management system that allows generating analytical data reports in real-time using SQL queries. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format ClickHouse metrics to Logz.io, you need to add the **inputs.clickhouse** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.clickhouse plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the ClickHouse data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.clickhouse]]
  ## Username for authorization on ClickHouse server
  ## example: username = "default"
  username = "default"

  ## Password for authorization on ClickHouse server
  ## example: password = "super_secret"

  ## HTTP(s) timeout while getting metrics values
  ## The timeout includes connection time, any redirects, and reading the response body.
  ##   example: timeout = 1s
  # timeout = 5s

  ## List of servers for metrics scraping
  ## metrics scrape via HTTP(s) clickhouse interface
  ## https://clickhouse.tech/docs/en/interfaces/http/
  ##    example: servers = ["http://127.0.0.1:8123","https://custom-server.mdb.yandexcloud.net"]
  servers         = ["http://127.0.0.1:8123"]

  ## If "auto_discovery"" is "true" plugin tries to connect to all servers available in the cluster
  ## with using same "user:password" described in "user" and "password" parameters
  ## and get this server hostname list from "system.clusters" table
  ## see
  ## - https://clickhouse.tech/docs/en/operations/system_tables/#system-clusters
  ## - https://clickhouse.tech/docs/en/operations/server_settings/settings/#server_settings_remote_servers
  ## - https://clickhouse.tech/docs/en/operations/table_engines/distributed/
  ## - https://clickhouse.tech/docs/en/operations/table_engines/replication/#creating-replicated-tables
  ##    example: auto_discovery = false
  # auto_discovery = true

  ## Filter cluster names in "system.clusters" when "auto_discovery" is "true"
  ## when this filter present then "WHERE cluster IN (...)" filter will apply
  ## please use only full cluster names here, regexp and glob filters is not allowed
  ## for "/etc/clickhouse-server/config.d/remote.xml"
  ## <yandex>
  ##  <remote_servers>
  ##    <my-own-cluster>
  ##        <shard>
  ##          <replica><host>clickhouse-ru-1.local</host><port>9000</port></replica>
  ##          <replica><host>clickhouse-ru-2.local</host><port>9000</port></replica>
  ##        </shard>
  ##        <shard>
  ##          <replica><host>clickhouse-eu-1.local</host><port>9000</port></replica>
  ##          <replica><host>clickhouse-eu-2.local</host><port>9000</port></replica>
  ##        </shard>
  ##    </my-onw-cluster>
  ##  </remote_servers>
  ##
  ## </yandex>
  ##
  ## example: cluster_include = ["my-own-cluster"]
  # cluster_include = []

  ## Filter cluster names in "system.clusters" when "auto_discovery" is "true"
  ## when this filter present then "WHERE cluster NOT IN (...)" filter will apply
  ##    example: cluster_exclude = ["my-internal-not-discovered-cluster"]
  # cluster_exclude = []

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/clickhouse/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
