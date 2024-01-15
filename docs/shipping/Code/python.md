---
id: Python 
title: Python
overview: Logz.io's Python integration allows you to send custom logs, custom metrics, and auto-instrument traces into your account, allowing you to identify and resolve issues in your code.
product: ['metrics','logs','tracing']
os: ['windows', 'linux', 'mac']
filters: ['Code', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/python.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Logs

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-python-handler/)
:::

Logz.io Python Handler sends logs in bulk over HTTPS to Logz.io.
Logs are grouped into bulks based on their size.

If the main thread quits,the handler tries to consume the remaining logs and then exits.
If the handler can't send the remaining logs, they're written to the local file system for later retrieval.

## Set up Logz.io Python Handler

 

*Supported versions*: Python 3.5 or newer. 

### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
pip install logzio-python-handler
```

If you'd like to use [Trace context](#trace-context), you need to install the OpenTelemetry logging instrumentation dependency by running the following command:

```shell
pip install logzio-python-handler[opentelemetry-logging]
```

### Configure Logz.io Python Handler for a standard Python project

Use the samples in the code block below as a starting point, and replace the sample with a configuration that matches your needs.

Replace:
* << LOG-SHIPPING-TOKEN >> - Your Logz.io account log shipping token.
* << LISTENER-HOST >> - Logz.io listener host, as described [here](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#regions-and-urls).
* << LOG-TYPE >> - Log type, for searching in logz.io (defaults to "python")

For a complete list of options, see the configuration parameters below the code block.👇

##### Config File

```python
[handlers]
keys=LogzioHandler

[handler_LogzioHandler]
class=logzio.handler.LogzioHandler
formatter=logzioFormat

# Parameters must be set in order. Replace these parameters with your configuration.
args=('<<LOG-SHIPPING-TOKEN>>', '<<LOG-TYPE>>', <<TIMEOUT>>, 'https://<<LISTENER-HOST>>:8071', <<DEBUG-FLAG>>,<<NETWORKING-TIMEOUT>>,<<RETRY-LIMIT>>,<<RETRY-TIMEOUT>>)

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
*args=() arguments, by order*
 - Your logz.io token
 - Log type, for searching in logz.io (defaults to "python")
 - Time to sleep between draining attempts (defaults to "3")
 - Logz.io Listener address (defaults to "https://listener.logz.io:8071")
 - Debug flag. Set to True, will print debug messages to stdout. (defaults to "False")
 - Backup logs flag. Set to False, will disable the local backup of logs in case of failure. (defaults to "True")
 - Network timeout, in seconds, int or float, for sending the logs to logz.io. (defaults to 10)
 - Retries number (retry_no, defaults to 4).
 - Retry timeout (retry_timeout) in seconds (defaults to 2).

 Please note, that you have to configure those parameters by this exact order.
 i.e. you cannot set Debug to true, without configuring all of the previous parameters as well.

##### Dict Config

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
            'retries_no': 4,
            'retry_timeout': 2,
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
##### Django configuration

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'logzioFormat': {
            'format': '{"additional_field": "value"}',
            'validate': False
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
        'logzio': {
            'class': 'logzio.handler.LogzioHandler',
            'level': 'INFO',
            'formatter': 'logzioFormat',
            'token': '<<LOG-SHIPPING-TOKEN>>',
            'logzio_type': "django",
            'logs_drain_timeout': 5,
            'url': 'https://<<LISTENER-HOST>>:8071'
            'debug': True,
            'network_timeout': 10,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', ],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
        '': {
            'handlers': ['console', 'logzio'],
            'level': 'INFO'
        }
    }
}

```



### Serverless platforms

If you're using a serverless function, you'll need to import and add the LogzioFlusher annotation before your sender function. To do this, in the code sample below, uncomment the `import` statement and the `@LogzioFlusher(logger)` annotation line.  
**Note:** For the LogzioFlusher to work properly, you'll need to make sure that the Logz.io. handler is added to the root logger. See the configuration above for an example.

### Dynamic Extra Fields
If you prefer, you can add extra fields to your logs dynamically, and not pre-defining them in the configuration.
This way, you can allow different logs to have different extra fields.
Example in the code below. 

### Code Example

```python
import logging
import logging.config
# If you're using a serverless function, uncomment.
# from logzio.flusher import LogzioFlusher

