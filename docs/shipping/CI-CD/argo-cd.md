---
id: Argo-CD
title: Argo CD
overview: Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['CI/CD']
recommendedFor: ['DevOps Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/argo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['6Gx8npV306IL2WZ4SJRIN4']
metrics_alerts: []
drop_filter: []
---


Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Argo CD metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["6Gx8npV306IL2WZ4SJRIN4"] -->

## Configure Telegraf to send your metrics data to Logz.io

 

### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
### Expose Argo CD metrics

First, you need to [expose Argo CD Prometheus-format metrics](https://argo-cd.readthedocs.io/en/stable/operator-manual/metrics/) on your server.


### Add the inputs.prometheus plug-in

Now you need to configure the input plug-in to enable Telegraf to scrape the Argo CD data from your hosts. To do this, add the following code to the configuration file:


``` ini 
[[inputs.prometheus]]
  ## An array of urls to scrape metrics from.
  urls = ["http://<<ARGOCD_HOST_URL>>:<<PORT>>/metrics"]
```

* Replace `<ARGOCD_HOST_URL>>` with the URL of your Argo CD host.
* Replace `<<PORT>>` with the port of your Argo CD host.

### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["6Gx8npV306IL2WZ4SJRIN4"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 


 
