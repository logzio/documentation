---
id: Dotnet-custom
title: .NET custom
overview: You can send custom metrics from your .NET Core application using Logzio.App.Metrics. Logzio.App.Metrics is an open-source and cross-platform .NET library used to record metrics within an application and forward the data to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/dotnet.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

 

You can send custom metrics from your .NET Core application using Logzio.App.Metrics. Logzio.App.Metrics is an open-source and cross-platform .NET library used to record metrics within an application and forward the data to Logz.io.

These instructions show you how to:

* Create a basic custom metrics export configuration with a hardcoded Logz.io exporter
* Create a basic custom metrics export configuration with a Logz.io exporter defined by a configuration file
* Add advanced settings to the basic custom metrics export configuration
  

  


#### Send custom metrics to Logz.io with a hardcoded Logz.io exporter

**Before you begin, you'll need**: 

* An application in .NET Core 3.1 or higher
* An active Logz.io account 


 


##### Install the App.Metrics.Logzio package


Install the App.Metrics.Logzio package from the Package Manager Console:

```shell
Install-Package Logzio.App.Metrics
```

If you prefer to install the library manually, download the latest version from the NuGet Gallery.


##### Create MetricsBuilder

To create MetricsBuilder, copy and paste the following code into the function of the code that you need to export metrics from:

```csharp
var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp("<<LISTENER-HOST>>:<<PORT>>", "<<METRICS-SHIPPING-TOKEN>>")
                .Build();
```

{@include: ../_include/log-shipping/listener-var.html} For HTTPS communication, use port 8053. For HTTP communication, use port 8052.

{@include: ../_include/metric-shipping/replace-metrics-token.html}


##### Create Scheduler

To create the Scheduler, copy and paste the following code into the same function of the code as the MetricsBuilder:

```csharp
var scheduler = new AppMetricsTaskScheduler(
                TimeSpan.FromSeconds(15),
                async () => { await Task.WhenAll(metrics.ReportRunner.RunAllAsync()); });
scheduler.Start();
```

##### Add required metrics to your code

You can send the following metrics from your code:

* [Apdex (Application Performance Index)](https://www.app-metrics.io/getting-started/metric-types/apdex/)
* [Counter](https://www.app-metrics.io/getting-started/metric-types/counters/)
* [Gauge](https://www.app-metrics.io/getting-started/metric-types/gauges/)
* [Histogram](https://www.app-metrics.io/getting-started/metric-types/histograms/)
* [Meter](https://www.app-metrics.io/getting-started/metric-types/meters/)
* [Timer](https://www.app-metrics.io/getting-started/metric-types/timers/)

You must have at least one of the above metrics in your code to use the Logzio.App.Metrics. 
For example, to add a counter metric to your code, copy and paste the following code block into the same function of the code as the MetricsBuilder and Scheduler. 

```csharp
var counter = new CounterOptions {Name = "my_counter", Tags = new MetricTags("test", "my_test")};
metrics.Measure.Counter.Increment(counter);
```

In the example above, the metric has a name ("my_counter"), a tag key ("test") and a tag value ("my_test"): These parameters are used to query data from this metric in your Logz.io dashboard.


###### Apdex

Apdex (Application Performance Index) allows you to monitor end-user satisfaction. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/apdex/).

###### Counter

Counters are one of the most basic supported metrics types: They enable you to track how many times something has happened. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/counters/).

###### Gauge

A Gauge is an action that returns an instantaneous measurement for a value that abitrarily increases and decreases (for example, CPU usage). For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/gauges/).

###### Histogram

Histograms measure the statistical distribution of a set of values. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/histograms/).

###### Meter

A Meter measures the rate at which an event occurs, along with the total count of the occurences. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/meters/).

###### Timer

A Timer is a combination of a histogram and a meter, which enables you to measure the duration of a type of event, the rate of its occurrence, and provide duration statistics. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/timers/).


##### Run your application

Run your application to start sending metrics to Logz.io.


