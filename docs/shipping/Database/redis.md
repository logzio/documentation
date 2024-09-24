---
id: Redis
title: Redis
overview: Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['Database']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/redis-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1sS7i6SyMz35RIay8NRYGp', '6XBrbjsUey4Agm0hAK4Yqn']
metrics_alerts: []
drop_filter: []
---


Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.

## Metrics

### Using Otel

#### Clone the Redis Exporter Repository

Open your terminal and run the following command:

```bash
git clone https://github.com/oliver006/redis_exporter.git
```

#### Build the Redis Exporter

```bash
cd redis_exporter
go build .
```

#### Configure Redis Password (if not already set)

1. Locate your Redis configuration file, `redis.conf`.
2. Open the file in a text editor.
3. Find the line `#requirepass`.
4. Uncomment it and replace the line with a secure password of your choice.
5. Save the file.
6. Restart Redis to apply the new configuration.

:::note
For detailed instructions, refer to this guide: [Change Redis Password](https://linuxhint.com/change-redis-password/).
:::

#### Run the Redis Exporter

```bash
./redis_exporter --redis.password=<<your_secure_password>>
```

Replace `<<YOUR_SECURE_PASSWORD>>` with the password you set.

#### Verify Redis Exporter Functionality

1. Open a web browser and navigate to http://localhost:9121/metrics.
2. Check if metrics are being displayed.

#### Set up Otel Collector

Create a configuration file for the Otel Collector. This file should contain the following components:
* **Receivers**: Define the Prometheus receiver with your specific job name and scrape interval.
* **Exporters**: Set up the Prometheus Remote Write exporter with the endpoint and necessary headers.
* **Processors**: Configure resource detection with system detectors.
* **Service**: Define the telemetry logs level and setup pipelines that tie receivers, exporters, and processors together.

Example configuration:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: '<<job_name>>'
          scrape_interval: 10s
          static_configs:
            - targets: ['localhost:9121']

exporters:
  prometheusremotewrite:
    endpoint: "https://listener.logz.io:8053"
    headers:
      Authorization: "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
    resource_to_telemetry_conversion:
      enabled: true

processors:
  resourcedetection/system:
    detectors: ["system"]
    system:
      hostname_sources: ["os"]

service:
  telemetry:
    logs:
      level: debug
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [prometheusremotewrite]
      processors: [resourcedetection/system]
```

{@include: ../../_include/p8s-shipping/replace-prometheus-token.html}

Replace `<<job_name>>` with a suitable job name for your setup.

##### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


### Using Telegraf

To send your Prometheus-format Redis metrics to Logz.io, you need to add the **inputs.redis** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["1sS7i6SyMz35RIay8NRYGp"] -->

#### Configure Telegraf to send your metrics data to Logz.io



##### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.redis plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Redis data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.redis]]
  ##  specify servers via a url matching:
     servers = [<<PROTOCOL>>://][:<<PASSWORD>>]@<<ADDRESS>>[:<<PORT>>]
  ##  e.g.
  ##    tcp://localhost:6379
  ##    tcp://:password@192.168.99.100
  ##    servers = ["tcp://20.77.110.14:6379","tcp://20.77.110.32:6379"]
```

* Replace `<<PROTOCOL>>` with the name of your shipping protocol (tcp protocol recommended).
* Replace `<<PASSWORD>>` with the password for your Redis database.
* Replace `<<ADDRESS>>` with the address of your Redis database host. This is `localhost` if installed locally.
* Replace `<<PORT>>` with the address of your host port allocated to Redis database.

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/redis/README.md).
::: 


##### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

#### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

#### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1sS7i6SyMz35RIay8NRYGp"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


## Logs and metrics

### Using Otel

#### Clone the Redis Exporter Repository

Open your terminal and run the following command:

```bash
git clone https://github.com/oliver006/redis_exporter.git
```

#### Build the Redis Exporter

```bash
cd redis_exporter
go build .
```

#### Configure Redis Password (if not already set)

1. Locate your Redis configuration file, `redis.conf`.
2. Open the file in a text editor.
3. Find the line `#requirepass`.
4. Uncomment it and replace the line with a secure password of your choice.
5. Save the file.
6. Restart Redis to apply the new configuration.

