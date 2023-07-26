---
id: Fluentd
title: Fluentd
overview: Fluentd is an open source data collector and a great option because of its flexibility. This implementation uses a Fluentd DaemonSet to collect Kubernetes logs and send them to Logz.io. The Kubernetes DaemonSet ensures that some or all nodes run a copy of a pod.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/iks.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
 
 
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

{@include: ../_include//log-shipping/multiline-logs-fluentd.md}


 
 

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

{@include: ../_include//general-shipping/replace-placeholders.html}


##### Deploy the DaemonSet

Run:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/logzio-daemonset-containerd.yaml -f https://raw.githubusercontent.com/logzio/logzio-k8s/master/configmap.yaml
```

#####  Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).



 

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

{@include: ../_include//general-shipping/replace-placeholders.html}

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
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).

 

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

  

{@include: ../_include//log-shipping/multiline-fluentd-plugin.md}
 