##### Check Logz.io for your events

Give your events some time to get from your system to ours, and then open the [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).

##### Filter the metrics by labels

Once the metrics are in Logz.io, you can query the required metrics using labels. Each metric has the following labels:

| App Metrics parameter name | Description | Logz.io parameter name |
|---|---|---|
| Name | The name of the metric. Required for each metric. | Metric name if not stated otherwise |
| MeasurementUnit | The unit you use to measure. By default it is `None`. | `unit` |
| Context | The context which the metric belong to. By default it is `Application`.	 | `context` |
| Tags | Pairs of key and value of the metric. It is not required to have tags for a metric.| Tags keys |

Some of the metrics have custom labels, as described below.

###### Meter

| App Metrics label name | Logz.io label name |
|---|---|
| RateUnit | rate_unit |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_meter_name]]_count |
| One Min Rate | [[your_meter_name]]_one_min_rate |
| Five Min Rate | [[your_meter_name]]_five_min_rate |
| Fifteen Min Rate | [[your_meter_name]]_fifteen_min_rate |
| Mean Rate | [[your_meter_name]]_mean_rate |
  
Replace [[your_meter_name]] with the name that you assigned to the meter metric.

###### Histogram

| App Metrics label name | Logz.io label name |
|---|---|
| Last User Value | last_user_value |
| Max User Value | max_user_value |
| Min User Value | min_user_value |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_histogram_name]]_count |
| Sum | [[your_histogram_name]]_sum |
| Last Value | [[your_histogram_name]]_lastValue |
| Max | [[your_histogram_name]]_max |
| Mean | [[your_histogram_name]]_mean |
| Median | [[your_histogram_name]]_median |
| Min | [[your_histogram_name]]_min |
| Percentile 75	| [[your_histogram_name]]_percentile75 |
| Percentile 95 | [[your_histogram_name]]_percentile95 |
| Percentile 98 | [[your_histogram_name]]_percentile98 |
| Percentile 99 | [[your_histogram_name]]_percentile99 |
| Percentile 999 | [[your_histogram_name]]_percentile999 |
| Sample Size | [[your_histogram_name]]_sample_size |
| Std Dev | [[your_histogram_name]]_std_dev |
  
Replace [[your_histogram_name]] with the name that you assigned to the histogram metric.

###### Timer

| App Metrics label name | Logz.io label name |
|---|---|
| Duration Unit	 | duration_unit |
| Rate Unit | rate_unit |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_timer_name]]_count |
| Histogram Active Session | [[your_timer_name]]_histogram_active_session |
| Histogram Sum | [[your_timer_name]]_histogram_sum |
| Histogram Last Value | [[your_timer_name]]_histogram_lastValue |
| Histogram Max	| [[your_timer_name]]_histogram_max |
| Histogram Median | [[your_timer_name]]_histogram_median |
| Histogram Percentile 75 | [[your_timer_name]]_histogram_percentile75 |
| Histogram Percentile 95 | [[your_timer_name]]_histogram_percentile95 |
| Histogram Percentile 98 | [[your_timer_name]]_histogram_percentile98 |
| Histogram Percentile 99 | [[your_timer_name]]_histogram_percentile99 |
| Histogram Percentile 999 | [[your_timer_name]]_histogram_percentile999 |
| Histogram Sample Size | [[your_timer_name]]_histogram_sample_size |
| Histogram Std Dev | [[your_timer_name]]_histogram_std_dev |
| Rate One Min Rate | [[your_timer_name]]_rate_one_min_rate |
| Rate Five Min Rate | [[your_timer_name]]_rate_five_min_rate |
| Rate Fifteen Min Rate | [[your_timer_name]]_rate_fifteen_min_rate |
| Rate Mean Rate | [[your_timer_name]]_rate_mean_rate |

Replace [[your_timer_name]] with the name that you assigned to the timer metric.
  
