---
id: OpenShift
title: OpenShift
overview: OpenShift is a family of containerization software products developed by Red Hat. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. This integration will deploy the default daemonset, which sends only container logs while ignoring all containers with "openshift" namespace.
product: ['logs']
os: ['windows', 'linux']
filters: ['Containers', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/openshift.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Overview 

OpenShift is a family of containerization software products developed by Red Hat. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. 
This integration will deploy the default daemonset, which sends only container logs while ignoring all containers with "openshift" namespace.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-openshift/)
:::

**Before you begin, you'll need**:

* Working Openshift cluster
* Openshift CLI (oc) installed on your machine

## Setup using default configuraiton

### Create monitoring namespace

```shell
oc create namespace monitoring
```

### Store your Logz.io credentials

```shell
oc create secret generic logzio-logs-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
  -n monitoring
```
{@include: ../../_include/log-shipping/log-shipping-token.md}
{@include: ../../_include/log-shipping/listener-var.html}

### Deploy the resources

```shell
oc create -f https://raw.githubusercontent.com/logzio/logzio-openshift/main/resources.yaml \
&& oc adm policy add-scc-to-user privileged -z fluentd \
&& oc delete pod -l k8s-app=fluentd-logzio
```

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).


## Setup using custom configuration 


OpenShift is a family of containerization software products developed by Red Hat. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. Deploy this integration to ship logs from your OpenShift cluster to Logz.io. This integration will deploy the daemonset with your custom configuration.

**Before you begin, you'll need**:

* Working Openshift cluster
* Openshift CLI (oc) installed on your machine



### Create monitoring namespace

```shell
oc create namespace monitoring
```

### Store your Logz.io credentials

```shell
oc create secret generic logzio-logs-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
  -n monitoring
```
{@include: ../../_include/log-shipping/log-shipping-token.md}
{@include: ../../_include/log-shipping/listener-var.html}

### Download the resources file

Download the [resouces file](https://raw.githubusercontent.com/logzio/logzio-openshift/main/resources.yaml) from our repository.

### Add environment variables to the resources file

In the resources file, go to the Daemonset section and edit the following environment variables:

| Parameter | Description |
|---|---|
| output_include_time | **Default**: `true` <br />  To append a timestamp to your logs when they're processed, `true`. Otherwise, `false`. |
| LOGZIO_BUFFER_TYPE | **Default**: `file` <br />  Specifies which plugin to use as the backend. |
| LOGZIO_BUFFER_PATH | **Default**: `/var/log/Fluentd-buffers/stackdriver.buffer` <br />  Path of the buffer. |
| LOGZIO_OVERFLOW_ACTION | **Default**: `block` <br />  Controls the behavior when the queue becomes full. |
| LOGZIO_CHUNK_LIMIT_SIZE | **Default**: `2M` <br />  Maximum size of a chunk allowed |
| LOGZIO_QUEUE_LIMIT_LENGTH | **Default**: `6` <br />  Maximum length of the output queue. |
| LOGZIO_FLUSH_INTERVAL | **Default**: `5s` <br />  Interval, in seconds, to wait before invoking the next buffer flush. |
| LOGZIO_RETRY_MAX_INTERVAL | **Default**: `30s` <br />  Maximum interval, in seconds, to wait between retries. |
| LOGZIO_FLUSH_THREAD_COUNT | **Default**: `2` <br />  Number of threads to flush the buffer. |
| LOGZIO_LOG_LEVEL | **Default**: `info` <br /> The log level for this container. |
| INCLUDE_NAMESPACE | **Default**: `""`(All namespaces) <br /> Use if you wish to send logs from specific k8s namespaces, space delimited. Should be in the following format: <br /> `kubernetes.var.log.containers.**_<<NAMESPACE-TO-INCLUDE>>_** kubernetes.var.log.containers.**_<<ANOTHER-NAMESPACE>>_**`. |

:::note
The above variables can be edited directly in the DaemonSet without the Configmap.
:::


### Add additional configuration in the Configmap

If you wish to make any further configuration changes, go to the ConfigMap section of the file and make the changes that you need.


### Deploy the resources

```shell
oc create -f /path/to/your/resources.yaml \
&& oc adm policy add-scc-to-user privileged -z fluentd \
&& oc delete pod -l k8s-app=fluentd-logzio
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting).
