---
id: Java
title: Java 
overview: Integrate your Java applications with Logz.io to gain observability needed to maintain and improve your applications and performance. With Logz.io, you can monitor your Java logs, metrics, and traces, know if and when incidents occur, and quickly resolve them.
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
recommendedFor: ['Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/java.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
toc_min_heading_level: 2
toc_max_heading_level: 3
---

:::tip
For Kubernetes data, use the [dedicated integration](https://docs.logz.io/docs/shipping/containers/kubernetes/).
:::

## Logs


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="Logzio-Log4j2-Appender" label="Logzio-Log4j2-Appender" default>

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-log4j2-appender/)
:::

The Logz.io Log4j 2 appender sends logs via non-blocking threading bulks and HTTPS encryption to port 8071. It uses LogzioSender, with logs queued in a buffer and are 100% non-blocking, shipped by a background task. This .jar includes LogzioSender, BigQueue, Gson, and Guava.



**Requirements:**:
* Log4j 2.7+
* Java 8+

 

### Add a dependency to a configuration file


JDK 8:
```xml
    <dependency>
        <groupId>io.logz.log4j2</groupId>
        <artifactId>logzio-log4j2-appender</artifactId>
        <version>1.0.19</version>
    </dependency>
```

:::note
If you encounter any issue, try using version 1.0.12 or earlier.
:::

JDK 11+:
```xml
    <dependency>
        <groupId>io.logz.log4j2</groupId>
        <artifactId>logzio-log4j2-appender</artifactId>
        <version>2.0.1</version>
    </dependency>
```

The appender also requires a logger implementation:
```xml
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-slf4j-impl</artifactId>
        <version>2.15.0</version>
    </dependency>
```

Find the logzio-log4j2-appender artifact in the [Maven central repo](https://search.maven.org/artifact/io.logz.log4j2/logzio-log4j2-appender).

### Appender configuration

Replace the placeholders with your configuration.


XML example:

```xml
<Appenders>

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
For more details, see the [Log4j documentation](https://logging.apache.org/log4j/2.x/manual/configuration.html).
::: 
 

### Appender parameters

| Parameter          | Default                              | Explained  | Required/Optional  |
| ------------------ | ------------------------------------ | ----- | ----- |
| **logzioToken**              | *None*                                 | Your Logz.io log shipping token. {@include: ../../_include/log-shipping/log-shipping-token.html} Begin with `$` to use an environment variable or system property with the specified name. For example, `$LOGZIO_TOKEN` uses the LOGZIO_TOKEN environment variable. | Required |
| **logzioType**               | *java*                                 | The [log type](https://support.logz.io/hc/en-us/articles/209486049-What-is-Type-). Can't contain spaces. | Optional |
| **logzioUrl**               | *https://listener.logz.io:8071*                                 | Listener URL and port.    {@include: ../../_include/log-shipping/listener-var.html}  | Required |
| **drainTimeoutSec**       | *5*                                    | How often the appender drains the buffer, in seconds. | Required |
| **socketTimeoutMs**       | *10 * 1000*                                    | Socket timeout during log shipment. | Required |
| **connectTimeoutMs**       | *10 * 1000*                                    | Connection timeout during log shipment, in milliseconds. | Required |
| **addHostname**       | *false*                                    | If true, adds a field named `hostname` with the machine's hostname. If there's no defined hostname, the field won't be added. | Required |
| **additionalFields**       | *None*                                    | Allows to add additional fields to the JSON message sent. The format is "fieldName1=fieldValue1;fieldName2=fieldValue2". Optionally, inject an environment variable value using this format: "fieldName1=fieldValue1;fieldName2=$ENV_VAR_NAME". The environment variable should be the only value. If the environment variable can't be resolved, the field will be omitted. | Optional |
| **debug**       | *false*                                    | Boolean. Set to `true` to print debug messages to stdout. | Required |
| **compressRequests**       | *false*                                    | Boolean. If `true`, logs are compressed in gzip format before sending. If `false`, logs are sent uncompressed. | Required |
| **exceedMaxSizeAction**       | *"cut"*                                    | String. Use "cut" to truncate the message or "drop" to discard oversized logs. Logs exceeding the maximum size after truncation will be dropped. | Required |

### In-memory queue parameters
| Parameter          | Default                              | Explained  |
| ------------------ | ------------------------------------ | ----- |
| **inMemoryQueueCapacityBytes**       | *1024 * 1024 * 100*                                | Memory (in bytes) allowed to use for the memory queue. -1 value means no limit.|
| **inMemoryLogsCountCapacity**       | *-1*                                | Number of logs allowed in the queue before dropping logs. -1 value means no limit.|
| **inMemoryQueue**       | *false*                                | Set to true to use in memory queue. Default is disk queue.|


### Disk queue parameters

| Parameter          | Default                              | Explained  |
| ------------------ | ------------------------------------ | ----- |
| **fileSystemFullPercentThreshold** | *98*                                   | Percentage of file system usage at which the sender stops queueing. Once reached, new logs are dropped until usage falls below the threshold. Set to -1 to never stop processing logs. |
| **gcPersistedQueueFilesIntervalSeconds**       | *30*                                    | Interval (in seconds) for cleaning sent logs from disk. |
| **bufferDir**(deprecated, use queueDir)          | *System.getProperty("java.io.tmpdir")* | Directory for storing the queue. |
| **queueDir**          | *System.getProperty("java.io.tmpdir")* | Directory for storing the queue. |


Code Example:

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

 

### Troubleshooting

If you receive an error about a missing appender, add the following to the configuration file:

```xml

<Configuration status="info" packages="io.logz.log4j2">

# Place the configuration from step 2

</Configuration>

```

#### Using Mapped Diagnostic Context (MDC)

Add MDC with the following code:


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

Which produces the following output:

```json
{
  "message": "This log will hold the MDC data as well",
  "Key": "Value",
  "Your log message follows": "..."
}
```

#### Using Markers

Markers are used to tag and enrich log statements. Add them by running this:


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

Which produces the following output:

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

This appender uses BigQueue for a persistent queue, backing up all logs to the local file system before sending. Logs are enqueued in the buffer and 100% non-blocking, with a background task handling shipment. The `.jar` includes BigQueue, Gson, and Guava for dependency management.

**Requirements**:
* Logback 1.1.7+
* Java 8+

 
### Add dependencies from Maven

Add the following dependencies to `pom.xml`:

JDK 11+:
```
<dependency>
    <groupId>io.logz.logback</groupId>
    <artifactId>logzio-logback-appender</artifactId>
    <version>2.0.1</version>
</dependency>
```


JDK 8+:
```
<dependency>
    <groupId>io.logz.logback</groupId>
    <artifactId>logzio-logback-appender</artifactId>
    <version>1.0.29</version>
</dependency>
```

Logback classic:
```
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.7</version>
</dependency>
```

Find logzio-log4j2-appender artifact in the [Maven central repo](https://search.maven.org/artifact/io.logz.log4j2/logzio-log4j2-appender).


#### Appender configuration

Replace placeholders with your configuration.

:::note
For more details, see the [Logback documentation](https://logback.qos.ch/manual/configuration.html).
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

To output `debug` messages, include the parameter into the code:


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

#### Appender parameters

| Parameter | Description | Required/Default |
|---|---|---|
| token | Your Logz.io log shipping token. {@include: ../../_include/log-shipping/log-shipping-token.html} Begin with `$` to use an environment variable or system property with the specified name. For example, `$LOGZIO_TOKEN` uses the LOGZIO_TOKEN environment variable. | Required |
| logzioUrl | Listener URL and port.    {@include: ../../_include/log-shipping/listener-var.html} | `https://listener.logz.io:8071` |
| logzioType | The [log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), shipped as `type` field. Can't contain spaces. | `java` |
| addHostname | If true, adds a field named `hostname` with the machine's hostname. If there's no defined hostname, the field won't be added.	 | `false` |
| additionalFields | Adds fields to the JSON message output, formatted as `field1=value1;field2=value2`. Use `$` to inject an environment variable value, such as `field2=$VAR_NAME`. The environment variable should be the only value in the key-value pair. If the environment variable can't be resolved, the field is omitted. | N/A |
| bufferDir | Filepath where the appender stores the buffer. | `System.getProperty("java.io.tmpdir")` |
| compressRequests | Boolean. If `true`, logs are compressed in gzip format before sending. If `false`, logs are sent uncompressed. | `false` |
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

 

#### Add MDC to your logs

Each key-value pair you define will be included in log lines while the thread is active. Add it by running the following:

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

Which produces this output:

```json
{
  "message": "This log will hold the MDC data as well",
  "Key": "Value",
  "Your log message follows": "..."
}
```

#### Add Markers to your logs

Markers are used to tag and enrich log statements. Add it by running:


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

Which produces this output:

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



  <TabItem value="OpenTelemetry" label="OpenTelemetry">


This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites

- Java 8+

:::note
If you need an example aplication to test this integration, please refer to our [Java OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/java/logs).
:::

### Configure the instrumentation

Add the following dependencies to `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.logzio.otel</groupId>
  <artifactId>otel-log</artifactId>
  <version>1.0-SNAPSHOT</version>
  <name>otel-log</name>
  <packaging>jar</packaging>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.release>17</maven.compiler.release>
    <spring-boot.version>3.0.6</spring-boot.version>
  </properties>

  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-bom</artifactId>
        <version>1.25.0</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
      <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-bom-alpha</artifactId>
        <version>1.25.0-alpha</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <dependencies>
    <!-- OpenTelemetry API and SDK dependencies -->
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-api</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-sdk</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-exporter-otlp</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-semconv</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-exporter-otlp-logs</artifactId>
    </dependency>

    <!-- Spring Boot dependencies -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>${spring-boot.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
      <version>${spring-boot.version}</version>
    </dependency>

    <!-- Logback dependencies -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-core</artifactId>
      <version>1.4.7</version>
    </dependency>
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.4.7</version>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.7</version>
    </dependency>

    <!-- OpenTelemetry Logback Appender -->
    <dependency>
      <groupId>io.opentelemetry.instrumentation</groupId>
      <artifactId>opentelemetry-logback-appender-1.0</artifactId>
      <version>1.25.1-alpha</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Spring Boot Maven plugin -->
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <version>${spring-boot.version}</version>
      </plugin>
      
      <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
          <archive>
            <manifest>
              <mainClass>com.logzio.otel.DiceApplication</mainClass>
            </manifest>
          </archive>
        </configuration>
        <executions>
          <execution>
            <id>make-assembly</id>
            <phase>package</phase>
            <goals>
              <goal>single</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>

```



#### Add the OpenTelemetry controller

```java
package com.logzio.otel;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.logs.GlobalLoggerProvider;
import io.opentelemetry.exporter.otlp.http.logs.OtlpHttpLogRecordExporter;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.logs.SdkLoggerProvider;
import io.opentelemetry.sdk.logs.export.BatchLogRecordProcessor;
import io.opentelemetry.sdk.resources.Resource;
import io.opentelemetry.semconv.resource.attributes.ResourceAttributes;
import io.opentelemetry.api.common.Attributes;

public class OpenTelemetryConfig {

    private static final String DEFAULT_ENDPOINT = "https://otlp-listener.logz.io/v1/logs";
    private static final String LOGZ_IO_TOKEN = "<LOG-SHIPPING-TOKEN>";
    private static final String SERVICE_NAME = "java-otlp";

    public void initializeOpenTelemetry() {

        // set service name on all OTel signals
        Resource resource = Resource.getDefault().merge(Resource.create(
                Attributes.of(ResourceAttributes.SERVICE_NAME, SERVICE_NAME)));

        // Set up the OTLP log exporter with the endpoint and necessary headers
        OtlpHttpLogRecordExporter logExporter = OtlpHttpLogRecordExporter.builder()
                .setEndpoint(DEFAULT_ENDPOINT)
                .addHeader("Authorization", "Bearer " + LOGZ_IO_TOKEN)
                .addHeader("user-agent", "logzio-java-logs-otlp")
                .build();

        // Initialize the logger provider
        SdkLoggerProvider sdkLoggerProvider = SdkLoggerProvider.builder()
                .setResource(resource)
                .addLogRecordProcessor(BatchLogRecordProcessor.builder(logExporter).build())
                .build();

        // create sdk object and set it as global
        OpenTelemetrySdk sdk = OpenTelemetrySdk.builder()
                        .setLoggerProvider(sdkLoggerProvider)
                        .build();
        GlobalOpenTelemetry.set(sdk);
        // connect logger
        GlobalLoggerProvider.set(sdk.getSdkLoggerProvider());
        // Add hook to close SDK, which flushes logs
        Runtime.getRuntime().addShutdownHook(new Thread(sdk::close));
    }
}
```

{@include: ../../_include/log-shipping/log-shipping-token.md}

Update the `listener.logz.io` part in `https://otlp-listener.logz.io/v1/logs` with the URL for [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).

#### Add the Logback

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration debug="true">

    <!-- #### Model 1: Logging via OpenTelemetry Instrumentation #### -->

    <appender name="otel-otlp"
        class="io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender">
        <captureExperimentalAttributes>false</captureExperimentalAttributes>
        <!-- include src origin info -->
        <captureCodeAttributes>true</captureCodeAttributes>
        <!-- include slf4j key/value arguments -->
        <captureKeyValuePairAttributes>true</captureKeyValuePairAttributes>
    </appender>


    <!-- #### send logs to all 3 loggers #### -->
    <root level="INFO">
        <appender-ref ref="otel-otlp" />
    </root>
</configuration>
```


#### Run the application

   ```bash
   mvn clean package
   java -jar target/*.jar
   ```


### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.


 
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

### Import to your code

```java
import io.micrometer.logzio.LogzioConfig;
import io.micrometer.logzio.LogzioMeterRegistry;
```

### Getting started

Replace the placeholders in the code (indicated by `<< >>`) to match your specifics.



| Environment variable | Description |Required/Default|
|---|---|---|
|`<<LISTENER-HOST>>`|  Logz.io Listener URL for your region. Port **8052** for HTTP, or port **8053** for HTTPS. See the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) for more info. | Required|
|`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`| Logz.io Prometheus Metrics account token. Find it under **Settings > Manage accounts**. [Look up your Metrics account token.](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/). | Required|
|interval | Interval in seconds to push metrics to Logz.io. **Your program must run for at least one interval**.  | Required|

### Example:

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

### Configuring common tags

Attach common tags to your registry to include them in all reported metrics. For example:

```java
// Initialize registry
LogzioMeterRegistry registry = new LogzioMeterRegistry(logzioConfig, Clock.SYSTEM);
// Define tags (labels)
registry.config().commonTags("key", "value");
```

### Filtering labels - Include

Use `includeLabels` in your `LogzioConfig()` constructor:

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

#### Filtering labels - Exclude

Use `excludeLabels` in your `LogzioConfig()` constructor:

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


### Using meter binders

Micrometer provides a set of binders for monitoring JVM metrics out of the box:



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

For more information about other binders check out the [Micrometer-core](https://github.com/micrometer-metrics/micrometer/tree/main/micrometer-core/src/main/java/io/micrometer/core/instrument/binder) Github repo.

### Metric types


| Name | Behavior | 
| ---- | ---------- | 
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.increment(value);` call. |
| Gauge             | Metric value can arbitrarily increment or decrement, values can set automaticaly by tracking `Collection` size or manually by `gauge.set(value)`.  | 
| DistributionSummary | Captured metric values via `summary.record(value)`. Outputs a distribution of `count`,`sum` and `max` for the recorded values during the push interval. |
| Timer       | Mesures timing. Metric values recorded by `timer.record()` call. |

For more details, see the Micrometer [documentation](https://micrometer.io/docs/concepts).


#### [Counter](https://micrometer.io/docs/concepts#_counters)

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

#### [Gauge](https://micrometer.io/docs/concepts#_gauges)

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

#### [DistributionSummary](https://micrometer.io/docs/concepts#_distribution_summaries)

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

#### [Timer](https://micrometer.io/docs/concepts#_timers)

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

Run your application to start sending metrics to Logz.io. Give it some time to run and check the Logz.io [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).


## Traces


Deploy this integration for automatic instrumentation of your Java application using OpenTelemetry. The Java agent captures spans and forwards them to the collector, which exports data to your Logz.io account.

This integration includes:

* Downloading the OpenTelemetry Java agent to your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Establishing communication between the agent and collector


**Requirements**:

* A Java application without instrumentation.
* An active Logz.io account.
* Port `4317` available on your host system.
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::


### Setting up auto-instrumentation and sending Traces to Logz.io


**1. Download Java agent**

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to your application host.


 
**2. Download and configure OpenTelemetry collector**

Create a dedicated directory on the host of your Java application and download the relevant [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0).

Next, create a configuration file, `config.yaml`, with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}



**3. Start the collector**

Run:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the collector's directory.
* Replace `<VERSION-NAME>` with the version name, e.g. `otelcontribcol_darwin_amd64`.



**4. Attach the agent**

Run the following command from your Java application's directory:



```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-SERVICE-NAME> \
     -Dotel.exporter.otlp.endpoint=http://localhost:4317 \
     -jar target/*.jar
```

* Replace `<path/to>` with the collector's directory.
* Replace `<YOUR-SERVICE-NAME>` with the tracing service name.



### Control the number of spans

Use the sampling option in the Java agent to limit outgoing spans.

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

### Viewing Traces in Logz.io

Give your traces time to process, after which they'll be available in your [Tracing](https://app.logz.io/#/dashboard/jaeger) dashboard.