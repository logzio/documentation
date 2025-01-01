---
id: Python 
title: Python
overview: Logz.io's Python integration allows you to send custom logs, custom metrics, and auto-instrument traces into your account, allowing you to identify and resolve issues in your code.
product: ['metrics','logs','tracing']
os: ['windows', 'linux', 'mac']
filters: ['Code', 'Most Popular']
recommendedFor: ['Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/python.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1B98fgq9MpqTviLUGFMe6Z']
metrics_alerts: []
drop_filter: []
---

## Logs

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="logzio-python-handler" label="Logz.io Python Handler" default>

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-python-handler/)
:::

The Logz.io Python Handler sends logs in bulk over HTTPS to Logz.io, grouping them based on size. If the main thread quits, the handler attempts to send any remaining logs before exiting. If unsuccessful, the logs are saved to the local file system for later retrieval.


## Setup Logz.io Python Handler

 

*Supported versions*: Python 3.5 or newer. 

### Install dependency

Navigate to your project's folder and run:

```shell
pip install logzio-python-handler
```

For Trace context, install the OpenTelemetry logging instrumentation dependency by running:

```shell
pip install logzio-python-handler[opentelemetry-logging]
```

### Configure Python Handler for a standard project

Replace placeholders with your details. You must configure these parameters **by this exact order**. i.e. you cannot set Debug to true, without configuring all of the previous parameters as well.



