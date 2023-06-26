Deploy this integration to send custom metrics from your Java application to Logz.io using [Micrometer](https://micrometer.io/). The dedicated Logz.io Micrometer metrics registry sends custom metrics from your Java application to your Logz.io account.

**Before you begin, you'll need**:
Java 8 or higher


#### Configuring your Java applicatin to send custom metrics to Logz.io

##### Add the Micrometer registry to your application

###### Via Maven

If you use Maven, add the dependency to your project configuration file (for instance, pom.xml in a Maven project) as follows:

```xml
<dependency>
    <groupId>io.logz.micrometer</groupId>
    <artifactId>micrometer-registry-logzio</artifactId>
    <version>1.0.2</version>
</dependency>
```

###### Via Gradle Groovy
  
If you use Gradle Groovy, add the dependency to your project as follows:

```java
implementation 'io.logz.micrometer:micrometer-registry-logzio:1.0.2'
```

###### Via Gradle Kotlin
  
If you use Gradle kotlin, add the dependency to your project as follows:

```java
implementation("io.logz.micrometer:micrometer-registry-logzio:1.0.2")
```

###### Import in your package
  
To add the dependency directly to your package:
  
```java
import io.micrometer.logzio.LogzioConfig;
import io.micrometer.logzio.LogzioMeterRegistry;
```

##### Initialize the Micrometer in your application code
   
Add the following code to your application:

```java
package your_package;
import io.micrometer.core.instrument.*;
import io.micrometer.core.instrument.Timer;
import io.micrometer.logzio.LogzioConfig;
import io.micrometer.logzio.LogzioMeterRegistry;

class MicrometerLogzio {

   public static void main(String[] args) {
       // initilize config
      LogzioConfig logzioConfig = new LogzioConfig() {
         @Override
         public String get(String key) {
            return null;
         }
         @Override
         public String uri() {
           return "<<LISTENER-HOST>>:<<PORT>>";
           // example:
           // return "https://listener.logz.io:8053"; 
         }
         
         @Override
         public String token() {
            return "<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>";
         }

         @Override
         public Duration step() {
           return Duration.ofSeconds(<<interval>>);
           // example:
           // return Duration.ofSeconds(30);                    
         }
         @Override
         public Hashtable<String, String> includeLabels() {
             return new Hashtable<>();
         }
         @Override
         public Hashtable<String, String> excludeLabels() {
             return new Hashtable<>();
      };
      // Initialize registry
       LogzioMeterRegistry registry = new LogzioMeterRegistry(logzioConfig, Clock.SYSTEM);
       // Define tags (labels)
       ArrayList<Tag> tags = new ArrayList<>();
       tags.add(Tag.of("env","dev-micrometer"));

      // Create counter
      Counter counter = Counter
              .builder("counter_example")
              .description("a description of what this counter does") // optional
              .tags(tags) // optional
              .register(registry);
      // Increment your counter
      counter.increment(); 
      counter.increment(2); 
   }
}
```

* {@include: ../general-shipping/eplace-placeholders-prometheus.html}

* Replace `<<PORT>>` with the applicable port for your traffic, which is 8052 for http or 8053 for https.

##### Add common tags to the registry

If required, you can attach common tags ("key" and "value") to your registry. These tags will be added to all metrics reported, for example:
  
```java
// Initialize registry
LogzioMeterRegistry registry = new LogzioMeterRegistry(logzioConfig, Clock.SYSTEM);
// Define tags (labels)
registry.config().commonTags("key", "value");
```

##### Filter labels

You can use the `includeLabels` or `excludeLabels` functions to filter your metrics by labels.

###### Include

Add the following to your `LogzioConfig()` constructor:

```java
@Override
public Hashtable<String, String> includeLabels() {
    Hashtable<String, String> includeLabels = new Hashtable<>();
    includeLabels.put("__name__", "my_counter_abc_total|my_second_counter_abc_total");
    includeLabels.put("k1", "v1");
    return includeLabels;
}
```

In this example, the registry will keep only metrics with the label `__name__` matching the regex `my_counter_abc_total|my_second_counter_abc_total`, and with the label `k1` matching the regex `v1`. Adjust the labels as required.


###### Exclude

Add the following to your `LogzioConfig()` constructor:

```java
@Override
public Hashtable<String, String> excludeLabels() {
    Hashtable<String, String> excludeLabels = new Hashtable<>();
    excludeLabels.put("__name__", "my_counter_abc_total|my_second_counter_abc_total");
    excludeLabels.put("k1", "v1");
    return excludeLabels;
}
```

The registry will drop all metrics with the label `__name__` matching the regex `my_counter_abc_total|my_second_counter_abc_total`, and with the label `k1` matching the regex `v1`. Adjust the labels as required.


##### Add required meter binders
  
Micrometer provides a set of binders for monitoring Java metrics out of the box. If you want to enable a meter binder, add the metric binder code defnition to your application code, after the registry initialization. For example:
  
```java
// Initialize registry
LogzioMeterRegistry registry = new LogzioMeterRegistry(logzioConfig, Clock.SYSTEM);

// Gauges buffer and memory pool utilization
new JvmMemoryMetrics().bindTo(registry);
// Gauges max and live data size, promotion and allocation rates, and times GC pauses
new JvmGcMetrics().bindTo(registry);
// Gauges current CPU total and load average.
new ProcessorMetrics().bindTo(registry);
// Gauges thread peak, number of daemon threads, and live threads
new JvmThreadMetrics().bindTo(registry);
// Gauges loaded and unloaded classes
new ClassLoaderMetrics().bindTo(registry);

// File descriptor metrics gathered by the JVM
new FileDescriptorMetrics(tags).bindTo(registry);
// Gauges The uptime and start time of the Java virtual machine
new UptimeMetrics(tags).bindTo(registry);

// Counter of logging events
new LogbackMetrics().bindTo(registry);
new Log4j2Metrics().bindTo(registry);
```

For the full list of available meter binders, refer to the [Micrometer-core](https://github.com/micrometer-metrics/micrometer/tree/main/micrometer-core/src/main/java/io/micrometer/core/instrument/binder) Github repo.

##### Add required metrics

This integration allows you to use the following metrics:

| Name | Behavior | 
| ---- | ---------- | 
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.increment(value); ` call. |
| Gauge             | Metric value can arbitrarily increment or decrement, values can set automaticaly by tracking `Collection` size or set manually by `gauge.set(value)`  | 
| DistributionSummary | Metric values captured by the `summary.record(value)` function, the output is a distribution of `count`,`sum` and `max` for the recorded values during the push interval. |
| Timer       | Mesures timing, metric values can be recorded by `timer.record()` call. |
  
Refer to the Micrometer [documentation](https://micrometer.io/docs/concepts) for more details on each metric.
  
To add a required metric to your code, copy and paste the required metric code to your application, placing it after the initialization code (or the meter binders, if present):

###### [Counter](https://micrometer.io/docs/concepts#_counters)
  
```java
Counter counter = Counter
        .builder("counter_example")
        .description("a description of what this counter does") // optional
        .tags(tags) // optional
        .register(registry);
// Increment your counter
counter.increment(); 
counter.increment(2); 
// The following metric will be created and sent to Logz.io: counter_example_total{env="dev"} 3
```

###### [Gauge](https://micrometer.io/docs/concepts#_gauges)
  
```java
// Create Gauge
List<String> cache = new ArrayList<>(4);
// Track list size
Gauge gauge = Gauge
        .builder("cache_size_gauge_example", cache, List::size)
        .tags(tags)
        .register(registry);
cache.add("1");
// The following metric will be created and sent to Logz.io: cache_size_gauge_example{env="dev"} 1
        
// Track map size
Map<String, Integer> map_gauge = registry.gaugeMapSize("map_gauge_example", tags, new HashMap<>());
map_gauge.put("key",1);
// The following metric will be created and sent to Logz.io: map_gauge_example{env="dev"} 1
        
// set value manually
AtomicInteger manual_gauge = registry.gauge("manual_gauge_example", new AtomicInteger(0));
manual_gauge.set(83);
// The following metric will be created and sent to Logz.io:: manual_gauge_example{env="dev"} 83

```

###### [DistributionSummary](https://micrometer.io/docs/concepts#_distribution_summaries)
  
```java
// Create DistributionSummary
DistributionSummary summary = DistributionSummary
        .builder("summary_example")
        .description("a description of what this summary does") // optional
        .tags(tags) // optional
        .register(registry);
// Record values to distributionSummary
summary.record(10);
summary.record(20);
summary.record(30);
// // The following metrics will be created and sent to Logz.io: 
// summary_example_count{env="dev"} 3
// summary_example_max{env="dev"} 30
// summary_example_sum{env="dev"} 60
```

###### [Timer](https://micrometer.io/docs/concepts#_timers)
  
```java
// Create Timer
Timer timer = Timer
        .builder("timer_example")
        .description("a description of what this timer does") // optional
        .tags(tags) // optional
        .register(registry);
// You can set a value manually
timer.record(1500,TimeUnit.MILLISECONDS);
// You can record the timing of a function
timer.record(()-> {
    try {
        Thread.sleep(1500);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
});
// The following metrics will be created and sent to Logz.io: 
// timer_example_duration_seconds_count{env="dev"} 2
// timer_example_duration_seconds_max{env="dev"} 1501
// timer_example_duration_seconds_sum{env="dev"} 3000

```

##### Run your application

Run your application to start sending metrics to Logz.io.


##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open the [Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