###### Apdex

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Sample Size | [[your_apdex_name]]_sample_size |
| Score | [[your_apdex_name]]_score |
| Frustrating | [[your_apdex_name]]_frustrating |
| Satisfied | [[your_apdex_name]]_satisfied |
| Tolerating | [[your_apdex_name]]_tolerating |

Replace [[your_apdex_name]] with the name that you assigned to the timer metric.

 

For troubleshooting this solution, see our [.NET core troubleshooting guide](/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting.html).

 

#### Send custom metrics to Logz.io with a Logz.io exporter defined by a config file

**Before you begin, you'll need**: 

* An application in .NET Core 3.1 or higher
* An active Logz.io account


 


##### Install the App.Metrics.Logzio package


Install the App.Metrics.Logzio package from the Package Manager Console:

```csharp
Install-Package Logzio.App.Metrics
```

If you prefer to install the library manually, download the latest version from NuGet Gallery.


##### Create MetricsBuilder

To create MetricsBuilder, copy and paste the following code into the function of the code that you need to export metrics from:

```csharp
var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp("<<path_to_the_config_file>>")
                .Build();
```

Add the following code to the configuration file:

```xml
<?xml version="1.0" encoding="utf-8"?>

<Configuration>
    <LogzioConnection>
        <Endpoint> <<LISTENER-HOST>> </Endpoint>
        <Token> <<METRICS-SHIPPING-TOKEN>> </Token>
    </LogzioConnection>
</Configuration>
```

{@include: ../_include/log-shipping/listener-var.html} For HTTPS communication, use port 8053. For HTTP communication, use port 8052.

{@include: ../_include/metric-shipping/replace-metrics-token.html}


##### Create Scheduler

To create a Scheduler, copy and paste the following code into the same function of the code as the MetricsBuilder:

```csharp
var scheduler = new AppMetricsTaskScheduler(
                TimeSpan.FromSeconds(15),
                async () => { await Task.WhenAll(metrics.ReportRunner.RunAllAsync()); });
scheduler.Start();
```

##### Add the required metrics to your code

You can send the following metrics from your code:

* [Apdex (Application Performance Index)](https://www.app-metrics.io/getting-started/metric-types/apdex/)
* [Counter](https://www.app-metrics.io/getting-started/metric-types/counters/)
* [Gauge](https://www.app-metrics.io/getting-started/metric-types/gauges/)
* [Histogram](https://www.app-metrics.io/getting-started/metric-types/histograms/)
* [Meter](https://www.app-metrics.io/getting-started/metric-types/meters/)
* [Timer](https://www.app-metrics.io/getting-started/metric-types/timers/)

You must have at least one of the above metrics in your code to use the Logzio.App.Metrics. For example, to add a counter metric to your code, copy and paste the following code block into the same function of the code as the MetricsBuilder and Scheduler:

```csharp
var counter = new CounterOptions {Name = "my_counter", Tags = new MetricTags("test", "my_test")};
metrics.Measure.Counter.Increment(counter);
```

In the example above, the metric has a name ("my_counter"), a tag key ("test") and a tag value ("my_test"). These parameters are used to query data from this metric in your Logz.io dashboard.


###### Apdex

Apdex (Application Performance Index) allows you to monitor end-user satisfaction. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/apdex/).

###### Counter

Counters are one of the most basic supported metrics types: They enable you to track how many times something has happened. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/counters/).

###### Gauge

A Gauge is an action that returns an instantaneous measurement for a value that abitrarily increases and decreases (for example, CPU usage). For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/gauges/).

###### Histogram

Histograms measure the statistical distribution of a set of values. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/histograms/).

###### Meter

A Meter measures the rate at which an event occurs, along with the total count of the occurences. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/meters/).

###### Timer

A Timer is a combination of a histogram and a meter, which enables you to measure the duration of a type of event, the rate of its occurrence, and provide duration statistics. For more information on this metric, refer to [App Metrics documentation](https://www.app-metrics.io/getting-started/metric-types/timers/).
 


##### Run your application

Run your application to start sending metrics to Logz.io.


##### Check Logz.io for your events

Give your events some time to get from your system to ours, and then open [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).

##### Filter the metrics by labels

Once the metrics are in Logz.io, you can query the required metrics using labels. Each metric has the following labels:

| App Metrics parameter name | Description | Logz.io parameter name |
|---|---|---|
| Name | The name of the metric. Required for each metric. | Metric name if not stated otherwise |
| MeasurementUnit | The unit you use to measure. By default it is `None`. | `unit` |
| Context | The context which the metric belong to. By default it is `Application`.	 | `context` |
| Tags | Pairs of key and value of the metric. It is not required to have tags for a metric.| Tags keys |

Some of the metrics have custom labels as described below.

###### Meter

| App Metrics label name | Logz.io label name |
|---|---|
| RateUnit | rate_unit |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_meter_name]]_count |
| One Min Rate | [[your_meter_name]]_one_min_rate |
| Five Min Rate | [[your_meter_name]]_five_min_rate |
| Fifteen Min Rate | [[your_meter_name]]_fifteen_min_rate |
| Mean Rate | [[your_meter_name]]_mean_rate |

