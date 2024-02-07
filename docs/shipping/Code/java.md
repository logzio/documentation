---
id: Java
title: Java 
overview: Integrate your Java applications with Logz.io to gain observability needed to maintain and improve your applications and performance. With Logz.io, you can monitor your Java logs, metrics, and traces, know if and when incidents occur, and quickly resolve them.
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/java.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

:::tip
If your code runs within Kubernetes, it's best practice to use our Kubernetes integration to collect various telemetry types.
:::

## Logs


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="Logzio-Log4j2-Appender" label="Logzio-Log4j2-Appender" default>

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-log4j2-appender/)
:::

The Logz.io Log4j 2 appender sends logs using non-blocking threading, bulks, and HTTPS encryption to port 8071.

This appender uses LogzioSender.
Logs queue in the buffer and are 100% non-blocking.
A background task handles log shipping.
To help manage dependencies, this .jar shades LogzioSender, BigQueue, Gson, and Guava.

**Before you begin, you'll need**:
Log4j 2.7 or higher,
Java 8 or higher

 

#### Add the dependency to your project

Add a dependency to your project configuration file (for instance, `pom.xml` in a Maven project). 

JDK 8:
```xml
    <dependency>
        <groupId>io.logz.log4j2</groupId>
        <artifactId>logzio-log4j2-appender</artifactId>
        <version>1.0.19</version>
    </dependency>
```

JDK 11 and above:
```xml
    <dependency>
        <groupId>io.logz.log4j2</groupId>
        <artifactId>logzio-log4j2-appender</artifactId>
        <version>2.0.0</version>
    </dependency>
```

The appender also requires a logger implementation, for example:
```xml
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-slf4j-impl</artifactId>
        <version>2.15.0</version>
    </dependency>
```

The logzio-log4j2-appender artifact can be found in the Maven central repo at https://search.maven.org/artifact/io.logz.log4j2/logzio-log4j2-appender.

#### Configure the appender

Use the samples in the code block below as a starting point, and replace the sample with a configuration that matches your needs.

For a complete list of options, see the configuration parameters below the code block.👇

XML example:

```xml
<Appenders>

  <!-- Replace these parameters with your configuration -->
  <LogzioAppender name="Logzio">
    <logzioToken><<LOG-SHIPPING-TOKEN>></logzioToken>
    <logzioUrl>https://<<LISTENER-HOST>>:8071</logzioUrl>
    <logzioType>myAwesomeType</logzioType>
  </LogzioAppender>

</Appenders>

<Loggers>
  <Root level="info">
    <AppenderRef ref="Logzio"/>
  </Root>
</Loggers>
```

log4j2.properties example:

```java
# Extra logging related to initialization of Log4j
# Set to debug or trace if log4j initialization is failing
status = debug
# Name of the configuration
name = io.logz.log4j2

appenders=logzioAppender

# Logz.io configuration
appender.logzioAppender.type = logzioAppender
appender.logzioAppender.name = Logzio
appender.logzioAppender.LogzioToken = <<LOG-SHIPPING-TOKEN>>
appender.logzioAppender.LogzioType = myAwesomeType
appender.logzioAppender.LogzioUrl = https://<<LISTENER-HOST>>:8071

# Root logger level
rootLogger.level = debug
# Root logger referring to logzio appender
rootLogger.appenderRef.logzioAppender.ref = logzioAppender
```


