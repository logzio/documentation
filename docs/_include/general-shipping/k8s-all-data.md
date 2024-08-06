## Send All Telemetry Data (logs, metrics, traces and security reports)


Send all of your telemetry data using one single Helm chart:


```sh
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
helm install  -n monitoring --create-namespace \
--set logs.enabled=true \
--set logzio-logs-collector.secrets.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-logs-collector.secrets.logzioRegion="<<LOGZIO-REGION>>" \
--set logzio-logs-collector.secrets.env_id="<<CLUSTER-NAME>>" \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set logzio-k8s-telemetry.secrets.MetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
--set logzio-k8s-telemetry.secrets.p8s_logzio_name="<<ENV-ID>>" \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO-REGION>>" \
--set logzio-k8s-telemetry.spm.enabled=true \
--set logzio-k8s-telemetry.secrets.env_id="<<ENV-ID>>" \
--set logzio-k8s-telemetry.secrets.SpmToken="<<SPM-ACCOUNT-SHIPPING-TOKEN>>" \
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
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<SPM-ACCOUNT-SHIPPING-TOKEN>>` | Your [SPM account shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping) |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO-REGION>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
