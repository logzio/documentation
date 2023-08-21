---
id: aws-eks
title: AWS EKS
overview: Send Kubernetes logs, metrics and traces to Logz.io.
product: ['logs','metrics','traces']
os: ['windows', 'linux']
filters: ['AWS', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-eks.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
drop_filter: []
---

The logzio-monitoring Helm Chart ships your EKS Fargate telemetry (logs, metrics, traces and security reports) to your Logz.io account.
 

## Prerequisites 

1. [Helm](https://helm.sh/)


Add Logzio-helm repository
`helm repo add logzio-helm https://logzio.github.io/logzio-helm && helm repo update`


## Send your logs
 

Send your logs

```sh
helm install -n monitoring \
--set logs.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="{@include: ../../_include/log-shipping/log-shipping-token.html}" \
--set logzio-fluentd.secrets.logzioListener="{@include: ../../_include/log-shipping/listener-var.html}" \
--set logzio-fluentd.env_id="<<CLUSTER-NAME>>" \
--set logzio-fluentd.fargateLogRouter.enabled=true \
logzio-monitoring logzio-helm/logzio-monitoring
```


| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
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

#### Example

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

## Monitoring fluentd with prometheus
In order to monitor fluentd and collect input & output metrics. You can 
enable prometheus configuration with the `logzio-fluentd.daemonset.fluentdPrometheusConf` and `logzio-fluentd.windowsDaemonset.fluentdPrometheusConf` parameter (default to false).
When enabling promehteus configuration, the pod collects and exposes fluentd metrics on port `24231`, `/metrics` endpoint.

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

For troubleshooting log shipping, see our [user guide](https://docs.logz.io/user-guide/kubernetes-troubleshooting/).



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


## Send your Metrics

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="{@include: ../../_include/p8s-shipping/replace-prometheus-token.html}" \
--set logzio-k8s-telemetry.secrets.ListenerHost="{@include: ../../_include/p8s-shipping/replace-prometheus-listener.html}" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.collector.mode=standalone \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |
| `<<P8S-LOGZIO-NAME>>` | The name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |


For troubleshooting metrics shipping, see our [user guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/k8-helm-opentelemetry-troubleshooting.html).
 
  

### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1aO3NWtPAtVwO5Ipmc3Deh", "6KQUyksnNT2E40PifmCHR5", "X6YYCFajD56zayxcQOG2H", "M06b1BjTSGsSNZBWeiLnR"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [EKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/eks-helm-opentelemetry-troubleshooting.html).
  
  

##  Customizing Helm chart parameters

 

### Customize the metrics collected by the Helm chart 

The default configuration uses the Prometheus receiver with the following scrape jobs:

* Cadvisor: Scrapes container metrics
* Kubernetes service endpoints: These jobs scrape metrics from the node exporters, from Kube state metrics, from any other service for which the `prometheus.io/scrape: true` annotaion is set, and from services that expose Prometheus metrics at the `/metrics` endpoint.

To customize your configuration, edit the `config` section in the `values.yaml` file.

 

For troubleshooting this solution, see our [EKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/eks-helm-opentelemetry-troubleshooting.html).


## Send your traces

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="{@include: ../../_include/tracing-shipping/replace-tracing-token.html}" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACES-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=traces). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=traces). |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |


For troubleshooting traces shipping, see our [user guide]([https://docs.logz.io/user-guide/kubernetes-troubleshooting/](https://docs.logz.io/user-guide/distributed-tracing/tracing-troubleshooting.html)).


## Send traces with SPM

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="{@include: ../../_include/tracing-shipping/replace-tracing-token.html}" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.SpmToken=<<SPM-SHIPPING-TOKEN>> \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACES-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=traces). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |
| `<<SPM-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |


## Scan your cluster for security vulnerabilities

```sh
helm install -n monitoring \
--set securityReport.enabled=true \
--set logzio-trivy.env_id="<<CLUSTER-NAME>>" \
--set logzio-trivy.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-trivy.secrets.logzioListener="<<LISTENER-HOST>>" \
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


## Modifying the configuration for logs

You can see a full list of the possible configuration values in the [logzio-fluentd Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).

If you would like to modify any of the values found in the `logzio-fluentd` folder, use the `--set` flag with the `logzio-fluentd` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:

```sh
--set logzio-fluentd.someField="my new value"
```
You can add `log_type` annotation with a custom value, which will be parsed into a `log_type` field with the same value.


### Modifying the configuration for metrics and traces

You can see a full list of the possible configuration values in the [logzio-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

If you would like to modify any of the values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:


```sh
--set logzio-k8s-telemetry.someField="my new value"
```



  

## **Uninstalling the Chart**

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```

  
