---
id: GO
title: GO
overview: Send logs, metrics and traces from you Go code
product: ["logs","metrics","tracing"]
os: ["windows", "linux"]
filters: ["Code", "AWS", "Compute"]
recommendedFor: ["Software Engineer"]
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/go.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ["2cm0FZu4VK4vzH0We6SrJb"]
metrics_alerts: ["1UqjU2gqNAKht1f62jBC9Q"]
drop_filter: []
---

:::tip
If your code is running inside Kubernetes the best practice will be to use our [kubernetes integrations](https://docs.logz.io/shipping/Containers/Kubernetes).
:::

## Logs

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="golang-api-client" label="Logz.io Golang API client" default>

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-go/)
:::

This shipper uses **goleveldb** and **goqueue** as a persistent storage implementation of a persistent queue, so the shipper backs up your logs to the local file system before sending them.
Logs are queued in the buffer and 100% non-blocking.
A background Go routine ships the logs every 5 seconds.

### Set up the Logz.io Golang API client

**Before you begin, you'll need**:
Go 1.x or higher

 

### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
go get -u github.com/logzio/logzio-go
```

### Configure the client

Use the sample in the code block below as a starting point, and replace the sample with a configuration that matches your needs.

For a complete list of options, see the configuration parameters below the code block.👇

```go
package main

import (
  "fmt"
  "os"
  "time"
  "github.com/logzio/logzio-go"
)

func main() {
  // Replace these parameters with your configuration
  l, err := logzio.New(
    "<<LOG-SHIPPING-TOKEN>>",
    logzio.SetDebug(os.Stderr),
    logzio.SetUrl("https://<<LISTENER-HOST>>:8071"),
    logzio.SetDrainDuration(time.Second * 5),
    logzio.SetTempDirectory("myQueue"),
    logzio.SetDrainDiskThreshold(99),
  )
  if err != nil {
    panic(err)
  }

  // Because you're configuring directly in the code,
  // you can paste the code sample here to send a test log.
  //
  // The code sample is below the parameters list. 👇
}
```

#### Parameters 

| Parameter | Description | Required/Default |
|---|---|---|
| `<<LOG-SHIPPING-TOKEN>>` | {@include: ../../_include/log-shipping/log-shipping-token.md}   | Required |
| SetUrl | Listener URL and port.    {@include: ../../_include/log-shipping/listener-var.html}  |Required (default:  `https://listener.logz.io:8071`) |
| SetDebug | Debug flag. | `false` |
| SetDrainDuration  | Time to wait between log draining attempts. | `5 * time.Second` |
| SetTempDirectory | Filepath where the logs are buffered. | -- |
| SetCheckDiskSpace  | To enable `SetDrainDiskThreshold`, set to `true`. Otherwise, `false`. | `true` |
| SetDrainDiskThreshold  | Maximum file system usage, in percent. Used only if `SetCheckDiskSpace` is set to `true`. If the file system storage exceeds this threshold, buffering stops and new logs are dropped. Buffering resumes if used space drops below the threshold. | `70.0` |


#### Code sample

```go
msg := fmt.Sprintf("{\"%s\": \"%d\"}", "message", time.Now().UnixNano())
err = l.Send([]byte(msg))
if err != nil {
  panic(err)
}

l.Stop() // Drains the log buffer
```

</TabItem>
  <TabItem value="OpenTelemetry" label="OpenTelemetry">

This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites
    
- Go 1.21 or newer

:::note
If you need an example application to test this integration, please refer to our [Go OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/go/logs).
:::

### Configure the instrumentation


1. Install OpenTelemetry dependencies:

   ```bash
   go get go.opentelemetry.io/otel
   go get go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp
   go get go.opentelemetry.io/otel/exporters/stdout/stdoutlog
   ```

