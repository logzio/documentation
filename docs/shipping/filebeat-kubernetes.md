---
id: Filebeat
title: Filebeat
sidebar_position: 1
overview: This implementation uses a Filebeat DaemonSet to collect Kubernetes logs from your cluster and ship them to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


 


This implementation uses a Filebeat DaemonSet to collect Kubernetes logs from your cluster and ship them to Logz.io.

You have 3 options for deploying this Daemonset:

* Standard configuration
* Autodiscover configuration - the standard configuration which also uses Filebeat's autodiscover and hints system
* Custom configuration - upload a Logz.io Daemonset with your own configuration

If you are sending multiline logs, see the relevant tab for further details.

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

  

#### Deploy Filebeat as a DaemonSet on Kubernetes


**Before you begin, you'll need**: Destination port 5015 open on your firewall for outgoing traffic


 

##### Store your Logz.io credentials

Save your Logz.io shipping credentials as a Kubernetes secret. Customize the sample command below to your specifics before running it.


```shell
kubectl create secret generic logzio-logs-secret \
  --from-literal=logzio-logs-shipping-token='<<LOG-SHIPPING-TOKEN>>' \
  --from-literal=logzio-logs-listener='<<LISTENER-HOST>>' \
  --from-literal=cluster-name='<<CLUSTER-NAME>>' \
  -n kube-system
```

{@include: ../_include//general-shipping/replace-placeholders.html}
* Replace `<<CLUSTER-NAME>>` with your cluster's name. If you manage Kubernetes in AWS or Azure, you can find it in your admin console. Alternatively, you can run the following to obtain your cluster name: `kubectl cluster-info`


##### Deploy

Run the relevant command for your type of deployment.

###### Standard configuration

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/k8s-filebeat.yaml -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/filebeat-standard-configuration.yaml
```

###### Autodiscover standard configuration

Autodiscover allows you to adapt settings as changes happen. By defining configuration templates, the autodiscover subsystem can monitor services as they start running. See Elastic documentation to [learn more about Filebeat Autodiscover](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover.html).

```shell
 kubectl apply -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/k8s-filebeat.yaml -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/filebeat-autodiscovery-configuration.yaml
```

###### Custom configuration

If you want to apply your own custom configuration, download the standard-configmap.yaml and apply your changes. Make sure to keep the file structure unchanged.

Run the following command to download the file:

```shell
wget https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/filebeat-standard-configuration.yaml
```

Apply your custom configuration to the paramaters under `filebeat.yml` and only there. The filebeat.yml field contains a basic Filebeat configuration. You should not change the 'output' field (indicated in the example below). See Elastic documentation to [learn more about Filebeat configuration options](https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.html).


**Note**
Make sure to keep `token: ${LOGZIO_LOGS_SHIPPING_TOKEN}` under `fields`, as it determines the token used to verify your Logz.io account.

```
filebeat.yml: |-

  # ...
  # Start editing your configuration here
  filebeat.inputs:
  - type: container
    paths:
      - /var/log/containers/*.log
    processors:
      - add_kubernetes_metadata:
          host: ${NODE_NAME}
          matchers:
          - logs_path:
              logs_path: "/var/log/containers/"

  processors:
    - add_cloud_metadata: ~
  # ...
  # Do not edit anything beyond this point. (Do not change 'fields' and 'output'.)

  fields:
    logzio_codec: ${LOGZIO_CODEC}
    token: ${LOGZIO_LOGS_SHIPPING_TOKEN}
    cluster: ${CLUSTER_NAME}
    type: ${LOGZIO_TYPE}
  fields_under_root: true
  ignore_older: ${IGNORE_OLDER}
  output:
    logstash:
      hosts: ["${LOGZIO_LOGS_LISTENER_HOST}:5015"]
      ssl:
        certificate_authorities: ['/etc/pki/tls/certs/SectigoRSADomainValidationSecureServerCA.crt']
```

Run the following to deploy your custom Filebeat configuration:

```shell
kubectl apply -f https://raw.githubusercontent.com/logzio/logz-docs/master/shipping-config-samples/k8s-filebeat.yaml -f <<Your-custom-configuration-file.yaml>>
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 

{@include: ../_include//log-shipping/multiline-logs-filebeat.md}


  