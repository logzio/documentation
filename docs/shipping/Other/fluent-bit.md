---
id: Fluent-Bit
title: Fluent Bit
overview: Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. This integration allows you to send logs from Fluent Bit running as a standalone app and forward them to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/fluent-bit.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

 

## Run Fluent Bit as a standalone app

Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. This integration allows you to send logs from Fluent Bit running as a standalone app and forward them to your Logz.io account.


 

### Install Fluent Bit

If you haven't installed Fluent Bit yet,
you can build it from source
according to the [instructions from Fluent Bit](https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit).

### Install and configure the Logz.io plugin

For Linux:

```shell
wget -o /fluent-bit/plugins/out_logzio.so \
https://github.com/logzio/fluent-bit-logzio-output/raw/master/build/out_logzio-linux.so
```

For MacOS:

```shell
wget -o /fluent-bit/plugins/out_logzio.so \
    https://github.com/logzio/fluent-bit-logzio-output/raw/master/build/out_logzio-macOS.so
```

For Windows:

```shell
wget https://github.com/logzio/fluent-bit-logzio-output/raw/master/build/out_logzio-windows.so
```

In your Fluent Bit configuration file (`fluent-bit.conf` by default),
add Logz.io as an output.

:::note
Logz.io-Out Plugin for Fluent Bit supports one output stream to Logz.io. We recommend running a new instance for each output stream you need.
:::
 

For a list of options, see the configuration parameters below the code block. 👇

```python
[OUTPUT]
    Name  logzio
    Match *
    Workers 1
    logzio_token <<LOG-SHIPPING-TOKEN>>
    logzio_url   https://<<LISTENER-HOST>>:8071
```

### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| logzio_token | {@include: ../../_include/log-shipping/log-shipping-token.md}| Required |
| logzio_url  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| logzio_type   | {@include: ../../_include/log-shipping/type.md} | `logzio-fluent-bit` |
| logzio_debug    | Set to `true` to print debug messages to stdout. | `false` |
| workers | Enables dedicated thread(s) for this output. | Default value is 1. To support more traffic, adjust this value accordingly. |


### Run Fluent Bit with the Logz.io plugin

Linux and MacOS:

```shell
fluent-bit -e /fluent-bit/plugins/out_logzio.so \
-c /fluent-bit/etc/fluent-bit.conf
```

Windows:

```shell
C:\PROGRA~1\td-agent-bit\bin\fluent-bit.exe -c C:\PROGRA~1\td-agent-bit\conf\fluent-bit.conf -e <<PATH_TO_PLUGIN>>\out_logzio-windows.so
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

  

## Run Fluent Bit in a Docker container

Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. This integration allows you to send logs from Fluent Bit running in a Docker container and forward them to your Logz.io account.


 

### Make the configuration file

To run in a container,
create a configuration file named `fluent-bit.conf`. 

:::note
Logz.io-Out Plugin for Fluent Bit supports one output stream to Logz.io. We recommend running a new instance for each output stream you need.
:::
 

For a list of options, see the configuration parameters below the code block. 👇

```python
[SERVICE]
    # Include your remaining SERVICE configuration here.
    Plugins_File plugins.conf

[OUTPUT]
    Name  logzio
    Match *
    logzio_token <<LOG-SHIPPING-TOKEN>>
    logzio_url   https://<<LISTENER-HOST>>:8071
```

###  Parameters

| Parameter | Description |Required/Default |
|---|---|---|
| logzio_token | {@include: ../../_include/log-shipping/log-shipping-token.md}  {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| logzio_url  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| logzio_type   | {@include: ../../_include/log-shipping/type.md} | `logzio-fluent-bit` |
| logzio_debug    | Set to `true` to print debug messages to stdout. | `false` |



### Run the Docker image

Run the Docker image
using the `fluent-bit.conf` file you made in step 1.

```shell
docker run -it --rm \
-v /path/to/fluent-bit.conf:/fluent-bit/etc/fluent-bit.conf \
logzio/fluent-bit-output
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


## Run Fluent Bit in Kubernetes


Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts. You can use this Helm chart to ship Kubernetes logs to Logz.io with Fluent Bit. 


:::note
This chart is based on the [fluent-bit](https://github.com/fluent/helm-charts/tree/main/charts/fluent-bit) Helm chart.
:::
 

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

### Enabling multiline logs parser

If you want to enable parsing for multiline logs, add the following code to `values.yaml` under the `customParsers` parameter:
  
```yaml
customParsers:
  [MULTILINE_PARSER]
      name          multiline-regex-test
      type          regex
      flush_timeout 1000
```


### Standard configuration

 

### Add `logzio-helm` repo
  
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```


### Run the Helm deployment code

```shell
helm install  \
--set logzio.token=<<LOG-SHIPPING-TOKEN>> \
--set logzio.listenerHost=<<LISTENER-HOST>> \
--set logzio.logType=<<LOG-TYPE>> \
logzio-fluent-bit logzio-helm/logzio-fluent-bit
```
  
{@include: ../../_include/log-shipping/listener-var.html} {@include: ../../_include/log-shipping/log-shipping-token.html} If required, replace `<<LOG_TYPE>>` with the desired name for the log type, the default value is `fluentbit`.


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).

 


###  Customizing Helm chart parameters


#### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

#### Example

```
helm install logzio-fluent-bit logzio-helm/logzio-fluent-bit -f my_values.yaml 
```

To modify fluentbit configuration, edit the `config` section in `values.yaml`.

#### Uninstalling the Chart

The Uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-fluent-bit` deployment, use the following command:

```shell
helm uninstall logzio-fluent-bit
```
