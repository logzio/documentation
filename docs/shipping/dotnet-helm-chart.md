---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---
 

Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts. This integration allows you to collect and ship diagnostic metrics of your .NET application in Kubernetes to Logz.io, using dotnet-monitor and OpenTelemetry. logzio-dotnet-monitor runs as a sidecar in the same pod as the .NET application.

###### Sending metrics from nodes with taints

If you want to ship metrics from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:
  
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

  

#### Standard configuration

 

##### Select the namespace

This integration will be deployed in the namespace you set in values.yaml. The default namespace for this integration is logzio-dotnet-monitor.

To select a different namespace, run:

```shell
kubectl create namespace <<NAMESPACE>>
```

* Replace `<<NAMESPACE>>` with the name of your namespace.


##### Add `logzio-helm` repo
  
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```


###### Run the Helm deployment code

```shell
helm install -n <<NAMESPACE>> \
--set secrets.logzioURL='<<LISTENER-HOST>>:8053' \
--set secrets.logzioToken='<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>' \
--set-file dotnetAppContainers='<<DOTNET_APP_CONTAINERS_FILE>>' \
logzio-dotnet-monitor logzio-helm/logzio-dotnet-monitor
```

* Replace `<<NAMESPACE>>` with the namespace you selected for this integration. The default value is `default`.
{@include: ../_include/log-shipping/listener-var.html} {@include: ../_include/log-shipping/log-shipping-token.html}
* Replace `<<DOTNET_APP_CONTAINERS_FILE>>` with your .NET application containers file. Make sure your main .NET application container has the following volumeMount:

```yaml
volumeMounts:
  - mountPath: /tmp
    name: diagnostics
```


##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, then open [Logz.io](https://app.logz.io/). You can search for your metrics in Logz.io by searching `{job="dotnet-monitor-collector"}`

 


####  Customizing Helm chart parameters


##### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install` or `--set-file key=value[,key=value]`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

##### Customization parameters

| Parameter | Description | Default |
|---|---|---|
| `nameOverride` | Overrides the Chart name for resources. | `""` |
| `fullnameOverride` | Overrides the full name of the resources. | `""` |
| `apiVersions.deployment` | Deployment API version. | `apps/v1` |
| `apiVersions.configmap` | Configmap API version. | `v1` |
| `apiVersions.secret` | Secret API version. | `v1` |
| `namespace` | Chart's namespace. | `logzio-dotnet-monitor` |
| `replicaCount` | The number of replicated pods, the deployment creates. | `1` |
| `labels` | Pod's labels. | `{}` |
| `annotations` | Pod's annotations. | `{}` |
| `customSpecs` | Custom spec fields to add to the deployment. | `{}` |
| `dotnetAppContainers` | List of your .NET application containers to add to the pod. | `[]` |
| `logzioDotnetMonitor.name` | The name of the container that collects and ships diagnostic metrics of your .NET application to Logz.io (sidecar) | `logzio-dotnet-monitor` |
| `logzioDotnetMonitor.image.name` | Name of the image that is going to run in `logzioDotnetMonitor.name` container | `logzio/logzio-dotnet-monitor` |
| `logzioDotnetMonitor.image.tag` | The tag of the image that is going to run in `logzioDotnetMonitor.name` container | `latest` |
| `logzioDotnetMonitor.ports` | List of ports the `logzioDotnetMonitor.name` container exposes | `52325` |
| `tolerations` | List of tolerations to applied to the pod. | `[]` | 
| `customVolumes` | List of custom volumes to add to deployment. | `[]` |
| `customResources` | Custom resources to add to helm chart deployment (make sure to separate each resource with `---`). | `{}` |
| `secrets.logzioURL` | Secret with your Logz.io listener url. | `https://listener.logz.io:8053` |
| `secrets.logzioToken` | Secret with your Logz.io metrics shipping token. | `""` |
| `configMap.dotnetMonitor` | The dotnet-monitor configuration. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/dotnet-monitor/values.yaml). |
| `configMap.opentelemetry` | The opentelemetry configuration. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/dotnet-monitor/values.yaml). |


* To get additional information about dotnet-monitor configuration, click [here](https://github.com/dotnet/dotnet-monitor/blob/main/documentation/api/metrics.md).
* To see well-known providers and their counters, click [here](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/available-counters).

#### Uninstalling the Chart

The Uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `dotnet-monitor-collector` deployment, use the following command:

```shell
helm uninstall dotnet-monitor-collector
```

For troubleshooting this solution, see our [.NET with helm troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/dotnet-helm-troubleshooting.html).

 