:::note
See the [Log4j documentation](https://logging.apache.org/log4j/2.x/manual/configuration.html) for more information on the Log4j 2 configuration file.
:::
 

#### Parameters

| Parameter          | Default                              | Explained  | Required/Optional  |
| ------------------ | ------------------------------------ | ----- | ----- |
| **logzioToken**              | *None*                                 | Your Logz.io log shipping token securely directs the data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} Begin with `$` to use an environment variable or system property with the specified name. For example, `$LOGZIO_TOKEN` uses the LOGZIO_TOKEN environment variable. | Required |
| **logzioType**               | *java*                                 | The [log type](https://support.logz.io/hc/en-us/articles/209486049-What-is-Type-) for that appender, it must not contain any spaces | Optional |
| **logzioUrl**               | *https://listener.logz.io:8071*                                 | Listener URL and port.    {@include: ../../_include/log-shipping/listener-var.html}  | Required |
| **drainTimeoutSec**       | *5*                                    | How often the appender should drain the queue (in seconds) | Required |
| **socketTimeoutMs**       | *10 * 1000*                                    | The socket timeout during log shipment | Required |
| **connectTimeoutMs**       | *10 * 1000*                                    | The connection timeout during log shipment | Required |
| **addHostname**       | *false*                                    | If true, then a field named 'hostname' will be added holding the host name of the machine. If from some reason there's no defined hostname, this field won't be added | Required |
| **additionalFields**       | *None*                                    | Allows to add additional fields to the JSON message sent. The format is "fieldName1=fieldValue1;fieldName2=fieldValue2". You can optionally inject an environment variable value using the following format: "fieldName1=fieldValue1;fieldName2=$ENV_VAR_NAME". In that case, the environment variable should be the only value. In case the environment variable can't be resolved, the field will be omitted. | Optional |
| **debug**       | *false*                                    | Print some debug messages to stdout to help to diagnose issues | Required |
| **compressRequests**       | *false*                                    | Boolean. `true` if logs are compressed in gzip format before sending. `false` if logs are sent uncompressed. | Required |
| **exceedMaxSizeAction**       | *"cut"*                                    | String. cut to truncate the message field or drop to drop log that exceed the allowed maximum size for logzio. If the log size exceeding the maximum size allowed after truncating the message field, the log will be dropped. | Required |

#### Parameters for in-memory queue
| Parameter          | Default                              | Explained  |
| ------------------ | ------------------------------------ | ----- |
| **inMemoryQueueCapacityBytes**       | *1024 * 1024 * 100*                                | The amount of memory(bytes) we are allowed to use for the memory queue. If the value is -1 the sender will not limit the queue size.|
| **inMemoryLogsCountCapacity**       | *-1*                                | Number of logs we are allowed to have in the queue before dropping logs. If the value is -1 the sender will not limit the number of logs allowed.|
| **inMemoryQueue**       | *false*                                | Set to true if the appender uses in memory queue. By default the appender uses disk queue|


#### Parameters for disk queue
| Parameter          | Default                              | Explained  |
| ------------------ | ------------------------------------ | ----- |
| **fileSystemFullPercentThreshold** | *98*                                   | The percent of used file system space at which the sender will stop queueing. When we will reach that percentage, the file system in which the queue is stored will drop all new logs until the percentage of used space drops below that threshold. Set to -1 to never stop processing new logs |
| **gcPersistedQueueFilesIntervalSeconds**       | *30*                                    | How often the disk queue should clean sent logs from disk |
| **bufferDir**(deprecated, use queueDir)          | *System.getProperty("java.io.tmpdir")* | Where the appender should store the queue |
| **queueDir**          | *System.getProperty("java.io.tmpdir")* | Where the appender should store the queue |


#### Code Example

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LogzioLog4j2Example {
  public static void main(String[] args) {
    Logger logger = LogManager.getLogger(LogzioLog4j2Example.class);

    logger.info("Testing logz.io!");
    logger.warn("Winter is coming");
  }
}
```

 

#### Troubleshooting

If you receive an error message regarding a missing appender, try adding the following configuration to the beginning and end of the configuration file:

```xml

<Configuration status="info" packages="io.logz.log4j2">

# Place the configuration from step 2

</Configuration>

```

#### MDC

When you add mapped diagnostic context (MDC) to your logs,
each key-value pair you define is added log lines while the thread is alive.

So this code sample...

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.ThreadContext;

public class LogzioLog4j2Example {
  public static void main(String[] args) {
    Logger logger = LogManager.getLogger(LogzioLog4j2Example.class);
    ThreadContext.put("Key", "Value");
    logger.info("This log will hold the MDC data as well");
  }
}
```

...produces this log output.

```json
{
  "message": "This log will hold the MDC data as well",
  "Key": "Value",
  "Your log message follows": "..."
}
```

#### Markers

Markers are values you can use to tag and enrich log statements.

This code...

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.Marker;
import org.apache.logging.log4j.MarkerManager;

public class LogzioLog4j2Example {
  public static void main(String[] args) {
    Logger logger = LogManager.getLogger(LogzioLog4j2Example.class);
    Marker marker = MarkerManager.getMarker("Fatal");
    logger.error(marker, "This line has a fatal error");
  }
}
```

...produces this log output.

```json
{
  "message": "This line has a fatal error",
  "Marker": "Fatal",
  "Your log message follows": "..."
}
```

</TabItem>
  <TabItem value="Logzio-Logback-Appender" label="Logzio-Logback-Appender">

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-logback-appender)
:::

Logback sends logs to your Logz.io account using non-blocking threading, bulks, and HTTPS encryption to port 8071.

This appender uses BigQueue implementation of persistent queue, so all logs are backed up to a local file system before being sent.
Once you send a log, it will be enqueued in the buffer and 100% non-blocking.
A background task handles the log shipment.
To help manage dependencies, this .jar shades BigQueue, Gson, and Guava.

**Before you begin, you'll need**:
Logback 1.1.7 or higher,
Java 8 or higher

 

#### Add the dependency to your project

Add a dependency to your project configuration file

#### Installation from Maven

In the `pom.xml` add the following dependencies:

JDK 11 and above:
```
<dependency>
    <groupId>io.logz.logback</groupId>
    <artifactId>logzio-logback-appender</artifactId>
    <version>2.0.0</version>
</dependency>
```


JDK 8 and above:
```
<dependency>
    <groupId>io.logz.logback</groupId>
    <artifactId>logzio-logback-appender</artifactId>
    <version>1.0.29</version>
</dependency>
```

Logback appender also requires logback classic:
```
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.7</version>
</dependency>
```

The logzio-log4j2-appender artifact can be found in the Maven central repo at https://search.maven.org/artifact/io.logz.log4j2/logzio-log4j2-appender.


#### Configure the appender

Use the samples in the code block below as a starting point, and replace the sample with a configuration that matches your needs.

For a complete list of options, see the configuration parameters below the code block.👇

:::note
See the [Logback documentation](https://logback.qos.ch/manual/configuration.html) for more information on the Logback configuration file.
:::
 

```xml
<!-- Use debug=true here if you want to see output from the appender itself -->
<!-- Use line=true here if you want to see the line of code that generated this log -->
<configuration>
    <!-- Use shutdownHook so that we can close gracefully and finish the log drain -->
    <shutdownHook class="ch.qos.logback.core.hook.DelayingShutdownHook"/>
    <appender name="LogzioLogbackAppender" class="io.logz.logback.LogzioLogbackAppender">
        <token>yourlogziopersonaltokenfromsettings</token>
        <logzioType>myAwesomeType</logzioType>
        <logzioUrl>https://listener.logz.io:8071</logzioUrl>
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
            <level>INFO</level>
        </filter>
    </appender>
    <root level="debug">
        <!-- IMPORTANT: This line is required -->
        <appender-ref ref="LogzioLogbackAppender"/>
    </root>
</configuration>
```

If you want to output `debug` messages, include the `debug` parameter into the code as follows:


```xml
<configuration>
  <!-- Closes gracefully and finishes the log drain -->
  <shutdownHook class="ch.qos.logback.core.hook.DelayingShutdownHook"/>

  <appender name="LogzioLogbackAppender" class="io.logz.logback.LogzioLogbackAppender">
    <!-- Replace these parameters with your configuration -->
    <token><<LOG-SHIPPING-TOKEN>></token>
    <logzioUrl>https://<<LISTENER-HOST>>:8071</logzioUrl>
    <logzioType>myType</logzioType>
	<debug>true</debug>

    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>INFO</level>
    </filter>
  </appender>

  <root level="debug">
    <!-- IMPORTANT: This line is required -->
    <appender-ref ref="LogzioLogbackAppender"/>
  </root>
</configuration>
```

#### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| token | Your Logz.io log shipping token securely directs the data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} Begin with `$` to use an environment variable or system property with the specified name. For example, `$LOGZIO_TOKEN` uses the LOGZIO_TOKEN environment variable. | Required |
| logzioUrl | Listener URL and port.    {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| logzioType | The [log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `java` |
| addHostname | Indicates whether to add `hostname` field to logs. This field holds the machine's host name.    Set to `true` to include hostname. Set to `false` to leave it off. If a host name can't be found, this field is not added. | `false` |
| additionalFields | Adds fields to the JSON message output, formatted as `field1=value1;field2=value2`.    Use `$` to inject an environment variable value, such as `field2=$VAR_NAME`. The environment variable should be the only value in the key-value pair. If the environment variable can't be resolved, the field is omitted. | N/A |
| bufferDir | Filepath where the appender stores the buffer. | `System.getProperty("java.io.tmpdir")` |
| compressRequests | Boolean. Set to `true` if you're sending gzip-compressed logs. Set to `false` if sending uncompressed logs. | `false` |
| connectTimeout  | Connection timeout during log shipment, in milliseconds. | `10 * 1000` |
| debug  | Boolean. Set to `true` to print debug messages to stdout. | `false` |
| drainTimeoutSec   | How often the appender drains the buffer, in seconds. | `5` |
| fileSystemFullPercentThreshold   | Integer. Identifies a maximum file system usage, in percent. Set to `-1` to disable.    If the file system storage exceeds this threshold, the appender stops buffering and drops all new logs. Buffering resumes if used space drops below the threshold. | `98` |
| format   | Set to `json` if the log message is to be sent as JSON, so that each JSON node is a field in Logz.io. Set to `text` to send the log message as plain text. | `text` |
| line   | Boolean. Set to `true` to print the line number of the code that generated this log message. Set to `false` to leave the line number out. | `false` |
| socketTimeout | Socket timeout during log shipment, in milliseconds. | `10 * 1000` |


#### Code sample

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LogzioLogbackExample {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(LogzioLogbackExample.class);

      logger.info("Testing logz.io!");
      logger.warn("Winter is coming");
  }
}
```

 

#### More options

You can optionally add mapped diagnostic context (MDC)
and markers to your logs.

#### MDC

You  can add Mapped Diagnostic Context (MDC) to your logs.
Each key-value pair you define is added log lines while the thread is alive.

So this code sample...

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

public class LogzioLogbackExample {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(LogzioLogbackExample.class);

    MDC.put("Key", "Value");
    logger.info("This log will hold the MDC data as well");
  }
}
```

...produces this log output.

```json
{
  "message": "This log will hold the MDC data as well",
  "Key": "Value",
  "Your log message follows": "..."
}
```

#### Markers

Markers are values you can use to tag and enrich log statements.

This code...

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.Marker;

public class LogzioLogbackExample {

  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(LogzioLogbackExample.class);

    Marker marker = MarkerFactory.getMarker("Fatal");
    logger.error(marker, "This line has a fatal error");
  }
}
```

