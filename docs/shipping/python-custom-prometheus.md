---
id: Python-custom-prometheus
title: Python custom metrics
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---
 

This page contains instructions on how to send custom metrics to Logz.io from your Python application. This example uses the [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python-contrib) and the [OpenTelemetry remote write exporter](https://pypi.org/project/opentelemetry-exporter-prometheus-remote-write/), which are both in alpha/preview.
 

#### Quick start


 

##### Install the snappy c-library

DEB: `sudo apt-get install libsnappy-dev`

RPM: `sudo yum install libsnappy-devel`

OSX/Brew: `brew install snappy`

Windows: `pip install python_snappy-0.5-cp36-cp36m-win_amd64.whl`

##### Install the exporter and opentelemtry sdk
```
pip install opentelemetry-exporter-prometheus-remote-write
```

##### Add instruments to your application

Replace the placeholders in the `exporter` section code (indicated by the double angle brackets `<< >>`) to match your specifics.


|Environment variable|Description|
|---|---|
|endpoint|  The Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. {@include: ../_include//log-shipping/listener-var.html} and add http/https protocol (https://listener.logz.io:8053) |
|Bearer| Your Logz.io Prometheus Metrics account token.  {@include: ../_include//p8s-shipping/replace-prometheus-token.html}  |



```python
from opentelemetry import metrics
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.sdk.metrics import MeterProvider

# configure the Logz.io listener endpoint and Prometheus metrics account token
exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint="<<LISTENER-HOST>>:8053",
    headers={
        "Authorization": "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>",
    }
)
# set push interval in seconds
push_interval = 15

# setup metrics export pipeline
metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__)
metrics.get_meter_provider().start_pipeline(meter, exporter, push_interval)

# create a counter instrument and provide the first data point
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
counter.add(25, labels)
```


## Types of metric instruments


Refer to the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md) for more details. 


| Name | Behavior | Default aggregation |
| ---- | ---------- | ------------------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.add(value,labels)` request. | Sum |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.add(value,labels)` request. | Sum |
| ValueRecorder     | Metric values captured by the `valuerecorder.record(value)` function, calculated per request. | TBD  |
| SumObserver       | Metric value can only go up or be reset to 0, calculated per push interval.| Sum |
| UpDownSumObserver | Metric value can arbitrarily increment or decrement, calculated per push interval.| Sum |
| ValueObserver     | Metric values captured by the `valuerecorder.observe(value)` function, calculated per push interval.| LastValue  |

### [Counter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#counter)
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

### [UpDownCounter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#updowncounter)
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

### [ValueRecorder](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#valuerecorder)
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

### [SumObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#sumobserver)
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

### [UpDownSumObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#updownsumobserver)
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

### [ValueObserver](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#valueobserver)
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

##### Check Logz.io for your metrics
Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

  
This integration uses OpenTelemetry collector extention and Python metrics SDK to create and send metrics from your Lambda functions to your Logz.io account.

:::note
This integration is currently only supported in the following AWS regions: **us-east-1**, **us-east-2**,**us-west-1**, **us-west-2**, **ca-central-1**, **ap-northeast-2**, **ap-northeast-1**,**eu-central-1**, **eu-west-2**. Contact Logz.io Customer Support if you need to deploy in a different region.
:::
 

#### Quick start


 

##### Create Lambda function

Create a new Lambda function in your AWS account (with Python version >= 3.8).

After creating your new Lambda function, you can use our example [deployment package](https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-otel-lambda-python/logzio-python-lambda-custom-metrics-deployment.zip) that includes the code sample. Upload the .zip file to the **code source** section inside your newly created Lambda function.


![Upload deployment package](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/uploadzip.gif)

##### Add OpenTelemetry collector config variable

Add `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` environment variable with a value of `/var/task/collector.yaml`. This will tell the collector extention the path to the configuration file.

##### Add OpenTelemetry config file

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
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| {@include: ../_include/p8s-shipping/replace-prometheus-token.html}  |


##### Create Lambda function Python script

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

##### Add Logz.io Otel Python layer

Add the `logzio-otel-python-layer` lambda layer to your function:

```
arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-otel-python-layer:1
```

Replace `<<YOUR-AWS-REGION>>` with your AWS resgion.

##### Run the Lambda function

Start running the Lambda function to send metrics to your Logz.io account.



##### Check Logz.io for your metrics
Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


## Types of metric instruments

For more information, see the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md).

| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values captured by the `histogram.Record(context,value,labels)` function, calculated per request. |

### More examples

#### Counter

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

#### Up down counter


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
 