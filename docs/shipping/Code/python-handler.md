---
id: Python-Handler
title: Python Handler
overview: Logz.io Python Handler sends logs in bulk over HTTPS to Logz.io.
product: ['logs']
os: ['windows', 'linux']
filters: ['Code']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/python.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---

 

Logz.io Python Handler sends logs in bulk over HTTPS to Logz.io.
Logs are grouped into bulks based on their size.

If the main thread quits,
the handler tries to consume the remaining logs and then exits.
If the handler can't send the remaining logs,
they're written to the local file system for later retrieval.

  

#### Set up Logz.io Python Handler

 

**Supported versions**: Python 3.5 or newer. 

##### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
pip install logzio-python-handler
```

##### Configure Logz.io Python Handler for a standard Python project

Use the samples in the code block below as a starting point,
and replace the sample with a configuration that matches your needs.

For a complete list of options, see the configuration parameters below the code block.👇

```python
[handlers]
keys=LogzioHandler

[handler_LogzioHandler]
class=logzio.handler.LogzioHandler
formatter=logzioFormat

# Parameters must be set in order. Replace these parameters with your configuration.
args=('<<LOG-SHIPPING-TOKEN>>', '<<LOG-TYPE>>', <<TIMEOUT>>, 'https://<<LISTENER-HOST>>:8071', <<DEBUG-FLAG>>)

[formatters]
keys=logzioFormat

[loggers]
keys=root

[logger_root]
handlers=LogzioHandler
level=INFO

[formatter_logzioFormat]
format={"additional_field": "value"}
```


###### Dict Config

This is an alternative configuration option recommended if you are using Python 3.8.

See Python's [documentation](https://docs.python.org/3/library/logging.config.html#configuration-file-format) regarding the `logging.config.dictConfig` method.

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logzioFormat': {
            'format': '{"additional_field": "value"}',
            'validate': False
        }
    },
    'handlers': {
        'logzio': {
            'class': 'logzio.handler.LogzioHandler',
            'level': 'INFO',
            'formatter': 'logzioFormat',
            'token': '<<LOG-SHIPPING-TOKEN>>',
            'logzio_type': '<<LOG-TYPE>>',
            'logs_drain_timeout': 5,
            'url': 'https://<<LISTENER-HOST>>:8071'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['logzio'],
            'propagate': True
        }
    }
}
```

{@include: ../../_include//general-shipping/replace-placeholders.html}


##### Parameters

:::note
Order matters. The arguments _must_ be configured in the order shown here. For example, to set debug-flag to `true`, you need to set every argument that comes before it.
:::
 

| Parameter | Description | Required/Default |
|---|---|---|
| token | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| logzio_type | The [log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `python` |
| timeout | Time to wait between log draining attempts, in seconds. | `3` |
| url | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| debug | Debug flag. To print debug messages to stdout, `True`. Otherwise, `False`. | `False` |
| backup-logs | If set to False, disables the local backup of logs in case of failure. | `True` |
| network-timeout | Timeout in seconds, int or float, for connecting to Logz.io. | `10` |
| logs_drain_timeout | Timeout in seconds, int or float, for sending the logs to Logz.io. | `5` |
| add_context | Set to `True` if you're using OpenTelemetry instrumentation and wish to inject trace context into your logs. For more info, see the **Trace context** section. | `False` |




#### Serverless platforms

If you're using a serverless function, you'll need to import and add the LogzioFlusher annotation before your sender function. To do this, in the code sample below, uncomment the `import` statement and the `@LogzioFlusher(logger)` annotation line.


:::note
For the LogzioFlusher to work properly, you'll need to make sure that the Logz.io. handler is added to the root logger. See the configuration above for an example.
:::
 




#### Code Example

```python
import logging
import logging.config
# If you're using a serverless function, uncomment.
# from logzio.flusher import LogzioFlusher

# Say I have saved my configuration as a dictionary in a variable named 'LOGGING' - see 'Dict Config' sample section
logging.config.dictConfig(LOGGING)
logger = logging.getLogger('superAwesomeLogzioLogger')

# If you're using a serverless function, uncomment.
# @LogzioFlusher(logger)
def my_func():
    logger.info('Test log')
    logger.warn('Warning')

    try:
        1/0
    except:
        logger.exception("Supporting exceptions too!")
```


To add dynamic metadata to your logger
other than the constant metadata from the formatter,
you can use the `extra` parameter.
Key-value pairs passed in `extra` are shown as new fields in Logz.io.
You can't override default fields from the python logger,
such as `lineno` or `thread`.

```python
logger.info('Warning', extra={'extra_key':'extra_value'})
```

#### Trace context

If you're sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context.
In this way, your logs will have traces data in it, such as service name, span id and trace id.
To enable this feature, set the `add_context` param in your handler configuration to `True`, like in this example:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logzioFormat': {
            'format': '{"additional_field": "value"}',
            'validate': False
        }
    },
    'handlers': {
        'logzio': {
            'class': 'logzio.handler.LogzioHandler',
            'level': 'INFO',
            'formatter': 'logzioFormat',
            'token': '<<LOG-SHIPPING-TOKEN>>',
            'logzio_type': 'python-handler',
            'logs_drain_timeout': 5,
            'url': 'https://<<LISTENER-HOST>>:8071',
            'retries_no': 4,
            'retry_timeout': 2,
            'add_context': True
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['logzio'],
            'propagate': True
        }
    }
}
```

{@include: ../../_include//general-shipping/replace-placeholders.html}


Note that this feature is only available from version 4.0.0.

 

For troubleshooting this solution, see our [Python troubleshooting guide](https://docs.logz.io/user-guide/log-troubleshooting/python-troubleshooting.html).
 

# Traces

Deploy this integration to enable automatic instrumentation of your Python application using OpenTelemetry.

## Architecture overview

This integration includes:

* Installing the OpenTelemetry Python instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your Python application in conjunction with the OpenTelemetry instrumentation

On deployment, the Python instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

### Trace context

If you're sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context.
In this way, your logs will have traces data in it, such as service name, span id and trace id.
To enable this feature, set the `add_context` param in your handler configuration to `True`, like in this example:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logzioFormat': {
            'format': '{"additional_field": "value"}',
            'validate': False
        }
    },
    'handlers': {
        'logzio': {
            'class': 'logzio.handler.LogzioHandler',
            'level': 'INFO',
            'formatter': 'logzioFormat',
            'token': '<<LOG-SHIPPING-TOKEN>>',
            'logzio_type': 'python-handler',
            'logs_drain_timeout': 5,
            'url': 'https://<<LISTENER-HOST>>:8071',
            'retries_no': 4,
            'retry_timeout': 2,
            'add_context': True
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['logzio'],
            'propagate': True
        }
    }
}
```

