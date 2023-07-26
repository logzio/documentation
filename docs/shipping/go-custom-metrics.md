---
id: GO
title: GO
overview: Deploy this integration to send custom metrics to Logz.io from your GO application. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/go.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


Deploy this integration to send custom metrics to Logz.io from your GO application. 

This integration uses an exporter that sends cumulative metrics data from the OpenTelemetry Go SDK to Logz.io using the Prometheus Remote Write API. The exporter integrates with the OpenTelemetry Go SDK Controller. The Controller periodically collects data and passes it on to the exporter. The exporter then converts the data into `TimeSeries` and sends it to Logz.io through HTTP POST requests. The request body is formatted according to the protocol defined by the Prometheus Remote Write API.

#### Quick start

**Before you begin, you'll need**:
Go 1.x or higher

 

##### Install the SDK

Run the following command:

`go get github.com/logzio/go-metrics-sdk`

##### Configure the exporter

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
|`<<LISTENER-HOST>>`|  The full Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic (example: https://listener.logz.io:8053). For more details, see the [regions page](https://docs.logz.io/user-guide/accounts/account-region.html) in logz.io docs | Required | https://listener.logz.io:8053 |
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| The Logz.io Prometheus Metrics account token. Find it under **Settings > Manage accounts**. [Look up your Metrics account token.](https://docs.logz.io/user-guide/accounts/finding-your-metrics-account-token/)  | Required | - |
| RemoteTimeout | The timeout for requests to the remote write Logz.io metrics listener endpoint. | Required | 30 (seconds) |
| PushInterval | The time interval for sending the metrics to Logz.io. | Required | 10 (seconds) |
| Quantiles | The quantiles of the histograms. | Optional | [0.5, 0.9, 0.95, 0.99] |
| HistogramBoundaries | The histogram boundaries. | Optional | - |

##### Add the exporter setup

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
	

##### Set up the Metric Instruments Creator
	
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



##### Add metric instruments

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

###### Counter

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

###### Asynchronous Counter

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

###### Histogram

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

###### Asynchronous Gauge

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

###### UpDownCounter

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

###### Asynchronous UpDownCounter

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

##### Check Logz.io for your metrics
Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

 