# If you'd like to leverage the dynamic extra fields feature, uncomment.
# from logzio.handler import ExtraFieldsLogFilter

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

# Example additional code that demonstrates how to dynamically add/remove fields within the code, make sure class is imported.

    logger.info("Test log")  # Outputs: {"message":"Test log"}
    
    extra_fields = {"foo":"bar","counter":1}
    logger.addFilter(ExtraFieldsLogFilter(extra_fields))
    logger.warning("Warning test log")  # Outputs: {"message":"Warning test log","foo":"bar","counter":1}
    
    error_fields = {"err_msg":"Failed to run due to exception.","status_code":500}
    logger.addFilter(ExtraFieldsLogFilter(error_fields))
    logger.error("Error test log")  # Outputs: {"message":"Error test log","foo":"bar","counter":1,"err_msg":"Failed to run due to exception.","status_code":500}
    
    # If you'd like to remove filters from future logs using the logger.removeFilter option:
    logger.removeFilter(ExtraFieldsLogFilter(error_fields))
    logger.debug("Debug test log") # Outputs: {"message":"Debug test log","foo":"bar","counter":1}

```

### Extra Fields

In case you need to dynamic metadata to a specific log and not [dynamically to the logger](#dynamic-extra-fields), other than the constant metadata from the formatter, you can use the "extra" parameter.
All key values in the dictionary passed in "extra" will be presented in Logz.io as new fields in the log you are sending.
Please note, that you cannot override default fields by the python logger (i.e. lineno, thread, etc..)
For example:

```python
logger.info('Warning', extra={'extra_key':'extra_value'})
```

### Trace context

If you're sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context.
That way, your logs will have traces data in it, such as service name, span id and trace id.

Make sure to install the OpenTelemetry logging instrumentation dependecy by running the following command:

```shell
pip install logzio-python-handler[opentelemetry-logging]
```
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
            'logzio_type': '<<LOG-TYPE>>',
            'logs_drain_timeout': 5,
            'url': 'https://<<LISTENER-HOST>>:8071'
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


## Metrics

You can send custom metrics to Logz.io from your Python application. This example uses the [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python-contrib) and the [OpenTelemetry remote write exporter](https://pypi.org/project/opentelemetry-exporter-prometheus-remote-write/), which are both in alpha/preview.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="Setup-in-code" label="Setup in code" default>

### Setup in code


#### Install the snappy c-library

DEB: `sudo apt-get install libsnappy-dev`

RPM: `sudo yum install libsnappy-devel`

OSX/Brew: `brew install snappy`

Windows: `pip install python_snappy-0.5-cp36-cp36m-win_amd64.whl`

#### Install the exporter and opentelemtry sdk
```
pip install opentelemetry-exporter-prometheus-remote-write
```

#### Add instruments to your application

Replace the placeholders in the `exporter` section code (indicated by the double angle brackets `<< >>`) to match your specifics.


|Parameter|Description|
|---|---|
|LISTENER-HOST|  The Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. {@include: ../../_include//log-shipping/listener-var.html} and add http/https protocol (https://listener.logz.io:8053) |
|PROMETHEUS-METRICS-SHIPPING-TOKEN| Your Logz.io Prometheus Metrics account token.  {@include: ../../_include//p8s-shipping/replace-prometheus-token.html}  |



```python
from opentelemetry import metrics
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# configure the Logz.io listener endpoint and Prometheus metrics account token
exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint="https://<<LISTENER-HOST>>:8053",
    headers={
        "Authorization": "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>",
    }
)
# set push interval in seconds
push_interval = 15

