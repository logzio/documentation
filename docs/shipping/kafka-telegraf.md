---
id: Apache-Kafka
title: Apache Kafka
sidebar_position: 1
overview: Apache Kafka is a distributed event store and stream-processing platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


Apache Kafka is a distributed event store and stream-processing platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

This integration lets you send metrics from your Apache Kafka HTTP server using the JMX to Prometheus exporter connected to Telegraf.

To send your Prometheus-format Apache Kafka metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Setup instructions


**Before you begin, you'll need**:
 Apache Kafka running on your server

 

##### Download the JMX to Prometheus exporter

:::note
Run all commands for this integration from your Apache Kafka directory.
:::
 
  
Navigate to the Kafka directory on your host and run the following command:

```shell
wget https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.16.1/jmx_prometheus_javaagent-0.16.1.jar
```

##### Create a configuration file for the JMX to Prometheus exporter

Navigate to the Kafka directory on your host, create a file named `kafka.yml` with the following content:

```yaml
lowercaseOutputName: true
 
 
rules:
# Special cases and very specific rules
- pattern : kafka.server<type=(.+), name=(.+), clientId=(.+), topic=(.+), partition=(.*)><>Value
 name: kafka_server_$1_$2
 type: GAUGE
 labels:
   clientId: "$3"
   topic: "$4"
   partition: "$5"
- pattern : kafka.server<type=(.+), name=(.+), clientId=(.+), brokerHost=(.+), brokerPort=(.+)><>Value
 name: kafka_server_$1_$2
 type: GAUGE
 labels:
   clientId: "$3"
   broker: "$4:$5"
- pattern : kafka.coordinator.(\w+)<type=(.+), name=(.+)><>Value
 name: kafka_coordinator_$1_$2_$3
 type: GAUGE
 
# Generic per-second counters with 0-2 key/value pairs
- pattern: kafka.(\w+)<type=(.+), name=(.+)PerSec\w*, (.+)=(.+), (.+)=(.+)><>Count
 name: kafka_$1_$2_$3_total
 type: COUNTER
 labels:
   "$4": "$5"
   "$6": "$7"
- pattern: kafka.(\w+)<type=(.+), name=(.+)PerSec\w*, (.+)=(.+)><>Count
 name: kafka_$1_$2_$3_total
 type: COUNTER
 labels:
   "$4": "$5"
- pattern: kafka.(\w+)<type=(.+), name=(.+)PerSec\w*><>Count
 name: kafka_$1_$2_$3_total
 type: COUNTER
 
- pattern: kafka.server<type=(.+), client-id=(.+)><>([a-z-]+)
 name: kafka_server_quota_$3
 type: GAUGE
 labels:
   resource: "$1"
   clientId: "$2"
 
- pattern: kafka.server<type=(.+), user=(.+), client-id=(.+)><>([a-z-]+)
 name: kafka_server_quota_$4
 type: GAUGE
 labels:
   resource: "$1"
   user: "$2"
   clientId: "$3"
 
# Generic gauges with 0-2 key/value pairs
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.+), (.+)=(.+)><>Value
 name: kafka_$1_$2_$3
 type: GAUGE
 labels:
   "$4": "$5"
   "$6": "$7"
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.+)><>Value
 name: kafka_$1_$2_$3
 type: GAUGE
 labels:
   "$4": "$5"
- pattern: kafka.(\w+)<type=(.+), name=(.+)><>Value
 name: kafka_$1_$2_$3
 type: GAUGE
 
# Emulate Prometheus 'Summary' metrics for the exported 'Histogram's.
#
# Note that these are missing the '_sum' metric!
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.+), (.+)=(.+)><>Count
 name: kafka_$1_$2_$3_count
 type: COUNTER
 labels:
   "$4": "$5"
   "$6": "$7"
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.*), (.+)=(.+)><>(\d+)thPercentile
 name: kafka_$1_$2_$3
 type: GAUGE
 labels:
   "$4": "$5"
   "$6": "$7"
   quantile: "0.$8"
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.+)><>Count
 name: kafka_$1_$2_$3_count
 type: COUNTER
 labels:
   "$4": "$5"
- pattern: kafka.(\w+)<type=(.+), name=(.+), (.+)=(.*)><>(\d+)thPercentile
 name: kafka_$1_$2_$3
 type: GAUGE
 labels:
   "$4": "$5"
   quantile: "0.$6"
- pattern: kafka.(\w+)<type=(.+), name=(.+)><>Count
 name: kafka_$1_$2_$3_count
 type: COUNTER
- pattern: kafka.(\w+)<type=(.+), name=(.+)><>(\d+)thPercentile
 name: kafka_$1_$2_$3
 type: GAUGE
 labels:
   quantile: "0.$4"
 
- pattern: 'java.lang<name=([\s\w]+), type=GarbageCollector, key=(\w+)>(.*): (\d+)'
 name: jvm_gc_$3
 labels:
   name: $1
   key: $2
 value: $4
 type: GAUGE
 
- pattern: 'java.lang<name=([\s\w]+), type=GarbageCollector>(.*): (\d+)'
 name: jvm_gc_$2
 labels:
   name: $1
 value: $3
 type: GAUGE
 
- pattern: kafka.log<type=LogFlushStats, name=LogFlushRateAndTimeMs><>Count
 name: kafka_log_log_flush_rate_time
 help: Log flush rate and time (rate in seconds, latency|time in ms)
 type: UNTYPED
 
#kafka.connect:type=app-info,client-id="{clientid}"
#kafka.consumer:type=app-info,client-id="{clientid}"
#kafka.producer:type=app-info,client-id="{clientid}"
- pattern: 'kafka.(.+)<type=app-info, client-id=(.+)><>start-time-ms'
 name: kafka_$1_start_time_seconds
 labels:
   clientId: "$2"
 help: "Kafka $1 JMX metric start time seconds"
 type: GAUGE
 valueFactor: 0.001
- pattern: 'kafka.(.+)<type=app-info, client-id=(.+)><>(commit-id|version): (.+)'
 name: kafka_$1_$3_info
 value: 1
 labels:
   clientId: "$2"
   $3: "$4"
 help: "Kafka $1 JMX metric info version and commit-id"
 type: GAUGE
 
#kafka.producer:type=producer-topic-metrics,client-id="{clientid}",topic="{topic}"", partition="{partition}"
#kafka.consumer:type=consumer-fetch-manager-metrics,client-id="{clientid}",topic="{topic}"", partition="{partition}"
- pattern: kafka.(.+)<type=(.+)-metrics, client-id=(.+), topic=(.+), partition=(.+)><>(.+-total|compression-rate|.+-avg|.+-replica|.+-lag|.+-lead)
 name: kafka_$2_$6
 labels:
   clientId: "$3"
   topic: "$4"
   partition: "$5"
 help: "Kafka $1 JMX metric type $2"
 type: GAUGE
 
#kafka.producer:type=producer-topic-metrics,client-id="{clientid}",topic="{topic}"
#kafka.consumer:type=consumer-fetch-manager-metrics,client-id="{clientid}",topic="{topic}"", partition="{partition}"
- pattern: kafka.(.+)<type=(.+)-metrics, client-id=(.+), topic=(.+)><>(.+-total|compression-rate|.+-avg)
 name: kafka_$2_$5
 labels:
   clientId: "$3"
   topic: "$4"
 help: "Kafka $1 JMX metric type $2"
 type: GAUGE
 
#kafka.connect:type=connect-node-metrics,client-id="{clientid}",node-id="{nodeid}"
#kafka.consumer:type=consumer-node-metrics,client-id=consumer-1,node-id="{nodeid}"
- pattern: kafka.(.+)<type=(.+)-metrics, client-id=(.+), node-id=(.+)><>(.+-total|.+-avg)
 name: kafka_$2_$5
 labels:
   clientId: "$3"
   nodeId: "$4"
 help: "Kafka $1 JMX metric type $2"
 type: UNTYPED
 
#kafka.connect:type=kafka-metrics-count,client-id="{clientid}"
#kafka.consumer:type=consumer-fetch-manager-metrics,client-id="{clientid}"
#kafka.consumer:type=consumer-coordinator-metrics,client-id="{clientid}"
#kafka.consumer:type=consumer-metrics,client-id="{clientid}"
- pattern: kafka.(.+)<type=(.+)-metrics, client-id=(.*)><>(.+-total|.+-avg|.+-bytes|.+-count|.+-ratio|.+-age|.+-flight|.+-threads|.+-connectors|.+-tasks|.+-ago)
 name: kafka_$2_$4
 labels:
   clientId: "$3"
 help: "Kafka $1 JMX metric type $2"
 type: GAUGE
 
#kafka.connect:type=connector-task-metrics,connector="{connector}",task="{task}<> status"
- pattern: 'kafka.connect<type=connector-task-metrics, connector=(.+), task=(.+)><>status: ([a-z-]+)'
 name: kafka_connect_connector_status
 value: 1
 labels:
   connector: "$1"
   task: "$2"
   status: "$3"
 help: "Kafka Connect JMX Connector status"
 type: GAUGE
 
#kafka.connect:type=task-error-metrics,connector="{connector}",task="{task}"
#kafka.connect:type=source-task-metrics,connector="{connector}",task="{task}"
#kafka.connect:type=sink-task-metrics,connector="{connector}",task="{task}"
#kafka.connect:type=connector-task-metrics,connector="{connector}",task="{task}"
- pattern: kafka.connect<type=(.+)-metrics, connector=(.+), task=(.+)><>(.+-total|.+-count|.+-ms|.+-ratio|.+-avg|.+-failures|.+-requests|.+-timestamp|.+-logged|.+-errors|.+-retries|.+-skipped)
 name: kafka_connect_$1_$4
 labels:
   connector: "$2"
   task: "$3"
 help: "Kafka Connect JMX metric type $1"
 type: GAUGE
 
#kafka.connect:type=connector-metrics,connector="{connector}"
#kafka.connect:type=connect-worker-metrics,connector="{connector}"
- pattern: kafka.connect<type=connect-worker-metrics, connector=(.+)><>([a-z-]+)
 name: kafka_connect_worker_$2
 labels:
   connector: "$1"
 help: "Kafka Connect JMX metric $1"
 type: GAUGE
 
#kafka.connect:type=connect-worker-metrics
- pattern: kafka.connect<type=connect-worker-metrics><>([a-z-]+)
 name: kafka_connect_worker_$1
 help: "Kafka Connect JMX metric worker"
 type: GAUGE
 
#kafka.connect:type=connect-worker-rebalance-metrics
- pattern: kafka.connect<type=connect-worker-rebalance-metrics><>([a-z-]+)
 name: kafka_connect_worker_rebalance_$1
 help: "Kafka Connect JMX metric rebalance information"
 type: GAUGE
```

##### Start Zookeeper

Start the Zookeeper as follows:

```shell
bin/zookeeper-server-start.sh config/zookeeper.properties
```

##### Start Apache Kafka with the JMX to Prometheus exporter

Open a new terminal and run the following command:

```shell
KAFKA_OPTS="`$KAFKA_OPTS` -javaagent:`PWD`/jmx_prometheus_javaagent-0.16.1.jar=9100:`PWD`/kafka.yml" bin/kafka-server-start.sh config/server.properties
```



##### Set up Telegraf v1.17 on a dedicated machine

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.prometheus plug-in

First you need to configure the input plug-in to enable Telegraf to scrape data from your hosts. To do this, add the below code to the configuration file. 

``` ini
[[inputs.prometheus]]
 urls = ["http://localhost:9100/metrics"]
 response_timeout = "10s"
```


##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}  
  
##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