{@include: ../../_include/general-shipping/replace-placeholders.html}


Note that this feature is only available from version 4.0.0.



## Setup auto-instrumentation for your locally hosted Python application and send traces to Logz.io

**Before you begin, you'll need**:

* A Python application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

<!-- info-box-start:info -->
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
<!-- info-box-end -->


{@include: ../../_include/tracing-shipping/python-steps.md}


### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Python application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the parameters below.

* {@include: ../../_include/tracing-shipping/replace-tracing-token.md}

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/tail-sampling.md}


### Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

### Run the OpenTelemetry instrumentation in conjunction with your Python application

Run the following command from the directory of your Python application script:

```shell
opentelemetry-instrument python3 <YOUR-APPLICATION-SCRIPT>.py
```

Replace `<YOUR-APPLICATION-SCRIPT>` with the name of your Python application script.

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).




## Setup auto-instrumentation for your Python application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your Python application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Python application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


{@include: ../../_include/tracing-shipping/python-steps.md}


{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

### Run the OpenTelemetry instrumentation in conjunction with your Python application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the following command from the directory of your Python application script:

```shell
opentelemetry-instrument python3 `<<YOUR-APPLICATION-SCRIPT>>`.py
```

Replace `<<YOUR-APPLICATION-SCRIPT>>` with the name of your Python application script.

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


## Overview

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of pre-configured Kubernetes resources that use charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

<!-- info-box-start:info -->
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
<!-- info-box-end -->

<!-- info-box-start:info -->
:::caution 
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
<!-- info-box-end -->

## Standard configuration



### Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

### Run the Helm deployment code

```
helm install  \
--set config.exporters.logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set config.exporters.logzio.account_token=<<TRACING-SHIPPING-TOKEN>> \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
`<<LOGZIO_ACCOUNT_REGION_CODE>>` - Your Logz.io account region code. [Available regions](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions).

### Define the logzio-k8s-telemetry service dns

In most cases, the service name will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.
  

{@include: ../../_include/tracing-shipping/python-steps.md}

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).


##  Customizing Helm chart parameters

### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

#### Example

You can run the logzio-k8s-telemetry chart with your custom configuration file that takes precedence over the `values.yaml` of the chart.

For example:

<!-- info-box-start:info -->
:::note
The collector will sample **ALL traces** where is some span with error with this example configuration. 
:::
<!-- info-box-end -->

```yaml
baseCollectorConfig:
  processors:
    tail_sampling:
      policies:
        [
          {
            name: error-in-policy,
            type: status_code,
            status_code: {status_codes: [ERROR]}
          },
          {
            name: slow-traces-policy,
            type: latency,
            latency: {threshold_ms: 400}
          },
          {
            name: health-traces,
            type: and,
            and: {
              and_sub_policy:
              [
                {
                  name: ping-operation,
                  type: string_attribute,
                  string_attribute: { key: http.url, values: [ /health ] }
                },
                {
                  name: main-service,
                  type: string_attribute,
                  string_attribute: { key: service.name, values: [ main-service ] }
                },
                {
                  name: probability-policy-1,
                  type: probabilistic,
                  probabilistic: {sampling_percentage: 1}
                }
              ]
            }
          },
          {
            name: probability-policy,
            type: probabilistic,
            probabilistic: {sampling_percentage: 20}
          }
        ] 
```

```
helm install -f <PATH-TO>/my_values.yaml \
--set logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set logzio.tracing_token=<<TRACING-SHIPPING-TOKEN>> \
--set traces.enabled=true \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

Replace `<PATH-TO>` with the path to your custom `values.yaml` file.

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}






## Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```


{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

