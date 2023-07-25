---
id: Kubernetes
title: Kubernetes
overview: logzio-k8s-telemetry allows you to ship metrics from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---
 

####  Overview


**logzio-k8s-telemetry** allows you to ship metrics from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

This chart is a fork of the [opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
  
It is also dependent on the [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/tree/master/charts/kube-state-metrics), [prometheus-node-exporter](https://github.com/helm/charts/tree/master/stable/prometheus-node-exporter) and [prometheus-pushgateway](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-pushgateway) charts, which are installed by default. 
  
To disable the dependency during installation, set `kubeStateMetrics.enabled`, `nodeExporter.enabled` or `pushGateway.enabled` to `false`.
  
For applications that run on Kubernetes, enable the Prometheus scrape feature:

```yaml
prometheus.io/scrape: true
```

###### Sending logs from nodes with taints

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

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7BMEKdVrHKPQtt5IgaQ7Bw", "4knWrgcTsEj5kqNXJTES87", "NwO3pdosDJVRWo6i9QJEy", "6RFNnTgcwAmmFnuRropnGu", "5lqRpL1ADesghZbNCEPaZ9"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 
  

  

#### Standard configuration for Linux nodes

 
  
##### Add logzio-helm repo to your helm repo list

  ```shell
  helm repo add logzio-helm https://logzio.github.io/logzio-helm
  helm repo update
  ```

##### Deploy the Helm chart

1. Configure the relevant parameters in the following code:

   ```
   helm install --namespace <<YOUR-NAMESPACE>>  \
   --set metrics.enabled=true \
   --set secrets.MetricsToken=<<METRICS-SHIPPING-TOKEN>> \
   --set secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
   --set secrets.p8s_logzio_name=<<ENV-TAG>> \
   logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
   ```

   * Replace `<<YOUR_NAMESPACE>>` with the required namespace.

   * {@include: ../_include//metric-shipping/replace-metrics-token.html}

   * {@include: ../_include//log-shipping/listener-var.html}

   * Replace `<<ENV-TAG>>` with the name for the environment's metrics, to easily identify the metrics for each environment.

2. Run the code.

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7BMEKdVrHKPQtt5IgaQ7Bw", "4knWrgcTsEj5kqNXJTES87", "NwO3pdosDJVRWo6i9QJEy", "6RFNnTgcwAmmFnuRropnGu", "5lqRpL1ADesghZbNCEPaZ9"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [Kubernetes troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/k8-helm-opentelemetry-troubleshooting.html).
  
  

####  Customizing Helm chart parameters

 

##### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

###### Example:

```
helm install logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry -f my_values.yaml 
```

##### Customize the metrics collected by the Helm chart 

The default configuration uses the Prometheus receiver with the following scrape jobs:

* Cadvisor: Scrapes container metrics
* Kubernetes service endpoints: These jobs scrape metrics from the node exporters, from Kube state metrics, from any other service for which the `prometheus.io/scrape: true` annotaion is set, and from services that expose Prometheus metrics at the `/metrics` endpoint.

To customize your configuration, edit the `config` section in the `values.yaml` file.

 

For troubleshooting this solution, see our [Kubernetes troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/k8-helm-opentelemetry-troubleshooting.html).

  

#### Uninstalling the Chart

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```

