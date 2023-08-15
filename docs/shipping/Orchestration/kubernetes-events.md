---
id: Kubernetes-events
title: Kubernetes events
overview: This guide uses the kubernetes-event-exporter tool to ship kubernetes events to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Containers', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kubernetes.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


#### Shipping Kubernetes events

Kubernetes events are a resource type that Kubernetes automatically creates when other resources get state changes, errors, or other messages that should be shared across the system.

This guide uses the [kubernetes-event-exporter](https://github.com/opsgenie/kubernetes-event-exporter) tool to ship kubernetes events to Logz.io.

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


 

##### Create monitoring namespace

```shell
kubectl create namespace monitoring
```

##### Store your Logz.io credentials
Save your Logz.io shipping credentials as a Kubernetes secret. To do this, customize the sample command below to your specifics and run it.

```shell
kubectl create secret generic logzio-events-secret \
  --from-literal=logzio-log-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-log-listener='<<LISTENER-HOST>>' \
  -n monitoring
```

* {@include: ../_include//log-shipping/listener-var.html}
* {@include: ../_include//log-shipping/log-shipping-token.html}

##### Deploy

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/k8s-events.yaml
```

##### Check Logz.io for your events

Give your events some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs,
see [Kubernetes log shipping troubleshooting]({{site.baseurl}}/user-guide/kubernetes-troubleshooting/).
  
 

