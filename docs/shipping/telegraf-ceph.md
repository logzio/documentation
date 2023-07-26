---
id: Ceph
title: Ceph
overview: Ceph is an open-source software (software-defined storage) storage platform, implements object storage on a single distributed computer cluster, and provides 3-in-1 interfaces for object-, block- and file-level storage. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/ceph-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


## Overview

Ceph is an open-source software (software-defined storage) storage platform, implements object storage on a single distributed computer cluster, and provides 3-in-1 interfaces for object-, block- and file-level storage. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Ceph Storage metrics to Logz.io, you need to add the **inputs.ceph** and **outputs.http** plug-ins to your Telegraf configuration file.

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher on each Ceph server

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
  
##### Add the inputs.ceph plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Ceph data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.ceph]]
  ## This is the recommended interval to poll.  Too frequent and you will lose
  ## data points due to timeouts during rebalancing and recovery
  interval = '1m'

  ## All configuration values are optional, defaults are shown below

  ## location of ceph binary
  ceph_binary = "/usr/bin/ceph"

  ## directory in which to look for socket files
  socket_dir = "/var/run/ceph"

  ## prefix of MON and OSD socket files, used to determine socket type
  mon_prefix = "ceph-mon"
  osd_prefix = "ceph-osd"
  mds_prefix = "ceph-mds"
  rgw_prefix = "ceph-client"

  ## suffix used to identify socket files
  socket_suffix = "asok"

  ## Ceph user to authenticate as, ceph will search for the corresponding keyring
  ## e.g. client.admin.keyring in /etc/ceph, or the explicit path defined in the
  ## client section of ceph.conf for example:
  ##
  ##     [client.telegraf]
  ##         keyring = /etc/ceph/client.telegraf.keyring
  ##
  ## Consult the ceph documentation for more detail on keyring generation.
  ceph_user = "client.admin"

  ## Ceph configuration to use to locate the cluster
  ceph_config = "/etc/ceph/ceph.conf"

  ## Whether to gather statistics via the admin socket
  gather_admin_socket_stats = true

  ## Whether to gather statistics via ceph commands, requires ceph_user and ceph_config
  ## to be specified
  gather_cluster_stats = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/ceph/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
