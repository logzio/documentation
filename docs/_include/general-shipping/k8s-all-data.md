## Send All Telemetry Data (logs, metrics, traces and security reports)


Send all of your telemetry data using one single Helm chart:


```shell
helm install  -n monitoring --create-namespace \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<ENV-ID>>" \
--set logs.enabled=true \
--set global.logzioLogsToken="<<LOG-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.metrics.enabled=true \
--set global.logzioMetricsToken="<<METRICS-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.k8sObjectsConfig.enabled=true \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-apm-collector.spm.enabled=true \
--set logzio-apm-collector.serviceGraph.enabled=true \
--set global.logzioSpmToken="<<METRICS-SHIPPING-TOKEN>>" \
--set securityReport.enabled=true \
--set deployEvents.enabled=true \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | Your [logs shipping token](https://app.logz.io/#/dashboard/settings/general). |
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<METRICS-SHIPPING-TOKEN>>` | Your [metrics shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<ENV-ID>>` | The name for your environment's identifier, to easily identify the telemetry data for each environment. For example, your cluster name. |
| `<<TRACING-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). |
| `<<LOGZIO_ACCOUNT_REGION_CODE>>` | Your Logz.io [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions) |
