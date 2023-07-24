---
id: etcd
title: etcd
sidebar_position: 1
overview: etcd is an open source, distributed, consistent key-value store for shared configuration, service discovery, and scheduler coordination of distributed systems or clusters of machines. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3Vr8IYt2XR2LEKP6PeVV0r']
metrics_alerts: []
---



## Overview

etcd is an open source, distributed, consistent key-value store for shared configuration, service discovery, and scheduler coordination of distributed systems or clusters of machines. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format etcd metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["3Vr8IYt2XR2LEKP6PeVV0r"] -->

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the same machine as etcd

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Add the inputs.prometheus plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the etcd data from your hosts. To do this, add the following code to the configuration file:


``` ini
# Read metrics from one or many prometheus clients
[[inputs.prometheus]]
  ## An array of urls to scrape metrics from.
  urls = ["http://localhost:9100/metrics"]
  
  ## Metric version controls the mapping from Prometheus metrics into
  ## Telegraf metrics.  When using the prometheus_client output, use the same
  ## value in both plugins to ensure metrics are round-tripped without
  ## modification.
  ##
  ##   example: metric_version = 1; 
  ##            metric_version = 2; recommended version
  # metric_version = 1
  
  ## Url tag name (tag containing scrapped url. optional, default is "url")
  # url_tag = "url"
  
  ## Whether the timestamp of the scraped metrics will be ignored.
  ## If set to true, the gather time will be used.
  # ignore_timestamp = false
  
  ## An array of Kubernetes services to scrape metrics from.
  # kubernetes_services = ["http://my-service-dns.my-namespace:9100/metrics"]
  
  ## Kubernetes config file to create client from.
  # kube_config = "/path/to/kubernetes.config"
  
  ## Scrape Kubernetes pods for the following prometheus annotations:
  ## - prometheus.io/scrape: Enable scraping for this pod
  ## - prometheus.io/scheme: If the metrics endpoint is secured then you will need to
  ##     set this to 'https' & most likely set the tls config.
  ## - prometheus.io/path: If the metrics path is not /metrics, define it with this annotation.
  ## - prometheus.io/port: If port is not 9102 use this annotation
  # monitor_kubernetes_pods = true
  
  ## Get the list of pods to scrape with either the scope of
  ## - cluster: the kubernetes watch api (default, no need to specify)
  ## - node: the local cadvisor api; for scalability. Note that the config node_ip or the environment variable NODE_IP must be set to the host IP.
  # pod_scrape_scope = "cluster"
  
  ## Only for node scrape scope: node IP of the node that telegraf is running on.
  ## Either this config or the environment variable NODE_IP must be set.
  # node_ip = "10.180.1.1"
	
  ## Only for node scrape scope: interval in seconds for how often to get updated pod list for scraping.
  ## Default is 60 seconds.
  # pod_scrape_interval = 60
  
  ## Restricts Kubernetes monitoring to a single namespace
  ##   ex: monitor_kubernetes_pods_namespace = "default"
  # monitor_kubernetes_pods_namespace = ""
  # label selector to target pods which have the label
  # kubernetes_label_selector = "env=dev,app=nginx"
  # field selector to target pods
  # eg. To scrape pods on a specific node
  # kubernetes_field_selector = "spec.nodeName=$HOSTNAME"

  ## Scrape Services available in Consul Catalog
  # [inputs.prometheus.consul]
  #   enabled = true
  #   agent = "http://localhost:8500"
  #   query_interval = "5m"

  #   [[inputs.prometheus.consul.query]]
  #     name = "a service name"
  #     tag = "a service tag"
  #     url = 'http://\{\{if ne .ServiceAddress ""\}\}\{\{.ServiceAddress\}\}{{else}}\{\{.Address\}\}{{end}}:\{\{.ServicePort\}\}/{{with .ServiceMeta.metrics_path}}\{\{.\}\}{{else}}metrics{{end}}'
  #     [inputs.prometheus.consul.query.tags]
  #       host = "\{\{.Node\}\}"
  
  ## Use bearer token for authorization. ('bearer_token' takes priority)
  # bearer_token = "/path/to/bearer/token"
  ## OR
  # bearer_token_string = "abc_123"
  
  ## HTTP Basic Authentication username and password. ('bearer_token' and
  ## 'bearer_token_string' take priority)
  # username = ""
  # password = ""
  
  ## Specify timeout duration for slower prometheus clients (default is 3s)
  # response_timeout = "3s"
  
  ## Optional TLS Config
  # tls_ca = /path/to/cafile
  # tls_cert = /path/to/certfile
  # tls_key = /path/to/keyfile
  
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false

```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/prometheus).
:::
 

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics
{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3Vr8IYt2XR2LEKP6PeVV0r"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 


 
