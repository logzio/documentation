---
id: Unified-Helm-Chart
title: Unified Helm Chart
overview: The logzio-monitoring Helm Chart ships your Kubernetes telemetry (logs, metrics, traces and security reports) to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Monitoring', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kubernetes.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ["7nILXHYFZbThgTSMObUxkw", "5TGD77ZKuTiZUXtiM51m6V", "6pY6DKD0oQJL4sO7bW728", "5kkUAuEwA0Ygvlgm9iXTHY", "53g5kSILqoj1T10U1jnvKV", "5e1xRaDdQnOvs5LCuwKCh5", "7Cy6DUN78jlKUtMCsbt6GC", "29HGYsE3kgFEdgJbalTqeY", "1Hij49FKdnAKVJTjOmpDbH" ]
metrics_alerts: []
---




The `logzio-monitoring` Helm Chart ships your Kubernetes telemetry (logs, metrics, traces and security reports) to your Logz.io account.

:::note
Please be aware that this project is presently in its beta stage, and as such, it may undergo alterations.
:::


:::note
To get the most out of Kubernetes 360, try out dedicated [dashboard](/user-guide/k360/kubernetes-360-pre.html).
:::


 {@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics. <!-- logzio-inject:install:grafana:dashboards ids=["7nILXHYFZbThgTSMObUxkw", "5TGD77ZKuTiZUXtiM51m6V", "6pY6DKD0oQJL4sO7bW728", "5kkUAuEwA0Ygvlgm9iXTHY", "53g5kSILqoj1T10U1jnvKV", "5e1xRaDdQnOvs5LCuwKCh5", "7Cy6DUN78jlKUtMCsbt6GC", "29HGYsE3kgFEdgJbalTqeY", "1Hij49FKdnAKVJTjOmpDbH" ] --> {@include: ../_include/metric-shipping/generic-dashboard.html}








##### Check if you have any taints on your nodes

```shell
kubectl get nodes -o json | jq '"\(.items[].metadata.name) \(.items[].spec.taints)"'
```

If you want to ship logs from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:

```yaml
tolerations:
- key:
  operator:
  value:
  effect:
```

##### Add the Helm Chart

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### Deploy the Chart

```shell
helm install -n monitoring \
--set logs.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set logzio-fluentd.env_id="<<ENV-ID>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<ENV-TAG>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACES-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | {@include: ../_include//log-shipping/log-shipping-token.html} |
| `<<LISTENER-HOST>>` | {@include: ../_include/log-shipping/listener-var.html}. |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<P8S-LOGZIO-NAME>>` | The name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<ENV-TAG>>` | Your custom name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<TRACES-SHIPPING-TOKEN>>` | Replace `<<TRACING-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing) of the account you want to ship to. |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us` or `eu`. You can find your region code in the [Regions and URLs](https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls) table. |

##### Check Logz.io for your data

Give your data some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7nILXHYFZbThgTSMObUxkw", "5TGD77ZKuTiZUXtiM51m6V", "6pY6DKD0oQJL4sO7bW728", "5kkUAuEwA0Ygvlgm9iXTHY", "53g5kSILqoj1T10U1jnvKV", "5e1xRaDdQnOvs5LCuwKCh5", "7Cy6DUN78jlKUtMCsbt6GC", "29HGYsE3kgFEdgJbalTqeY", "1Hij49FKdnAKVJTjOmpDbH" ] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}



### Collecting span metrics and Trivy reports

To enable the `logzio-monitoring` Helm Chart collect span metrics and Trivy reports, add the following command to the default deployment:

```shell
helm install -n monitoring \
--set logzio-k8s-telemetry.secrets.SpmToken=<<SPM-SHIPPING-TOKEN>> \
--set securityReport.enabled=true \
--set logzio-trivy.env_id="<<ENV-ID>>" \
--set logzio-trivy.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-trivy.secrets.logzioListener="<<LISTENER-HOST>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<SPM-SHIPPING-TOKEN>>` | Your [span metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<LOG-SHIPPING-TOKEN>>` | {@include: ../_include//log-shipping/log-shipping-token.html} |
| `<<LISTENER-HOST>>` | {@include: ../_include/log-shipping/listener-var.html}. |


### Further configuration

You can modify the default `logzio-monitoring` Helm Chart by using the `--set` flag in your `helm install` command:

| Parameter	| Description | Default |
| --- | --- | --- |
| `logs.enabled` | Enable to send k8s logs | `false` |
| `metricsOrTraces` | Enable to send k8s metrics or traces | `false` |

##### Modifying the configuration for logs

You can see a full list of the possible configuration values in the [logzio-fluentd Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).

If you would like to modify any of the values found in the `logzio-fluentd` folder, use the `--set` flag with the `logzio-fluentd` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:

```sh
--set logzio-fluentd.someField="my new value"
```
You can add `log_type` annotation with a custom value, which will be parsed into a `log_type` field with the same value.


##### Modifying the configuration for metrics and traces

You can see a full list of the possible configuration values in the [logzio-telemetry Chart folder](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-telemetry).

If you would like to modify any of the values found in the `logzio-telemetry` folder, use the `--set` flag with the `logzio-k8s-telemetry` prefix.

For instance, if there is a parameter called `someField` in the `logzio-telemetry`'s `values.yaml` file, you can set it by adding the following to the `helm install` command:


```sh
--set logzio-k8s-telemetry.someField="my new value"
```

### Sending telemetry data from eks on fargate

To ship logs from pods running on Fargate, set the `fargateLogRouter.enabled` value to `true`. Doing so will deploy a dedicated `aws-observability` namespace and a `configmap` for the Fargate log router. For more information on EKS Fargate logging, please refer to the [official AWS documentation]((https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html).

```shell
helm install -n monitoring \
--set logs.enabled=true \
--set logzio-fluentd.fargateLogRouter.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<ENV-TAG>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACES-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | {@include: ../_include//log-shipping/log-shipping-token.html} |
| `<<LISTENER-HOST>>` | {@include: ../_include/log-shipping/listener-var.html}. |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<P8S-LOGZIO-NAME>>` | The name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<ENV-TAG>>` | Your custom name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<TRACES-SHIPPING-TOKEN>>` | Replace `<<TRACING-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing) of the account you want to ship to. |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us` or `eu`. You can find your region code in the [Regions and URLs](https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls) table. |

### Handling image pull rate limit

In certain situations, such as with spot clusters where pods/nodes are frequently replaced, you may encounter the pull rate limit for images fetched from Docker Hub. This could result in the following error: Y`ou have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limits`.

To address this issue, you can use the `--set` commands provided below in order to access an alternative image repository:

```shell
--set logzio-k8s-telemetry.image.repository=ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib
--set logzio-k8s-telemetry.prometheus-pushgateway.image.repository=public.ecr.aws/logzio/prom-pushgateway
--set logzio-fluentd.image=public.ecr.aws/logzio/logzio-fluentd
--set logzio-trivy.image=public.ecr.aws/logzio/trivy-to-logzio
```
