---
id: Kubernetes
title: Kubernetes
overview: Send Kubernetes logs, metrics and traces to Logz.io.
product: ['logs', 'metrics', 'tracing']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kubernetes.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1', '1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
drop_filter: []
drop_filter: []
---

## Logs
 
Fluentd is an open source data collector and a great option because of its flexibility. This implementation uses a Fluentd DaemonSet to collect Kubernetes logs and send them to Logz.io. The Kubernetes DaemonSet ensures that some or all nodes run a copy of a pod.


The image used in this integration comes pre-configured for Fluentd to gather all logs from the Kubernetes node environment and append the proper metadata to the logs. If you prefer to customize your Fluentd configuration, you can edit it before it's deployed.


:::note
The latest version pulls the image from `logzio/logzio-fluentd`. Previous versions pulled the image from `logzio/logzio-k8s`.
:::
 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
 

For troubleshooting this solution, see our [user guide](https://docs.logz.io/user-guide/kubernetes-troubleshooting/).

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


### K8S version compatibility

Your Kubernetes version may affect your options, as follows:

* **K8S 1.19.3+** - If you're running on K8S 1.19.3+ or later, be sure to use the DaemonSet that supports a containerd at runtime. It can be downloaded and customized from[`logzio-daemonset-containerd.yaml`](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml).

* **K8S 1.16 or earlier** - If you're running K8S 1.16 or earlier, you may need to manually change the API version in your DaemonSet to `apiVersion: rbac.authorization.k8s.io/v1beta1`.

  The API versions of `ClusterRole` and `ClusterRoleBinding` are found in `logzio-daemonset-rbac.yaml` and `logzio-daemonset-containerd.yaml`.
  
  If you are running K8S 1.17 or later, the DaemonSet is set to use `apiVersion: rbac.authorization.k8s.io/v1` by default. No change is needed.

* **ARM architecture** is supported as of logzio/logzio-fluentd:1.0.2.

{@include: ../../_include//log-shipping/multiline-logs-fluentd.md}
 

## Deploy logzio-k8s with default configuration

For most environments, we recommend using the default configuration.
However, you can deploy a custom configuration if your environment needs it.


### Deploy Fluentd as a DaemonSet on Kubernetes


#### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.


```shell
kubectl create namespace monitoring
```


#### Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

```shell
kubectl create secret generic logzio-logs-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
  -n monitoring
```

#### Deploy the DaemonSet

##### For an RBAC cluster:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-rbac.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

##### For a non-RBAC cluster:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

##### For container runtime Containerd:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).

 
 

## Deploy logzio-k8s with custom configuration

You can customize the configuration of your Fluentd container by editing either your DaemonSet or your Configmap.


 


### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.


```shell
kubectl create namespace monitoring
```

### Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret.


```shell
kubectl create secret generic logzio-logs-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
  -n monitoring
```

{@include: ../../_include//general-shipping/replace-placeholders.html}


### Configure Fluentd

There are 3 DaemonSet options: [RBAC DaemonSet](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-rbac.yaml), [non-RBAC DaemonSet](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset.yaml), [Containerd](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml). Download the relevant DaemonSet and open it in your text editor to edit it.

If you wish to make advanced changes in your Fluentd configuration, you can download and edit the [configmap yaml file](https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml).


{@include: ../../_include/k8s-fluentd.md}

#### Good to know

* If `FLUENT_FILTER_KUBERNETES_URL` is not specified, the environment variables `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT` will be used, as long as both of them are  present. Typically, they are present when running Fluentd in a pod.

* Note that `FLUENT_FILTER_KUBERNETES_URL` does not appear in the default environment variable list in the DaemonSet.
If you wish to use this variable, you'll have to add it manually to the DaemonSet's environment variables.

* Verify that your node / k8s instance timezone is running in UTC timezone for your container logs to be parsed and shipped correctly. Otherwise replace `time_format` line in the config with `%Y-%m-%dT%H:%M:%S.%N%:z`. For more details about formatting see this [doc](https://docs.ruby-lang.org/en/2.4.0/Time.html#method-i-strftime).

### Deploy the DaemonSet

#### For the RBAC DaemonSet:

```shell
kubectl apply -f /path/to/logzio-daemonset-rbac.yaml -f /path/to/configmap.yaml
```

#### For the non-RBAC DaemonSet:

```shell
kubectl apply -f /path/to/logzio-daemonset.yaml -f /path/to/configmap.yaml
```

#### For container runtime Containerd:

```shell
kubectl apply -f /path/to/logzio-daemonset-containerd.yaml -f /path/to/configmap.yaml
```


### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).

 


#### Disabling systemd input

To suppress Fluentd system messages, set the `FLUENTD_SYSTEMD_CONF` environment variable to `disable` in your Kubernetes environment.

##### Exclude logs from certain namespaces

If you wish to exclude logs from certain namespaces, add the following to your Fluentd configuration:

```shell
<match kubernetes.var.log.containers.**_NAMESPACE_**>
  @type null
</match>
```

Replace `NAMESPACE` with the name of the namespace you need to exclude logs from. 
  
If you need to specify multiple namespaces, add another `kubernetes.var.log.containers.**_NAMESPACE_**` line to the above function as follows:

```shell
<match kubernetes.var.log.containers.**_NAMESPACE1_** kubernetes.var.log.containers.**_NAMESPACE2_**>
  @type null
</match>
```

 

{@include: ../../_include//log-shipping/multiline-fluentd-plugin.md}

  



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

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7BMEKdVrHKPQtt5IgaQ7Bw", "4knWrgcTsEj5kqNXJTES87", "NwO3pdosDJVRWo6i9QJEy", "6RFNnTgcwAmmFnuRropnGu", "5lqRpL1ADesghZbNCEPaZ9"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  

  

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

   * {@include: ../../_include//metric-shipping/replace-metrics-token.html}

   * {@include: ../../_include//log-shipping/listener-var.html}

   * Replace `<<ENV-TAG>>` with the name for the environment's metrics, to easily identify the metrics for each environment.

2. Run the code.

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7BMEKdVrHKPQtt5IgaQ7Bw", "4knWrgcTsEj5kqNXJTES87", "NwO3pdosDJVRWo6i9QJEy", "6RFNnTgcwAmmFnuRropnGu", "5lqRpL1ADesghZbNCEPaZ9"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

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



####  Overview


**logzio-k8s-telemetry** allows you to ship metrics from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.
For AKS clusters, this chart also allows you to ship Windows node metrics.

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

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5jMvBtrxQwMo0GuDO13kpb", "5BjRR3NuNQb3XHVPhn3HQ0", "2TRgFib4ICfKsrzS5oJwgC", "1EcVjdr5c6heqbxpd6Zs8X"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 


  

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

   * {@include: ../../_include//metric-shipping/replace-metrics-token.html}

   * {@include: ../../_include//log-shipping/listener-var.html}

   * Replace `<<ENV-TAG>>` with the name for the environment's metrics, to easily identify the metrics for each environment.

2. Run the code.

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5jMvBtrxQwMo0GuDO13kpb", "5BjRR3NuNQb3XHVPhn3HQ0", "2TRgFib4ICfKsrzS5oJwgC", "1EcVjdr5c6heqbxpd6Zs8X"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [AKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/aks-helm-opentelemetry-troubleshooting.html).
  
  

#### Standard configuration for Windows nodes

 
  
##### Add logzio-helm repo to your helm repo list

  ```shell
  helm repo add logzio-helm https://logzio.github.io/logzio-helm
  helm repo update
  ```

##### Update your Windows node pool credentials (if needed)
  
To extract and scrape metrics from Windows nodes, you need to install a Windows Exporter service on the node host. To do this, you need to establish a SSH connection to the node by authenticating with a username and password. The `windows-exporter-installer` job performs the installation on each Windows node using the provided Windows credentials. The default username for Windows node pool is `azureuser`.
  
If your Windows node pool does not share the same username and password across the nodes, you will need to run the `windows-exporter-installer` job for each node pool using the relevant credentials. You can change your Windows node pool password in AKS cluster with the following command:


   ```
   az aks update \
   --resource-group $RESOURCE_GROUP \
   --name $CLUSTER_NAME \
   --windows-admin-password $NEW_PW
   ```

   * Replace `RESOURCE_GROUP` with the resource group name.
   * Replace `CLUSTER_NAME` with the cluster name.
   * Replace `NEW_PW` with the password selected for this pool.

##### Deploy the Helm chart

1. Configure the relevant parameters in the following code:

   ```
   helm install --namespace <<YOUR-NAMESPACE>>  \
   --set metrics.enabled=true \
   --set secrets.MetricsToken=<<METRICS-SHIPPING-TOKEN>> \
   --set secrets.ListenerHost="https://<<LISTENER-HOST>>:8053" \
   --set secrets.p8s_logzio_name=<<ENV-TAG>> \
   --set secrets.windowsNodeUsername=<<WINDOWS-NODE-USERNAME>> \
   --set secrets.windowsNodePassword=<<WINDOWS-NODE-PASSWORD>> \
   logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
   ```

   * Replace `<<YOUR_NAMESPACE>>` with the required namespace.

   * {@include: ../../_include//metric-shipping/replace-metrics-token.html}

   * {@include: ../../_include//log-shipping/listener-var.html}

   * Replace `<<ENV-TAG>>` with the name for the environment's metrics, to easily identify the metrics for each environment.

   * Replace `<WINDOWS-NODE-USERNAME>>` with the username for the Node pool you want the Windows Exporter to be installed on.

   * Replace `<<WINDOWS-NODE-PASSWORD>>` with the password for the Node pool you want the Windows exporter to be installed on.

2. Run the code.

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5jMvBtrxQwMo0GuDO13kpb", "5BjRR3NuNQb3XHVPhn3HQ0", "2TRgFib4ICfKsrzS5oJwgC", "1EcVjdr5c6heqbxpd6Zs8X" ] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [AKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/aks-helm-opentelemetry-troubleshooting.html).
  
  

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

 

For troubleshooting this solution, see our [AKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/aks-helm-opentelemetry-troubleshooting.html).

  

#### Uninstalling the Chart

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```



###### Overview

You can use a Helm chart to ship k8s logs to Logz.io via Filebeat from Linux and Windows nodes.

Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts.
Logzio-k8s-logs allows you to ship logs from your Kubernetes cluster to Logz.io.
You can either deploy this Daemonset with the standard Filebeat configuration or with Filebeat Autodiscover. (Learn more about [Filebeat Autodiscover](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover.html) from Elastic.)

Filebeat's basic configuration tends to split longer, multiline logs into multiple logs - 1 log per line. See the relevant tab for details and options for controlling this setting.

:::note
Helm 2 reached [EOL on November 2020](https://helm.sh/blog/2019-10-22-helm-2150-released/#:~:text=6%20months%20after%20Helm%203's,Helm%202%20will%20formally%20end). This document follows the command syntax recommended for Helm 3, but the Chart will work with both Helm 2 and Helm 3.
:::
 

For troubleshooting this solution, see our [user guide](https://docs.logz.io/user-guide/kubernetes-troubleshooting/).


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

 

#### Standard configuration

**Before you begin, you'll need**:

* [Helm CLI](https://helm.sh/docs/intro/install/) installed
* Outgoing traffic to destination port 5015 allowed

 

##### Add logzio-k8s-logs repo to your helm repo list

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update

```

##### Deploy

Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.

Replace `<<LISTENER-REGION>>` with your region’s code (for example, `eu`). For more information on finding your account’s region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html).

Replace `<<CLUSTER-NAME>>` with your cluster's name.

```shell
helm install --namespace=kube-system \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioRegion='<<LISTENER-REGION>>' \
--set secrets.clusterName='<<CLUSTER-NAME>>' \
logzio-k8s-logs logzio-helm/logzio-k8s-logs
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Logz.io](https://app.logz.io/).

 
  

#### Autodiscover configuration

Autodiscover allows you to adapt settings as changes happen. By defining configuration templates, the autodiscover subsystem can monitor services as they start running.



 

##### Add logzio-k8s-logs repo to your helm repo list

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### Deploy

In the following commands, make the following changes:

* Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.

* Replace `<<LISTENER-REGION>>` with your region’s code (for example, `eu`). For more information on finding your account’s region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html).

* Replace `<<CLUSTER-NAME>>` with your cluster's name.

* Use `--set configType='<<TYPE>>'` for linux based filebeat and/or `--set filebeatWindowsConfigType='<<TYPE>>'` for windows based filebeat.


This Daemonset's default autodiscover configuration is [hints based](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover-hints.html). If you wish to deploy it use:

```shell
helm install --namespace=kube-system \
--set configType='autodiscover' \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioRegion='<<LISTENER-REGION>>' \
--set secrets.clusterName='<<CLUSTER-NAME>>' \
logzio-k8s-logs logzio-helm/logzio-k8s-logs
```

If you have a custom configuration, deploy with:

```shell
helm install --namespace=kube-system \
--set configType='auto-custom' \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioRegion='<<LISTENER-REGION>>' \
--set secrets.clusterName='<<CLUSTER-NAME>>' \
--set-file filebeatConfig.autoCustomConfig=/path/to/your/config.yaml \
logzio-k8s-logs logzio-helm/logzio-k8s-logs
```

If you're using a custom config, please make sure that you're using a `.yaml` file with the following structure:

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```
filebeat.yml: |-
  filebeat.autodiscover:
  #....
    # your autodiscover config
    # ...
  processors:
    - add_cloud_metadata: ~
  fields:
    logzio_codec: ${LOGZIO_CODEC}
    token: ${LOGZIO_LOGS_SHIPPING_TOKEN}
    cluster: ${CLUSTER_NAME}
    type: ${LOGZIO_TYPE}
  fields_under_root: ${FIELDS_UNDER_ROOT}
  ignore_older: ${IGNORE_OLDER}
  output:
    logstash:
      hosts: ["${LOGZIO_LOGS_LISTENER_HOST}:5015"]
      ssl:
        certificate_authorities: ['/etc/pki/tls/certs/SectigoRSADomainValidationSecureServerCA.crt']
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see Kubernetes log shipping troubleshooting.

 

#### Uninstalling the Chart

The command removes all the k8s components associated with the chart and deletes the release.  
To uninstall the `logzio-k8s-logs` deployment:

```shell
helm uninstall --namespace=kube-system logzio-k8s-logs
```

 

#### Autodiscover configuration

Autodiscover allows you to adapt settings as changes happen. By defining configuration templates, the autodiscover subsystem can monitor services as they start running.



 

##### Add logzio-k8s-logs repo to your helm repo list

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### Deploy

In the following commands, make the following changes:

* Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.

* Replace `<<LISTENER-REGION>>` with your region’s code (for example, `eu`). For more information on finding your account’s region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html).

* Replace `<<CLUSTER-NAME>>` with your cluster's name.

* Use `--set configType='<<TYPE>>'` for linux based filebeat and/or `--set filebeatWindowsConfigType='<<TYPE>>'` for windows based filebeat.


This Daemonset's default autodiscover configuration is [hints based](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover-hints.html). If you wish to deploy it use:

```shell
helm install --namespace=kube-system \
--set configType='autodiscover' \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioRegion='<<LISTENER-REGION>>' \
--set secrets.clusterName='<<CLUSTER-NAME>>' \
logzio-k8s-logs logzio-helm/logzio-k8s-logs
```

If you have a custom configuration, deploy with:

```shell
helm install --namespace=kube-system \
--set configType='auto-custom' \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioRegion='<<LISTENER-REGION>>' \
--set secrets.clusterName='<<CLUSTER-NAME>>' \
--set-file filebeatConfig.autoCustomConfig=/path/to/your/config.yaml \
logzio-k8s-logs logzio-helm/logzio-k8s-logs
```

If you're using a custom config, please make sure that you're using a `.yaml` file with the following structure:

```
filebeat.yml: |-
  filebeat.autodiscover:
  #....
    # your autodiscover config
    # ...
  processors:
    - add_cloud_metadata: ~
  fields:
    logzio_codec: ${LOGZIO_CODEC}
    token: ${LOGZIO_LOGS_SHIPPING_TOKEN}
    cluster: ${CLUSTER_NAME}
    type: ${LOGZIO_TYPE}
  fields_under_root: ${FIELDS_UNDER_ROOT}
  ignore_older: ${IGNORE_OLDER}
  output:
    logstash:
      hosts: ["${LOGZIO_LOGS_LISTENER_HOST}:5015"]
      ssl:
        certificate_authorities: ['/etc/pki/tls/certs/SectigoRSADomainValidationSecureServerCA.crt']
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see Kubernetes log shipping troubleshooting.

 

#### Uninstalling the Chart

The command removes all the k8s components associated with the chart and deletes the release.  
To uninstall the `logzio-k8s-logs` deployment:

```shell
helm uninstall --namespace=kube-system logzio-k8s-logs
```

 

### Changing a default

If you wish to change the default values, specify each parameter using the `--set key=value` argument to `helm install`. For example,

```shell
helm install --namespace=kube-system logzio-k8s-logs logzio-helm/logzio-k8s-logs \
  --set imageTag=7.7.0 \
  --set terminationGracePeriodSeconds=30
```


#### Configurations & defaults

| Parameter | Description | Default |
|---|---|---|
| `image` | The linux based Filebeat docker image. | `docker.elastic.co/beats/filebeat` |
| `imageTag` | The linux based Filebeat docker image tag. | `7.8.1` |
| `filebeatWindowsImage` | The windows based Filebeat docker image. | `docker.io/logzio/logzio-filebeat-win` |
| `filebeatWindowsImageTag` | The windows based Filebeat docker image tag. | `0.0.1` |
| `winglogbeatImage` | The winlogbeat docker image. | `docker.io/logzio/logzio-winlogbeat` |
| `winglogbeatImageTag` | The winlogbeat docker image tag. | `0.0.1` |
| `nameOverride` | Overrides the Chart name for resources. | `""` |
| `fullnameOverride` | Overrides the full name of the resources. | `filebeat` |
| `namespaceOverride` | Overrides the namespace of the resources. | `""` |
| `apiVersions.configMap` | ConfigMap API version. | `v1` |
| `apiVersions.daemonset` | Daemonset API version. | `apps/v1` |
| `apiVersions.clusterRoleBinding` | ClusterRoleBinding API version. | `rbac.authorization.k8s.io/v1` |
| `apiVersions.clusterRole` | ClusterRole API version. | `rbac.authorization.k8s.io/v1` |
| `apiVersions.serviceAccount` | ServiceAccount API version. | `v1` |
| `apiVersions.secret` | Secret API version. | `v1` |
| `managedServiceAccount` | Specifies whether the serviceAccount should be managed by this Helm Chart. Set this to `false` to manage your own service account and related roles. | `true` |
| `clusterRoleRules` | Configurable [cluster role rules](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) that Filebeat uses to access Kubernetes resources. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `logzioCert` | Logzio public SSL certificate. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `configType` | Specifies which configuration to use for Filebeat. Set to `autodiscover` to use autodiscover (available only for filebeat). | `standard` |
| `filebeatConfig.standardConfig` | Standard linux based Filebeat configuration, using `filebeat.input`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `filebeatConfig.autodiscoverConfig` | Autodiscover linux based Filebeat configuration, using `filebeat.autodiscover`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `filebeatConfig.autoCustomConfig` | Autodiscover linux based Filebeat custom configuration, using `filebeat.autodiscover`. Should be used if you want to use your customized autodiscover config | {} |
| `filebeatWindowsConfig.standardConfig` | Standard windows based Filebeat configuration, using `filebeat.input`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `filebeatConfig.autodiscoverConfig` | Autodiscover windows based Filebeat configuration, using `filebeat.autodiscover`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `filebeatConfig.autoCustomConfig` | Autodiscover windows based Filebeat custom configuration, using `filebeat.autodiscover`. Should be used if you want to use your customized autodiscover config | {} |
| `winlogbeatConfig.standardConfig` | Standard Winlogbeat configuration, using `winlogbeat.event_logs`. (Currently this is the only available option)| See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `serviceAccount.create` | Specifies whether a service account should be created. | `true` |
| `serviceAccount.name` | Name of the service account. | `filebeat` |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing Filebeat pod process on pod shutdown. | `30` |
| `hostNetwork` | Controls whether the pod may use the node network namespace. | `true` |
| `windowsHostNetwork` | Controls whether the pod may use the Windows node network namespace. | `false` |
| `dnsPolicy` | Specifies pod-specific DNS policies. | `ClusterFirstWithHostNet` |
| `daemonset.ignoreOlder` | Logs older than this will be ignored. (linux based Filebeat)| `3h` |
| `daemonset.logzioCodec` | Set to `json` if shipping JSON logs. Otherwise, set to `plain`. (linux based Filebeat)| `json` |
| `daemonset.logzioType` | The log type you'll use with this Daemonset. This is shown in your logs under the `type` field in Open Search Dashboards. Logz.io applies parsing based on type. (linux based Filebeat)| `filebeat` |
| `daemonset.fieldsUnderRoot` | If this option is set to true, the custom fields are stored as top-level fields in the output document instead of being grouped under a `fields` sub-dictionary. (linux based Filebeat)| `"true"` |
| `daemonset.securityContext` | Configurable [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for Filebeat DaemonSet pod execution environment. (linux based Filebeat)| See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `daemonset.resources` | Allows you to set the resources for Filebeat Daemonset. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (linux based Filebeat)|
| `daemonset.tolerations` | Set [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for all DaemonSet pods. (linux based Filebeat)| `{}` |
| `daemonset.volumes` | Templatable string of additional `volumes` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (linux based Filebeat)|
| `daemonset.volumeMounts` | Templatable string of additional `volumeMounts` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (linux based Filebeat)|
| `daemonset.priorityClassName` | Set [priorityClassName](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) for all DaemonSet pods. | `""` |
| `winlogbeatDaemonset.ignoreOlder` | Logs older than this will be ignored. (Winlogbeat)| `3h` |
| `winlogbeatDaemonset.logzioCodec` | Set to `json` if shipping JSON logs. Otherwise, set to `plain`. (Winlogbeat)| `json` |
| `winlogbeatDaemonset.logzioType` | The log type you'll use with this Daemonset. This is shown in your logs under the `type` field in Open Search Dashboards. Logz.io applies parsing based on type. (Winlogbeat)| `winlogbeat` |
| `winlogbeatDaemonset.fieldsUnderRoot` | If this option is set to true, the custom fields are stored as top-level fields in the output document instead of being grouped under a `fields` sub-dictionary. (Winlogbeat)| `"true"` |
| `winlogbeatDaemonset.securityContext` | Configurable [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for Filebeat DaemonSet pod execution environment. (Winlogbeat)| See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `winlogbeatDaemonset.resources` | Allows you to set the resources for Filebeat Daemonset. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Winlogbeat)|
| `winlogbeatDaemonset.tolerations` | Set [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for all DaemonSet pods. (Winlogbeat)| `{}` |
| `winlogbeatDaemonset.volumes` | Templatable string of additional `volumes` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Winlogbeat)|
| `winlogbeatDaemonset.volumeMounts` | Templatable string of additional `volumeMounts` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Winlogbeat)|
| `windowsDaemonset.priorityClassName` | Set [priorityClassName](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) for all DaemonSet pods. (windows) | `""` |
| `filebeatWindowsDaemonset.ignoreOlder` | Logs older than this will be ignored. (Windows based Filebeat)| `3h` |
| `filebeatWindowsDaemonset.logzioCodec` | Set to `json` if shipping JSON logs. Otherwise, set to `plain`. (Windows based Filebeat)| `json` |
| `filebeatWindowsDaemonset.logzioType` | The log type you'll use with this Daemonset. This is shown in your logs under the `type` field in Open Search Dashboards. Logz.io applies parsing based on type. (Windows based Filebeat)| `filebeat-win` |
| `filebeatWindowsDaemonset.fieldsUnderRoot` | If this option is set to true, the custom fields are stored as top-level fields in the output document instead of being grouped under a `fields` sub-dictionary. (Windows based Filebeat)| `"true"` |
| `filebeatWindowsDaemonset.securityContext` | Configurable [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for Filebeat DaemonSet pod execution environment. (Windows based Filebeat)| See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) |
| `filebeatWindowsDaemonset.resources` | Allows you to set the resources for Filebeat Daemonset. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Windows based Filebeat)|
| `filebeatWindowsDaemonset.tolerations` | Set [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for all DaemonSet pods. (Windows based Filebeat)| `{}` |
| `filebeatWindowsDaemonset.volumes` | Templatable string of additional `volumes` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Windows based Filebeat)|
| `filebeatWindowsDaemonset.volumeMounts` | Templatable string of additional `volumeMounts` to be passed to the DaemonSet. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/filebeat/values.yaml) (Windows based Filebeat)|
| `secrets.create` | Boolean to toggle secrets creation. Set to false to disable secrets generation.| `true` |
| `secrets.logzioShippingToken`| Secret with your [logzio shipping token](https://app.logz.io/#/dashboard/settings/general). | `""` |
| `secrets.logzioRegion`| Secret with your [logzio region](https://docs.logz.io/user-guide/accounts/account-region.html). Defaults to US East. | `" "` |
| `secrets.clusterName`| Secret with your cluster name. | `""` |

 

Some values, such as `daemonset.tolerations`, should be set as follows:

```shell
--set daemonset.tolerations[0].key='value' \
--set daemonset.tolerations[0].operator='Equal' \
```
 

{@include: ../../_include//log-shipping/multiline-logs-filebeat.md}

  

 
Fluentd is an open source data collector and a great option because of its flexibility. This implementation uses a Fluentd DaemonSet to collect Kubernetes logs and send them to Logz.io. The Kubernetes DaemonSet ensures that some or all nodes run a copy of a pod.


The image used in this integration comes pre-configured for Fluentd to gather all logs from the Kubernetes node environment and append the proper metadata to the logs. If you prefer to customize your Fluentd configuration, you can edit it before it's deployed.

:::note
The latest version pulls the image from `logzio/logzio-fluentd`. Previous versions pulled the image from `logzio/logzio-k8s`.
:::
 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
 

For troubleshooting this solution, see our [user guide](https://docs.logz.io/user-guide/kubernetes-troubleshooting/).


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


###### K8S version compatibility

* **K8S 1.16 or earlier** - If you're running K8S 1.16 or earlier, you may need to manually change the API version in your DaemonSet to `apiVersion: rbac.authorization.k8s.io/v1beta1`.

  The API versions of `ClusterRole` and `ClusterRoleBinding` are found in `logzio-daemonset-rbac.yaml` and `logzio-daemonset-containerd.yaml`.
  
  If you are running K8S 1.17 or later, the DaemonSet is set to use `apiVersion: rbac.authorization.k8s.io/v1` by default. No change is needed.

{@include: ../../_include//log-shipping/multiline-logs-fluentd.md}


 
 

For most environments, deploying logzio-k8s with the default configuration is recommended.
If your environment requires a custom configuration, follow the steps for deploying a custom configuration.


#### To deploy logzio-k8s

 

##### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.


```shell
kubectl create namespace monitoring
```



##### Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret.


```shell
kubectl create secret generic logzio-logs-secret \
--from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
--from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
-n monitoring
```

{@include: ../../_include//general-shipping/replace-placeholders.html}


##### Deploy the DaemonSet

Run:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

#####  Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see Kubernetes log shipping troubleshooting.



 

You can customize the configuration of your Fluentd container by editing either your DaemonSet or your Configmap.


#### To deploy logzio-k8s

 


##### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.


```shell
kubectl create namespace monitoring
```


#####  Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret.


```shell
kubectl create secret generic logzio-logs-secret \
--from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
--from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
-n monitoring
```

{@include: ../../_include//general-shipping/replace-placeholders.html}

##### Configure Fluentd

Download Logz.io's [Containerd DaemonSet](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml) and open it in your text editor to edit it.

If you wish to make advanced changes in your Fluentd configuration, you can download and edit the [configmap yaml file](https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml).


{@include: ../_include/k8s-fluentd.md}


##### Deploy the DaemonSet

Run:

```shell
kubectl apply -f path/logzio-daemonset-containerd.yaml -f path/configmap.yaml
```

Replace `path` with the actual paths to your `logzio-daemonset-containerd.yaml` and `configmap.yaml` files.


#####  Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see Kubernetes log shipping troubleshooting.

 

### Disabling systemd input

To suppress Fluentd system messages, set the environment variable `FLUENTD_SYSTEMD_CONF` to `disable` in your Kubernetes environment.

### Disabling Prometheus input plugins

By default, the latest images launch `prometheus` plugins to monitor Fluentd.
If you'd like to disable the Prometheus input plugin, set the environment variable `FLUENTD_PROMETHEUS_CONF` to `disable` in your Kubernetes configuration.

### Exclude logs from certain namespaces

If you wish to exclude logs from certain namespaces, add the following to your Fluentd configuration:

```shell
<match kubernetes.var.log.containers.**_NAMESPACE_**>
  @type null
</match>
```

Replace `NAMESPACE` with the name of the namespace you need to exclude logs from. 
  
If you need to specify multiple namespaces, add another `kubernetes.var.log.containers.**_NAMESPACE_**` line to the above function as follows:

```shell
<match kubernetes.var.log.containers.**_NAMESPACE1_** kubernetes.var.log.containers.**_NAMESPACE2_**>
  @type null
</match>
```

  

{@include: ../../_include//log-shipping/multiline-fluentd-plugin.md}
 

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

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["6QjEUDKisk0OUW8KXsUizG", "4sSvbeAMUASACnq3icEm9I", "3zijX333NMPTtoWbZlyW8O", "4v4CNkbUxCsYu4MvMYqVod"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

  
 

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

   * {@include: ../../_include//metric-shipping/replace-metrics-token.html}

   * {@include: ../../_include//log-shipping/listener-var.html}

   * Replace `<<ENV-TAG>>` with the name for the environment's metrics, to easily identify the metrics for each environment.

2. Run the code.

##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["6QjEUDKisk0OUW8KXsUizG", "4sSvbeAMUASACnq3icEm9I", "3zijX333NMPTtoWbZlyW8O", "4v4CNkbUxCsYu4MvMYqVod"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [GKE troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/gke-helm-opentelemetry-troubleshooting.html).
  
  

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

 

For troubleshooting this solution, see our [GKE troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/gke-helm-opentelemetry-troubleshooting.html).

  
#### Uninstalling the Chart

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```
 
