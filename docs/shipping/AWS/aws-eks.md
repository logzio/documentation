---
id: aws-eks
title: AWS EKS
overview: Send Kubernetes logs, metrics and traces to Logz.io.
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['AWS', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-eks.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

The logzio-monitoring Helm Chart ships your EKS Fargate telemetry (logs, metrics, traces and security reports) to your Logz.io account.
 

## Prerequisites 

* [Helm](https://helm.sh/)


* Add Logzio-helm repository
`helm repo add logzio-helm https://logzio.github.io/logzio-helm && helm repo update`

{@include: ../../_include/general-shipping/k8s-all-data.md}


## Send your logs 
 

Send your logs

```sh
helm install -n monitoring \
--set logs.enabled=true \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set logzio-fluentd.fargateLogRouter.enabled=true \
logzio-monitoring logzio-helm/logzio-monitoring
```


| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO-REGION>>` | Replace `<<LOGZIO_ACCOUNT_REGION_CODE>>` with your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


### Adding a custom log_type field from attribute
To add a `log_type` field with a custom value to each log, you can use the annotation key `log_type` with a custom value. The annotation will be automatically parsed into a `log_type` field with the provided value.
e.g:
```
...
  metadata:
    annotations:
      log_type: "my_type"
```
Will result with the following log (json):
```
{
...
,"log_type": "my_type"
...
}
```


### Configuring Fluentd to concatenate multiline logs using a plugin

Fluentd splits multiline logs by default. If your original logs span multiple lines, you may find that they arrive in your Logz.io account split into several partial logs.

The Logz.io Docker image comes with a pre-built Fluentd filter plug-in that can be used to concatenate multiline logs. The plug-in is named `fluent-plugin-concat` and you can view the full list of configuration options in the [GitHub project](https://github.com/fluent-plugins-nursery/fluent-plugin-concat).

### Example

The following is an example of a multiline log sent from a deployment on a k8s cluster:

```shell
2021-02-08 09:37:51,031 - errorLogger - ERROR - Traceback (most recent call last):
File "./code.py", line 25, in my_func
1/0
ZeroDivisionError: division by zero
```

Fluentd's default configuration will split the above log into 4 logs, 1 for each line of the original log. In other words, each line break (`\n`) causes a split.

To avoid this, you can use the `fluent-plugin-concat` and customize the configuration to meet your needs. The additional configuration is added to:

* `kubernetes.conf` for RBAC/non-RBAC DaemonSet
* `kubernetes-containerd.conf` for Containerd DaemonSet

For the above example, we could use the following regex expressions to demarcate the start and end of our example log:


```shell
<filter **>
  @type concat
  key message # The key for part of multiline log
  multiline_start_regexp /^[0-9]{4}-[0-9]{2}-[0-9]{2}/ # This regex expression identifies line starts.
</filter>
```

### Monitoring fluentd with prometheus
In order to monitor fluentd and collect input & output metrics. You can 
enable prometheus configuration with the `logzio-fluentd.daemonset.fluentdPrometheusConf` and `logzio-fluentd.windowsDaemonset.fluentdPrometheusConf` parameter (default to false).
When enabling Prometheus configuration, the pod collects and exposes fluentd metrics on port `24231`, `/metrics` endpoint.

### Modifying the configuration

You can see a full list of the possible configuration values in the [logzio-fluentd Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).

If you would like to modify any of the values found in the `logzio-fluentd` folder, use the `--set` flag with the `logzio-fluentd` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:

```sh
--set logzio-fluentd.someField="my new value"
```
You can add `log_type` annotation with a custom value, which will be parsed into a `log_type` field with the same value.

### Sending logs from nodes with taints

If you want to ship logs from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:
  
```yaml
tolerations:
- key: 
  operator: 
  value: 
  effect: 
```
  
To determine if a node uses taints as well as to display the taint keys, run:
  
```
kubectl get nodes -o json | jq ".items[]|{name:.metadata.name, taints:.spec.taints}"
```

For example:

```
--set logzio-fluentd.daemonset.tolerations[0].key=node-role.kubernetes.io/master --set logzio-fluentd.daemonset.tolerations[0].effect=NoSchedule
```

:::node
You need to use `Helm` client with version `v3.9.0` or above.
:::

Encounter an issue? See our [user guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).



## Send your Metrics

```sh
helm install -n monitoring \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set global.logzioMetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.collector.mode=standalone \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Replace `<<LOGZIO_ACCOUNT_REGION_CODE>>` with your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |


Encounter an issue? See our [user guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/k8s-troubleshooting/).
 

### Customize the metrics collected by the Helm chart 

The default configuration uses the Prometheus receiver with the following scrape jobs:

* Cadvisor: Scrapes container metrics
* Kubernetes service endpoints: These jobs scrape metrics from the node exporters, from Kube state metrics, from any other service for which the `prometheus.io/scrape: true` annotaion is set, and from services that expose Prometheus metrics at the `/metrics` endpoint.

To customize your configuration, edit the `config` section in the `values.yaml` file.

#### Adding addiotional filters for metrics scraping

To add flexibility for the metrics filtering, you can add custom filters for the following:

* Metric name (keep & drop)
* Service names (keep & drop - only for infrastructure pipeline)
* Namespace names

Filters should be written as regex patterns, e.g., `"metric1|metric2"`.

To add a custom filter, select the pipeline where the filter should be applied, and add the filter under the relevant `custom` key. 

For example, to add a custom `namespace` keep filter to the application metric job, you can set:

```bash
--set prometheusFilters.namespaces.applications.keep.custom="namesapce_1|namespace_2"
```

For more information, refer to `prometheusFitlers` in [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-telemetry/values.yaml).

 
### Check Logz.io for your metrics
Give your metrics some time to get from your system to ours.


Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1aO3NWtPAtVwO5Ipmc3Deh", "6KQUyksnNT2E40PifmCHR5", "X6YYCFajD56zayxcQOG2H", "M06b1BjTSGsSNZBWeiLnR"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 
Encounter an issue? See our [EKS troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/eks-helm/).
 
## Send your traces

```sh
helm install -n monitoring \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACES-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=traces). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |


Encounter an issue? See our [Distributed Tracing troubleshooting](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting/).


## Send traces with SPM

```sh
helm install -n monitoring \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set logzio-apm-collector.spm.enabled=true \
--set global.logzioSpmToken={@include: ../../_include/tracing-shipping/replace-spm-token.html} \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACES-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=traces). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |
| `<<SPM-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |


## Modifying the configuration for metrics and traces

You can see a full list of the possible configuration values in the [logzio-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

If you would like to modify any of the values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:


```sh
--set logzio-k8s-telemetry.someField="my new value"
```


## Scan your cluster for security vulnerabilities

```sh
helm install -n monitoring \
--set securityReport.enabled=true \
--set global.env_id="<<CLUSTER-NAME>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LISTENER-HOST>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LOGZIO-REGION>>` | Replace `<<LOGZIO_ACCOUNT_REGION_CODE>>` with your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


## Uninstalling the Chart

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-monitoring` deployment, use the following command:

```shell
helm uninstall logzio-monitoring
```