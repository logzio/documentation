Before you integrate Kubernetes you'll need:

## Prerequisites 

* [Helm](https://helm.sh/)
* Add Logzio-helm repository

  ```shell
  helm repo add logzio-helm https://logzio.github.io/logzio-helm && helm repo update
  ```


{@include: ../../_include/general-shipping/k8s-all-data.md}


## Manual Setup
Below are instructions for configuring each type of telemetry data individually.


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="log-data" label="Logs" default>


## Send your Logs

To send your logs, our chart`logzio-monitoring` offers two methods:

* `logzio-logs-collector`, based on OpenTelemetry collector
* `logzio-fluentd`, based on fluentd


### Log collection with OpenTelemetry collector

```shell
helm install -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-logs-collector.secrets.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-logs-collector.secrets.logzioRegion="<<LOGZIO-REGION>>" \
--set logzio-logs-collector.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

### Log collection with Fluentd
The `logzio-fluentd` chart is disabled by default in favor of the `logzio-logs-collector` chart.
Deploy `logzio-fluentd` by adding the following `--set` flags:

```shell
helm install -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-fluentd.enabled=true \
--set logzio-logs-collector.enabled=false \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set logzio-fluentd.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```


| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |



Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).



### Custom Configuration

You can view the full list of possible configuration options for each chart in the links below:
1. [logzio-fluentd Chart](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration)
2. [logzio-logs-collector Chart](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-logs-collector#configuration)

To modify values, use the `--set` flag with the chart name as a prefix.

**Example:** 
For a parameter called `someField` in the `logzio-logs-collector`'s `values.yaml` file, set it by adding the following to the `helm install` command:

```shell
--set logzio-logs-collector.someField="my new value"
```


Adding `log_type` annotation with a custom value will be parsed into a `log_type` field with the same value.



</TabItem>
<TabItem value="deployment-data" label="Deployment Events" default>


## Send deployment events logs

Send data about deployment events in the cluster, and how they affect its resources.

:::note
Supported resource kinds are `Deployment`, `Daemonset`, `Statefulset`, `ConfigMap`, `Secret`, `Service Account`, `Cluster Role` and `Cluster Role Binding`.
:::

```shell
helm install -n monitoring --create-namespace \
--set logzio-k8s-events.secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set logzio-k8s-events.secrets.logzioListener='<<LISTENER-HOST>>' \
--set logzio-k8s-events.secrets.env_id='<<CLUSTER-NAME>>' \
--set logzio-k8s-events.secrets.customListener='<<CUSTOM-HOST>>' \
logzio-monitoring logzio-helm/logzio-monitoring

```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<CUSTOM-HOST>>` | (*optional*) HTTP/s listener endpoint that receives JSON input, overrides the Logz.io listener. |

### Deployment events versioning

To add a versioning indicator in Kubernetes 360 and Service Overview, include the `logzio/commit_url` annotation in the resource metadata. The 'View commit' button will link to the commit URL in your version control system (VCS).


```yaml
metadata:
  annotations:
    logzio/commit_url: ""  
```

#### GitHub VCS Example 

Commit URL structure: `https://github.com/<account>/<repository>/commit/<commit-hash>`
   - Example: `https://github.com/logzio/logzio-k8s-events/commit/069c75c95caeca58dd0776405bb8dfb4eed3acb2`


Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).



</TabItem>
<TabItem value="metrics-data" label="Metrics" default>


## Send your metrics

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |


Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/k8s-troubleshooting/).




### Custom Configuration

