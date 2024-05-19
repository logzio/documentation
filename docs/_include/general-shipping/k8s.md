




## Prerequisites 

1. [Helm](https://helm.sh/)

Add Logzio-helm repository

```sh
helm repo add logzio-helm https://logzio.github.io/logzio-helm && helm repo update
```
{@include: ../../_include/general-shipping/k8s-all-data.md}

## Send your logs

```sh
helm install -n monitoring \
--set logs.enabled=true \
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


For log shipping troubleshooting, see our [user guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).

## Send your deploy events logs

This integration sends data about deployment events in the cluster, and how they affect the cluster's resources. 
Currently supported resource kinds are `Deployment`, `Daemonset`, `Statefulset`, `ConfigMap`, `Secret`, `Service Account`, `Cluster Role` and `Cluster Role Binding`.

```sh
helm install --namespace=monitoring \
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

To add a versioning indicator to our K8S 360 and Service Overview UI, the specified annotation must be included in the metadata of each resource whose versioning you wish to track. The 'View commit' button will link to the commit URL in your version control system (VCS) from the logzio/commit_url annotation value.

```yaml
metadata:
  annotations:
    logzio/commit_url: ""  
```

#### GitHub VCS Example 

Commit URL structure: `https://github.com/<account>/<repository>/commit/<commit-hash>`
   - Example: `https://github.com/logzio/logzio-k8s-events/commit/069c75c95caeca58dd0776405bb8dfb4eed3acb2`


For log shipping troubleshooting, see our [user guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).

## Send your metrics

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |


For metrics shipping troubleshooting, see our [user guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/k8s-troubleshooting/).



## Send your traces

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO_ACCOUNT_REGION_CODE>>` | Name of your Logz.io traces region e.g `us`, `eu`... |


For traces shipping troubleshooting, see our [Distributed Tracing troubleshooting](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting/).


## Send traces with SPM

```sh
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.SpmToken=<<SPM-METRICS-SHIPPING-TOKEN>> \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<LOGZIO_ACCOUNT_REGION_CODE>>` | Name of your Logz.io traces region e.g `us`, `eu`... |
| `<<SPM-METRICS-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |

## Deploy both charts with span metrics and service graph
**Note** `serviceGraph.enabled=true` will have no effect unless `traces.enabled` & `spm.enabled=true` is also set to `true`
```sh
helm install -n monitoring \
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

#### Deploy metrics chart with Kuberenetes object logs correlation
**Note** `k8sObjectsConfig.enabled=true` will have no effect unless `metrics.enabled` is also set to `true`
```sh
helm install  \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.k8sObjectsConfig.enabled=true \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO-REGION>> \
--set logzio-k8s-telemetry.secrets.k8sObjectsLogsToken=<<LOGZIO-LOG-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.ListenerHost=<<LISTENER-HOST>> \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name=<<P8S-LOGZIO-NAME>> \
--set logzio-k8s-telemetry.secrets.env_id=<<ENV-ID>> \
logzio-monitoring logzio-helm/logzio-monitoring
```

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

## Sending telemetry data from eks on fargate

To ship logs from pods running on Fargate, set the `fargateLogRouter.enabled` value to `true`. Doing so will deploy a dedicated `aws-observability` namespace and a `configmap` for the Fargate log router. For more information on EKS Fargate logging, please refer to the [official AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html).

```shell
helm install -n monitoring \
--set logs.enabled=true \
--set logzio-fluentd.fargateLogRouter.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.collector.mode=standalone \
--set logzio-k8s-telemetry.enableMetricsFilter.eks=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<CLUSTER-NAME>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics). |
| `<<P8S-LOGZIO-NAME>>` | The name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<CLUSTER-NAME>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<ENV-TAG>>` | Your custom name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<TRACING-SHIPPING-TOKEN>>` | Replace `<<TRACING-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing) of the account you want to ship to. |
| `<<LOGZIO_ACCOUNT_REGION_CODE>>` | Name of your Logz.io traces region e.g `us` or `eu`. You can find your region code in the [Regions and URLs](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#regions-and-urls/) table. |

## Handling image pull rate limit

In certain situations, such as with spot clusters where pods/nodes are frequently replaced, you may encounter the pull rate limit for images fetched from Docker Hub. This could result in the following error: `You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limits`.

To address this issue, you can use the `--set` commands provided below in order to access an alternative image repository:

```shell
--set logzio-k8s-telemetry.image.repository=ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib
--set logzio-k8s-telemetry.prometheus-pushgateway.image.repository=public.ecr.aws/logzio/prom-pushgateway
--set logzio-fluentd.image=public.ecr.aws/logzio/logzio-fluentd
--set logzio-fluentd.daemonset.init.containerImage=public.ecr.aws/docker/library/busybox
--set logzio-trivy.image=public.ecr.aws/logzio/trivy-to-logzio
```

## Upgrading logzio-monitoring to v3.0.0

Before upgrading your logzio-monitoring Chart to v3.0.0 with `helm upgrade`, note that you may encounter an error for some of the logzio-telemetry sub-charts.

There are two possible approaches to the upgrade you can choose from:
- Reinstall the chart.
- Before running the `helm upgrade` command, delete the old subcharts resources: `logzio-monitoring-prometheus-pushgateway` deployment and the `logzio-monitoring-prometheus-node-exporter` daemonset.

## Configuring logs in JSON format

This configuration sets up a log processor to parse, restructure, and clean JSON-formatted log messages for streamlined analysis and monitoring:

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

## Adding metric names to K8S 360 filter

To customize the metrics collected by Prometheus in your Kubernetes environment, you need to modify the `prometheusFilters` configuration in your Helm chart.

### Identify metrics to keep

Decide which metrics you need to add to your collection, formatted as a regex string (e.g., `new_metric_1|new_metric_2`).

### Set filters

Run the following command:

```shell
helm upgrade <RELEASE_NAME> logzio-helm/logzio-monitoring \
--set prometheusFilters.metrics.infrastructure.keep.aks="existing_metric_1|existing_metric_2|new_metric_1|new_metric_2" \
--set logzio-k8s-telemetry.enableMetricsFilter.<SERVICE>=true
```

* Replace `<RELEASE_NAME>` with the name of your Helm release.
* Replace `<SERVICE>` with the appropriate service name: `ask`, `eks` or `gke`.

## Applying Labels to Helm Chart Components

You can apply labels to your pods to help organize and manage the components of your deployment more effectively. Below are examples of how to apply labels to different components within the `logzio-k8s-telemetry` chart.

### Standalone Collector

To apply labels to the `standaloneCollector`, add the `podLabels` under the `standaloneCollector` section:

```yaml
logzio-k8s-telemetry:
  standaloneCollector:
    enabled: true
    podLabels:
      team: devops-tooling
```

Ensure that the `enabled` flag is set to `true` to activate the standalone collector with the specified labels.

### Other Components

Similarly, you can apply labels to other components such as kube-state-metrics and prometheus-node-exporter:

```yaml
logzio-k8s-telemetry:
  kube-state-metrics:
    podLabels:
      team: devops-tooling
  prometheus-node-exporter:
    podLabels:
      team: devops-tooling
```