:::note
For detailed instructions, refer to this guide: [Change Redis Password](https://linuxhint.com/change-redis-password/).
:::

#### Configure Redis Logfile

1. Locate your Redis configuration file, `redis.conf`.
2. Open the file in a text editor.
3. Locate the entry `loglevel` and choose the level you want.
4. Locate the entry `logfile` and replace `“”` with the directory you want to write the logs to.
5. Save the file.
6. Restart Redis to apply the new configuration.

#### Run the Redis Exporter

```bash
./redis_exporter --redis.password=<<your_secure_password>>
```

Replace `<<YOUR_SECURE_PASSWORD>>` with the password you set.

#### Verify Redis Exporter Functionality

1. Open a web browser and navigate to http://localhost:9121/metrics.
2. Check if metrics are being displayed.

#### Set up Otel Collector

Create a configuration file for the Otel Collector. This file should contain the following components:
* **Receivers**: Define the Prometheus receiver with your specific job name and scrape interval.
* **Exporters**: Set up the Prometheus Remote Write exporter with the endpoint and necessary headers.
* **Processors**: Configure resource detection with system detectors.
* **Service**: Define the telemetry logs level and setup pipelines that tie receivers, exporters, and processors together.

Example configuration:

```yaml
receivers:
 prometheus:
     config:
       scrape_configs:
         - job_name: '<<job_name>>'
           scrape_interval: 10s
           static_configs:
             - targets: ['localhost:9121']
  filelog/redis:
   include: [<<logfile directory>>]
   include_file_path: true
   operators:
     - type: move
       from: attributes["log.file.name"]
       to: attributes["log_file_name"]
     - type: move
       from: attributes["log.file.path"]
       to: attributes["log_file_path"]
   attributes:
     type: agent-mac
     source: redis
    
exporters:
 logging:
 logzio/logs:
   account_token: "<<LOG-SHIPPING-TOKEN>>"
   region: "us"
 prometheusremotewrite:
   endpoint: "https://listener.logz.io:8053"
   headers:
     Authorization: "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
   resource_to_telemetry_conversion:
     enabled: true


processors:
 resourcedetection/system:
   detectors: ["system"]
   system:
     hostname_sources: ["os"]


service:
 pipelines:
   logs:
     receivers: [filelog/redis]
     processors: [resourcedetection/system]
     exporters: [logzio/logs]
   metrics:
     receivers: [prometheus]
     exporters: [prometheusremotewrite]
     processors: [resourcedetection/system]
```

{@include: ../../_include/p8s-shipping/replace-prometheus-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

Replace `<<job_name>>` with a suitable job name for your setup.

Replace `<<logfile directory>>` with your logfile directory


##### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

##### Check Logz.io for your logs and metrics

Give your data some time to get from your system to ours, then log in to your Logz.io account.


## Logs

### Using Otel

#### Clone the Redis Exporter Repository

Open your terminal and run the following command:

```bash
git clone https://github.com/oliver006/redis_exporter.git
```

#### Build the Redis Exporter

```bash
cd redis_exporter
go build .
```

#### Configure Redis Logfile

1. Locate your Redis configuration file, `redis.conf`.
2. Open the file in a text editor.
3. Locate the entry `loglevel` and choose the level you want.
4. Locate the entry `logfile` and replace `“”` with the directory you want to write the logs to.
5. Save the file.
6. Restart Redis to apply the new configuration.

#### Set up Otel Collector

Create a configuration file for the Otel Collector. This file should contain the following components:
* **Receivers**: Define the Prometheus receiver with your specific job name and scrape interval.
* **Exporters**: Set up the Prometheus Remote Write exporter with the endpoint and necessary headers.
* **Processors**: Configure resource detection with system detectors.
* **Service**: Define the telemetry logs level and setup pipelines that tie receivers, exporters, and processors together.

Example configuration:

```yaml
receivers:
  filelog/redis:
   include: [<<logfile directory>>]
   include_file_path: true
   operators:
     - type: move
       from: attributes["log.file.name"]
       to: attributes["log_file_name"]
     - type: move
       from: attributes["log.file.path"]
       to: attributes["log_file_path"]
   attributes:
     type: agent-mac
     source: redis
    

exporters:
 logging:
 logzio/logs:
   account_token: "<<LOG-SHIPPING-TOKEN>>"
   region: "us"


processors:
 resourcedetection/system:
   detectors: ["system"]
   system:
     hostname_sources: ["os"]


service:
 pipelines:
   logs:
     receivers: [filelog/redis]
     processors: [resourcedetection/system]
     exporters: [logzio/logs]
```

{@include: ../../_include/log-shipping/listener-var.html} 

Replace `<<logfile directory>>` with your logfile directory


##### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

##### Check Logz.io for your logs

Give your data some time to get from your system to ours, then log in to your Logz.io Logs account, and open [the Dashboard](https://app.logz.io/#/dashboard/).
