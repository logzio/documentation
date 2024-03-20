---
id: Kafka-JMX-Receiver
title: Kafka-JMX-Receiver
overview: The JMX Receiver complements the OpenTelemetry JMX Metric Gatherer by capturing metrics from an MBean server. It utilizes a Groovy script with the assistance of a built-in OpenTelemetry helper.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kafka.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


The Kafka JMX Receiver enhances Java application monitoring by utilizing the OpenTelemetry JMX Metric Gatherer. This combination facilitates the collection of metrics from MBean servers via a Groovy script, using an OpenTelemetry (otel) helper.

## Setup Instructions


**Before you begin, you'll need**:
  Apache Kafka running on your server


### Install the JMX Metric Gatherer

1. **Download the JMX Metric Gatherer JAR**: Obtain the latest version (1.9 or above) from [OpenTelemetry Java Contrib GitHub releases](https://github.com/open-telemetry/opentelemetry-java-contrib/releases).

2. **Specify the JAR Path**: Ensure the JMX Metric Gatherer JAR is accessible. By default, use `/opt/opentelemetry-java-contrib-jmx-metrics.jar` or specify your own path if different.

:::note
The JAR path must represent a released version 1.9+ of the jar, which can be [downloaded from GitHub](https://github.com/open-telemetry/opentelemetry-java-contrib/releases). If a non-released version is required, you can specify a custom version by providing the `sha256 hash` of your custom version of the jar during collector build time using the `ldflags` option:

```go
go build -ldflags "-X github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jmxreceiver.MetricsGathererHash=<sha256hash>"
```
:::

### Configure the JMX Receiver

1. **Set Up the Child JRE Process**: The receiver initiates a child JRE process equipped with your JMX connection details and the target Groovy script for metric gathering.

2. **JMX Connection Configuration**:

  * **Endpoint**: Define the JMX Service URL or host and port. Use the format `service:jmx:<protocol>:<sap> or host:port`. The `host:port` format will transform into a Service URL like `service:jmx:rmi:///jndi/rmi://<host>:<port>/jmxrmi`.

3. **Target System Selection**:

  * Choose from built-in target systems like `activemq`, `cassandra`, `hbase`, `hadoop`, `jetty`, `jvm`, `kafka`, `kafka-consumer`, `kafka-producer`, `solr`, `tomcat`, `wildfly`.
  * For additional systems, custom JMX metric gatherer jars might be necessary, configurable via build flags.

### Set Up Kafka JMX Reporting

1. **Kafka Broker and Producer Metrics Collection**:

  * Configure a JMX remote connection without authentication for Kafka metrics.
  * Use the command `JMX_PORT=12346 ./bin/kafka-server-start.sh` to start Kafka with JMX enabled.

2. **Starting Zookeeper and Kafka**:

  * First, launch Zookeeper by running the following command:
  
    ```bash
    installation_location\bin\windows\zookeeper-server-start.bat config\zookeeper.properties
    ```

  * Then, start the Kafka server by running the following command:
  
    ```bash
    installation_location\bin\windows\kafka-server-start.bat config\server.properties
    ```

3. **Additional JVM Metric Exposure**:

  * To monitor other applications, modify the environment files accordingly. For Solr, add `SOLR_JMX_CONFIG="-Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.port=12346"` to the `solr.env` file.

### Configure OpenTelemetry

Configure the collector as follows:

```yaml
receivers:
 jmx:
   jar_path: /Users/israelefrati/Downloads/jmxOpen/opentelemetry-jmx-metrics.jar
   endpoint: localhost:12346
   target_system: jvm,kafka
   collection_interval: 10s


processors:
 attributes/jmx:
   actions:
     - key: host
       value: localhost:12345
       action: insert
 attributes/agent:
   actions:
     - key: logzio_agent_version
       value: v1.0.36
       action: insert
     - key: targets
       value: _CloudService_
       action: insert
     - key: role
       value: _role_
       action: insert


exporters:
 logging:
 logzio/logs:------------------------------
   region: us
 prometheusremotewrite:
   endpoint: https://listener.logz.io:8053
   headers:
     Authorization: Bearer —-----------------------
   resource_to_telemetry_conversion:
     enabled: true


service:
 pipelines:
   metrics:
     receivers:
     - jmx
     exporters: [prometheusremotewrite]
     processors:
       - attributes/jmx   
       - attributes/agent
 telemetry:
   logs:
     level: debug
   metrics:
     address: localhost:8899
```

  
### Check Logz.io for your metrics

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1G48F1M2FrS9tBtZ4P8jP6", "1G48F1M2FrS9tBtZ4P8jP6"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1G48F1M2FrS9tBtZ4P8jP6", "1G48F1M2FrS9tBtZ4P8jP6"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


 
