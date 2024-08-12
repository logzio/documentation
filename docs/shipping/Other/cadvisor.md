---
id: cadvisor
title: cAdvisor
overview: This integration lets you send cAdvisor metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other', 'Most Popular']
logo: https://dytvr9ot2sszz.cloudfront.net/logz-docs/shipper-logos/cadvisor.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


cAdvisor (Container Advisor) is a container monitoring tool developed by Google that collects, aggregates, processes, and exports information about running containers. To send your Prometheus cAdvisor metrics to a Logz.io Infrastructure Monitoring account, use remote write to connect to Logz.io as the endpoint.

### Before you begin
These are the prerequisites you’ll need before you can begin:

* Docker and Docker Compose installed on your machine.
* Logz.io account 


#### Create a Prometheus configuration file

Navigate to your application directory or create a new one. In this directory, create a `prometheus.yml` file with the following content:

```yaml
global:
  scrape_interval: 15s
  external_labels:
    monitor: 'docker-monitor'

scrape_configs:
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

remote_write:
  - url: "https://<<LISTENER-HOST>>:8053"
    bearer_token: "<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
    remote_timeout: 30s
    queue_config:
      batch_send_deadline: 5s
      max_shards: 10
      min_shards: 1
      max_samples_per_send: 500
      capacity: 10000
``` 

{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

#### Create a Docker Compose file

In the same directory, create a `docker-compose.yml` file with the following content:

```yaml
version: '3.7'

services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - 9090:9090

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - 8080:8080
```

#### Run the setup

From your application directory, run:

```bash
docker-compose up -d
```

#### Verify the setup

To verify that your metrics are being sent correctly:

1. Open your browser and go to http://localhost:9090 to access the Prometheus UI.
2. In the Prometheus UI, run a query for p`rometheus_remote_storage_samples_in_total`. You should see metrics if everything is set up correctly.


#### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).





