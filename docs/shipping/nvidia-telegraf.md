---
id: NVIDIA
title: NVIDIA
overview: TNVIDIA System Management Interface (nvidia-smi) is a command line utility, based on top of the NVIDIA Management Library (NVML), intended to aid in the management and monitoring of NVIDIA GPU devices. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/nvidia.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



## Overview

NVIDIA System Management Interface (nvidia-smi) is a command line utility, based on top of the NVIDIA Management Library (NVML), intended to aid in the management and monitoring of NVIDIA GPU devices. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format NVIDIA SMI metrics to Logz.io, you need to add the **inputs.nvidia_smi** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on the same machine as the NVIDIA card

**Ubuntu & Debian**

```shell
sudo apt-get update && sudo apt-get install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**RedHat and CentOS**

```shell
sudo yum install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**SLES & openSUSE**

```shell
# add go repository
zypper ar -f obs://devel:languages:go/ go
# install latest telegraf
zypper in telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

**FreeBSD/PC-BSD**

```shell
sudo pkg install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.
  
##### Add the inputs.nvidia_smi plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the NVIDIA SMI data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.nvidia_smi]]
  ## Optional: path to nvidia-smi binary, defaults to $PATH via exec.LookPath
  # bin_path = "/usr/bin/nvidia-smi"

  ## Optional: timeout for GPU polling
  # timeout = "5s"
```


:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/nvidia_smi/README.md).
:::
 

##### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