2. Create a new file named `otel.go` and add the following code to set up OpenTelemetry logging:


   ```go
   package main

   import (
   	"context"
   	"fmt"
   	"log"
   
   	"go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp"
   	"go.opentelemetry.io/otel/exporters/stdout/stdoutlog"
   	"go.opentelemetry.io/otel/log/global"
   	sdklog "go.opentelemetry.io/otel/sdk/log"
   )
   
   func newLoggerProvider() (*sdklog.LoggerProvider, error) {
   	// Create stdout log exporter
   	stdoutExporter, err := stdoutlog.New(stdoutlog.WithPrettyPrint())
   	if err != nil {
   		return nil, fmt.Errorf("failed to create stdout exporter: %w", err)
   	}
   
   	// Create OTLP HTTP log exporter for Logz.io
   	httpExporter, err := otlploghttp.New(context.Background(),
   		otlploghttp.WithEndpoint("otlp-listener.logz.io"),
   		otlploghttp.WithHeaders(map[string]string{
   			"Authorization": "Bearer <LOG-SHIPPING-TOKEN>",
   			"user-agent":    "logzio-go-logs-otlp",
   		}),
   		otlploghttp.WithURLPath("/v1/logs"),
   	)
   	if err != nil {
   		return nil, fmt.Errorf("failed to create OTLP HTTP exporter: %w", err)
   	}
   
   	// Create a logger provider with both exporters
   	loggerProvider := sdklog.NewLoggerProvider(
   		sdklog.WithProcessor(sdklog.NewBatchProcessor(stdoutExporter)), // For stdout
   		sdklog.WithProcessor(sdklog.NewBatchProcessor(httpExporter)),   // For HTTP export
   	)
   
   	return loggerProvider, nil
   }
   
   // setupOTelSDK bootstraps the OpenTelemetry logging pipeline.
   func setupOTelSDK(ctx context.Context) (shutdown func(context.Context) error, err error) {
   	// Set up logger provider.
   	loggerProvider, err := newLoggerProvider()
   	if err != nil {
   		return nil, err
   	}
   
   	// Set the global logger provider
   	global.SetLoggerProvider(loggerProvider)
   
   	// Return a shutdown function
   	shutdown = func(ctx context.Context) error {
   		err := loggerProvider.Shutdown(ctx)
   		if err != nil {
   			log.Printf("Error during logger provider shutdown: %v", err)
   		}
   		return err
   	}
   
   	return shutdown, nil
   }
   
   ```


   {@include: ../../_include/log-shipping/log-shipping-token.md}
   Update the `listener.logz.io` part in `https://otlp-listener.logz.io/v1/logs` with the URL for [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).


3. Run your application.

### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.


</TabItem>
</Tabs>

## Metrics

