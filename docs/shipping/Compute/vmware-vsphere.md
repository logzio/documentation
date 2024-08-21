---
id: VMware-vSphere 
title: VMware vSphere
overview: VMware vSphere is VMware's cloud computing virtualization platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/vsphere-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ["VpeHVDlhfo1mF22Lc0UKf", "6CpW1YzdonmTQ8uIXAN5OL", "3AvORCMPVJd8948i9oKaBO"]
metrics_alerts: []
drop_filter: []
---

VMware vSphere is VMware's cloud computing virtualization platform. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Vmware Vsphere metrics to Logz.io, you need to add the **inputs.vsphere** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["VpeHVDlhfo1mF22Lc0UKf", "6CpW1YzdonmTQ8uIXAN5OL", "3AvORCMPVJd8948i9oKaBO"] -->

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

Set up Telegraf on a dedicated server as described below.
  
{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.vsphere plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Vmware Vsphere data from your hosts. To do this, add the following code to the configuration file:


``` ini
# Read metrics from one or many vCenters
[[inputs.vsphere]]
    ## List of vCenter URLs to be monitored. These three lines must be uncommented and edited for the plugin to work.
  vcenters = [ "https://vcenter.local/sdk" ]
  username = "user@corp.local"
  password = "secret"
```


:::note
The above integration scrapes all Vmware Vsphere metrics available on your machines. 
If you wish to include or exclude specific metrics, add them to the inputs file as described [here](https://github.com/influxdata/telegraf/blob/release-1.19/plugins/inputs/vsphere/README.md).
:::
 


Here is an example of the configuration file that will enable Telegraf to scrape metrics defined by `vm_metric_include` and `host_metric_include` arrays.

``` ini
# Read metrics from one or many vCenters
[[inputs.vsphere]]
    ## List of vCenter URLs to be monitored. These three lines must be uncommented and edited for the plugin to work.
  vcenters = [ "https://vcenter.local/sdk" ]
  username = "user@corp.local"
  password = "secret"

  ## VMs
  ## Typical VM metrics (if omitted or empty, all metrics are collected)
  # vm_include = [ "/*/vm/**"] # Inventory path to VMs to collect (by default all are collected)
  # vm_exclude = [] # Inventory paths to exclude
  vm_metric_include = [
    "cpu.demand.average",
    "cpu.idle.summation",
    "cpu.latency.average",
    "cpu.readiness.average",
    "cpu.ready.summation",
    "cpu.run.summation",
    "cpu.usagemhz.average",
    "cpu.used.summation",
    "cpu.wait.summation",
    "mem.active.average",
    "mem.granted.average",
    "mem.latency.average",
 ]

  ## Hosts
  ## Typical host metrics (if omitted or empty, all metrics are collected)
  # host_include = [ "/*/host/**"] # Inventory path to hosts to collect (by default all are collected)
  # host_exclude [] # Inventory paths to exclude
  host_metric_include = [
    "cpu.swapwait.summation",
    "cpu.usage.average",
    "cpu.usagemhz.average",
    "cpu.used.summation",
    "cpu.utilization.average",
    "cpu.wait.summation",
    "disk.deviceReadLatency.average",
    "disk.deviceWriteLatency.average",
    "disk.kernelReadLatency.average",
    "disk.kernelWriteLatency.average",
    "disk.numberReadAveraged.average",
    "disk.numberWriteAveraged.average",
  ]

  ## Datacenters
  # datacenter_include = [ "/*/host/**"] # Inventory path to clusters to collect (by default all are collected)
  # datacenter_exclude = [] # Inventory paths to exclude
  # datacenter_metric_include = [] ## if omitted or empty, all metrics are collected
  datacenter_metric_exclude = [ "*" ] ## Datacenters are not collected by default.
  # datacenter_instances = false ## false by default 
  
```

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["VpeHVDlhfo1mF22Lc0UKf", "6CpW1YzdonmTQ8uIXAN5OL", "3AvORCMPVJd8948i9oKaBO"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 


 
