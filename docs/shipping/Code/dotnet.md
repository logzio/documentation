---
id: dotnet
title: .NET
overview: Send .NET metrics.
product: ['logs', 'metrics', 'tracing']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/dotnet.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---
## Logs

### log4net

**Before you begin, you'll need**:

* log4net 2.0.8 or higher
* .NET Core SDK version 2.0 or higher
* .NET Framework version 4.6.1 or higher


#### Add the dependency to your project

If you're on Windows, navigate to your project's folder in the command line, and run this command to install the dependency.

```
Install-Package Logzio.DotNet.Log4net
```

If you're on a Mac or Linux machine, you can install the package using Visual Studio. Select **Project > Add NuGet Packages...**, and then search for `Logzio.DotNet.Log4net`.

#### Configure the appender

You can configure the appender in a configuration file or directly in the code.
Use the samples in the code blocks below as a starting point, and replace them with a configuration that matches your needs. See [log4net documentation 🔗](https://github.com/apache/logging-log4net) to learn more about configuration options.

For a complete list of options, see the configuration parameters below the code blocks.👇

##### Option 1: In a configuration file

```xml
<log4net>
    <appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
    	<!--
		Required fields
	-->
	<!-- Your Logz.io API token -->
	<token><<LOG-SHIPPING-TOKEN>></token>

	<!--
		Optional fields (with their default values)
	-->
	<!-- The type field will be added to each log message, making it
	easier for you to differ between different types of logs. -->
    	<type>log4net</type>
	<!-- The URL of the Lgz.io listener -->
    	<listenerUrl>https://<<LISTENER-HOST>>:8071</listenerUrl>
        <!--Optional proxy server address:
        proxyAddress = "http://your.proxy.com:port" -->
	<!-- The maximum number of log lines to send in each bulk -->
    	<bufferSize>100</bufferSize>
	<!-- The maximum time to wait for more log lines, in a hh:mm:ss.fff format -->
    	<bufferTimeout>00:00:05</bufferTimeout>
	<!-- If connection to Logz.io API fails, how many times to retry -->
    	<retriesMaxAttempts>3</retriesMaxAttempts>
    	<!-- Time to wait between retries, in a hh:mm:ss.fff format -->
	<retriesInterval>00:00:02</retriesInterval>
	<!-- Set the appender to compress the message before sending it -->
	<gzip>true</gzip>
	<!-- Uncomment this to enable sending logs in Json format -->
	<!--<parseJsonMessage>true</parseJsonMessage>-->
	<!-- Enable the appender's internal debug logger (sent to the console output and trace log) -->
	<debug>false</debug>
	<!-- If you have custom fields keys that start with capital letter and want to see the fields
	with capital letter in Logz.io, set this field to true. The default is false
	(first letter will be small letter). -->
	<jsonKeysCamelCase>false</jsonKeysCamelCase>
	<!-- Add trace context (traceId and spanId) to each log. The default is false -->
	<addTraceContext>false</addTraceContext>
    </appender>

    <root>
    	<level value="INFO" />
    	<appender-ref ref="LogzioAppender" />
    </root>
</log4net>
```

Add a reference to the configuration file in your code, as shown in the example [here](https://github.com/logzio/logzio-dotnet/blob/master/sample-applications/LogzioLog4netSampleApplication/Program.cs).

###### Code sample

```csharp
using System.IO;
using log4net;
using log4net.Config;
using System.Reflection;

namespace dotnet_log4net
{
    class Program
    {
        static void Main(string[] args)
        {
            var logger = LogManager.GetLogger(typeof(Program));
            var logRepository = LogManager.GetRepository(Assembly.GetEntryAssembly());

            // Replace "App.config" with the config file that holds your log4net configuration
            XmlConfigurator.Configure(logRepository, new FileInfo("App.config"));

            logger.Info("Now I don't blame him 'cause he run and hid");
            logger.Info("But the meanest thing he ever did");
            logger.Info("Before he left was he went and named me Sue");

            LogManager.Shutdown();
        }
    }
}
```


##### Option 2: In the code

```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
// <-- Uncomment and edit this line to enable proxy routing: -->
// logzioAppender.AddProxyAddress("http://your.proxy.com:port");
// <-- Uncomment this to enable sending logs in Json format -->
// logzioAppender.ParseJsonMessage(true);
// <-- Uncomment these lines to enable gzip compression -->
// logzioAppender.AddGzip(true);
// logzioAppender.ActivateOptions();
// logzioAppender.JsonKeysCamelCase(false);
// logzioAppender.AddTraceContext(false);
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```


###### Code sample

```csharp
using log4net;
using log4net.Core;
using log4net.Repository.Hierarchy;
using Logzio.DotNet.Log4net;

namespace dotnet_log4net
{
    class Program
    {
        static void Main(string[] args)
        {
            var hierarchy = (Hierarchy)LogManager.GetRepository();
            var logger = LogManager.GetLogger(typeof(Program));
            var logzioAppender = new LogzioAppender();

            logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
            logzioAppender.AddListenerUrl("https://<<LISTENER-HOST>>:8071");
            // <-- Uncomment and edit this line to enable proxy routing: -->
            // logzioAppender.AddProxyAddress("http://your.proxy.com:port");
            // <-- Uncomment this to enable sending logs in Json format -->
            // logzioAppender.ParseJsonMessage(true);
            // <-- Uncomment these lines to enable gzip compression -->
            // logzioAppender.AddGzip(true);
            // logzioAppender.ActivateOptions();
            // logzioAppender.JsonKeysCamelCase(false)
            // logzioAppender.AddTraceContext(false);
            logzioAppender.ActivateOptions();

            hierarchy.Root.AddAppender(logzioAppender);
            hierarchy.Configured = true;
            hierarchy.Root.Level = Level.All;

            logger.Info("Now I don't blame him 'cause he run and hid");
            logger.Info("But the meanest thing he ever did");
            logger.Info("Before he left was he went and named me Sue");

            LogManager.Shutdown();
        }
    }
}
```

###### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | Your [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `log4net` |
| bufferSize | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| bufferTimeout | Maximum time to wait for more log lines, as _hh:mm:ss.fff_. | `00:00:05` |
| retriesMaxAttempts | Maximum number of attempts to connect to Logz.io. | `3` |
| retriesInterval | Time to wait between retries, as _hh:mm:ss.fff_. | `00:00:02` |
| gzip | To compress the data before shipping, `true`. Otherwise, `false`. | `false` |
| debug | To print debug messages to the console and trace log, `true`. Otherwise, `false`. | `false`
| parseJsonMessage | To parse your message as JSON format, add this field and set it to `true`. | `false` |
| proxyAddress | Proxy address to route your logs through. | `None` |
| jsonKeysCamelCase | If you have custom fields keys that start with a capital letter and want to see the fields with a capital letter in Logz.io, set this field to true. | `false` |
| addTraceContext | If want to add trace context to each log, set this field to true. | `false` |



##### Custom fields

You can add static keys and values to be added to all log messages.
These custom fields must be children of `<appender>`, as shown here.

```xml
<appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
  <customField>
    <key>Environment</key>
    <value>Production</value>
  </customField>
  <customField>
    <key>Location</key>
    <value>New Jerseay B1</value>
  </customField>
</appender>
```

##### Extending the appender

To change or add fields to your logs, inherit the appender and override the `ExtendValues` method.

```csharp
public class MyAppLogzioAppender : LogzioAppender
{
  protected override void ExtendValues(LoggingEvent loggingEvent, Dictionary<string, object> values)
  {
    values["logger"] = "MyPrefix." + values["logger"];
    values["myAppClientId"] = new ClientIdProvider().Get();
  }
}
```

Change your configuration to use your new appender name.
For the example above, you'd use `MyAppLogzioAppender`.

##### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

If you’re sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context. In this way, your logs will have traces data in it: `span id` and `trace id`. To enable this feature, set `<addTraceContext>true</addTraceContext>` in your configuration file or `logzioAppender.AddTraceContext(true);` in your code. For example:

```csharp
using log4net;
using log4net.Core;
using log4net.Repository.Hierarchy;
using Logzio.DotNet.Log4net;

namespace dotnet_log4net
{
    class Program
    {
        static void Main(string[] args)
        {
            var hierarchy = (Hierarchy)LogManager.GetRepository();
            var logger = LogManager.GetLogger(typeof(Program));
            var logzioAppender = new LogzioAppender();

            logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
            logzioAppender.AddListenerUrl("https://<<LISTENER-HOST>>:8071");
            // <-- Uncomment and edit this line to enable proxy routing: -->
            // logzioAppender.AddProxyAddress("http://your.proxy.com:port");
            // <-- Uncomment this to enable sending logs in Json format -->
            // logzioAppender.ParseJsonMessage(true);
            // <-- Uncomment these lines to enable gzip compression -->
            // logzioAppender.AddGzip(true);
            // logzioAppender.ActivateOptions();
            // logzioAppender.JsonKeysCamelCase(false)
            logzioAppender.AddTraceContext(true);
            logzioAppender.ActivateOptions();

            hierarchy.Root.AddAppender(logzioAppender);
            hierarchy.Configured = true;
            hierarchy.Root.Level = Level.All;

            logger.Info("Now I don't blame him 'cause he run and hid");
            logger.Info("But the meanest thing he ever did");
            logger.Info("Before he left was he went and named me Sue");

            LogManager.Shutdown();
        }
    }
}
```


### NLog

**Before you begin, you'll need**:

* NLog 4.5.0 or higher
* .NET Core SDK version 2.0 or higher
* .NET Framework version 4.6.1 or higher


#### Add the dependency to your project

If you're on Windows, navigate to your project's folder in the command line, and run this command to install the dependency.

```
Install-Package Logzio.DotNet.NLog
```

If you’re on a Mac or Linux machine, you can install the package using Visual Studio. **Select Project > Add NuGet Packages...**, and then search for `Logzio.DotNet.NLog`.

#### Configure the appender

You can configure the appender in a configuration file or directly in the code.
Use the samples in the code blocks below as a starting point, and replace them with a configuration that matches your needs. See [NLog documentation 🔗](https://github.com/NLog/NLog/wiki/Configuration-file) to learn more about configuration options.

For a complete list of options, see the configuration parameters below the code blocks.👇

##### Option 1: In a configuration file

```xml
<nlog>
    <extensions>
	<add assembly="Logzio.DotNet.NLog"/>
    </extensions>
    <targets>
	<!-- parameters are shown here with their default values.
	Other than the token, all of the fields are optional and can be safely omitted.
        -->

	<target name="logzio" type="Logzio"
		token="<<SHIPPING-TOKEN>>"
		logzioType="nlog"
		listenerUrl="<<LISTENER-HOST>>:8071"
                <!--Optional proxy server address:
                proxyAddress = "http://your.proxy.com:port" -->
		bufferSize="100"
		bufferTimeout="00:00:05"
		retriesMaxAttempts="3"
		retriesInterval="00:00:02"
		includeEventProperties="true"
		useGzip="false"
		debug="false"
		jsonKeysCamelCase="false"
		addTraceContext="false"
		<!-- parseJsonMessage="true"-->
	>
		<contextproperty name="host" layout="${machinename}" />
		<contextproperty name="threadid" layout="${threadid}" />
	</target>
    </targets>
    <rules>
	<logger name="*" minlevel="Info" writeTo="logzio" />
    </rules>
</nlog>
```

##### Option 2: In the code

```csharp
var config = new LoggingConfiguration();

// Replace these parameters with your configuration
var logzioTarget = new LogzioTarget {
    Name = "Logzio",
    Token = "<<SHIPPING-TOKEN>>",
    LogzioType = "nlog",
    ListenerUrl = "<<LISTENER-HOST>>:8071",
    BufferSize = 100,
    BufferTimeout = TimeSpan.Parse("00:00:05"),
    RetriesMaxAttempts = 3,
    RetriesInterval = TimeSpan.Parse("00:00:02"),
    Debug = false,
    JsonKeysCamelCase = false,
    AddTraceContext = false,
    // ParseJsonMessage = true,
    // ProxyAddress = "http://your.proxy.com:port"
};

config.AddRule(LogLevel.Debug, LogLevel.Fatal, logzioTarget);
LogManager.Configuration = config;
```

###### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | Your [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `nlog` |
| bufferSize | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| bufferTimeout | Maximum time to wait for more log lines, as _hh:mm:ss.fff_. | `00:00:05` |
| retriesMaxAttempts | Maximum number of attempts to connect to Logz.io. | `3` |
| retriesInterval | Time to wait between retries, as _hh:mm:ss.fff_. | `00:00:02` |
| debug | To print debug messages to the console and trace log, `true`. Otherwise, `false`. | `false` |
| parseJsonMessage | To parse your message as JSON format, add this field and set it to `true`. | `false` |
| proxyAddress | Proxy address to route your logs through. | `None` |
| jsonKeysCamelCase | If you have custom fields keys that start with a capital letter and want to see the fields with a capital letter in Logz.io, set this field to true. | `false` |
| addTraceContext | If want to add trace context to each log, set this field to true. | `false` |

###### Code sample

```csharp
using System;
using System.IO;
using Logzio.DotNet.NLog;
using NLog;
using NLog.Config;
using NLog.Fluent;

namespace LogzioNLogSampleApplication
{
  public class Program
  {
    static void Main(string[] args)
    {
      var logger = LogManager.GetCurrentClassLogger();

      logger.Info()
        .Message("If you'll be my bodyguard")
        .Property("iCanBe", "your long lost pal")
        .Property("iCanCallYou", "Betty, and Betty when you call me")
        .Property("youCanCallMe", "Al")
        .Write();

      LogManager.Shutdown();
    }
  }
}
```

##### Include context properties

You can configure the target to include your own custom values when forwarding logs to Logz.io. For example:

```xml
<nlog>
  <variable name="site" value="New Zealand" />
  <variable name="rings" value="one" />
  <target name="logzio" type="Logzio" token="<<LOG-SHIPPING-TOKEN>>">
    <contextproperty name="site" layout="${site}" />
    <contextproperty name="rings" layout="${rings}" />
  </target>
</nlog>
```

##### Extending the appender

To change or add fields to your logs, inherit the appender and override the `ExtendValues` method.

```csharp
[Target("MyAppLogzio")]
public class MyAppLogzioTarget : LogzioTarget
{
  protected override void ExtendValues(LogEventInfo logEvent, Dictionary<string, object> values)
  {
    values["logger"] = "MyPrefix." + values["logger"];
    values["myAppClientId"] = new ClientIdProvider().Get();
  }
}
```

Change your configuration to use your new target. For the example above, you'd use `MyAppLogzio`.

##### Json Layout

When using 'JsonLayout' set the name of the attribute to **other than** 'message'. for example:

```xml
<layout type="JsonLayout" includeAllProperties="true">
 <attribute name="msg"  layout="${message}" encode="false"/>
</layout>
```

##### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

If you’re sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context. In this way, your logs will have traces data in it: `span id` and `trace id`. To enable this feature, set `addTraceContext="true"` in your configuration file or `AddTraceContext = true` in your code. For example:

```csharp
var config = new LoggingConfiguration();

// Replace these parameters with your configuration
var logzioTarget = new LogzioTarget {
    Name = "Logzio",
    Token = "<<SHIPPING-TOKEN>>",
    LogzioType = "nlog",
    ListenerUrl = "<<LISTENER-HOST>>:8071",
    BufferSize = 100,
    BufferTimeout = TimeSpan.Parse("00:00:05"),
    RetriesMaxAttempts = 3,
    RetriesInterval = TimeSpan.Parse("00:00:02"),
    Debug = false,
    JsonKeysCamelCase = false,
    AddTraceContext = true,
    // ParseJsonMessage = true,
    // ProxyAddress = "http://your.proxy.com:port"
};

config.AddRule(LogLevel.Debug, LogLevel.Fatal, logzioTarget);
LogManager.Configuration = config;
```




### Loggerfactiry

**Before you begin, you'll need**:

* log4net 2.0.8 or higher
* .NET Core SDK version 2.0 or higher
* .NET Framework version 4.6.1 or higher



#### Add the dependency to your project

If you're on Windows, navigate to your project's folder in the command line, and run these commands to install the dependencies.

```
Install-Package Logzio.DotNet.Log4net
```

```
Install-Package Microsoft.Extensions.Logging.Log4Net.AspNetCore
```

If you're on a Mac or Linux machine, you can install the package using Visual Studio. Select **Project > Add NuGet Packages...**, and then search for `Logzio.DotNet.Log4net` and `Microsoft.Extensions.Logging.Log4Net.AspNetCore`.

#### Configure the appender

You can configure the appender in a configuration file or directly in the code.
Use the samples in the code blocks below as a starting point, and replace them with a configuration that matches your needs. See [log4net documentation 🔗](https://github.com/apache/logging-log4net) to learn more about configuration options.

For a complete list of options, see the configuration parameters below the code blocks.👇

###### Option 1: In a configuration file

```xml
<log4net>
    <appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
    	<!--
		Required fields
	-->
	<!-- Your Logz.io API token -->
	<token><<LOG-SHIPPING-TOKEN>></token>

	<!--
		Optional fields (with their default values)
	-->
	<!-- The type field will be added to each log message, making it
	easier for you to differ between different types of logs. -->
    	<type>log4net</type>
	<!-- The URL of the Lgz.io listener -->
    	<listenerUrl>https://<<LISTENER-HOST>>:8071</listenerUrl>
        <!--Optional proxy server address:
        proxyAddress = "http://your.proxy.com:port" -->
	<!-- The maximum number of log lines to send in each bulk -->
    	<bufferSize>100</bufferSize>
	<!-- The maximum time to wait for more log lines, in a hh:mm:ss.fff format -->
    	<bufferTimeout>00:00:05</bufferTimeout>
	<!-- If connection to Logz.io API fails, how many times to retry -->
    	<retriesMaxAttempts>3</retriesMaxAttempts>
    	<!-- Time to wait between retries, in a hh:mm:ss.fff format -->
	<retriesInterval>00:00:02</retriesInterval>
	<!-- Set the appender to compress the message before sending it -->
	<gzip>true</gzip>
	<!-- Enable the appender's internal debug logger (sent to the console output and trace log) -->
	<debug>false</debug>
        <!-- Set to true if you want json keys in Logz.io to be in camel case. The default is false. -->
        <jsonKeysCamelCase>false</jsonKeysCamelCase>
        <!-- Add trace context (traceId and spanId) to each log. The default is false -->
        <addTraceContext>false</addTraceContext>
    </appender>

    <root>
    	<level value="INFO" />
    	<appender-ref ref="LogzioAppender" />
    </root>
</log4net>
```

###### Option 2: In the code

```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
// Uncomment and edit this line to enable proxy routing:
// logzioAppender.AddProxyAddress("http://your.proxy.com:port");
// Uncomment these lines to enable gzip compression
// logzioAppender.AddGzip(true);
// logzioAppender.ActivateOptions();
// logzioAppender.JsonKeysCamelCase(false);
// logzioAppender.AddTraceContext(false);
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```

###### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `log4net` |
| bufferSize | Maximum number of messages the logger will accumulate before sending them all in bulk. | `100` |
| bufferTimeout | Maximum time to wait for more log lines, as _hh:mm:ss.fff_. | `00:00:05` |
| retriesMaxAttempts | Maximum number of attempts to connect to Logz.io. | `3` |
| retriesInterval | Time to wait between retries, as _hh:mm:ss.fff_. | `00:00:02` |
| gzip | To compress the data before shipping, `true`. Otherwise, `false`. | `false` |
| debug | To print debug messages to the console and trace log, `true`. Otherwise, `false`. | `false`
| parseJsonMessage | To parse your message as JSON format, add this field and set it to `true`. | `false` |
| proxyAddress | Proxy address to route your logs through. | `None` |
| jsonKeysCamelCase | If you have custom fields keys that start with capital letter and want to see the fields with capital letter in Logz.io, set this field to true. | `false` |
| addTraceContext | If want to add trace context to each log, set this field to true. | `false` |

###### Code sample

###### ASP.NET Core

Update Startup.cs file in Configure method to include the Log4Net middleware as in the code below.

```csharp
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILoggerFactory loggerFactory)
    {
        ...

        loggerFactory.AddLog4Net();

        ...
    }
```

In the Controller, add Data Member and Constructor, as in the code below.

```csharp
    private readonly ILoggerFactory _loggerFactory;

    public ExampleController(ILoggerFactory loggerFactory, ...)
        {
            _loggerFactory = loggerFactory;

            ...
        }
```

In the Controller methods:

```csharp
    [Route("<PUT_HERE_YOUR_ROUTE>")]
    public ActionResult ExampleMethod()
    {
        var logger = _loggerFactory.CreateLogger<ExampleController>();
        var logRepository = LogManager.GetRepository(Assembly.GetEntryAssembly());

        // Replace "App.config" with the config file that holds your log4net configuration
        XmlConfigurator.Configure(logRepository, new FileInfo("log4net.config"));

        logger.LogInformation("Hello");
        logger.LogInformation("Is it me you looking for?");

        LogManager.Shutdown();

        return Ok();
    }
```

###### .NET Core Desktop Application

```csharp
    using System.IO;
    using System.Reflection;
    using log4net;
    using log4net.Config;
    using Microsoft.Extensions.Logging;

    namespace LoggerFactoryAppender
    {
        class Program
        {
            static void Main(string[] args)
            {
                ILoggerFactory loggerFactory = new LoggerFactory();
                loggerFactory.AddLog4Net();

                var logger = loggerFactory.CreateLogger<Program>();
                var logRepository = LogManager.GetRepository(Assembly.GetEntryAssembly());

                // Replace "App.config" with the config file that holds your log4net configuration
                XmlConfigurator.Configure(logRepository, new FileInfo("log4net.config"));

                logger.LogInformation("Hello");
                logger.LogInformation("Is it me you looking for?");

                LogManager.Shutdown();
            }
        }
    }
```


##### Custom fields

You can add static keys and values to all log messages.
These custom fields must be children of `<appender>`, as shown in the code below.

```xml
<appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
  <customField>
    <key>Environment</key>
    <value>Production</value>
  </customField>
  <customField>
    <key>Location</key>
    <value>New Jerseay B1</value>
  </customField>
</appender>
```

#### Extending the appender

To change or add fields to your logs, inherit the appender and override the `ExtendValues` method.

```csharp
public class MyAppLogzioAppender : LogzioAppender
{
  protected override void ExtendValues(LoggingEvent loggingEvent, Dictionary<string, object> values)
  {
    values["logger"] = "MyPrefix." + values["logger"];
    values["myAppClientId"] = new ClientIdProvider().Get();
  }
}
```

Change your configuration to use your new appender name.
For the example above, you'd use `MyAppLogzioAppender`.

##### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

If you’re sending traces with OpenTelemetry instrumentation (auto or manual), you can correlate your logs with the trace context. In this way, your logs will have traces data in it: `span id` and `trace id`. To enable this feature, set `addTraceContext="true"` in your configuration file or `AddTraceContext = true` in your code. For example:

```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
// Uncomment and edit this line to enable proxy routing:
// logzioAppender.AddProxyAddress("http://your.proxy.com:port");
// Uncomment these lines to enable gzip compression
// logzioAppender.AddGzip(true);
// logzioAppender.ActivateOptions();
// logzioAppender.JsonKeysCamelCase(false);
logzioAppender.AddTraceContext(true);
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```


### Serilog

:::note
This integration is based on [Serilog.Sinks.Logz.Io repository](https://github.com/serilog-contrib/Serilog.Sinks.Logz.Io). Refer to this repo for further usage and settings information.
:::


**Before you begin, you'll need**:

* .NET Core SDK version 2.0 or higher
* .NET Framework version 4.6.1 or higher


#### Install the Logz.io Serilog sink

Install `Serilog.Sinks.Logz.Io` using Nuget or by running the following command in the Package Manager Console:

```shell
PM> Install-Package Serilog.Sinks.Logz.Io
```

#### Configure the sink

There are 2 ways to use Serilog:

1. Using a configuration file
2. In the code

###### Using a configuration file

Create `appsettings.json` file and copy the following configuration:

```json
{
  "Serilog": {
    "MinimumLevel": "Warning",
    "WriteTo": [
      {
        "Name": "LogzIoDurableHttp",
        "Args": {
          "requestUri": "https://<<LISTENER-HOST>>:8071/?type=<<TYPE>>&token=<<LOG-SHIPPING-TOKEN>>"
        }
      }
    ]
  }
}
```

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

Replace `<<TYPE>` with the type that you want to assign to your logs. You will use this value to identify these logs in Logz.io.

Add the following code to use the configuration and create logs:

* Using Serilog.Settings.Configuration and Microsoft.Extensions.Configuration.Json packages

```csharp
using System.IO;
using System.Threading;
using Microsoft.Extensions.Configuration;
using Serilog;

namespace Example
{
    class Program
    {
        static void Main(string[] args)
        {
            var configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json")
                .Build();

            var logger = new LoggerConfiguration()
                .ReadFrom.Configuration(configuration)
                .CreateLogger();

            logger.Information("Hello. Is it me you looking for?");
            Thread.Sleep(5000);     // gives the log enough time to be sent to Logz.io
        }
    }
}
```


###### In the code


```csharp
using System.Threading;
using Serilog;
using Serilog.Sinks.Logz.Io;

namespace Example
{
    class Program
    {
        static void Main(string[] args)
        {
            ILogger logger = new LoggerConfiguration()
                .WriteTo.LogzIoDurableHttp(
                    "https://<<LISTENER-HOST>>:8071/?type=<<TYPE>>&token=<<LOG-SHIPPING-TOKEN>>",
                    logzioTextFormatterOptions: new LogzioTextFormatterOptions
                    {
                        BoostProperties = true,
                        LowercaseLevel = true,
                        IncludeMessageTemplate = true,
                        FieldNaming = LogzIoTextFormatterFieldNaming.CamelCase,
                        EventSizeLimitBytes = 261120,
                    })
                .MinimumLevel.Verbose()
                .CreateLogger();

            logger.Information("Hello. Is it me you looking for?");
            Thread.Sleep(5000);     // gives the log enough time to be sent to Logz.io
        }
    }
}
```

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

Replace `<<TYPE>` with the type that you want to assign to your logs. You will use this value to identify these logs in Logz.io.


## Metrics

### Kubernetes

Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts. This integration allows you to collect and ship diagnostic metrics of your .NET application in Kubernetes to Logz.io, using dotnet-monitor and OpenTelemetry. logzio-dotnet-monitor runs as a sidecar in the same pod as the .NET application.

###### Sending metrics from nodes with taints

If you want to ship metrics from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:
  
```yaml
tolerations:
- key: 
  operator: 
  value: 
  effect: 
```
  
To determine if a node uses taints as well as to display the taint keys, run:
  
```
kubectl get nodes -o json | jq ".items[]|{name:.metadata.name, taints:.spec.taints}"
```

  

#### Standard configuration

 

##### Select the namespace

This integration will be deployed in the namespace you set in values.yaml. The default namespace for this integration is logzio-dotnet-monitor.

To select a different namespace, run:

```shell
kubectl create namespace <<NAMESPACE>>
```

* Replace `<<NAMESPACE>>` with the name of your namespace.


##### Add `logzio-helm` repo
  
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```


###### Run the Helm deployment code

```shell
helm install -n <<NAMESPACE>> \
--set secrets.logzioURL='<<LISTENER-HOST>>:8053' \
--set secrets.logzioToken='<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>' \
--set-file dotnetAppContainers='<<DOTNET_APP_CONTAINERS_FILE>>' \
logzio-dotnet-monitor logzio-helm/logzio-dotnet-monitor
```

* Replace `<<NAMESPACE>>` with the namespace you selected for this integration. The default value is `default`.
{@include: ../../_include/log-shipping/listener-var.html} {@include: ../../_include/log-shipping/log-shipping-token.html}
* Replace `<<DOTNET_APP_CONTAINERS_FILE>>` with your .NET application containers file. Make sure your main .NET application container has the following volumeMount:

```yaml
volumeMounts:
  - mountPath: /tmp
    name: diagnostics
```


##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, then open [Logz.io](https://app.logz.io/). You can search for your metrics in Logz.io by searching `{job="dotnet-monitor-collector"}`

 


####  Customizing Helm chart parameters


##### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install` or `--set-file key=value[,key=value]`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

##### Customization parameters

| Parameter | Description | Default |
|---|---|---|
| `nameOverride` | Overrides the Chart name for resources. | `""` |
| `fullnameOverride` | Overrides the full name of the resources. | `""` |
| `apiVersions.deployment` | Deployment API version. | `apps/v1` |
| `apiVersions.configmap` | Configmap API version. | `v1` |
| `apiVersions.secret` | Secret API version. | `v1` |
| `namespace` | Chart's namespace. | `logzio-dotnet-monitor` |
| `replicaCount` | The number of replicated pods, the deployment creates. | `1` |
| `labels` | Pod's labels. | `{}` |
| `annotations` | Pod's annotations. | `{}` |
| `customSpecs` | Custom spec fields to add to the deployment. | `{}` |
| `dotnetAppContainers` | List of your .NET application containers to add to the pod. | `[]` |
| `logzioDotnetMonitor.name` | The name of the container that collects and ships diagnostic metrics of your .NET application to Logz.io (sidecar) | `logzio-dotnet-monitor` |
| `logzioDotnetMonitor.image.name` | Name of the image that is going to run in `logzioDotnetMonitor.name` container | `logzio/logzio-dotnet-monitor` |
| `logzioDotnetMonitor.image.tag` | The tag of the image that is going to run in `logzioDotnetMonitor.name` container | `latest` |
| `logzioDotnetMonitor.ports` | List of ports the `logzioDotnetMonitor.name` container exposes | `52325` |
| `tolerations` | List of tolerations to applied to the pod. | `[]` | 
| `customVolumes` | List of custom volumes to add to deployment. | `[]` |
| `customResources` | Custom resources to add to helm chart deployment (make sure to separate each resource with `---`). | `{}` |
| `secrets.logzioURL` | Secret with your Logz.io listener url. | `https://listener.logz.io:8053` |
| `secrets.logzioToken` | Secret with your Logz.io metrics shipping token. | `""` |
| `configMap.dotnetMonitor` | The dotnet-monitor configuration. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/dotnet-monitor/values.yaml). |
| `configMap.opentelemetry` | The opentelemetry configuration. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/dotnet-monitor/values.yaml). |


* To get additional information about dotnet-monitor configuration, click [here](https://github.com/dotnet/dotnet-monitor/blob/main/documentation/api/metrics.md).
* To see well-known providers and their counters, click [here](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/available-counters).

#### Uninstalling the Chart

The Uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `dotnet-monitor-collector` deployment, use the following command:

```shell
helm uninstall dotnet-monitor-collector
```

For troubleshooting this solution, see our [.NET with helm troubleshooting guide](https://docs.logz.io/user-guide/infrastructure-monitoring/troubleshooting/dotnet-helm-troubleshooting.html).

 
### SDK


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

{@include: ../../_include/log-shipping/listener-var.html} For HTTPS communication, use port 8053. For HTTP communication, use port 8052.

{@include: ../../_include/metric-shipping/replace-metrics-token.html}


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

{@include: ../../_include/log-shipping/listener-var.html} For HTTPS communication, use port 8053. For HTTP communication, use port 8052.

{@include: ../../_include/metric-shipping/replace-metrics-token.html}


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

* {@include: ../../_include/log-shipping/listener-var.html} For HTTPS communication use port 8053. For HTTP communication use port 8052.
* {@include: ../../_include/metric-shipping/replace-metrics-token.html}
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
  


## Traces

This integration enables you to send traces from your instrumented applications running in Docker. This is achieved by using a dedicated Logz.io OpenTelemetry collector deployed in the same Docker network as your application. This collector configuration can collect traces from:

* OpenTelemetry
* Zipkin
* Jaeger
* OpenCensus 


**Before you begin, you'll need**:

* An instrumented application running in a Docker network
* An active account with Logz.io
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


In the same Docker network as your application:

{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}

Run the application to generate traces.


### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).

### Troubleshooting

#### OpenTelemetry instrumentation 
For troubleshooting the OpenTelemetry instrumentation, see our [OpenTelemetry troubleshooting guide](/docs/user-guide/distributed-tracing/troubleshooting/otel-troubleshooting).