:::note
[Project's GitHub repo](https://github.com/logzio/go-metrics-sdk/)
:::

The Logz.io Go Metrics Exporter enables you to send metrics directly from your code using the Prometheus Remote Write API.
Below, you'll find a guide for setting it up, along with examples of how to manually instrument your application using the OpenTelemetry SDK.

### Install the Logzio Metrics exporter

Run the following command:

```shell
go get github.com/logzio/go-metrics-sdk
```

### Configure the exporter

Add the exporter definition to your application code:

```go
import (
    "context"
    metricsExporter "github.com/logzio/go-metrics-sdk"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/attribute"
    m "go.opentelemetry.io/otel/metric"
    "go.opentelemetry.io/otel/sdk/metric"
    "go.opentelemetry.io/otel/sdk/resource"
    semconv "go.opentelemetry.io/otel/semconv/v1.26.0"
    "log"
    "time"
)

func newLogzioExporter() (*metricsExporter.Exporter, error) {
    return metricsExporter.New(
        metricsExporter.Config{
            LogzioMetricsListener: "https://<<LISTENER-HOST>>:8053",
            LogzioMetricsToken:    "<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>",
            RemoteTimeout:         30 * time.Second,
            PushInterval:          10 * time.Second,
            Quantiles:             []float64{0, 0.25, 0.5, 0.75, 1},
            AddMetricSuffixes: true,
            ExternalLabels: map[string]string{
                "<<LABEL_KEY>>": "<<LABEL_VALUE>>",
            },
        })
}
```

### Exporter parameters

Replace the placeholders in the code to match your specifics.

| Parameter Name        | Description                                                                           | Required/Optional | Default                       |
|-----------------------|---------------------------------------------------------------------------------------|-------------------|-------------------------------|
| LogzioMetricsListener | The full Logz.io Listener URL for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic (example: https://listener.logz.io:8053). For more details, see the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) in logz.io docs                      | Required          | https://listener.logz.io:8053 |
| LogzioMetricsToken    | The Logz.io Prometheus Metrics account token. Find it under **Settings > Manage accounts**. [Look up your Metrics account token.](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/) | Required          | -                             |
| RemoteTimeout         | The timeout for requests to the remote write Logz.io metrics listener endpoint.       | Required          | 30 (seconds)                  |
| PushInterval          | The time interval for sending the metrics to Logz.io.                                 | Required          | 10 (seconds)                  |
| Quantiles             | The quantiles of the histograms.                                                      | Optional          | [0.5, 0.9, 0.95, 0.99]        |
| HistogramBoundaries   | The histogram boundaries.                                                             | Optional          | -                             |
| ExternalLabels        | Allow adding global labels to all metrics that are processed by the exporter.         | Optional          | -                             |
| AddMetricSuffixes     | Adds Unit suffix to the metric, if the Unit was defined.                              | Optional          | `false`                       |


### Set up the Metric Instruments Creator
	
Create `Meter` to be able to create metric instruments.

```go
func newResource() (*resource.Resource, error) {
    return resource.Merge(resource.Default(),
        resource.NewWithAttributes(semconv.SchemaURL,
            semconv.ServiceName("<<SERVICE_NAME>>"),
            semconv.ServiceVersion("<<SERVICE_VERSION>>"),
        ))
}

func newMeterProvider(res *resource.Resource) (*metric.MeterProvider, error) {
    metricExporter, err := newLogzioExporter()
	if err != nil {
        return nil, err
    }

    meterProvider := metric.NewMeterProvider(
        metric.WithResource(res),
        metric.WithReader(metric.NewPeriodicReader(metricExporter,
        metric.WithInterval(60*time.Second))),
    )
    return meterProvider, nil
}

// create a context
con := context.Background()

// Create resource
res, err := newResource()
if err != nil {
    panic(err)
}

// Create a meter provider.
meterProvider, err := newMeterProvider(res)
if err != nil {
	panic(err)
}

// Handle shutdown properly so nothing leaks.
defer func() {
    if err := meterProvider.Shutdown(con); err != nil {
        log.Println(err)
    }
}()

// Register as global meter provider so that it can be used via otel.Meter
// and accessed using otel.GetMeterProvider.
// Most instrumentation libraries use the global meter provider as default.
// If the global meter provider is not set then a no-op implementation
// is used, which fails to generate data.
otel.SetMeterProvider(meterProvider)

meter := otel.Meter("example-meter")  // replace `example-meter` with any custom instrumentation meter name you'd like
```


### Add metric instruments

Add a required metric intrument to your code. Below are the available metric instruments and their code definition.


The exporter uses the `simple` selector's `metric.DefaultAggregationSelector()`. This means that the instruments are mapped to aggregations as shown in the table below.

| Instrument | Behavior | Aggregation |
| --- | --- | --- |
| Counter | A synchronous Instrument which supports non-negative increments. | Sum |
| Asynchronous Counter | An asynchronous Instrument which reports monotonically increasing value(s) when the instrument is being observed. | Sum |
| Histogram | A synchronous Instrument which can be used to report arbitrary values that are likely to be statistically meaningful. It is intended for statistics such as histograms, summaries, and percentile. | Histogram |
| Asynchronous Gauge | An asynchronous Instrument which reports non-additive value(s) when the instrument is being observed. | Gauge |
| UpDownCounter | A synchronous Instrument which supports increments and decrements. | Sum |
| Asynchronous UpDownCounter | An asynchronous Instrument which reports additive value(s) when the instrument is being observed. | Sum |

#### Counter

```go
// Create counter instruments
counter, err := meter.Int64Counter(
    "int_counter",  // name of the metric
    // m.WithUnit("ms")  // add a unit to the metric, if needed
    m.WithDescription("Counts the total number of requests"),
)

floatCounter, err := meter.Float64Counter("float_counter")  // name of the metric

// Record values to the metric instruments and add labels
counter.Add(con, 1)
counter.Add(con, 10, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
floatCounter.Add(con, 2.5)
```

#### Asynchronous Counter

```go
// Create callbacks for your observable counter instruments
// Float64ObservableCounter is also a supported type
observableCounter, err := meter.Int64ObservableCounter(
    "observable_counter",  // name of the metric
    // m.WithUnit("By"),  // add a unit to the metric, if needed
    m.WithDescription("observable counter description"),
)

_, err = meter.RegisterCallback(
    func(con context.Context, o m.Observer) error {
        o.ObserveInt64(observableCounter, 10, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
        return nil
    },
    observableCounter,
)
```

#### Histogram

```go
// Create Histogram instruments
intHistogram, err := meter.Int64Histogram(
	"histogram-meter",  // name of the metric
    // m.WithUnit("seconds")  // add a unit to the metric, if needed
    m.WithDescription("Histogram description"),
)

floatHistogram, err := meter.Float64Histogram("float-histogram-meter")  // name of the metric

// Record values to the metric instruments and add labels
intHistogram.Record(con, 2)
intHistogram.Record(con, 2, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
floatHistogram.Record(con, 3.4)
```

#### Gauge

```go
g, err := meter.Int64Gauge(
	"g-test",
	// m.WithUnit("seconds"),  // add a unit to the metric, if needed
    m.WithDescription("Gauge description"),
)

g.Record(con, 4)
g.Record(con, 4, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
```

#### Asynchronous Gauge

```go
// Create callbacks for your observable up-down counter instruments
// Float64ObservableGauge is also a supported type
observableGauge, err := meter.Int64ObservableGauge(
    "observable_gauge",  // name of the metric
    // m.WithUnit("By"),  // add a unit to the metric, if needed
    m.WithDescription("observable gauge description"),
)

_, err = meter.RegisterCallback(
    func(con context.Context, o m.Observer) error {
        o.ObserveInt64(observableGauge, 10, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
        return nil
    },
observableGauge,
)
```

#### UpDownCounter

```go
intUpDownCounter, err := meter.Int64UpDownCounter(
    "int_up_down_counter",  // name of the metric
    // m.WithUnit("ms"),  // add a unit to the metric, if needed
    m.WithDescription("Up-down counter description"),
)

floatUpDownCounter, err := meter.Float64UpDownCounter(
    "float_up_down_counter",  // name of the metric
    m.WithDescription("Up-down counter description"),
)

intUpDownCounter.Add(con, 5)
floatUpDownCounter.Add(con, 5.6, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
```

#### Asynchronous UpDownCounter

```go
// Create callbacks for your observable up-down counter instruments
// Float64ObservableUpDownCounter is also a supported type
observableCounter, err := meter.Int64ObservableUpDownCounter(
    "observable_up_down_counter",  // name of the metric
    // m.WithUnit("By"),  // add a unit to the metric, if needed
    m.WithDescription("observable up down counter description"),
)

_, err = meter.RegisterCallback(
    func(con context.Context, o m.Observer) error {
        o.ObserveInt64(observableCounter, 10, m.WithAttributes(attribute.Key("<<LABEL_KEY>>").String("<<LABEL_VALUE>>")))
        return nil
    },
    observableCounter,
)
```

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2cm0FZu4VK4vzH0We6SrJb"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


## Traces

<Tabs>
<TabItem value="opentelemetry" label="OpenTelemetry" default>

### Auto Instrumentation

Deploy this integration to enable instrumentation of your Go application using OpenTelemetry. 


**Before you begin, you'll need**:
* A Go application without instrumentation
* An active Logz.io account
* Port `4318` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

#### Install dependencies

```shell
go get -u go.opentelemetry.io/otel
go get -u go.opentelemetry.io/otel/propagation
go get -u go.opentelemetry.io/otel/sdk/resource
go get -u go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
go get -u go.opentelemetry.io/otel/sdk/trace
go get -u go.opentelemetry.io/otel/semconv/v1.26.0
```

#### Setup Tracer Provider
Create a new file `otel.go` and place the below code in it:

:::note
Change `<<SERVICE-NAME>>` to your own service name.
:::


```go
import (
	"context"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/resource"
	"log"

	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.26.0"
)

func newTraceProvider() (*sdktrace.TracerProvider, error) {
	// Ensure default SDK resources and the required service name are set.
	r, err := resource.Merge(
		resource.Default(),
		resource.NewWithAttributes(
			semconv.SchemaURL,
			semconv.ServiceName("<<SERVICE-NAME>>"),
		),
	)
	if err != nil {
		return nil, err
	}

	exp, _ := otlptracehttp.New(context.Background(),
		otlptracehttp.WithEndpoint("localhost:4318"),
		otlptracehttp.WithInsecure())

	return sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(exp),
		sdktrace.WithResource(r),
	), nil
}

// setupOTelSDK bootstraps the OpenTelemetry logging pipeline.
func setupOTelSDK(ctx context.Context) (shutdown func(context.Context) error, err error) {
	// setup trace provider
	traceProvider, err := newTraceProvider()
	if err != nil {
		return nil, err
	}

	otel.SetTracerProvider(traceProvider)
	otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
		propagation.TraceContext{}, propagation.Baggage{}))

	// Return a shutdown function
	shutdown = func(ctx context.Context) error {
		err := traceProvider.Shutdown(ctx)
		if err != nil {
			log.Printf("Error during tracer provider shutdown: %v", err)
		}
		return err
	}

	return shutdown, nil
}
```

#### Call Tracer Provider from main function
Make sure the application will setup the instrumentation by calling `setupOTelSDK()` that was created in the previous step from your main function.

```go
// Set up OpenTelemetry.
otelShutdown, err := setupOTelSDK(ctx)
if err != nil {
	return
}
// Handle shutdown properly so nothing leaks.
defer func() {
	err = errors.Join(err, otelShutdown(context.Background()))
}()
```

#### Setup OpenTelemetry Collector

Create a dedicated directory on the host of your Go application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.116.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Start OpenTelemetry Collector
Run the following command from the directory of your application file:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.


##### Check Logz.io for your traces

Run the application after building it with the new Instrumentation.
Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


### Manual Instrumentation

If you're using specific libararies and want to be specific or precise with instrumentation, you can opt to [instrument your code manually](https://opentelemetry.io/docs/languages/go/instrumentation/#traces).


</TabItem>
<TabItem value="lambda-otel" label="Lambda via OpenTelemetry">

 Deploy this integration to instrument your Go application running on AWS Lambda and send the traces to your Logz.io account. This is done by adding a dedicated layer for OpenTelemetry collector and configuring environment variables of these layer.

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
- A Lambda function with Go application.

:::note
Using `aws lambda update-function-configuration` with `--layers` replaces all existing layers with the specified ARN(s). To add a new layer without removing existing ones, include all desired layer ARNs in the command, both new and previously attached.
:::

:::note
Adding environmental variables using the AWS CLI commands below, will overwrite all existing variables for your Lambda function.
:::

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::

#### Add the OpenTelemetry collector layer to your Lambda function

This layer contains the OpenTelemetry collector that will capture data from your application.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers <<LAYER-ARN>>
```


Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Go application.

Copy the appropriate `<<LAYER-ARN>>` for your Lambda architecture (amd64 or arm64) from the [latest release notes](https://github.com/logzio/opentelemetry-lambda/releases).

Replace `<<REGION>>` with the code of your AWS regions. [See all available Logz.io hosting regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).


#### Create a configuration file for the OpenTelemetry collector

By default, the OpenTelemetry collector layer exports data to the Lambda console. To customize the collector configuration, you need to add a `collector.yaml` to your function and specifiy its location via the `OPENTELEMETRY_COLLECTOR_CONFIG_URI` environment variable.

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

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_URI=<<PATH_TO_YOUR_COLLECTOR.YAML>>}
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Go application.

Replace `<<PATH_TO_YOUR_COLLECTOR.YAML>>` with the actual path to your `collector.yaml` file.
(If `collector.yaml` is located in the root directory of your application, use the path `/var/task/collector.yaml`.)

#### Activate tracing for your Lambda function

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --tracing-config Mode=Active
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Go application.

## Example: Manual Instrumentation for Go Lambda Functions

Below is a simple example that demonstrates how to instrument a Go-based AWS Lambda function using OpenTelemetry:

```go
package main

import (
	"context"
	"github.com/aws/aws-lambda-go/lambda"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	"log"
)

// handler is your Lambda function handler
func handler(ctx context.Context, event any) (string, error) {
	log.Println("Starting function")
	// Configure the OTLP exporter to send traces to an OpenTelemetry Collector
	exporter, err := otlptrace.New(ctx, otlptracegrpc.NewClient(
		otlptracegrpc.WithEndpoint("localhost:4317"), // Replace with your collector endpoint
		otlptracegrpc.WithInsecure(),
	))
	if err != nil {
		log.Fatalf("Failed to create OTLP trace exporter: %v", err)
	}

	// Set up a trace provider with a batch span processor and the OTLP exporter
	tp := sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(exporter),
	)
	otel.SetTracerProvider(tp)
	// Create a tracer
	tracer := tp.Tracer("example-tracer")

	// Start a span
	_, span := tracer.Start(ctx, "lambda-example-span")
	// Your Lambda logic here
	log.Println("Handling event", span)
	span.End()
	tp.ForceFlush(ctx)
	return "Event handled successfully", nil
}

func main() {
	lambda.Start(handler)
}
```

This example manually sets up OpenTelemetry tracing within a Go Lambda function, configuring the OTLP exporter to send traces to an OpenTelemetry Collector. Remember to replace `localhost:4317` with the actual endpoint of your collector.

For additional information and best practices on instrumenting your Go applications with OpenTelemetry, refer to the [OpenTelemetry Go documentation](https://opentelemetry.io/docs/languages/go/instrumentation/#traces)

</TabItem>
</Tabs>