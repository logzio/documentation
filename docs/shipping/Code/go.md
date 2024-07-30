---
id: GO
title: GO
overview: Send logs, metrics and traces from you Go code
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['Code']
recommendedFor: ['Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/go.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2cm0FZu4VK4vzH0We6SrJb']
metrics_alerts: ['1UqjU2gqNAKht1f62jBC9Q']
drop_filter: []
---

:::tip
If your code is running inside Kubernetes the best practice will be to use our [kubernetes integrations](https://docs.logz.io/shipping/Containers/Kubernetes).
:::

## Logs

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

## Metrics

:::note
[Project's GitHub repo](https://github.com/logzio/go-metrics-sdk/)
:::

### Install the SDK

Run the following command:

```shell
go get github.com/logzio/go-metrics-sdk
```

### Configure the exporter

Add the exporter definition to your application code:

```go
import (
    metricsExporter "github.com/logzio/go-metrics-sdk"
    controller "go.opentelemetry.io/otel/sdk/metric/controller/basic"
    semconv "go.opentelemetry.io/otel/semconv/v1.7.0"
    // ...
)

config := metricsExporter.Config {
	LogzioMetricsListener: "<<LISTENER-HOST>>",
	LogzioMetricsToken:    "<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>",
	RemoteTimeout:         30 * time.Second,
	PushInterval:          5 * time.Second,
}
```


Replace the placeholders in the code to match your specifics.

| Parameter | Description | Required | Default|
|---|---|---|---|
|`<<LISTENER-HOST>>`|  The full Logz.io Listener URL for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic (example: https://listener.logz.io:8053). For more details, see the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) in logz.io docs | Required | https://listener.logz.io:8053 |
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| The Logz.io Prometheus Metrics account token. Find it under **Settings > Manage accounts**. [Look up your Metrics account token.](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/)  | Required | - |
| RemoteTimeout | The timeout for requests to the remote write Logz.io metrics listener endpoint. | Required | 30 (seconds) |
| PushInterval | The time interval for sending the metrics to Logz.io. | Required | 10 (seconds) |
| Quantiles | The quantiles of the histograms. | Optional | [0.5, 0.9, 0.95, 0.99] |
| HistogramBoundaries | The histogram boundaries. | Optional | - |

### Add the exporter setup

Add the exporter setup definition to your application code:

```go
// Use the `config` instance from last step.

cont, err := metricsExporter.InstallNewPipeline(
    config,
    controller.WithCollectPeriod(<<COLLECT_PERIOD>>*time.Second),
    controller.WithResource(
        resource.NewWithAttributes(
            semconv.SchemaURL,
            attribute.<<TYPE>>("<<LABEL_KEY>>", "<<LABEL_VALUE>>"),
        ),
    ),
)
if err != nil {
    return err
}
```

Replace the placeholders in the code to match your specifics.

| Parameter | Description | 
|---|---|
| `<<COLLECT_PERIOD>>` | The collect period time in seconds. |
| `<<TYPE>>` | The available label value types according to the `<<LABEL_VALUE>>`. |
| `<<LABEL_KEY>>` | The label key. |
| `<<LABEL_VALUE>>` | The label value. | 
	

### Set up the Metric Instruments Creator
	
Create `Meter` to create metric instruments:
	
```go
// Use `cont` instance from last step.

ctx := context.Background()
defer func() {
    handleErr(cont.Stop(ctx))
}()

meter := cont.Meter("<<INSTRUMENTATION_NAME>>")

func handleErr(err error) {
    if err != nil {
        panic(fmt.Errorf("encountered error: %v", err))
    }
}	
```	
	
Replace `<<INSTRUMENTATION_NAME>>` with your instrumentation name.
	
Additionally, add the error handler:
	
```go
func handleErr(err error) {
    if err != nil {
        panic(fmt.Errorf("encountered error: %v", err))
    }
}
```



### Add metric instruments

Add a required metric intrument to your code. Below are the available metric instruments and their code definition.


The exporter uses the `simple` selector's `NewWithHistogramDistribution()`. This means that the instruments are mapped to aggregations as shown in the table below.

| Instrument | Behavior | Aggregation |
| --- | --- | --- |
| Counter | A synchronous Instrument which supports non-negative increments. | Sum |
| Asynchronous Counter | An asynchronous Instrument which reports monotonically increasing value(s) when the instrument is being observed. | Sum |
| Histogram | A synchronous Instrument which can be used to report arbitrary values that are likely to be statistically meaningful. It is intended for statistics such as histograms, summaries, and percentile. | Histogram |
| Asynchronous Gauge | An asynchronous Instrument which reports non-additive value(s) when the instrument is being observed. | LastValue |
| UpDownCounter | A synchronous Instrument which supports increments and decrements. | Sum |
| Asynchronous UpDownCounter | An asynchronous Instrument which reports additive value(s) when the instrument is being observed. | Sum |

#### Counter

```go
// Use `ctx` and `meter` from last steps.

// Create counter instruments
intCounter := metric.Must(meter).NewInt64Counter(
    "go_metrics.int_counter",
    metric.WithDescription("int_counter description"),
)
floatCounter := metric.Must(meter).NewFloat64Counter(
    "go_metrics.float_counter",
    metric.WithDescription("float_counter description"),
)

// Record values to the metric instruments and add labels
intCounter.Add(ctx, int64(10), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
floatCounter.Add(ctx, float64(2.5), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
```

#### Asynchronous Counter

```go
// Use `meter` from last steps.

// Create callbacks for your CounterObserver instruments
intCounterObserverCallback := func(_ context.Context, result metric.Int64ObserverResult) {
    result.Observe(10, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
}
floatCounterObserverCallback := func(_ context.Context, result metric.Float64ObserverResult) {
    result.Observe(2.5, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
}

// Create CounterObserver instruments
_ = metric.Must(meter).NewInt64CounterObserver(
    "go_metrics.int_counter_observer",
    intCounterObserverCallback,
    metric.WithDescription("int_counter_observer description"),
)
_ = metric.Must(meter).NewFloat64CounterObserver(
    "go_metrics.float_counter_observer",
    floatCounterObserverCallback,
    metric.WithDescription("float_counter_observer description"),
)
```

#### Histogram

```go
// Use `ctx` and `meter` from last steps.

// Create Histogram instruments
intHistogram := metric.Must(meter).NewInt64Histogram(
    "go_metrics.int_histogram",
    metric.WithDescription("int_histogram description"),
)
floatHistogram := metric.Must(meter).NewFloat64Histogram(
    "go_metrics.float_histogram",
    metric.WithDescription("float_histogram description"),
)

// Record values to the metric instruments and add labels
intHistogram.Record(ctx, int(10), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
floatHistogram.Record(ctx, float64(2.5), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
```

#### Asynchronous Gauge

```go
// Use `meter` from last steps.

// Create callbacks for your GaugeObserver instruments
intGaugeObserverCallback := func(_ context.Context, result metric.Int64ObserverResult) {
    result.Observe(10, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
}
floatGaugeObserverCallback := func(_ context.Context, result metric.Float64ObserverResult) {
result.Observe(2.5, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>>"))
}

// Create GaugeObserver instruments
_ = metric.Must(meter).NewInt64GaugeObserver(
    "go_metrics.int_gauge_observer", 
    intGaugeObserverCallback,
    metric.WithDescription("int_gauge_observer description"),
)
_ = metric.Must(meter).NewFloat64GaugeObserver(
    "go_metrics.float_gauge_observer",
    floatGaugeObserverCallback,
    metric.WithDescription("float_gauge_observer description"),
)
```

#### UpDownCounter

```go
// Use `ctx` and `meter` from last steps.

// Create UpDownCounter instruments
intUpDownCounter := metric.Must(meter).NewInt64UpDownCounter(
    "go_metrics.int_up_down_counter",
    metric.WithDescription("int_up_down_counter description"),
)
floatUpDownCounter := metric.Must(meter).NewFloat64UpDownCounter(
    "go_metrics.float_up_down_counter",
    metric.WithDescription("float_up_down_counter description"),
)

// Record values to the metric instruments and add labels
intUpDownCounter.Add(ctx, int64(-10), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
floatUpDownCounter.Add(ctx, float64(2.5), attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
```

#### Asynchronous UpDownCounter

```go
// Use `meter` from last steps.

// Create callback for your UpDownCounterObserver instruments
intUpDownCounterObserverCallback := func(_ context.Context, result metric.Int64ObserverResult) {
    result.Observe(-10, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
}
floatUpDownCounterObserverCallback := func(_ context.Context, result metric.Float64ObserverResult) {
    result.Observe(2.5, attribute.String("<<LABEL_KEY>>", "<<LABEL_VALUE>"))
}

// Create UpDownCounterObserver instruments
_ = metric.Must(meter).NewInt64UpDownCounterObserver(
    "go_metrics.int_up_down_counter_observer",
    intUpDownCounterObserverCallback,
    metric.WithDescription("int_up_down_counter_observer description"),
)
_ = metric.Must(meter).NewFloat64UpDownCounterObserver(
    "go_metrics.float_up_down_counter_observer",
    floatUpDownCounterObserverCallback,
    metric.WithDescription("float_up_down_counter_observer description"),
)
```

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2cm0FZu4VK4vzH0We6SrJb"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}



## Traces

Deploy this integration to enable instrumentation of your Go application using OpenTelemetry. 

### Manual configuration

This integration includes:

* Installing the OpenTelemetry Go instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your Go application in conjunction with the OpenTelemetry instrumentation

On deployment, the Go instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.




#### Setup instrumentation for your locally hosted Go application and send traces to Logz.io

**Before you begin, you'll need**:

* A Go application without instrumentation
* An active account with Logz.io
* Port `4318` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::




##### Download the general instrumentation packages

These packages are required to enable instrumentation for your code regardless of the type of application that you need to instrument. 

To download these packages, run the following command from the application directory:

```shell
go get -u go.opentelemetry.io/otel
go get -u go.opentelemetry.io/otel/exporters/otlp
go get -u go.opentelemetry.io/otel
go get -u go.opentelemetry.io/otel/attribute
go get -u go.opentelemetry.io/otel/baggage
go get -u go.opentelemetry.io/otel/propagation
go get -u go.opentelemetry.io/otel/sdk/resource
go get -u go.opentelemetry.io/otel/sdk/trace
go get -u go.opentelemetry.io/otel/semconv/v1.4.0
go get -u go.opentelemetry.io/otel/trace
go get -u go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```


:::note
We recommend sending OTLP traces using HTTP. This is why we import the `otlptracehttp` package.
:::


##### Download the application specific instrumentation packages

Depending on the type of your application, you need to download instrumentation packages specific to your application. For example, if your application is a HTTP server, you will need the `opentelemetry.io/contrib/instrumentation/net/http/otelhttp` package. The full list of all available packages can be found in the [OpenTelemetry contrib directory](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/v0.22.0/instrumentation).

The example below is given for a HTTP server application:

```shell
go get -u go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

##### Add the instrumentation to the `import` function

Add all the packages downloaded in the previous steps to the `import` function of your application.

The example below is given for a HTTP server application:

```go
import (
	"context"
	"io"
	"log"
	"net/http"

	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/baggage"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.4.0"
	"go.opentelemetry.io/otel/trace"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
)
```

##### Add the `initProvider` function


Add the `initProvider` function to the application code as follows:

```go
func initProvider() func() {
	ctx := context.Background()

	res, err := resource.New(ctx,
		resource.WithAttributes(
			semconv.ServiceNameKey.String("test-service"),
		),
	)
	handleErr(err, "failed to create resource")

	traceExporter, err := otlptracehttp.New(ctx,
		otlptracehttp.WithInsecure(),
		otlptracehttp.WithEndpoint("localhost:4318"),
	)
	handleErr(err, "failed to create trace exporter")

	bsp := sdktrace.NewBatchSpanProcessor(traceExporter)
	tracerProvider := sdktrace.NewTracerProvider(
		sdktrace.WithSampler(sdktrace.AlwaysSample()),
		sdktrace.WithResource(res),
		sdktrace.WithSpanProcessor(bsp),
	)
	otel.SetTracerProvider(tracerProvider)
	otel.SetTextMapPropagator(propagation.TraceContext{})
	return func() {
		handleErr(tracerProvider.Shutdown(ctx), "failed to shutdown TracerProvider")
	}
}
```

##### Instrument the code in the `main` function

In the `main` function of your application, add the following code:

```go
	shutdown := initProvider()
	defer shutdown()
```

After this, you need to declare the instrumentation according to your application. The example below is given for a HTTP server application. The HTTP handler instructs the tracer to create spans on each request.

```go
uk := attribute.Key("username")

	helloHandler := func(w http.ResponseWriter, req *http.Request) {
		ctx := req.Context()
		span := trace.SpanFromContext(ctx)
		bag := baggage.FromContext(ctx)
		span.AddEvent("handling this...", trace.WithAttributes(uk.String(bag.Member("username").Value())))

		_, _ = io.WriteString(w, "Hello, world!\n")
	}

	otelHandler := otelhttp.NewHandler(http.HandlerFunc(helloHandler), "Hello")

	http.Handle("/hello", otelHandler)
	err := http.ListenAndServe(":7777", nil)
	if err != nil {
		panic(err)
	}
}
func handleErr(err error, message string) {
	if err != nil {
		log.Fatalf("%s: %v", message, err)
	}
```


##### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Go application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.



After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


##### Start the collector

Run the following command from the directory of your application file:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

##### Run the application

Run the application to generate traces:

```shell
go run <YOUR-APPLICATION-FILE-NAME>.go
```


##### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


