This section contains some guidelines for handling errors that you may encounter when trying to collect Kubernetes metrics.


#### Problem: Permanent error - context deadline exceeded

The following error appears:

```shell
Permanent error: Post \"https://<<LISTENER-HOST>>:8053\": context deadline exceeded
meaning that the post request timeout.
```

##### Possible cause - Connectivity issue

A connectivity issue may be causing this error.

###### Suggested remedy

Check your shipper's connectivity as follows.

For macOS and Linux, use telnet to make sure your log shipper can connect to Logz.io listeners.

:::note
As of macOS High Sierra (10.13),
telnet is not installed by default.
You can install telnet with Homebrew
by running `brew install telnet`.
:::

Run this command from the environment you're shipping from, after adding the appropriate port number:

```shell
telnet listener.logz.io {port-number}
```
For Windows servers running Windows 8/Server 2012 and later, run the following command in PowerShell:


```shell
Test-NetConnection listener.logz.io -Port {port-number}
```

The port numbers are 8052 and 8053.

##### Possible cause - Service exposing the metrics need more time


A service exposing the metrics may need more time to send the response to the OpenTelemetry collector.

###### Suggested remedy


Increase the OpenTelemetry collector timeout as follows.

In values.yaml,under: `config: receivers: prometheus: config: global: scrape_timeout: <<timeout time>>`.

#### Problem: Incorrect listener and/or token

You may be using an incorrect listener and/or token.

You will need to look in the logs of a pod whose name contains `otel-collector`. 

##### Possible cause - The token is not valid


In the logs, for the token the error will be: `"error": "Permanent error: remote write returned HTTP status 401 Unauthorized; err = <nil>: Shipping token is not valid"`. 

##### Possible cause - The listener is not valid


For the Url the error will be: `"error": "Permanent error: Post \"https://liener.logz.io:8053\": dial tcp: lookup <<provided listener>> on <<ip>>: no such host"`.

###### Suggested remedy


Check that the listener and token of your account are correct. You can view them in the [Manage tokens section](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics).


#### Problem: Windows nodes error


##### Possible cause - Incorrect username and/or password for Windows nodes

You may be using an incorrect username and/or password for Windows nodes.

You will need to look in the logs of the `windows-exporter-installer` pod. The error will look like this: `INFO:paramiko.transport:Authentication (password) failed.`

`ERROR:root:SSH connection to node aksnpwin000002 failed, please check username and password`.
 

###### Suggested remedy

Ensure the username and password to Windows nodes are correct.

#### Problem: Invalid helm chart version

##### Possible cause - The version of the helm chart is not up to date

The helm chart version that you are using may have expired.

###### Suggested remedy


Update the helm chart by running:

```shell
helm repo update
```

#### Problem: The prometheusremotewrite exporter timeout


When checking the Logz.io app you don't see any metrics, or you only see some of your metrics, but when checking your otel-collector pod for logs, you don't see any errors. This might indicate this issue.

##### Possible cause - The timeout in prometheusremotewrite exporter too short


The `timeout` setting in the `prometheusremotewrite` exporter is too short.

###### Suggested remedy


Increase the `timeout` setting in the `prometheusremotewrite` exporter.

For example, if our timeout setting is `5s`:

```yaml
endpoint: ${LISTENER_URL}
      timeout: 5s
      external_labels:
        p8s_logzio_name: ${P8S_LOGZIO_NAME}
      headers:
        Authorization: "Bearer ${METRICS_TOKEN}"

```

You can increase it to `20s`:

```yaml
endpoint: ${LISTENER_URL}
      timeout: 20s
      external_labels:
        p8s_logzio_name: ${P8S_LOGZIO_NAME}
      headers:
        Authorization: "Bearer ${METRICS_TOKEN}"

```

## Problem: Permanent error - log state shows as waiting

The log shows the following:

```yaml
State: Waiting
Reason: CrashLoopBackOff
Last State: Terminated
Reason: OOMKilled
Exit Code: 137
```


#### Possible cause


Insufficient memory allocated to the pod.

###### Suggested remedy


In `values.yaml`, increase the memory of the `standaloneCollector` resources by approximately `100Mi`.

For example, if you are using `512Mi`:

```yaml
standaloneCollector:
  enabled: true

  containerLogs:
    enabled: false

  resources:
    limits:
      cpu: 256m
      memory: 512Mi
```

You can increase it as much as needed. In this example, it's `612Mi`:

```yaml
standaloneCollector:
  enabled: true

  containerLogs:
    enabled: false

  resources:
    limits:
      cpu: 256m
      memory: 612Mi
```

###### When running apps on Kubernetes 



You need to make sure that the `prometheus.io/scrape` is set to `true`:

```yaml
prometheus.io/scrape: true
```


####  Problem: You have reached your pull rate limit

In some cases (i.e. spot clusters) where the pods or nodes are replaced frequently, they might reach the pull rate limit for images pulled from dockerhub with the following error:

```yaml
You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: 
https://www.docker.com/increase-rate-limits
```

###### Suggested remedy


You can use the following `--set` commands to use an alternative image repository:

For the monitoring chart and the Telemetry Collector Kubernetes installation:


`--set logzio-k8s-telemetry.image.repository=ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib`
`--set logzio-k8s-telemetry.prometheus-pushgateway.image.repository=public.ecr.aws/logzio/prom-pushgateway`

For the telemetry chart:


`--set image.repository=ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib`
`--set prometheus-pushgateway.image.repository=public.ecr.aws/logzio/prom-pushgateway`