...produces this log output.

```json
{
  "message": "This line has a fatal error",
  "Marker": "Fatal",
  "Your log message follows": "..."
}
```
  
#### Troubleshooting
  
If the log appender does not ship logs, add `<inMemoryQueue>true</inMemoryQueue>` and `<inMemoryQueueCapacityBytes>-1</inMemoryQueueCapacityBytes>` to the configuration file as follows:
  
```xml
<configuration>
  <!-- Closes gracefully and finishes the log drain -->
  <shutdownHook class="ch.qos.logback.core.hook.DelayingShutdownHook"/>

  <appender name="LogzioLogbackAppender" class="io.logz.logback.LogzioLogbackAppender">
    <!-- Replace these parameters with your configuration -->
    <token><<LOG-SHIPPING-TOKEN>></token>
    <logzioUrl><<LISTENER-HOST>>:8071</logzioUrl>
    <logzioType>myType</logzioType>

    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>INFO</level>
    </filter>
    <inMemoryQueue>true</inMemoryQueue> 
    <inMemoryQueueCapacityBytes>-1</inMemoryQueueCapacityBytes>
  </appender>

  <root level="debug">
    <!-- IMPORTANT: This line is required -->
    <appender-ref ref="LogzioLogbackAppender"/>
  </root>
</configuration>
```
</TabItem>
</Tabs>
  