|Parameter|Description| Required/Default |
|---|---|----|
| `<< LOG-SHIPPING-TOKEN >>` | Your Logz.io account log shipping token.                      | Required |
| `<< LOG-TYPE >>`           | Log type, for searching in logz.io.                           | `python` |
| `<<TIMEOUT>>`              | Time to sleep between draining attempts                       | `3`      |
| `<< LISTENER-HOST >>`      | Logz.io listener host, as described [here](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#regions-and-urls). | `https://listener.logz.io:8071` |
| `<<DEBUG-FLAG>>`           | Debug flag. If set to True, will print debug messages to stdout. | `false` |
| `<<BACKUP-LOGS>>`          | If set to False, disables the local backup of logs in case of failure.| `true`   |
| `<<NETWORK-TIMEOUT>>`      | Network timeout, in seconds, int or float, for sending the logs to logz.io. | `10`|
| `<<RETRY-LIMIT>>`          | Retries number                    | `4` |
| `<<RETRY-TIMEOUT>>`        | Retry timeout (retry_timeout) in seconds    | `2`|



```python
[handlers]
keys=LogzioHandler

[handler_LogzioHandler]
class=logzio.handler.LogzioHandler
formatter=logzioFormat

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


### Dictionary configuration:

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
### Django configuration

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

When using a serverless function, import and add LogzioFlusher annotation before your sender function. In the code example below umcomment `import` and the `@LogzioFlusher(logger)` annotation line. Next, ensure the Logz.io handler is added to the root logger.

Be sure to replace `superAwesomeLogzioLoggers` with the name of your logger.




```python
'loggers': {
     'superAwesomeLogzioLogger': {
         'level': 'DEBUG',
         'handlers': ['logzio'],
         'propagate': True
     }
 }
```

For example:

```python
import logging
import logging.config
# from logzio.flusher import LogzioFlusher
# from logzio.handler import ExtraFieldsLogFilter

# Say I have saved my configuration as a dictionary in a variable named 'LOGGING' - see 'Dict Config' sample section
logging.config.dictConfig(LOGGING)
logger = logging.getLogger('superAwesomeLogzioLogger')

# @LogzioFlusher(logger)
def my_func():
    logger.info('Test log')
    logger.warning('Warning')

    try:
        1/0
    except:
        logger.exception("Supporting exceptions too!")
```

### Dynamic extra fields

You can dynamically add extra fields to your logs without predefining them in the configuration. This allows each log to have unique extra fields.


``` python

logger.info("Test log") 

extra_fields = {"foo":"bar","counter":1}
logger.addFilter(ExtraFieldsLogFilter(extra_fields))
logger.warning("Warning test log") 

error_fields = {"err_msg":"Failed to run due to exception.","status_code":500}
logger.addFilter(ExtraFieldsLogFilter(error_fields))
logger.error("Error test log")  

# If you'd like to remove filters from future logs using the logger.removeFilter option:
logger.removeFilter(ExtraFieldsLogFilter(error_fields))
logger.debug("Debug test log") 
```

To add dynamic metadata to a specific log rather than to the logger, use the "extra" parameter. All key-value pairs in the dictionary passed to "extra" will appear as new fields in Logz.io. Note that you cannot override default fields set by the Python logger (e.g., lineno, thread).

For example:

```python
logger.info('Warning', extra={'extra_key':'extra_value'})
```

### Trace context

You can correlate your logs with the trace context by installing the OpenTelemetry logging instrumentation dependency:




```shell
pip install logzio-python-handler[opentelemetry-logging]
```

Enable this feature by setting `add_context` parameter to `True` in your handler configuration:



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

### Truncating logs

To create a Python logging filter that truncates log messages to a specific number of characters before processing, use the following code:

```python
class TruncationLoggerFilter(logging.Filter):
    def __init__(self):
        super(TruncationLoggerFilter, self).__init__()

    def filter(self, record):
        record.msg = record.msg[:32700]
        print(record.msg)
        return True

logger = logging.getLogger("logzio")
logger.addFilter(TruncationLoggerFilter())
```

The default limit is 32,700, but you can adjust this value as required.

</TabItem>
  <TabItem value="OpenTelemetry" label="OpenTelemetry">

This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites
    
- Python 3.7 or newer
- pip (Python package installer)
- A Python application
- An active account with Logz.io

:::note
If you need an example aplication to test this integration, please refer to our [Python OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/python/logs).
:::

1. Install OpenTelemetry dependencies:

    ```bash
    pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
    ```

2. Update the Flask Application to Include OpenTelemetry:


    ```python
    import logging
    from opentelemetry._logs import set_logger_provider
    from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
    from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
    
    # Configuration
    service_name = "YOUR-SERVICE-NAME"
    logzio_endpoint = "https://otlp-listener.logz.io/v1/logs"  # Update this to match your region if needed
    logzio_token = "<<LOG-SHIPPING-TOKEN>>"
    
    # Set up OpenTelemetry resources
    resource = Resource.create({"service.name": service_name})
    
    # Set up Logger Provider and OTLP Log Exporter (HTTP/JSON)
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    log_exporter = OTLPLogExporter(
        endpoint=logzio_endpoint,
        headers={
            "Authorization": f"Bearer {logzio_token}",
            "user-agent": "logzio-python-logs-otlp"
        }
    )
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))
    
    # Set up a specific logger for the application
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    
    # Attach OTLP handler to the specific logger
    otlp_handler = LoggingHandler(logger_provider=logger_provider)
    logger.addHandler(otlp_handler)
    
    # Example usage of the logger
    if __name__ == "__main__":
    logger.info("Log message sent to Logz.io")
    ```

    Replace `YOUR-SERVICE-NAME` with the required service name.


    {@include: ../../_include/log-shipping/log-shipping-token.md}

    Update the `listener.logz.io` part in `https://otlp-listener.logz.io/v1/logs` with the URL for [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).


3. Run your application.

    ```bash
    python app.py
    ```

### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

</TabItem>
</Tabs>


## Metrics