# setup metrics export pipeline
reader = PeriodicExportingMetricReader(exporter, 1000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

# create a counter instrument and provide the first data point
counter = meter.create_counter(
    name="MyCounter",
    description="Description of MyCounter",
    unit="1"
)
# add labels
labels = {
    "dimension": "value",
    "from": "testlogzio"
}
counter.add(25, labels)
```


#### Types of metric instruments


Refer to the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md) for more details. 


| Name | Behavior | Default aggregation |
| ---- | ---------- | ------------------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.add(value,labels)` request. | Sum |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.add(value,labels)` request. | Sum |
| ValueRecorder     | Metric values captured by the `valuerecorder.record(value)` function, calculated per request. | TBD  |
| SumObserver       | Metric value can only go up or be reset to 0, calculated per push interval.| Sum |
| UpDownSumObserver | Metric value can arbitrarily increment or decrement, calculated per push interval.| Sum |
| ValueObserver     | Metric values captured by the `valuerecorder.observe(value)` function, calculated per push interval.| LastValue  |

##### [Counter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#counter)

```python
# create a counter instrument
counter = meter.create_counter(
    name="MyCounter",
    description="Description of MyCounter",
    unit="1",
    value_type=int
)
# add labels
labels = {
    "dimension": "value"
}
# provide the first data point
counter.add(25, labels)
```

##### [UpDownCounter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#updowncounter)

```python
# create a updowncounter instrument
requests_active = meter.create_updowncounter(
    name="requests_active",
    description="number of active requests",
    unit="1",
    value_type=int,
)
# add labels
labels = {
    "dimension": "value"
}
# provide the first data point
requests_active.add(-2, labels)
```

##### [ValueRecorder](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#valuerecorder)

```python
# create a valuerecorder instrument
requests_size = meter.create_valuerecorder(
    name="requests_size",
    description="size of requests",
    unit="1",
    value_type=int,
)
# add labels
labels = {
    "dimension": "value"
}
# provide the first data point
requests_size.record(85, labels)
```

##### [SumObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#sumobserver)

```python
import psutil
# Callback to gather RAM usage
def get_ram_usage_callback(observer):
    ram_percent = psutil.virtual_memory().percent
    # add labels
    labels = {
        "dimension": "value"
    }
    observer.observe(ram_percent, labels)
# create a sumobserver instrument
meter.register_sumobserver(
    callback=get_ram_usage_callback,
    name="ram_usage",
    description="ram usage",
    unit="1",
    value_type=float,
)
```

##### [UpDownSumObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#updownsumobserver)

```python
# Callback to gather RAM usage
def get_ram_usage_callback(observer):
    ram_percent = psutil.virtual_memory().percent
    # add labels
    labels = {
        "dimension": "value"
    }
    observer.observe(ram_percent, labels)
# create a updownsumobserver instrument
meter.register_updownsumobserver(
    callback=get_ram_usage_callback,
    name="ram_usage",
    description="ram usage",
    unit="1",
    value_type=float,
)
```

##### [ValueObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#valueobserver)

```python
import psutil
def get_cpu_usage_callback(observer):
    for (number, percent) in enumerate(psutil.cpu_percent(percpu=True)):
        labels = {"cpu_number": str(number)}
        observer.observe(percent, labels)
# create a valueobserver instrument
meter.register_valueobserver(
    callback=get_cpu_usage_callback,
    name="cpu_percent",
    description="per-cpu usage",
    unit="1",
    value_type=float,
)
```

#### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

</TabItem>
  <TabItem value="Setup-Metrics-using-Lambda" label="Setup Metrics using Lambda">

### Setup Metrics using Lambda

This integration uses OpenTelemetry collector extention and Python metrics SDK to create and send metrics from your Lambda functions to your Logz.io account.

:::note
This integration is currently only supported in the following AWS regions: **us-east-1**, **us-east-2**,**us-west-1**, **us-west-2**, **ca-central-1**, **ap-northeast-2**, **ap-northeast-1**,**eu-central-1**, **eu-west-2**. Contact Logz.io Customer Support if you need to deploy in a different region.
:::

#### Create Lambda function

Create a new Lambda function in your AWS account (with Python version >= 3.8).

After creating your new Lambda function, you can use our example [deployment package](https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-otel-lambda-python/logzio-python-lambda-custom-metrics-deployment.zip) that includes the code sample. Upload the .zip file to the **code source** section inside your newly created Lambda function.


![Upload deployment package](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/uploadzip.gif)

#### Add OpenTelemetry collector config variable

Add `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` environment variable with a value of `/var/task/collector.yaml`. This will tell the collector extention the path to the configuration file.

#### Add OpenTelemetry config file

Add `collector.yaml` at the root of your lambda function:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

exporters:
  logging:
    loglevel: info
  prometheusremotewrite:
    endpoint: "<<LISTENER-HOST>>:<PORT>>" # example: https://listener.logz.io:8053
    resource_to_telemetry_conversion:
      enabled: true # Convert resource attributes to metric labels
    target_info:
        enabled: false
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
service:
  pipelines:
    metrics:
      receivers: [otlp]
      exporters: [logging,prometheusremotewrite]
```

Replace the placeholders (indicated by the double angle brackets `<< >>`) to match your specifics as per the table below.

|Environment variable|Description|
|---|---|
|`<<LISTENER-HOST>>`|  The Logz.io [Listener URL](https://docs.logz.io/user-guide/accounts/account-region.html) for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. |
|`<<PORT>>`| The Logz.io listener port. **8052** for HTTP traffic, or **8053** for HTTPS traffic. |
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| {@include: ../../_include/p8s-shipping/replace-prometheus-token.html}  |


#### Create Lambda function Python script

Create a `lambda_function.py` file for your lambda handler:

```python
import json
import os
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk._metrics.export import (
    PeriodicExportingMetricReader,
)
from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


def lambda_handler(event, context):
    print("lets start sending metrics")
    # Initialize otlp exporter, reader, meterProvier, meter
    exporter = OTLPMetricExporter(insecure=True)
    # Add service name and lambda function metadata
    resource = Resource(attributes={
        SERVICE_NAME: "logzio-lambda",
        "function_name": os.environ["AWS_LAMBDA_FUNCTION_NAME"],
        "aws_region": os.environ["AWS_REGION"],
    })
    reader = PeriodicExportingMetricReader(exporter)
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    # set_meter_provider(provider)
    meter = provider.get_meter("logzio", "0.1.2")

    # create a counter metric and provide the first data point
    counter = meter.create_counter("counter")
    counter.add(5)
    # add labels
    labels = {
        "env": "prod"
    }
    counter.add(25, labels)
 
    # Flush all metrics and close meter provider
    provider.force_flush()
    provider.shutdown()

    return {
        'statusCode': 200,
        'body': json.dumps('Finished sending metrics')
    }

```

#### Add Logz.io Otel Python layer

Add the `logzio-otel-python-layer` lambda layer to your function:

```
arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-otel-python-layer:1
```

Replace `<<YOUR-AWS-REGION>>` with your AWS resgion.

#### Run the Lambda function

Start running the Lambda function to send metrics to your Logz.io account.



#### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


#### Types of metric instruments

For more information, see the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md).

| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values captured by the `histogram.Record(context,value,labels)` function, calculated per request. |

#### More examples

##### [Counter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#counter)

```python
    # create a counter metric and provide the first data point
    counter = meter.create_counter("counter")
    # add labels
    labels = {
        "env": "prod"
    }
    counter.add(5,labels)
    counter.add(25, labels)
```


##### [UpDownCounter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#updowncounter)

```python
    # create an up down counter metric and provide the first data points
    up_down_counter = meter.create_up_down_counter(
        name="example_up_down_counter",
        description="example_up_down_counter",
    )
    labels = {
        "env": "prod"
    }
    up_down_counter.add(20,labels)
    up_down_counter.add(-10,labels)
```

</TabItem>
</Tabs>

## Traces

Deploy this integration to enable automatic instrumentation of your Python application using OpenTelemetry.

### Architecture overview

This integration includes:

* Installing the OpenTelemetry Python instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your Python application in conjunction with the OpenTelemetry instrumentation

On deployment, the Python instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

### Local host Python application auto instrumentation

**Before you begin, you'll need**:

* A Python application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


#### Install general Python OpenTelemetry instrumentation components

Run the following commands:

```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

After installation, configure the exporter by running the following command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with the name of your tracing service defined earlier.

#### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Python application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.82.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the parameters below.

* {@include: ../../_include/tracing-shipping/replace-tracing-token.md}

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/tail-sampling.md}


#### Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

#### Run the OpenTelemetry instrumentation in conjunction with your Python application

Run the following command from the directory of your Python application script:

```shell
opentelemetry-instrument python3 <YOUR-APPLICATION-SCRIPT>.py
```

Replace `<YOUR-APPLICATION-SCRIPT>` with the name of your Python application script.

#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).



### Docker Python application auto instrumentation

This integration enables you to auto-instrument your Python application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Python application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


#### Install general Python OpenTelemetry instrumentation components

Run the following commands:

```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

After installation, configure the exporter by running the following command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with the name of your tracing service defined earlier.


#### Pull the Docker image for the OpenTelemetry collector

```shell
docker pull otel/opentelemetry-collector-contrib:0.78.0
```

#### Create a configuration file

Create a file `config.yaml` with the following content:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"
  

exporters:
  logzio/traces:
    account_token: "<<TRACING-SHIPPING-TOKEN>>"
    region: "<<LOGZIO_ACCOUNT_REGION_CODE>>"

  logging:

processors:
  batch:
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        }, 
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }        
      ]

extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logging, logzio/traces]
```
 

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

{@include: ../../_include/tracing-shipping/tail-sampling.md}
 


If you already have an OpenTelemetry installation, add the following parameters to the configuration file of your existing OpenTelemetry collector:

* Under the `exporters` list

```yaml
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
```

* Under the `service` list:

```yaml
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

An example configuration file looks as follows:

```yaml
receivers:  
  otlp:
    protocols:
      grpc:
      http:

exporters:
  logzio/traces:
    account_token: "<<TRACING-SHIPPING-TOKEN>>"
    region: "<<LOGZIO_ACCOUNT_REGION_CODE>>"

processors:
  batch:
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        }, 
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }        
      ]

extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


{@include: ../../_include/tracing-shipping/tail-sampling.md}


#### Run the container

Mount the `config.yaml` as volume to the `docker run` command and run it as follows.

###### Linux

```
docker run  \
--network host \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
otel/opentelemetry-collector-contrib:0.78.0

```

Replace `<PATH-TO>` to the path to the `config.yaml` file on your system.

###### Windows

```
docker run  \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
-p 55678-55680:55678-55680 \
-p 1777:1777 \
-p 9411:9411 \
-p 9943:9943 \
-p 6831:6831 \
-p 6832:6832 \
-p 14250:14250 \
-p 14268:14268 \
-p 4317:4317 \
-p 55681:55681 \
otel/opentelemetry-collector-contrib:0.78.0
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