You can view the full list of the possible configuration values in the [logzio-k8s-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

To modify values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For example, for a parameter called `someField` in the `logzio-k8s-telemetry`'s `values.yaml` file, set it by adding the following to the `helm install` command:

```shell
--set logzio-k8s-telemetry.someField="my new value"
```


 </TabItem>

<TabItem value="opentelemetry-metrics-data" label="OpenTelemetry Metrics" default>

## Send your metrics

Sends infrastructure and applications metrics using the OpenTelemetry collector.

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=false \
--set logzio-metrics-collector.enabled=true \
--set logzio-metrics-collector.secrets.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-metrics-collector.secrets.logzioRegion="<<LOGZIO-REGION>>" \
--set logzio-metrics-collector.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [ Logz.io metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Your account's [Logz.io region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |


Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/k8s-troubleshooting/).

### Send Metrics with Kubernetes object logs

:::caution Important
`logzio-metrics-collector.k8sObjectsConfig.enabled=true` will have no effect unless `logzio-metrics-collector.enabled` is also set to `true`.
:::

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=false \
--set logzio-metrics-collector.enabled=true \
--set logzio-metrics-collector.secrets.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-metrics-collector.k8sObjectsLogs.enabled=true \
--set logzio-metrics-collector.secrets.k8sObjectsLogsToken="<<LOGS-SHIPPING-TOKEN>>" \
--set logzio-metrics-collector.secrets.logzioRegion="<<LOGZIO-REGION>>" \
--set logzio-metrics-collector.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [ Logz.io metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGS-SHIPPING-TOKEN>>` | Your [ Logz.io logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Your account's [Logz.io region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |


### Configure customization options

You can use the following options to update the `logzio-metrics-collector` Helm chart values [parameters](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-metrics-collector/VALUES.md): 

To modify values found in the `logzio-metrics-collector` sub chart, use the `--set` flag with the `logzio-metrics-collector` prefix.

For example, for a parameter called `someField` in the `logzio-metrics-collector`'s `values.yaml` file, set it by adding the following to the `helm install` / `helm upgrade`  command:

```shell
--set logzio-metrics-collector.someField="my new value"
```

  </TabItem>

<TabItem value="tracing-data" label="Tracing and SPM" default>


## Send your traces

We offer three options for sending send your traces:
* Send Traces only
* Send Traces and SPM 
* Send Traces, SPM and Service Graph data

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_REGION>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

## Send traces with SPM

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_REGION>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.SpmToken=<<SPM-METRICS-SHIPPING-TOKEN>> \
logzio-monitoring logzio-helm/logzio-monitoring
```

## Send Service Graph data

:::caution Important
`serviceGraph.enabled=true` will have no effect unless `traces.enabled` and `spm.enabled=true` is set to `true`.
:::

```shell
helm install -n monitoring --create-namespace \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.SpmToken=<<SPM-METRICS-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.serviceGraph.enabled=true \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
| `<<SPM-METRICS-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |

:::note
Encounter an issue? See our [Distributed Tracing troubleshooting](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting/).
:::

### Custom Configuration

You can view the full list of the possible configuration values in the [logzio-k8s-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

To modify values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For example, for a parameter called `someField` in the `logzio-k8s-telemetry`'s `values.yaml` file, set it by adding the following to the `helm install` command:

```shell
--set logzio-k8s-telemetry.someField="my new value"
```


 </TabItem>
<TabItem value="k8s-obj-data" label="K8S Objects" default>


## Send Metrics with Kubernetes object logs

:::caution Important
`k8sObjectsConfig.enabled=true` will have no effect unless `metrics.enabled` is also set to `true`.
:::

```shell
helm install  \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.k8sObjectsConfig.enabled=true \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO-REGION>> \
--set logzio-k8s-telemetry.secrets.k8sObjectsLogsToken=<<LOG-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.MetricsToken=<<METRICS-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.ListenerHost=<<LISTENER-HOST>> \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name=<<CLUSTER-NAME>> \
--set logzio-k8s-telemetry.secrets.env_id=<<CLUSTER-NAME>> \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


 </TabItem>
<TabItem value="trivy-data" label="Trivy" default>


## Scan your cluster for security vulnerabilities

```shell
helm install -n monitoring --create-namespace \
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


 </TabItem>
<TabItem value="eks-fargate-data" label="EKS Fargate" default>



 ## Sending telemetry data from EKS on Fargate

Set the `fargateLogRouter.enabled` value to `true`. This deploys a dedicated `aws-observability` namespace and a `configmap` for the Fargate log router. Read more on EKS Fargate logging in the [official AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html).

```shell
helm install -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-fluentd.fargateLogRouter.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.collector.mode=standalone \
--set logzio-k8s-telemetry.enableMetricsFilter.eks=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_REGION>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |
| `<<CLUSTER-NAME>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<TRACING-SHIPPING-TOKEN>>` | Replace `<<TRACING-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing) of the account you want to ship to. |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |


 </TabItem>
</Tabs>


## Advanced Configuration and Troubleshooting


<Tabs>
<TabItem value="pull-rate-limit-issue" label="Pull Rate Limit" default>

## Handling image pull rate limit

Docker Hub pull rate limits could result in the following error: `You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limits`. To avoid this, use the `--set` commands below to access an alternative image repository:

```shell
--set logzio-k8s-telemetry.image.repository=ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib
--set logzio-k8s-telemetry.prometheus-pushgateway.image.repository=public.ecr.aws/logzio/prom-pushgateway
--set logzio-fluentd.image=public.ecr.aws/logzio/logzio-fluentd
--set logzio-fluentd.daemonset.init.containerImage=public.ecr.aws/docker/library/busybox
--set logzio-trivy.image=public.ecr.aws/logzio/trivy-to-logzio
```


 </TabItem>
<TabItem value="json-logs" label="Parse JSON Logs" default>


## Configuring logs in JSON format

To parse JSON Logs using the fluentd chart, configure the following processor using the `configmap.extraConfig` configuration option:

```json
<filter **>
  @type parser
  key_name message
  reserve_data true
  remove_key_name_field true
  <parse>
    @type json
  </parse>
</filter>
```

Instructions of using `configmap.extraConfig` can be found [here](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).


</TabItem>
 <TabItem value="filter-metrics" label="Filter Metrics" default>


## Custom Filter for Metrics

We provide a setting (`enableMetricsFilter`) which filters by default only the metrics needed for K8360.
If you wish to customize the metrics being sent, you can do so by modifying the `prometheusFilters` configuration in your Helm chart.
Follow the steps below to adjust this configuration:

**1. Identify metrics to keep**

Determine which metrics you need to add to your collection, and format them as a regex string (e.g., `new_metric_1|new_metric_2`).

**2. Set filters**

Run the following command to update your Chart with the specified metrics:


```shell
helm upgrade <RELEASE_NAME> logzio-helm/logzio-monitoring \
--set prometheusFilters.metrics.infrastructure.keep.aks="existing_metric_1|existing_metric_2|new_metric_1|new_metric_2" \
--set logzio-k8s-telemetry.enableMetricsFilter.<SERVICE>=true
```

* Replace `<RELEASE_NAME>` with the name of your Helm release.
* Replace `<SERVICE>` with the appropriate service name: `ask`, `eks` or `gke`.


 </TabItem>
</Tabs>

