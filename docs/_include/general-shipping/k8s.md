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
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
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
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```


| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |



Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-fluentd-for-kubernetes-logs/).

### Adding pod labels

To ensure that labels are applied correctly to the pods managed by the Logz.io collector, add the following section to your Helm chart configuration:

```yaml
logzio-k8s-telemetry:
  standaloneCollector:
    podLabels:
      team: devops-tooling
```


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
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set global.customLogsEndpoint="<<CUSTOM-HOST>>" \
logzio-monitoring logzio-helm/logzio-monitoring

```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LOGZIO-REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |
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
--set logzio-k8s-telemetry.metrics.enabled=true \
--set global.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO-REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). |


Encounter an issue? See our [troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/k8s-troubleshooting/).




### Custom Configuration

You can view the full list of the possible configuration values in the [logzio-k8s-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

To modify values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For example, for a parameter called `someField` in the `logzio-k8s-telemetry`'s `values.yaml` file, set it by adding the following to the `helm install` command:

```shell
--set logzio-k8s-telemetry.someField="my new value"
```


 </TabItem>
<TabItem value="tracing-data" label="Tracing and SPM" default>


## Send your traces

Together with Traces data you can also choose to send SPM or Service graph, or both.

```shell
helm install -n monitoring --create-namespace \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

## Send traces with SPM

```shell
helm install -n monitoring --create-namespace \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set logzio-apm-collector.spm.enabled=true \
--set global.logzioSpmToken="<<SPM-METRICS-SHIPPING-TOKEN>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

## Send Service Graph data

```shell
helm install -n monitoring --create-namespace \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<SPM-METRICS-SHIPPING-TOKEN>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
| `<<SPM-METRICS-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |

:::note
Encounter an issue? See our [Distributed Tracing troubleshooting](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting/).
:::

### Custom Configuration

You can view the full list of the possible configuration values in the [logzio-apm-collector Chart folder](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-apm-collector/VALUES.md).

To modify values found in the `logzio-apm-collector` folder, use the `--set` flag with the `logzio-apm-collector` prefix.

For example, for a parameter called `someField` in the `logzio-apm-collector`'s `values.yaml` file, set it by adding the following to the `helm install` command:

```shell
--set logzio-apm-collector.someField="my new value"
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
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


 </TabItem>
<TabItem value="trivy-data" label="Trivy" default>


## Scan your cluster for security vulnerabilities

```shell
helm install -n monitoring --create-namespace \
--set securityReport.enabled=true \
--set global.env_id="<<CLUSTER-NAME>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LOGZIO_REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |


 </TabItem>
<TabItem value="eks-fargate-data" label="EKS Fargate" default>



 ## Sending telemetry data from EKS on Fargate

Set the `fargateLogRouter.enabled` value to `true`. This deploys a dedicated `aws-observability` namespace and a `configmap` for the Fargate log router. Read more on EKS Fargate logging in the [official AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html).

```shell
helm install -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-fluentd.fargateLogRouter.enabled=true \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set logzio-k8s-telemetry.collector.mode=standalone \
--set logzio-k8s-telemetry.enableMetricsFilter.eks=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set global.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACING-SHIPPING-TOKEN>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
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

<TabItem value="resolve-readiness-probe-and-liveness-probe-failures" label="Readiness probe and Liveness probe failures" default>

## Resolve Readiness probe and Liveness probe failures

If, after installing the chart, the `logzio-apm-collector` or `logzio-spm-collector` (if you enabled SPM) pod fails to get scheduled on a node, and describing the pod shows the following errors:

```txt
Readiness probe failed: HTTP probe failed with statuscode: 503
Liveness probe failed: HTTP probe failed with statuscode: 503
```

Try increasing the initial delay for the liveness and readiness probes:

```sh
helm upgrade logzio-apm-collector logzio-helm/logzio-apm-collector -n monitoring \
--set livenessProbe.initialDelaySeconds=10 \
--set readinessProbe.initialDelaySeconds=10 \
--reuse-values
```

:::note
If `10s` is insufficient, try increasing it to `15s` or higher.
:::

 </TabItem>
</Tabs>


## Instrumentation
If you're using manual instrumentation or an instrumentation agent, configure it to export data to the Logz.io APM collector by setting the export/output address as follows:
```
logzio-apm-collector.monitoring.svc.cluster.local:<<PORT>>
```

:::note
Replace `<<PORT>>` based on the protocol your agent uses:
- 4317 for OTLP GRCP
- 4318 for OTLP HTTP
For a complete list, see [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-apm-collector/values.yaml#L71).
:::


## Enable auto-instrumentation

The OpenTelemetry Operator manages auto-instrumentation of workloads using OpenTelemetry instrumentation libraries, automatically generating traces and metrics.

To send the instrumentation data it generates to Logz.io, you need to enable the operator within the `logzio-monitoring` chart, along with either the `logzio-apm-collector` (for traces), `logzio-k8s-telemetry` (for metrics), or both, depending on the type of data you want to forward to the Logz.io platform.


:::caution
The Operator does not support Windows nodes at the moment.
:::


### Step by step

#### Step 1
Enable the OpenTelemetry operator in the chart
```sh
--set otel-operator.enabled=true \
```

:::note
It can take a few minutes for the OpenTelemetry Operator components to be installed and deployed on your cluster.
:::

#### Step 2
Add annotations to your relevant Kubernetes object. You can annotate individual resources such as a Deployment, StatefulSet, DaemonSet, or Pod, or apply annotations at the Namespace level to instrument all pods within that namespace. 
These annotations should specify the programming language used in your application:
```sh
instrumentation.opentelemetry.io/inject-<APP_LANGUAGE>: "monitoring/logzio-monitoring-instrumentation"
```

:::tip
`<APP_LANGUAGE>` can be one of `apache-httpd`, `dotnet`, `go`, `java`, `nginx`, `nodejs` or `python`.
:::

### Multi-container pods
By default, in multi-container pods, instrumentation is performed on the first container available in the pod spec. To fine tune which containers to instrument, add the below annotations to your pod:

```sh
instrumentation.opentelemetry.io/inject-<APP_LANGUAGE>: "monitoring/logzio-monitoring-instrumentation"
instrumentation.opentelemetry.io/<APP_LANGUAGE>-container-names: "myapp,myapp2"
instrumentation.opentelemetry.io/inject-<APP_LANGUAGE_2>: "monitoring/logzio-monitoring-instrumentation"
instrumentation.opentelemetry.io/<APP_LANGUAGE_2>-container-names: "myapp3"
```

:::tip
`<APP_LANGUAGE>` can be one of `apache-httpd`, `dotnet`, `go`, `java`, `nginx`, `nodejs` or `python`.
:::

:::caution
Go auto-instrumentation does not support multicontainer pods. When injecting Go auto-instrumentation the first pod should be the only pod you want instrumented.
:::

## Customize Auto-instrumentation

<Tabs>
<TabItem value="customize-propagator" label="Customize Propagator" default>

### Customize Propagator
The propagator specifies how context is injected into and extracted from carriers for distributed tracing.
By default, the propagators `tracecontext` (W3C Trace Context) and `baggage` (W3C Correlation Context) are enabled.
You can customize this to include other formats ([full list here](https://opentelemetry.io/docs/languages/sdk-configuration/general/#otel_propagators)) or set it to "none" to disable automatic propagation.
```sh
--set instrumentation.propagator={tracecontext, baggage, b3}
```

</TabItem>
<TabItem value="customize-sampler" label="Customize Sampler" default>

### Add a custom Sampler
You can specify a sampler to be used by the instrumentor. You'll need to specify the below:
- Sampler used to sample the traces ([available options](https://opentelemetry.io/docs/languages/sdk-configuration/general/#otel_traces_sampler))
- Sampler arguments ([Sampler type expected input](https://opentelemetry.io/docs/languages/sdk-configuration/general/#otel_traces_sampler_arg))

Example:
```shell
--set instrumentation.sampler.type="parentbased_always_on" \
--set instrumentation.sampler.argument="0.25"
```


</TabItem>
<TabItem value="tls-certificate-requirements" label="TLS certificate requirements" default>

### TLS certificate requirements
OpenTelemetry operator requires a TLS certificate. For more details, refer to [OpenTelemetry documentation](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-operator#tls-certificate-requirement).

There are 3 TLS certificate options, by default this chart is using option 2.

**1.** If you have `cert-manager` installed on your cluster, you can set `otel-operator.admissionWebhooks.certManager.enabled` to true and the cert-manager will generate a self-signed certificate for the otel-operator automatically.

```shell
--set otel-operator.admissionWebhooks.certManager.enabled=true \
```

**2.** Helm will automatically create a self-signed cert and secret for you. (Enabled by default by this chart)

**3.** Use your own self-signed certificate, To enable this option, set `otel-operator.admissionWebhooks.autoGenerateCert.enabled` to `false` and provide the necessary `certFile`, `keyFile` and `caFile`.

```shell
--set otel-operator.admissionWebhooks.autoGenerateCert.enabled=false \
--set otel-operator.admissionWebhooks.certFile="<<PEM_CERT_PATH>>" \
--set otel-operator.admissionWebhooks.keyFile="<<PEM_KEY_PATH>>" \
--set otel-operator.admissionWebhooks.caFile="<<CA_CERT_PATH>>" \
```
</TabItem>
<TabItem value="enable-go-instrumentation" label="Enable Go Instrumentation" default>

### Enable Go Instrumentation
Go Instrumentation is disabled by default in the OpenTelemetry Operator. To enable it, follow the below steps:

#### Step 1
Add the following configuration to your `values.yaml`:
```yaml
otel-operator:
  manager:
    extraArgs:
      - "--enable-go-instrumentation=true"
```

#### Step 2
Set the `OTEL_GO_AUTO_TARGET_EXE` environment variable in your Go application to the path of the target executable.


:::note
For further details, refer to the [OpenTelemetry Go Instrumentation documentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/v0.21.0/docs/how-it-works.md#opentelemetry-go-instrumentation---how-it-works).
:::


</TabItem>
</Tabs>


## Migrating to `logzio-monitoring` 7.x.x

### Step 1: Update helm repositories
Run the following command to ensure you have the latest chart versions:

```shell
helm repo update
```

### Step 2: Build the upgrade command
Choose the appropriate upgrade command for your current setup. If you're unsure of your configuration, use the following command to retrieve the current values

```shell
helm get values logzio-monitoring -n monitoring
```

:::caution Important
If you have enabled any of the following
- `logzio-k8s-events` (`deployEvents`)
- `logzio-trivy` (`securityReport`)
- `logzio-k8s-telemetry.k8sObjectsConfig`
You must use one of the Logs command options as part of the upgrade process.
:::

<Tabs>
<TabItem value="migrate-all" label="Logs, Metrics and Traces" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioMetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.traces.enabled=false \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \

# If you also send SPM or ServiceGraph, add the relevant enable flag for them and the token
--set logzio-apm-collector.spm.enabled=true \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<SPM-SHIPPING-TOKEN>>" \

--reuse-values
```


:::note
If you were using `logzio-logs-collector.secrets.logType`, add to your command `--set global.logType=<<LOG-TYPE>> \`
:::


:::note
Make sure to update your Instrumentation service endpoint from `logzio-monitoring-otel-collector.monitoring.svc.cluster.local` to `logzio-apm-collector.monitoring.svc.cluster.local`.
:::

</TabItem>

<TabItem value="migrate-logs-metrics" label="Logs and Metrics" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set global.logzioMetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--reuse-values
```


:::note
If you were using `logzio-logs-collector.secrets.logType`, add to your command `--set global.logType=<<LOG-TYPE>> \`
:::


</TabItem>

<TabItem value="migrate-metrics-traces" label="Metrics and Traces" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioMetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.traces.enabled=false \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \

# If you also send SPM or ServiceGraph, add the relevant enable flag for them and the token
--set logzio-apm-collector.spm.enabled=true \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<SPM-SHIPPING-TOKEN>>" \

--reuse-values
```


:::note
Make sure to update your Instrumentation service endpoint from `logzio-monitoring-otel-collector.monitoring.svc.cluster.local` to `logzio-apm-collector.monitoring.svc.cluster.local`.
:::

</TabItem>

<TabItem value="migrate-logs-traces" label="Logs and Traces" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.traces.enabled=false \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \

# If you also send SPM or ServiceGraph, add the relevant enable flag for them and the token
--set logzio-apm-collector.spm.enabled=true \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<SPM-SHIPPING-TOKEN>>" \

--reuse-values
```


:::note
If you were using `logzio-logs-collector.secrets.logType`, add to your command `--set global.logType=<<LOG-TYPE>> \`
:::


:::note
Make sure to update your Instrumentation service endpoint from `logzio-monitoring-otel-collector.monitoring.svc.cluster.local` to `logzio-apm-collector.monitoring.svc.cluster.local`.
:::

</TabItem>

<TabItem value="migrate-logs-only" label="Only Logs" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--reuse-values
```


:::note
If you were using `logzio-logs-collector.secrets.logType`, add to your command `--set global.logType=<<LOG-TYPE>> \`
:::

</TabItem>

<TabItem value="migrate-metrics-only" label="Only Metrics" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioMetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--reuse-values
```

</TabItem>

<TabItem value="migrate-traces-only" label="Only Traces" default>

```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set logzio-k8s-telemetry.traces.enabled=false \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACES-SHIPPING-TOKEN>>" \

# If you also send SPM or ServiceGraph, add the relevant enable flag for them and the token
--set logzio-apm-collector.spm.enabled=true \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<SPM-SHIPPING-TOKEN>>" \

--reuse-values
```


:::note
Make sure to update your Instrumentation service endpoint from `logzio-monitoring-otel-collector.monitoring.svc.cluster.local` to `logzio-apm-collector.monitoring.svc.cluster.local`.
:::

</TabItem>


</Tabs>


### Managing own secret
If you manage your own secret for the Logz.io charts, please also add to your command:

 ```shell
--set sub-chart-name.secret.name="<<NAME-OF-SECRET>>" \
--set sub-chart-name.secret.enabled=false \
```

:::caution Important
This change is not relevant for the `logzio-k8s-telemetry` chart.
:::


Replace `sub-chart-name` with the name of the sub chart which you manage the secrets for.

For example, if you manage secret for both `logzio-logs-collector` and for `logzio-trivy`, use:

 ```shell
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring -n monitoring --version 7.0.0 \
--set global.logzioRegion="<<LOGZIO-REGION>>" \
--set global.env_id="<<ENV-ID>>" \
--set logzio-logs-collector.secret.name="<<NAME-OF-SECRET>>" \
--set logzio-logs-collector.secret.enabled=false \
--set logzio-trivy.secret.name="<<NAME-OF-SECRET>>" \
--set logzio-trivy.secret.enabled=false \
--reuse-values
```

