---
id: Nginx
title: Nginx
overview: Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. Deploy this integration to ship Nginx metrics.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/nginx.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3HKho6pQhCmEYmwMc4xCeY']
metrics_alerts: []
---



## Overview

Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. Deploy this integration to ship Nginx metrics.

Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Nginx metrics to Logz.io, you need to add the **inputs.nginx** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["3HKho6pQhCmEYmwMc4xCeY"] -->

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Configure Nginx server

1. Enable `stub_status` module in the NGINX configuration file - nginx.conf:

   ```
   server {
   
           listen       80;
   
           server_name  localhost;

     
           location / {
   
           stub_status;
   
           allow `<<YOUR-LOCALHOST-ADDRESS>>`;
   
           deny all;
   
           }

   }
   ```

2. Replace `<<YOUR-LOCALHOST-ADDRESS>>` with your localhost address.
3. Restart Nginx. 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Add the inputs.nginx plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Nginx data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.nginx]]
  ## An array of Nginx stub_status URI to gather stats.
  urls = ["http://localhost/server_status"]

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false

  ## HTTP response timeout (default: 5s)
  response_timeout = "5s"
  
[[inputs.disk]]
[[inputs.net]]
[[inputs.mem]]
[[inputs.system]]
[[inputs.cpu]]
   ## Whether to report per-cpu stats or not
   percpu = false
   ## Whether to report total system cpu stats or not
   totalcpu = true
   ## If true, collect raw CPU time metrics.
   collect_cpu_time = true
   ## If true, compute and report the sum of all non-idle CPU states.
   report_active = true
  
```



##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics
  
{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3HKho6pQhCmEYmwMc4xCeY"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 

 
