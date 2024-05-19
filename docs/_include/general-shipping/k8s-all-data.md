## All telemetry (logs, metrics, traces and security reports) at once


To enjoy the full Kubernetes 360 experience, you can send all your telemetry data to Logz.io using one single Helm chart:

```sh
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
helm install  -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-fluentd.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-fluentd.secrets.logzioListener="<<LISTENER-HOST>>" \
--set logzio-fluentd.env_id="<<ENV-ID>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<ENV-ID>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.env_id="<<ENV-ID>>" \
--set logzio-k8s-telemetry.secrets.SpmToken="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.serviceGraph.enabled=true \
--set logzio-k8s-telemetry.k8sObjectsConfig.enabled=true \
--set logzio-k8s-telemetry.secrets.k8sObjectsLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set securityReport.enabled=true \
--set logzio-trivy.env_id="<<ENV-ID>>" \
--set logzio-trivy.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-trivy.secrets.logzioListener="<<LISTENER-HOST>>" \
--set deployEvents.enabled=true \
--set logzio-k8s-events.secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-k8s-events.secrets.logzioListener="<<LISTENER-HOST>>" \
--set logzio-k8s-events.secrets.env_id="<<ENV-ID>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<P8S-LOGZIO-NAME>>` | The name for the environment's metrics, to easily identify the metrics for each environment. |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |

### Applying Labels to Helm Chart Components

You can apply labels to your pods to help organize and manage the components of your deployment more effectively. Below are examples of how to apply labels to different components within the `logzio-k8s-telemetry` chart.

#### Standalone Collector

To apply labels to the `standaloneCollector`, add the `podLabels` under the `standaloneCollector` section:

```yaml
logzio-k8s-telemetry:
  standaloneCollector:
    enabled: true
    podLabels:
      team: devops-tooling
```

Ensure that the `enabled` flag is set to `true` to activate the standalone collector with the specified labels.

#### Other Components

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