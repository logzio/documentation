---
id: aws-eks
title: AWS EKS
overview: logzio-k8s-telemetry allows you to ship metrics from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-eks.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
drop_filter: []
---

 

Fluentd is an open source data collector and a great option because of its flexibility. This implementation uses a Fluentd DaemonSet to collect Kubernetes logs and send them to Logz.io. The Kubernetes DaemonSet ensures that some or all nodes run a copy of a pod.


The image used in this integration comes pre-configured for Fluentd to gather all logs from the Kubernetes node environment and append the proper metadata to the logs. If you prefer to customize your Fluentd configuration, you can edit it before it's deployed.


:::note
The latest version pulls the image from `logzio/logzio-fluentd`. Previous versions pulled the image from `logzio/logzio-k8s`.
:::
 

:::caution Important
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

{@include: ../../_include//log-shipping/multiline-logs-fluentd.md}

 

## Deploy logzio-k8s with default configuration

For most environments, we recommend using the default configuration.
However, you can deploy a custom configuration if your environment needs it.


### Deploy Fluentd as a DaemonSet on Kubernetes

 


### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.


```shell
kubectl create namespace monitoring
```


### Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

```shell
kubectl create secret generic logzio-logs-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='https://<<LISTENER-HOST>>:8071' \
  -n monitoring
```

### Deploy the DaemonSet

###### For an RBAC cluster:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-rbac.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

###### For a non-RBAC cluster:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

###### For container runtime Containerd:

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

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}


### Configure Fluentd

There are 3 DaemonSet options: [RBAC DaemonSet](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-rbac.yaml), [non-RBAC DaemonSet](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset.yaml), [Containerd](https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml). Download the relevant DaemonSet and open it in your text editor to edit it.

If you wish to make advanced changes in your Fluentd configuration, you can download and edit the [configmap yaml file](https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml).


{@include: ../../_include/k8s-fluentd.md}

#### Good to know

* If `FLUENT_FILTER_KUBERNETES_URL` is not specified, the environment variables `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT` will be used, as long as both of them are  present. Typically, they are present when running Fluentd in a pod.

* Note that `FLUENT_FILTER_KUBERNETES_URL` does not appear in the default environment variable list in the DaemonSet.
If you wish to use this variable, you'll have to add it manually to the DaemonSet's environment variables.


### Deploy the DaemonSet

###### For the RBAC DaemonSet:

```shell
kubectl apply -f /path/to/logzio-daemonset-rbac.yaml -f /path/to/configmap.yaml
```

###### For the non-RBAC DaemonSet:

```shell
kubectl apply -f /path/to/logzio-daemonset.yaml -f /path/to/configmap.yaml
```

###### For container runtime Containerd:

```shell
kubectl apply -f /path/to/logzio-daemonset-containerd.yaml -f /path/to/configmap.yaml
```


### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).

 


### Disabling systemd input

To suppress Fluentd system messages, set the `FLUENTD_SYSTEMD_CONF` environment variable to `disable` in your Kubernetes environment.

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

## Multiline logs


{@include: ../../_include//log-shipping/multiline-fluentd-plugin.md}

 



**logzio-k8s-telemetry** allows you to ship metrics from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

This chart is a fork of the [opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
  
It is also dependent on the [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/tree/master/charts/kube-state-metrics), [prometheus-node-exporter](https://github.com/helm/charts/tree/master/stable/prometheus-node-exporter) and [prometheus-pushgateway](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-pushgateway) charts, which are installed by default. 
  
To disable the dependency during installation, set `kubeStateMetrics.enabled`, `nodeExporter.enabled` or `pushGateway.enabled` to `false`.
  
For applications that run on Kubernetes, enable the Prometheus scrape feature:

```yaml
prometheus.io/scrape: true
```

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

If you are using Fargate, you need to disable the node exporter deployment. To do this, add the following settings to the values.yaml, under the `prometheus-node-exporter` field:

```yaml
affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: eks.amazonaws.com/compute-type
                operator: DoesNotExist
```



{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1aO3NWtPAtVwO5Ipmc3Deh", "6KQUyksnNT2E40PifmCHR5", "X6YYCFajD56zayxcQOG2H", "M06b1BjTSGsSNZBWeiLnR"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

  
 

## Standard configuration for Linux nodes

 
  
### Add logzio-helm repo to your helm repo list

  ```shell
  helm repo add logzio-helm https://logzio.github.io/logzio-helm
  helm repo update
  ```

### Deploy the Helm chart

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

### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours.


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1aO3NWtPAtVwO5Ipmc3Deh", "6KQUyksnNT2E40PifmCHR5", "X6YYCFajD56zayxcQOG2H", "M06b1BjTSGsSNZBWeiLnR"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 
  
 

For troubleshooting this solution, see our [EKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/eks-helm-opentelemetry-troubleshooting.html).
  
  

##  Customizing Helm chart parameters

 

### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

#### Example:

```
helm install logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry -f my_values.yaml 
```

### Customize the metrics collected by the Helm chart 

The default configuration uses the Prometheus receiver with the following scrape jobs:

* Cadvisor: Scrapes container metrics
* Kubernetes service endpoints: These jobs scrape metrics from the node exporters, from Kube state metrics, from any other service for which the `prometheus.io/scrape: true` annotaion is set, and from services that expose Prometheus metrics at the `/metrics` endpoint.

To customize your configuration, edit the `config` section in the `values.yaml` file.

 

For troubleshooting this solution, see our [EKS troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/eks-helm-opentelemetry-troubleshooting.html).


  

## **Uninstalling the Chart**

The `uninstall` command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```

  