Replace [[your_meter_name]] with the name that you assigned to the meter metric.
  
###### Histogram

| App Metrics label name | Logz.io label name |
|---|---|
| Last User Value | last_user_value |
| Max User Value | max_user_value |
| Min User Value | min_user_value |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_histogram_name]]_count |
| Sum | [[your_histogram_name]]_sum |
| Last Value | [[your_histogram_name]]_lastValue |
| Max | [[your_histogram_name]]_max |
| Mean | [[your_histogram_name]]_mean |
| Median | [[your_histogram_name]]_median |
| Min | [[your_histogram_name]]_min |
| Percentile 75	| [[your_histogram_name]]_percentile75 |
| Percentile 95 | [[your_histogram_name]]_percentile95 |
| Percentile 98 | [[your_histogram_name]]_percentile98 |
| Percentile 99 | [[your_histogram_name]]_percentile99 |
| Percentile 999 | [[your_histogram_name]]_percentile999 |
| Sample Size | [[your_histogram_name]]_sample_size |
| Std Dev | [[your_histogram_name]]_std_dev |

Replace [[your_histogram_name]] with the name that you assigned to the histogram metric.

###### Timer

| App Metrics label name | Logz.io label name |
|---|---|
| Duration Unit	 | duration_unit |
| Rate Unit | rate_unit |

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Count | [[your_timer_name]]_count |
| Histogram Active Session | [[your_timer_name]]_histogram_active_session |
| Histogram Sum | [[your_timer_name]]_histogram_sum |
| Histogram Last Value | [[your_timer_name]]_histogram_lastValue |
| Histogram Max	| [[your_timer_name]]_histogram_max |
| Histogram Median | [[your_timer_name]]_histogram_median |
| Histogram Percentile 75 | [[your_timer_name]]_histogram_percentile75 |
| Histogram Percentile 95 | [[your_timer_name]]_histogram_percentile95 |
| Histogram Percentile 98 | [[your_timer_name]]_histogram_percentile98 |
| Histogram Percentile 99 | [[your_timer_name]]_histogram_percentile99 |
| Histogram Percentile 999 | [[your_timer_name]]_histogram_percentile999 |
| Histogram Sample Size | [[your_timer_name]]_histogram_sample_size |
| Histogram Std Dev | [[your_timer_name]]_histogram_std_dev |
| Rate One Min Rate | [[your_timer_name]]_rate_one_min_rate |
| Rate Five Min Rate | [[your_timer_name]]_rate_five_min_rate |
| Rate Fifteen Min Rate | [[your_timer_name]]_rate_fifteen_min_rate |
| Rate Mean Rate | [[your_timer_name]]_rate_mean_rate |
  
Replace [[your_timer_name]] with the name that you assigned to the timer metric.