#### Run the OpenTelemetry instrumentation in conjunction with your Python application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the following command from the directory of your Python application script:

```shell
opentelemetry-instrument python3 `<<YOUR-APPLICATION-SCRIPT>>`.py
```

Replace `<<YOUR-APPLICATION-SCRIPT>>` with the name of your Python application script.

#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).



### Kuberenetes Python application auto insturmentation

#### Overview 

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of preconfigured Kubernetes resources that use charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

 
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
  

 
:::caution 
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


#### Standard configuration



##### Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### Run the Helm deployment code

```
helm install  \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set logzio-k8s-telemetry.secrets.TracesToken=<<TRACING-SHIPPING-TOKEN>> \
logzio-monitoring logzio-helm/logzio-monitoring -n monitoring
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
`<<LOGZIO_ACCOUNT_REGION_CODE>>` - Your Logz.io account region code. [Available regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).


##### Define the logzio-k8s-telemetry service DNS

In most cases, the service name will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.
  

#### Install general Python OpenTelemetry instrumentation components

Run the following commands:

```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

After installation, configure the exporter by running the following command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with the name of your tracing service defined earlier.

#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).

 Customizing Helm chart parameters

#### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

##### Example

You can run the logzio-k8s-telemetry chart with your custom configuration file that takes precedence over the `values.yaml` of the chart.

For example:

 
:::note
The collector will sample **ALL traces** where is some span with error with this example configuration. 
:::
  

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

Command:
```
helm install -f <PATH-TO>/my_values.yaml \
--set logzio-k8s-telemetry.secrets.TracesToken=<<TRACES-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set metricsOrTraces=true \
logzio-monitoring logzio-helm/logzio-monitoring
```

Replace `<PATH-TO>` with the path to your custom `values.yaml` file.

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}



#### Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-monitoring` deployment, use the following command:

```shell
helm uninstall logzio-monitoring
```


## Troubleshooting


#### Logz.io Python handler 
For troubleshooting the Logz.io Python handler, see our [Python logging troubleshooting guide](https://docs.logz.io/user-guide/log-management/troubleshooting/troubleshooting-python.html).
 
#### OpenTelemetry instrumentation 
For troubleshooting the OpenTelemetry instrumentation, see our [OpenTelemetry troubleshooting guide](https://docs.logz.io/user-guide/distributed-tracing/troubleshooting/otel-troubleshooting.html).

#### Distributed Tracing account
For troubleshooting your Distributed Tracing account, see our [Distributed Tracing troubleshooting guide](https://docs.logz.io/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting.html)
