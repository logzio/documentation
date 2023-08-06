---
id: RabbitMQ
title: RabbitMQ
overview: RabbitMQ is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, MQ Telemetry Transport, and other protocols. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/rabbitmq-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['77P29wgQwu1pqCaZFMcwnC']
metrics_alerts: []
---


RabbitMQ is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, MQ Telemetry Transport, and other protocols. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format RabbitMQ metrics to Logz.io, you need to add the **inputs.rabbitmq** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["77P29wgQwu1pqCaZFMcwnC"] -->

### Configure Telegraf to send your metrics data to Logz.io



#### Set up Telegraf v1.17 or higher on the RabbitMQ server

{@include: ../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.RabbitMQ plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the RabbitMQ data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.rabbitmq]]
  ## Management Plugin url. (default: http://localhost:15672)
  # url = "http://localhost:15672"
  ## Tag added to rabbitmq_overview series; deprecated: use tags
  # name = "rmq-server-1"
  ## Credentials
  # username = "guest"
  # password = "guest"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false

  ## Optional request timeouts
  ##
  ## ResponseHeaderTimeout, if non-zero, specifies the amount of time to wait
  ## for a server's response headers after fully writing the request.
  # header_timeout = "3s"
  ##
  ## client_timeout specifies a time limit for requests made by this client.
  ## Includes connection time, any redirects, and reading the response body.
  # client_timeout = "4s"

  ## A list of nodes to gather as the rabbitmq_node measurement. If not
  ## specified, metrics for all nodes are gathered.
  # nodes = ["rabbit@node1", "rabbit@node2"]

  ## A list of queues to gather as the rabbitmq_queue measurement. If not
  ## specified, metrics for all queues are gathered.
  # queues = ["telegraf"]

  ## A list of exchanges to gather as the rabbitmq_exchange measurement. If not
  ## specified, metrics for all exchanges are gathered.
  # exchanges = ["telegraf"]

  ## Metrics to include and exclude. Globs accepted.
  ## Note that an empty array for both will include all metrics
  ## Currently the following metrics are supported: "exchange", "federation", "node", "overview", "queue"
  # metric_include = []
  # metric_exclude = []

  ## Queues to include and exclude. Globs accepted.
  ## Note that an empty array for both will include all queues
  # queue_name_include = []
  # queue_name_exclude = []

  ## Federation upstreams to include and exclude specified as an array of glob
  ## pattern strings.  Federation links can also be limited by the queue and
  ## exchange filters.
  # federation_upstream_include = []
  # federation_upstream_exclude = []
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/rabbitmq/README.md)
:::


#### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["77P29wgQwu1pqCaZFMcwnC"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}




