---
id: Telegraf-windows-performance
title: Telegraf Windows Performance
overview: Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3AND5wMrjcMC9ngDTghmHx']
metrics_alerts: []
---


Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Windows Performance metrics to Logz.io, you need to add the **inputs.win_perf_counters** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["3AND5wMrjcMC9ngDTghmHx"] -->

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

```shell
wget https://dl.influxdata.com/telegraf/releases/telegraf-1.19.2_windows_amd64.zip
```

After downloading the archive, extract its content into `C:\Program Files\Logzio\telegraf\`.

The configuration file is located at `C:\Program Files\Logzio\telegraf\`.
  
#### Add the inputs.win_perf_counters plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Windows Performance data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.win_perf_counters]]
  [[inputs.win_perf_counters.object]]
    # Processor usage, alternative to native, reports on a per core.
    ObjectName = "Processor"
    Instances = ["*"]
    Counters = [
      "% Idle Time",
      "% Interrupt Time",
      "% Privileged Time",
      "% User Time",
      "% Processor Time",
      "% DPC Time",
    ]
    Measurement = "win_cpu"
    # Set to true to include _Total instance when querying for all (*).
    IncludeTotal=true

  [[inputs.win_perf_counters.object]]
    # Disk times and queues
    ObjectName = "LogicalDisk"
    Instances = ["*"]
    Counters = [
      "% Idle Time",
      "% Disk Time",
      "% Disk Read Time",
      "% Disk Write Time",
      "% Free Space",
      "Current Disk Queue Length",
      "Free Megabytes",
    ]
    Measurement = "win_disk"
    # Set to true to include _Total instance when querying for all (*).
    #IncludeTotal=false

  [[inputs.win_perf_counters.object]]
    ObjectName = "PhysicalDisk"
    Instances = ["*"]
    Counters = [
      "Disk Read Bytes/sec",
      "Disk Write Bytes/sec",
      "Current Disk Queue Length",
      "Disk Reads/sec",
      "Disk Writes/sec",
      "% Disk Time",
      "% Disk Read Time",
      "% Disk Write Time",
    ]
    Measurement = "win_diskio"

  [[inputs.win_perf_counters.object]]
    ObjectName = "Network Interface"
    Instances = ["*"]
    Counters = [
      "Bytes Received/sec",
      "Bytes Sent/sec",
      "Packets Received/sec",
      "Packets Sent/sec",
      "Packets Received Discarded",
      "Packets Outbound Discarded",
      "Packets Received Errors",
      "Packets Outbound Errors",
    ]
    Measurement = "win_net"

  [[inputs.win_perf_counters.object]]
    ObjectName = "System"
    Counters = [
      "Context Switches/sec",
      "System Calls/sec",
      "Processor Queue Length",
      "System Up Time",
    ]
    Instances = ["------"]
    Measurement = "win_system"
    # Set to true to include _Total instance when querying for all (*).
    #IncludeTotal=false

  [[inputs.win_perf_counters.object]]
    # Example query where the Instance portion must be removed to get data back,
    # such as from the Memory object.
    ObjectName = "Memory"
    Counters = [
      "Available Bytes",
      "Cache Faults/sec",
      "Demand Zero Faults/sec",
      "Page Faults/sec",
      "Pages/sec",
      "Transition Faults/sec",
      "Pool Nonpaged Bytes",
      "Pool Paged Bytes",
      "Standby Cache Reserve Bytes",
      "Standby Cache Normal Priority Bytes",
      "Standby Cache Core Bytes",
    ]
    # Use 6 x - to remove the Instance bit from the query.
    Instances = ["------"]
    Measurement = "win_mem"
    # Set to true to include _Total instance when querying for all (*).
    #IncludeTotal=false

  [[inputs.win_perf_counters.object]]
    # Example query where the Instance portion must be removed to get data back,
    # such as from the Paging File object.
    ObjectName = "Paging File"
    Counters = [
      "% Usage",
    ]
    Instances = ["_Total"]
    Measurement = "win_swap"
```


#### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

```shell
telegraf.exe --service start
```

### Check Logz.io for your metrics

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3AND5wMrjcMC9ngDTghmHx"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 


 
