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

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Argo CD metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["6Gx8npV306IL2WZ4SJRIN4"] -->

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
##### Expose Argo CD metrics

First, you need to [expose Argo CD Prometheus-format metrics](https://argo-cd.readthedocs.io/en/stable/operator-manual/metrics/) on your server.


##### Add the inputs.prometheus plug-in

Now you need to configure the input plug-in to enable Telegraf to scrape the Argo CD data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.prometheus]]
  ## An array of urls to scrape metrics from.
  urls = ["http://<<ARGOCD_HOST_URL>>:<<PORT>>/metrics"]
```

* Replace `<ARGOCD_HOST_URL>>` with the URL of your Argo CD host.
* Replace `<<PORT>>` with the port of your Argo CD host.

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["6Gx8npV306IL2WZ4SJRIN4"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 


 