###### Apdex

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Sample Size | [[your_apdex_name]]_sample_size |
| Score | [[your_apdex_name]]_score |
| Frustrating | [[your_apdex_name]]_frustrating |
| Satisfied | [[your_apdex_name]]_satisfied |
| Tolerating | [[your_apdex_name]]_tolerating |

Replace [[your_apdex_name]] with the name that you assigned to the apdex metric.

 

For troubleshooting this solution, see our [.NET core troubleshooting guide](/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting.html).

  

#### Export using ToLogzioHttp exporter

You can configure MetricsBuilder to use ToLogzioHttp exporter, which allows you to export metrics via HTTP using additional export settings. To enable this exporter, add the following code block to define the MetricsBuilder:

```csharp
var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp(options =>
                {
                    options.Logzio.EndpointUri = new Uri("<<LISTENER-HOST>>:<<PORT>>");
                    options.Logzio.Token = "<<METRICS-SHIPPING-TOKEN>>";
                    options.FlushInterval = TimeSpan.FromSeconds(15);
                    options.Filter = new MetricsFilter().WhereType(MetricType.Counter);
                    options.HttpPolicy.BackoffPeriod = TimeSpan.FromSeconds(30);
                    options.HttpPolicy.FailuresBeforeBackoff = 5;
                    options.HttpPolicy.Timeout = TimeSpan.FromSeconds(10);
                })
                .Build();
```

* {@include: ../_include/log-shipping/listener-var.html} For HTTPS communication use port 8053. For HTTP communication use port 8052.
* {@include: ../_include/metric-shipping/replace-metrics-token.html}
* `FlushInterval` is the value in seconds defining delay between reporting metrics.
* `Filter`is used to filter metrics for this reporter.
* `HttpPolicy.BackoffPeriod	` is the value in seconds defining the `TimeSpan` to back-off when metrics are failing to report to the metrics ingress endpoint.
* `HttpPolicy.FailuresBeforeBackoff	` is the value defining the number of failures before backing-off when metrics are failing to report to the metrics ingress endpoint.
* `HttpPolicy.Timeout	` is the value in seconds defining the HTTP timeout duration when attempting to report metrics to the metrics ingress endpoint.

#### .NET Core runtime metrics

The runtime metrics are additional parameters that will be sent from your code. These parameters include:

* Garbage collection frequencies and timings by generation/type, pause timings and GC CPU consumption ratio.
* Heap size by generation.
* Bytes allocated by small/large object heap.
* JIT compilations and JIT CPU consumption ratio.
* Thread pool size, scheduling delays and reasons for growing/shrinking.
* Lock contention.

To enable collection of these metrics with default settings, add the following code block after the MetricsBuilder:

```csharp
// metrics is the MetricsBuilder
IDisposable collector = DotNetRuntimeStatsBuilder.Default(metrics).StartCollecting();
```

To enable collection of these metrics with custom settings, add the following code block after the MetricsBuilder:

```csharp
IDisposable collector = DotNetRuntimeStatsBuilder
    .Customize()
    .WithContentionStats()
    .WithJitStats()
    .WithThreadPoolSchedulingStats()
    .WithThreadPoolStats()
    .WithGcStats()
    .StartCollecting(metrics);          // metrics is the MetricsBuilder
```

Data collected from these metrics is found in Logz.io, under the Contexts labels `process` and `dotnet`.

#### Get current snapshot

The current snapshot creates a preview of the metrics in Logz.io format. To enable this option, add the following code block to the MetricsBuilder:

```csharp
var metrics = new MetricsBuilder()
                .OutputMetrics.AsLogzioCompressedProtobuf()
                .Build();

var snapshot = metrics.Snapshot.Get();
            
using (var stream = new MemoryStream())
{
    await metrics.DefaultOutputMetricsFormatter.WriteAsync(stream, snapshot);

    // Your code here...
}
```

For troubleshooting this solution, see our [.NET core troubleshooting guide](/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting.html).
  