Send custom metrics to Logz.io from your Python application. This example uses [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python-contrib) and the [OpenTelemetry remote write exporter](https://pypi.org/project/opentelemetry-exporter-prometheus-remote-write/).



<Tabs>
  <TabItem value="Setup-in-code" label="Setup in code" default>

### Code configuration setup


**1. Install the snappy c-library**

DEB: `sudo apt-get install libsnappy-dev`

RPM: `sudo yum install libsnappy-devel`

OSX/Brew: `brew install snappy`

Windows: `pip install python_snappy-0.5-cp36-cp36m-win_amd64.whl`

**2.  Install the exporter and opentelemtry sdk**

```
pip install opentelemetry-exporter-prometheus-remote-write 
```

**3.  Add instruments to your application**

Replace the placeholders in the `exporter` section to match your specifics.


|Parameter|Description|
|---|---|
|LISTENER-HOST|  The Logz.io Listener URL for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. {@include: ../../_include//log-shipping/listener-var.html} and add http/https protocol (https://listener.logz.io:8053). |
|PROMETHEUS-METRICS-SHIPPING-TOKEN| Your Logz.io Prometheus Metrics account token.  {@include: ../../_include//p8s-shipping/replace-prometheus-token.html}  |



```python
from time import sleep
from typing import Iterable

from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.metrics import (
    CallbackOptions,
    Observation,
    get_meter_provider,
    set_meter_provider,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# configure the Logz.io listener endpoint and Prometheus metrics account token
exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint="https://<<LISTENER-HOST>>:8053",
    headers={
        "Authorization": "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>",
    },
)

reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
set_meter_provider(provider)


def observable_counter_func(options: CallbackOptions) -> Iterable[Observation]:
    yield Observation(1, {})


def observable_up_down_counter_func(
    options: CallbackOptions,
) -> Iterable[Observation]:
    yield Observation(-10, {})


def observable_gauge_func(options: CallbackOptions) -> Iterable[Observation]:
    yield Observation(9, {})


meter = get_meter_provider().get_meter("getting-started", "0.1.2")

# Counter
counter = meter.create_counter("counter")
counter.add(1)

# Async Counter
observable_counter = meter.create_observable_counter(
    "observable_counter",
    [observable_counter_func],
)

# UpDownCounter
updown_counter = meter.create_up_down_counter("updown_counter")
updown_counter.add(1)
updown_counter.add(-5)

# Async UpDownCounter
observable_updown_counter = meter.create_observable_up_down_counter(
    "observable_updown_counter", [observable_up_down_counter_func]
)

# Histogram
histogram = meter.create_histogram("histogram")
histogram.record(99.9)

# Async Gauge
gauge = meter.create_observable_gauge("gauge", [observable_gauge_func])
sleep(6)
```


#### Types of metric instruments


See OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md) for more details. 


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
# create an updowncounter instrument
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
# create an updownsumobserver instrument
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

**5.  Check Logz.io for your metrics**

Allow some time for your data to transfer. Then log in to your Logz.io Metrics account and open the [Metrics](https://app.logz.io/#/dashboard/metrics/) dashboard.








</TabItem>
  <TabItem value="Setup-Metrics-using-Lambda" label="Setup Metrics using Lambda">

### Setup Metrics using Lambda

This integration uses the OpenTelemetry collector extension and Python metrics SDK to create and send metrics from your Lambda functions to your Logz.io account.



:::note
This integration is currently supported in the following AWS regions: **us-east-1**, **us-east-2**,**us-west-1**, **us-west-2**, **ca-central-1**, **ap-northeast-2**, **ap-northeast-1**,**eu-central-1**, **eu-west-2**. Contact Logz.io [Customer Support](mailto:help@logz.io) for other regions.
:::

#### Create Lambda function

Create a new Lambda function in your AWS account (with Python version >= 3.8).

You can use our example [deployment package](https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-otel-lambda-python/logzio-python-lambda-custom-metrics-deployment.zip) by uploading the .zip file to the **code source** section inside your newly created Lambda function.


![Upload deployment package](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/uploadzip.gif)

#### Add OpenTelemetry collector config variable

Add the `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` environment variable with a value of `/var/task/collector.yaml`. This indicates the path to the configuration file.



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

Replace the placeholders to match your data:

|Environment variable|Description|
|---|---|
|`<<LISTENER-HOST>>`|  The Logz.io [Listener URL](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. |
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

#### Add Logz.io OTEL Python layer

Add the `logzio-otel-python-layer` lambda layer to your function:

```
arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-otel-python-layer:1
```

Replace `<<YOUR-AWS-REGION>>` with your AWS resgion.

#### Run the Lambda function

Run the Lambda function to send metrics to your Logz.io account.



#### Viewing metrics in Logz.io

Give your metrics time to process, after which they'll be available in your [Metrics](https://app.logz.io/#/dashboard/metrics/) dashboard.



#### Types of metric instruments

Refer to the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md) for more details.


| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values captured by the `histogram.Record(context,value,labels)` function, calculated per request. |


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

  <TabItem value="Prometheus-client-library" label="Setup Metrics with prometheus_client Library">

### Setup Metrics using prometheus_client Library

**1. Install Prometheus_client Library:**

```python
pip3 install Prometheus-client
```

**2. Add the prometheus_client library to your application**

In your Python script, use the prometheus_client library and expose the built-in metrics to the Prometheus HTTP server:

```python
from prometheus_client import start_http_server
import time


def main():
   # Start up the server to expose the metrics.
   start_http_server(8000)
   # Generate some requests.
   while True:
       time.sleep(1)


if __name__== '__main__':
   main() 
```

**3. Add system metrics (if required)**


For non-Linux OS, install the psutil library:

1. Instal the `psutil` library:

   ```python
   psutil library - pip3 install psutil
   ```

2. Add the following script to your code:

   ```python
   from prometheus_client import start_http_server, Gauge
   import time
   import psutil
   import os
   import resource
   
   
   # Create gauges
   cpu_seconds_total = Gauge('python_process_cpu_seconds_total', 'Total user and system CPU time spent in seconds.')
   virtual_memory_bytes = Gauge('python_process_virtual_memory_bytes', 'Virtual memory size in bytes.')
   resident_memory_bytes = Gauge('python_process_resident_memory_bytes', 'Resident memory size in bytes.')
   open_fds = Gauge('python_process_open_fds', 'Number of open file descriptors.')
   max_fds = Gauge('python_process_max_fds', 'Maximum number of open file descriptors.')
   total_memory = Gauge('python_process_total_memory_bytes', 'Total memory size in bytes.')
   
   
   def collect_metrics():
      while True:
          p = psutil.Process(os.getpid())
          # Collect metrics
          cpu_seconds_total.set(p.cpu_times().user + p.cpu_times().system)
          virtual_memory_bytes.set(p.memory_info().vms)
          resident_memory_bytes.set(p.memory_info().rss)
          open_fds.set(p.num_fds())
          max_fds.set(resource.getrlimit(resource.RLIMIT_NOFILE)[1])
          total_memory.set(psutil.virtual_memory().total)
          time.sleep(1)
   
   
   if __name__ == '__main__':
      start_http_server(8000)
      collect_metrics()
   ```


**3. Check metrics locally**

Go to `localhost:8000` to see the metrics.

**4. Download OpenTelemetry collector**

:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the OpenTelemetry collector for your OS.

Create a configuration file `config.yaml` with the following: 

#### Receivers configuration


```yaml
receivers: 
 prometheus:
   config:
     scrape_configs:
       - job_name: otel-collector-python
         scrape_interval: 5s
         static_configs:
           - targets: ['localhost:8000']
```

#### Exporters configuration

```yaml
exporters:
 logging:
 prometheusremotewrite:
   resource_to_telemetry_conversion:
     enabled: true
   endpoint: https://<<LISTENER-HOST>>:8053
   headers:
     Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
```

{@include: ../../_include/log-shipping/listener-var.html}

{@include: ../../_include/p8s-shipping/replace-prometheus-token.html}

#### Processors and Service configuration

```yaml
processors:
resourcedetection/system:
  detectors: ["system"]
  system:
    hostname_sources: ["os"]


service:
 pipelines:
   metrics:
     receivers: [prometheus]
     processors: [resourcedetection/system]
     exporters: [prometheusremotewrite, logging]
```

**5. Start the Collector**

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the directory path where you downloaded the collector. Adjust the configuration file name if it is different.



#### Viewing metrics in Logz.io

Give your metrics time to process, after which they'll be available in your [Metrics](https://app.logz.io/#/dashboard/metrics/) dashboard.




</TabItem>
</Tabs>

## Traces

Deploy this integration to enable automatic instrumentation of your Python application using OpenTelemetry.

## Architecture overview

This integration includes:

* Installing the OpenTelemetry Python instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your Python application in conjunction with the OpenTelemetry instrumentation

On deployment, the Python instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.
<Tabs>
<TabItem value="python-traces-localhost" label="Local Host" default>

### Local host Python application auto instrumentation

**Requirements**:

* A Python application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  

#### Install OpenTelemetry components for Python


```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

After installation, configure the exporter with this command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```
 
#### Download and configure OpenTelemetry collector

Create a directory on your Python application and download the relevant [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.111.0). Create a `config.yaml` with the following parameters:

* {@include: ../../_include/tracing-shipping/replace-tracing-token.md}

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/tail-sampling.md}


#### Start the collector

Run:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the collector's directory.
* Replace `<VERSION-NAME>` with the version name, e.g. `otelcontribcol_darwin_amd64`.

#### Run OpenTelemetry with your Python application

Run this code from the directory of your Python application script:

```shell
opentelemetry-instrument python3 <YOUR-APPLICATION-SCRIPT>.py
```

Replace `<YOUR-APPLICATION-SCRIPT>` with your Python application script name.

#### Viewing Traces in Logz.io

Give your traces time to process, after which they'll be available in your [Tracing](https://app.logz.io/#/dashboard/jaeger) dashboard.


</TabItem>
<TabItem value="python-traces-docker" label="Docker" default>

### Docker Python application auto instrumentation

Auto-instrument your Python application and run a containerized OpenTelemetry collector to send traces to Logz.io. Ensure both application and collector containers share the same network.

**Requirements**:

* A Python application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service


#### Install OpenTelemetry instrumentation components


```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

Configure the exporter by running:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with your tracing service name.


#### Pull OpenTelemetry collector docker image


```shell
docker pull otel/opentelemetry-collector-contrib:0.111.0
```

#### Create a configuration file

Create a `config.yaml` file with the following content:

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
 

If you already have an OpenTelemetry installation, add these parameters to your existing collector's configuration file:




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

An example configuration file:

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

Mount `config.yaml` as volume to the `docker run` command and run it as follows.

##### Linux

```
docker run  \
--network host \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
otel/opentelemetry-collector-contrib:0.111.0

```

Replace `<PATH-TO>` to the path to the `config.yaml` file on your system.

##### Windows

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
otel/opentelemetry-collector-contrib:0.111.0
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

#### Run the OpenTelemetry instrumentation in conjunction with your Python application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run this code from your Python application script directory:

```shell
opentelemetry-instrument python3 `<<YOUR-APPLICATION-SCRIPT>>`.py
```

Replace `<<YOUR-APPLICATION-SCRIPT>>` with your Python application script name.

#### Viewing Traces in Logz.io

Give your traces time to process, after which they'll be available in your [Tracing](https://app.logz.io/#/dashboard/jaeger) dashboard.
</TabItem>
<TabItem value="python-traces-ecs" label="ECS" default>

## Python Application Setup for ECS Service with OpenTelemetry

This guide provides an overview of deploying your Python application on Amazon ECS, using OpenTelemetry to collect and send tracing data to Logz.io. It offers a step-by-step process for setting up OpenTelemetry instrumentation and deploying both the application and OpenTelemetry Collector sidecar in an ECS environment.

#### Prerequisites

Before you begin, ensure you have the following prerequisites in place:

- AWS CLI configured with access to your AWS account.
- Docker installed for building images.
- AWS IAM role with sufficient permissions to create and manage ECS resources.
- Amazon ECR repository for storing the Docker images.
- Python 3.x and pip installed locally for development and testing.

:::note
For a complete example, refer to [this repo](https://github.com/logzio/opentelemetry-examples/tree/main/python/traces/ecs-service).
:::

#### Architecture Overview

The deployment will involve two main components:

1. Python Application Container

   A container running your Python application, instrumented with OpenTelemetry to capture traces.

2. OpenTelemetry Collector Sidecar

   A sidecar container that receives telemetry data from the application, processes it, and exports it to Logz.io.

The architecture is structured as follows:

```
project-root/
├── python-app/                      # Your Python application directory
│   ├── app.py                       # Python application entry point
│   ├── Dockerfile                   # Dockerfile to build Python application image
│   └── requirements.txt             # Python dependencies, includes OpenTelemetry
├── ecs/
│   └── task-definition.json         # ECS task definition file
└── otel-collector
     ├── collector-config.yaml        # OpenTelemetry Collector configuration
     └── Dockerfile                   # Dockerfile for the Collector
```

#### Steps to Deploy the Application

1. Project Structure Setup

   Ensure your project structure follows the architecture outline. You should have a directory for your Python application and a separate directory for the OpenTelemetry Collector.

2. Set Up OpenTelemetry Instrumentation

   Add OpenTelemetry instrumentation to your Python application by including the necessary OpenTelemetry packages and configuring the tracing setup. This can be done by installing the `opentelemetry-distro` and `opentelemetry-instrumentation-flask` packages and using them to instrument your Flask app.

Install dependencies:

#### requirements.txt

```
flask
opentelemetry-distro
opentelemetry-exporter-otlp
opentelemetry-instrumentation-flask
```

The package `opentelemetry-instrumentation-flask` handles the automatic instrumentation of Flask at runtime.

#### Dockerize Your Application

Create a Dockerfile to build a Docker image of your Python application. Below is the Dockerfile to get started:

#### Dockerfile

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for OpenTelemetry configuration
ENV OTEL_TRACES_SAMPLER=always_on
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
ENV OTEL_RESOURCE_ATTRIBUTES="service.name=python-app"

EXPOSE 5000

CMD ["opentelemetry-instrument", "python", "app.py"]
```

#### Configure the OpenTelemetry Collector

The OpenTelemetry Collector receives traces from the application and exports them to Logz.io. Create a `collector-config.yaml` file to define how the Collector should handle traces.

#### collector-config.yaml

{@include: ../../_include/tracing-shipping/collector-config.md}

#### Build Docker Images

Build Docker images for both the Node.js application and the OpenTelemetry Collector:

```shell
# Build Node.js application image
cd python-app/
docker build --platform linux/amd64 -t your-python-app:latest .

# Build OpenTelemetry Collector image
cd ../otel-collector/
docker build --platform linux/amd64 -t otel-collector:latest .
```

#### Push Docker Images to Amazon ECR

Push both images to your Amazon ECR repository:

```shell
# Authenticate Docker to Amazon ECR
aws ecr get-login-password --region <aws-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

# Tag and push images
docker tag your-python-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/your-python-app:latest
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/your-python-app:latest

docker tag otel-collector:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/otel-collector:latest
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/otel-collector:latest
```

##### Log Group Creation: 

Create log groups for your Python application and OpenTelemetry Collector in CloudWatch.

```shell
aws logs create-log-group --log-group-name /ecs/python-app
aws logs create-log-group --log-group-name /ecs/otel-collector
```

#### Define ECS Task

Create a task definition (task-definition.json) for ECS that defines both the Node.js application container and the OpenTelemetry Collector container.

#### task-definition.json

```json
{
  "family": "your-python-app-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::<aws_account_id>:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "your-python-app",
      "image": "<aws_account_id>.dkr.ecr.<region>.amazonaws.com/your-python-app:latest",
      "cpu": 128,
      "portMappings": [
        {
          "containerPort": 5000,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "environment": [],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/your-python-app",
          "awslogs-region": "<aws-region>",
          "awslogs-stream-prefix": "ecs"
        }
      }
    },
    {
      "name": "otel-collector",
      "image": "<aws_account_id>.dkr.ecr.<aws-region>.amazonaws.com/otel-collector:latest",
      "cpu": 128,
      "essential": false,
      "command": ["--config=/etc/collector-config.yaml"],
      "environment": [
        {
          "name": "LOGZIO_TRACING_TOKEN",
          "value": "<logzio_tracing_token>"
        },
        {
          "name": "LOGZIO_REGION",
          "value": "<logzio_region>"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/otel-collector",
          "awslogs-region": "<aws-region>",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

#### Deploy to ECS

- Create an ECS Cluster: Create a cluster to deploy your containers:

  ```shell
  aws ecs create-cluster --cluster-name your-app-cluster --region <aws-region>
  ```

- Register the Task Definition:

  ```shell
  aws ecs register-task-definition --cli-input-json file://ecs/task-definition.json
  ```

- Create ECS Service: Deploy the task definition using a service:

  ```shell
  aws ecs create-service \
    --cluster your-app-cluster \
    --service-name your-python-app-service \
    --task-definition your-python-app-task \
    --desired-count 1 \
    --launch-type FARGATE \
    --network-configuration "awsvpcConfiguration={subnets=[\"YOUR_SUBNET_ID\"],securityGroups=[\"YOUR_SECURITY_GROUP_ID\"],assignPublicIp=ENABLED}" \
    --region <aws-region> \
  ```

#### Verify Application and Tracing

After deploying, run your application to generate activity that will create tracing data. Wait a few minutes, then check the Logz.io dashboard to confirm that traces are being sent correctly.

---
</TabItem>
<TabItem value="python-traces-k8s" label="Kuberenetes" default>

### Kuberenetes Python application auto insturmentation 


Use a Helm chart to ship traces to Logz.io via the OpenTelemetry collector. The Helm tool manages packages of preconfigured Kubernetes resources.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

 
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts is [logzio-helm](https://github.com/logzio/logzio-helm).
:::



 
:::caution 
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::

  


#### Standard configuration



**1. Deploy the Helm chart**

 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

**2.  Run the Helm deployment code**

```
helm install  \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set logzio-k8s-telemetry.secrets.TracesToken=<<TRACING-SHIPPING-TOKEN>> \
logzio-monitoring logzio-helm/logzio-monitoring -n monitoring
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
`<<LOGZIO_ACCOUNT_REGION_CODE>>` - Your Logz.io account region code. [Available regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).


**3. Define the service DNS**

You'll need the following service DNS:

`http://<<CHART-NAME>>-otel-collector.<<NAMESPACE>>.svc.cluster.local:<<PORT>>/`.

Replace `<<CHART-NAME>>` with the relevant service you're using (`logzio-k8s-telemetry`, `logzio-monitoring`).
Replace `<<NAMESPACE>>` with your Helm chart's deployment namespace (e.g., default or monitoring).
Replace `<<PORT>>` with the [port for your agent's protocol](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-telemetry/values.yaml#L249-L267) (Default is 4317).

If you're not sure what your cluster domain name is, you can run the following command to look it up:

```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.<<NAMESPACE>> | grep Name | sed "s/Name:\skubernetes.<<NAMESPACE>>//"'
```

This command deploys a pod to extract your cluster domain name, which can be removed after.

**4.  Install general Python OpenTelemetry instrumentation components**

```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

**5. Set environment variables**

Configure the exporter by running the following command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with your tracing service name.

**6. Viewing Traces in Logz.io**

Give your traces time to process, after which they'll be available in your [Tracing](https://app.logz.io/#/dashboard/jaeger) dashboard.



#### Customizing Helm chart parameters

You can update Helm chart parameters in three ways:

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Override default values with your own `my_values.yaml` and apply it in the `helm install` command. 

Optional parameters can be added as environment variables:
  
| Parameter | Description | Default |
|---|---|---|
| secrets.SamplingLatency | Threshold for the span latency - all traces slower than the threshold value will be filtered in. | `500` |
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. | `10` |

##### Example

You can run the logzio-k8s-telemetry chart with a custom configuration file that takes precedence over the `values.yaml` of the chart by running the following:


```
helm install -f <PATH-TO>/my_values.yaml \
--set logzio-k8s-telemetry.secrets.TracesToken=<<TRACES-SHIPPING-TOKEN>> \
--set logzio-k8s-telemetry.secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set metricsOrTraces=true \
logzio-monitoring logzio-helm/logzio-monitoring
```

Replace `<PATH-TO>` with your custom `values.yaml` file path.

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


 
:::note
The collector will sample **ALL traces** that contain any span with an error with this example configuration. 
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






#### Uninstalling the Chart


To uninstall the `logzio-monitoring` deployment, run:

```shell
helm uninstall logzio-monitoring
```

</TabItem>
<TabItem value="opentelemetry-lambda" label="Lambda via OpenTelemetry" default>

Deploy this integration to auto-instrument your Python application running on AWS Lambda and send the traces to your Logz.io account. This is done by adding a dedicated layer for OpenTelemetry collector, a dedicated layer for Python auto-instrumentation and configuring environment variables of these layers. This integration will require no change to your application code.


:::note
This integration only works for the following AWS regions: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`,
`ap-south-1`, `ap-northeast-3`, `ap-northeast-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`,
`eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `eu-north-1`,
`sa-east-1`,
`ca-central-1`.
:::

**Before you begin, you'll need**:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Configured [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- A Lambda function with a Python application that is not yet instrumented.

:::note
Using `aws lambda update-function-configuration` with `--layers` replaces all existing layers with the specified ARN(s). To add a new layer without removing existing ones, include all desired layer ARNs in the command, both new and previously attached.
:::

:::note
Adding environmental variables using the AWS CLI commands below, will overwrite all existing variables for your Lambda function.
:::

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::

**Instrumentation adds overhead.** A 60-second timeout ensures reliable trace exports.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --timeout 60
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of the Lambda function you want to update.

#### Add the OpenTelemetry collector layer to your Lambda function

This layer contains the OpenTelemetry collector that will capture data from your application.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers <<LAYER-ARN>>
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Python application.

Copy the appropriate `<<LAYER-ARN>>` for your Lambda architecture (amd64 or arm64) from the [latest release notes](https://github.com/logzio/opentelemetry-lambda/releases).

Replace `<<REGION>>` with the code of your AWS regions. [See all available Logz.io hosting regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).

#### Create a configuration file for the OpenTelemetry collector

By default, the OpenTelemetry collector layer exports data to the Lambda console. To customize the collector configuration, you need to add a `collector.yaml` to your function and specify its location via the `OPENTELEMETRY_COLLECTOR_CONFIG_URI` environment variable.
The `collector.yaml` file will have the following configuration:

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
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [logzio/traces]
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

{@include: ../../_include/tracing-shipping/tail-sampling.md}

#### Direct the OpenTelemetry collector to the configuration file

Add `OPENTELEMETRY_COLLECTOR_CONFIG_URI` variable to direct the OpenTelemetry collector to the configuration file:

```
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_URI=<<PATH_TO_YOUR_COLLECTOR.YAML>>}
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Python application.

Replace `<<PATH_TO_YOUR_COLLECTOR.YAML>>` with the actual path to your `collector.yaml` file.
(If `collector.yaml` is located in the root directory of your application, use the path `/var/task/collector.yaml`.)

#### Activate tracing for your Lambda function

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --tracing-config Mode=Active
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Python application.

#### Add the OpenTelemetry Python wrapper layer to your Lambda function

The OpenTelemetry Python wrapper layer automatically instruments the Python application in your Lambda function.
Find the latest ARN for the OpenTelemetry Python wrapper layer on the [OpenTelemetry Lambda GitHub Releases page](https://github.com/open-telemetry/opentelemetry-lambda/releases) under `layer-python`.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers <LAYER_ARN>
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Python application.

Replace `<<LAYER_ARN>>` with the latest ARN from the GitHub releases page.

Replace `<<REGION>>` with the code of your AWS regions, e.g. `us-east-1`.

#### Add environment variable for the wrapper

Add the `AWS_LAMBDA_EXEC_WRAPPER` environment variable to point to the `otel-instrument` executable:
```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument}
```
Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Python application.

</TabItem>
</Tabs>

## Troubleshooting


* [Python logging troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-python/).
 
* [OpenTelemetry troubleshooting guide](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/otel-troubleshooting/).

* [Distributed Tracing troubleshooting guide](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/tracing-troubleshooting/)