## Metrics


:::note
[Project's GitHub repo](https://github.com/logzio/micrometer-registry-logzio/)
:::
### Usage

<Tabs>
  <TabItem value="Via-maven" label="Via maven" default>

```xml
<dependency>
    <groupId>io.logz.micrometer</groupId>
    <artifactId>micrometer-registry-logzio</artifactId>
    <version>1.0.2</version>
</dependency>
```

</TabItem>
  <TabItem value="Via-gradle-groovy" label="Via gradle groovy">

```groovy
implementation 'io.logz.micrometer:micrometer-registry-logzio:1.0.2'
```
</TabItem>
  <TabItem value="Via-gradle-Kotlin" label="Via gradle Kotlin">


```kotlin
implementation("io.logz.micrometer:micrometer-registry-logzio:1.0.2")
```
</TabItem>
</Tabs>

#### Import in your package

```java
import io.micrometer.logzio.LogzioConfig;
import io.micrometer.logzio.LogzioMeterRegistry;
```

#### Quick start

Replace the placeholders in the code (indicated by the double angle brackets `<< >>`) to match your specifics.

| Environment variable | Description |Required/Default|
|---|---|---|
|`<<LISTENER-HOST>>`|  The full Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic (example: https://listener.logz.io:8053). For more details, see the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) in logz.io docs | Required|
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| The Logz.io Prometheus Metrics account token. Find it under **Settings > Manage accounts**. [Look up your Metrics account token.](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/)  | Required|
|interval | The interval in seconds, to push metrics to Logz.io **Note that your program will need to run for at least one interval for the metrics to be sent**  | Required|

#### In your package

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
           return "https://<<LISTENER-HOST>>":8053;
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

#### Common tags

You can attach common tags to your registry that will be added to all metrics reported, for example:

```java
// Initialize registry
LogzioMeterRegistry registry = new LogzioMeterRegistry(logzioConfig, Clock.SYSTEM);
// Define tags (labels)
registry.config().commonTags("key", "value");
```

#### Filter labels

You can the `includeLabels` or `excludeLabels` functions to filter your metrics by labels.

#### Include

Take for example this following usage, In your `LogzioConfig()` constructor:

```java
@Override
public Hashtable<String, String> includeLabels() {
    Hashtable<String, String> includeLabels = new Hashtable<>();
    includeLabels.put("__name__", "my_counter_abc_total|my_second_counter_abc_total");
    includeLabels.put("k1", "v1");
    return includeLabels;
}
```
The registry will keep only metrics with the label `__name__` matching the regex `my_counter_abc_total|my_second_counter_abc_total`, and with the label `k1` matching the regex `v1`.

#### Exclude

In your `LogzioConfig()` constructor

```java
@Override
public Hashtable<String, String> excludeLabels() {
    Hashtable<String, String> excludeLabels = new Hashtable<>();
    excludeLabels.put("__name__", "my_counter_abc_total|my_second_counter_abc_total");
    excludeLabels.put("k1", "v1");
    return excludeLabels;
}
```

The registry will drop all metrics with the label `__name__` matching the regex `my_counter_abc_total|my_second_counter_abc_total`, and with the label `k1` matching the regex `v1`.


#### Meter binders

Micrometer provides a set of binders for monitoring JVM metrics out of the box, for example:

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

For more information about other binders check out [Micrometer-core](https://github.com/micrometer-metrics/micrometer/tree/main/micrometer-core/src/main/java/io/micrometer/core/instrument/binder) Github repo.

#### Types of metrics 

Refer to the Micrometer [documentation](https://micrometer.io/docs/concepts) for more details.


| Name | Behavior | 
| ---- | ---------- | 
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.increment(value); ` call. |
| Gauge             | Metric value can arbitrarily increment or decrement, values can set automaticaly by tracking `Collection` size or set manually by `gauge.set(value)`  | 
| DistributionSummary | Metric values captured by the `summary.record(value)` function, the output is a distribution of `count`,`sum` and `max` for the recorded values during the push interval. |
| Timer       | Mesures timing, metric values can be recorded by `timer.record()` call. |

##### [Counter](https://micrometer.io/docs/concepts#_counters)

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

##### [Gauge](https://micrometer.io/docs/concepts#_gauges)

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

##### [DistributionSummary](https://micrometer.io/docs/concepts#_distribution_summaries)

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

##### [Timer](https://micrometer.io/docs/concepts#_timers)

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



### Run your application

Run your application to start sending metrics to Logz.io.


### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).


## Traces

Deploy this integration to enable automatic instrumentation of your Java application using OpenTelemetry.

This integration includes:

* Downloading the OpenTelemetry Java agent to your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Establishing communication between the agent and collector

On deployment, the Java agent automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

### Setup auto-instrumentation for your locally hosted Java application and send traces to Logz.io

**Before you begin, you'll need**:

* A Java application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


### Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.

### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Java application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


### Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

### Attach the agent to the runtime and run it

Run the following command from the directory of your Java application:

```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-SERVICE-NAME> \
     -Dotel.exporter.otlp.endpoint=http://localhost:4317 \
     -jar target/*.jar
```

* Replace `<path/to>` with the path to the directory where you downloaded the agent.
* Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.


### Controlling the number of spans

To limit the number of outgoing spans, you can use the sampling option in the Java agent.

The sampler configures whether spans will be recorded for any call to `SpanBuilder.startSpan`.

| System property                 | Environment variable            | Description                                                  |
|---------------------------------|---------------------------------|--------------------------------------------------------------|
| otel.traces.sampler              | OTEL_TRACES_SAMPLER              | The sampler to use for tracing. Defaults to `parentbased_always_on` |
| otel.traces.sampler.arg          | OTEL_TRACES_SAMPLER_ARG          | An argument to the configured tracer if supported, for example a ratio. |

Supported values for `otel.traces.sampler` are

- "always_on": AlwaysOnSampler
- "always_off": AlwaysOffSampler
- "traceidratio": TraceIdRatioBased. `otel.traces.sampler.arg` sets the ratio.
- "parentbased_always_on": ParentBased(root=AlwaysOnSampler)
- "parentbased_always_off": ParentBased(root=AlwaysOffSampler)
- "parentbased_traceidratio": ParentBased(root=TraceIdRatioBased). `otel.traces.sampler.arg` sets the ratio.

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).
