---
id: dotnet
title: .NET
overview: .NET is an open-source, managed computer software framework for Windows, Linux, and MacOS operating systems. Integrate .NET with Logz.io to monitor logs, metrics, and traces, identify when issues occur, easily troubleshoot them, and improve your applications and services. 
product: ['logs', 'metrics', 'tracing']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
recommendedFor: ['Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/dotnet.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3lGo7AE5839jDfkAYU8r21']
metrics_alerts: ['1ALFpmGPygXKWi18TDoO5C']
drop_filter: []
toc_min_heading_level: 2
toc_max_heading_level: 3
---




## Logs

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-dotnet/)
:::


<Tabs queryString="current-lib">
  <TabItem value="log4net" label="log4net" default>

**Before you begin, you'll need**:

* log4net 2.0.8+.
* .NET Core SDK version 2.0+.
* .NET Framework version 4.6.1+.


### Add the dependency

On Windows, navigate to your project folder, and run the following command:

```
Install-Package Logzio.DotNet.Log4net
```

On Mac or Linux, open Visual Studio, navigate to **Project > Add NuGet Packages...**, search and install `Logzio.DotNet.Log4net`.


### Configure the appender in a configuration file

Use the sample configuration and edit it according to your needs. View [log4net documentation](https://github.com/apache/logging-log4net) for additional options.


```xml
<log4net>
    <appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
	<token><<LOG-SHIPPING-TOKEN>></token>
    	<type>log4net</type>
    	<listenerUrl>https://<<LISTENER-HOST>>:8071</listenerUrl>
    	<bufferSize>100</bufferSize>
    	<bufferTimeout>00:00:05</bufferTimeout>
    	<retriesMaxAttempts>3</retriesMaxAttempts>
	<retriesInterval>00:00:02</retriesInterval>
	<gzip>true</gzip>
	<debug>false</debug>
	<jsonKeysCamelCase>false</jsonKeysCamelCase>
	<addTraceContext>false</addTraceContext>
	<useStaticHttpClient>false</useStaticHttpClient>

    </appender>

    <root>
    	<level value="INFO" />
    	<appender-ref ref="LogzioAppender" />
    </root>
</log4net>
```


To enable JSON format logging, add the following to your configuration file:

`<parseJsonMessage>true</parseJsonMessage>`
	

Next, reference the configuration file in your code as shown in the example [here](https://github.com/logzio/logzio-dotnet/blob/master/sample-applications/LogzioLog4netSampleApplication/Program.cs).


**Run the code:**

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


### Configure the appender in the code

Use the sample configuration and edit it according to your needs. View [log4net documentation](https://github.com/apache/logging-log4net) for additional options.



```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```

Customize your code by adding the following:


| Why? | What? |
|------|-------|
| Enable proxy routing | `logzioAppender.AddProxyAddress("http://your.proxy.com:port");` |
| Enable sending logs in JSON format | `logzioAppender.ParseJsonMessage(true);` |
| Enable gzip compression | `logzioAppender.AddGzip(true);` , `logzioAppender.ActivateOptions();` , `logzioAppender.JsonKeysCamelCase(false);` , `logzioAppender.AddTraceContext(false);` , `logzioAppender.UseStaticHttpClient(false);` |



<!-- #### Run the code

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
-->

### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | Your [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `log4net` |
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
| useStaticHttpClient | If want to use the same static HTTP/s client for sending logs, set this field to true. | `false` |



### Custom fields

Add static keys and values to all log messages by including these custom fields under `<appender>`, as shown:


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

### Extending the appender

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

Update your configuration to use the new appender name, such as `MyAppLogzioAppender`.

### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

To correlate logs with trace context in OpenTelemetry, set `<addTraceContext>true</addTraceContext>` in your configuration file or use `logzioAppender.AddTraceContext(true);` in your code. This adds `span id` and `trace id` to your logs. For example:


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

### Serverless platforms

For serverless functions, call the appender's flush method at the end to ensure logs are sent before execution finishes. Create a static appender in Startup.cs with `UseStaticHttpClient` set to `true` for consistent invocations.

For example: 

*Startup.cs*
```csharp
using Microsoft.Azure.Functions.Extensions.DependencyInjection;
using log4net;
using log4net.Repository.Hierarchy;
using Logzio.DotNet.Log4net;

[assembly: FunctionsStartup(typeof(LogzioLog4NetSampleApplication.Startup))]

namespace LogzioLog4NetSampleApplication
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            var hierarchy = (Hierarchy)LogManager.GetRepository();
            var logzioAppender = new LogzioAppender();
            logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
            logzioAppender.AddListenerUrl("https://<<LISTENER-HOST>>:8071");
            logzioAppender.ActivateOptions();
            logzioAppender.UseStaticHttpClient(true);
            hierarchy.Root.AddAppender(logzioAppender);
            hierarchy.Configured = true;
        }
    }
}

```

*FunctionApp.cs*
```csharp
using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Extensions.Logging;
using log4net;
using MicrosoftLogger = Microsoft.Extensions.Logging.ILogger;

namespace LogzioLog4NetSampleApplication
{
    public class TimerTriggerCSharpLog4Net
    {
        
        private static readonly ILog logger = LogManager.GetLogger(typeof(TimerTriggerCSharpLog4Net));

        [FunctionName("TimerTriggerCSharpLog4Net")]
        public void Run([TimerTrigger("*/30 * * * * *")]TimerInfo myTimer, MicrosoftLogger msLog)
        {
            msLog.LogInformation($"Log4Net C# Timer trigger function executed at: {DateTime.Now}");

            logger.Info("Now I don't blame him 'cause he run and hid");
            logger.Info("But the meanest thing he ever did");
            logger.Info("Before he left was he went and named me Sue");
            LogManager.Flush(5000);

            msLog.LogInformation($"Log4Net C# Timer trigger function finished at: {DateTime.Now}");
        }
    }
}
```
</TabItem>
  <TabItem value="NLog" label="NLog">


**Before you begin, you'll need**:

* NLog 4.5.0+.
* .NET Core SDK version 2.0+.
* .NET Framework version 4.6.1+.



### Add the dependency

On Windows, navigate to your project folder, and run the following command:


```
Install-Package Logzio.DotNet.NLog
```

On Mac or Linux, open Visual Studio, navigate to **Project > Add NuGet Packages...**, search and install `Logzio.DotNet.Log4net`.


### Configure the appender in a configuration file

Use the sample configuration and edit it according to your needs. View [NLog documentation](https://github.com/NLog/NLog/wiki/Configuration-file) for additional options.



```xml
<nlog>
    <extensions>
        <add assembly="Logzio.DotNet.NLog"/>
    </extensions>
    <targets>
        <!-- Parameters are shown with their default values. 
        Except for the token, all fields are optional and can be omitted. -->
        <target name="logzio" type="Logzio"
            token="<<LOG-SHIPPING-TOKEN>>"
            logzioType="nlog"
            listenerUrl="<<LISTENER-HOST>>:8071"
            bufferSize="100"
            bufferTimeout="00:00:05"
            retriesMaxAttempts="3"
            retriesInterval="00:00:02"
            includeEventProperties="true"
            useGzip="false"
            debug="false"
            jsonKeysCamelCase="false"
            addTraceContext="false">
            <!-- Optional proxy server address:
                 proxyAddress="http://your.proxy.com:port" -->
            <!-- parseJsonMessage="true" -->
            <!-- useStaticHttpClient="true" -->
            <contextproperty name="host" layout="${machinename}" />
            <contextproperty name="threadid" layout="${threadid}" />
        </target>
    </targets>
    <rules>
        <logger name="*" minlevel="Info" writeTo="logzio" />
    </rules>
</nlog>
```

### Configure the appender in the code

Use the sample configuration and edit it according to your needs.

```csharp
var config = new LoggingConfiguration();
var logzioTarget = new LogzioTarget {
    Name = "Logzio",
    Token = "<<LOG-SHIPPING-TOKEN>>",
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
    // ProxyAddress = "http://your.proxy.com:port",
    // UseStaticHttpClient = false,
};

config.AddRule(LogLevel.Debug, LogLevel.Fatal, logzioTarget);
LogManager.Configuration = config;
```

### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | Your [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `nlog` |
| bufferSize | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| bufferTimeout | Maximum time to wait for more log lines, as _hh:mm:ss.fff_. | `00:00:05` |
| retriesMaxAttempts | Maximum number of attempts to connect to Logz.io. | `3` |
| retriesInterval | Time to wait between retries, as _hh:mm:ss.fff_. | `00:00:02` |
| debug | To print debug messages to the console and trace log, `true`. Otherwise, `false`. | `false` |
| parseJsonMessage | To parse your message as JSON format, add this field and set it to `true`. | `false` |
| proxyAddress | Proxy address to route your logs through. | `None` |
| jsonKeysCamelCase | If you have custom fields keys that start with a capital letter and want to see the fields with a capital letter in Logz.io, set this field to true. | `false` |
| addTraceContext | If want to add trace context to each log, set this field to true. | `false` |
| useStaticHttpClient | If want to use the same static HTTP/s client for sending logs, set this field to true. | `false` |

**Code sample**

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

### Include context properties

Configure the target to include custom values when forwarding logs to Logz.io. For example:


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

### Extending the appender

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

Update your configuration to use the new appender name, such as `MyAppLogzio`.



### JSON Layout

When using `JsonLayout`, set the attribute name to something **other than** 'message'. For example:



```xml
<layout type="JsonLayout" includeAllProperties="true">
 <attribute name="msg"  layout="${message}" encode="false"/>
</layout>
```

### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

To correlate logs with trace context in OpenTelemetry (auto or manual), set `addTraceContext="true"` in your configuration file or `AddTraceContext = true` in your code. This adds `span id` and `trace id` to your logs. For example:



```csharp
var config = new LoggingConfiguration();

// Replace these parameters with your configuration
var logzioTarget = new LogzioTarget {
    Name = "Logzio",
    Token = "<<LOG-SHIPPING-TOKEN>>",
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

### Serverless platforms

For serverless functions, call the appender's flush method at the end to ensure logs are sent before execution finishes. Create a static appender in Startup.cs with `UseStaticHttpClient` flag set to `true` for consistent invocations.


**Azure serverless function code sample**

*Startup.cs*

```csharp
using Microsoft.Azure.Functions.Extensions.DependencyInjection;
using Logzio.DotNet.NLog;
using NLog;
using NLog.Config;
using System;

[assembly: FunctionsStartup(typeof(LogzioNLogSampleApplication.Startup))]

namespace LogzioNLogSampleApplication
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            var config = new LoggingConfiguration();

            // Replace these parameters with your configuration
            var logzioTarget = new LogzioTarget
            {
                Name = "Logzio",
                Token = "<<LOG-SHIPPING-TOKEN>>",
                LogzioType = "nlog",
                ListenerUrl = "https://<<LISTENER-HOST>>:8071",
                BufferSize = 100,
                BufferTimeout = TimeSpan.Parse("00:00:05"),
                RetriesMaxAttempts = 3,
                RetriesInterval = TimeSpan.Parse("00:00:02"),
                Debug = false,
                JsonKeysCamelCase = false,
                AddTraceContext = false,
                UseStaticHttpClient = true,
                // ParseJsonMessage = true,
                // ProxyAddress = "http://your.proxy.com:port",
            };

            config.AddRule(NLog.LogLevel.Debug, NLog.LogLevel.Fatal, logzioTarget);
            LogManager.Configuration = config;
        }
    }
}
```

*FunctionApp.cs*

```csharp
using System;
using Microsoft.Azure.WebJobs;
using NLog;
using Microsoft.Extensions.Logging;
using MicrosoftLogger = Microsoft.Extensions.Logging.ILogger;

namespace LogzioNLogSampleApplication
{
    public class TimerTriggerCSharpNLog
    {
        private static readonly Logger nLog = LogManager.GetCurrentClassLogger();

        [FunctionName("TimerTriggerCSharpNLog")]
        public void Run([TimerTrigger("*/30 * * * * *")]TimerInfo myTimer, MicrosoftLogger msLog)
        {
            msLog.LogInformation($"NLogzio C# Timer trigger function executed at: {DateTime.Now}");

            nLog.WithProperty("iCanBe", "your long lost pal")
                .WithProperty("iCanCallYou", "Betty, and Betty when you call me")
                .WithProperty("youCanCallMe", "Al")
                .Info("If you'll be my bodyguard");
            // Call Flush method before function trigger finishes
            LogManager.Flush(5000);
        }
    }
}
```

</TabItem>
  <TabItem value="LoggerFactory" label="LoggerFactory">

**Before you begin, you'll need**:

* log4net 2.0.8+.
* .NET Core SDK version 2.0+.
* .NET Framework version 4.6.1+.



### Add the dependency

On Windows, navigate to your project folder, and run the following command:

```
Install-Package Logzio.DotNet.Log4net
```

```
Install-Package Microsoft.Extensions.Logging.Log4Net.AspNetCore
```

On Mac or Linux, open Visual Studio, navigate to **Project > Add NuGet Packages...**, search and install Logzio.DotNet.Log4net and `Microsoft.Extensions.Logging.Log4Net.AspNetCore`.



### Configure the appender in a configuration file

Use the sample configuration and edit it according to your needs. View [log4net documentation](https://github.com/apache/logging-log4net) for additional options.




```xml
<log4net>
    <appender name="LogzioAppender" type="Logzio.DotNet.Log4net.LogzioAppender, Logzio.DotNet.Log4net">
	<token><<LOG-SHIPPING-TOKEN>></token>
    	<type>log4net</type>
    	<listenerUrl>https://<<LISTENER-HOST>>:8071</listenerUrl>
    	<bufferSize>100</bufferSize>
    	<bufferTimeout>00:00:05</bufferTimeout>
    	<retriesMaxAttempts>3</retriesMaxAttempts>
	<retriesInterval>00:00:02</retriesInterval>
	<gzip>true</gzip>
	<debug>false</debug>
        <jsonKeysCamelCase>false</jsonKeysCamelCase>
        <addTraceContext>false</addTraceContext>
	    <useStaticHttpClient>false</useStaticHttpClient>

    </appender>

    <root>
    	<level value="INFO" />
    	<appender-ref ref="LogzioAppender" />
    </root>
</log4net>
```

### Configure the appender in the code

Use the sample configuration and edit it according to your needs. View [log4net documentation](https://github.com/apache/logging-log4net) for additional options.




```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```

Customize your code by adding the following:


| Why? | What? |
|------|-------|
| Enable proxy routing | `logzioAppender.AddProxyAddress("http://your.proxy.com:port");` |
| Enable gzip compression | `logzioAppender.AddGzip(true);` , `logzioAppender.ActivateOptions();` , `logzioAppender.JsonKeysCamelCase(false);` , `logzioAppender.AddTraceContext(false);` , `logzioAppender.UseStaticHttpClient(false);` |


### Parameters

| Parameter | Description | Default/Required |
|---|---|---|
| token | [Logz.io log shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) securely directs the data to your Logz.io account. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| listenerUrl  | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | `https://listener.logz.io:8071` |
| type | The [log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), shipped as `type` field. Used by Logz.io for consistent parsing. Can't contain spaces. | `log4net` |
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
| useStaticHttpClient | If want to use the same static HTTP/s client for sending logs, set this field to true. | `false` |


### ASP.NET Core

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

### .NET Core Desktop Application

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


### Custom fields

Add static keys and values to all log messages by including these custom fields under `<appender>`, as shown:


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

### Extending the appender

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

Update your configuration to use the new appender name, such as `MyAppLogzioAppender`.


### Add trace context

:::note
The Trace Context feature does not support .NET Standard 1.3.
:::

To correlate logs with trace context in OpenTelemetry (auto or manual), set `addTraceContext="true"` in your configuration file or `AddTraceContext = true` in your code. This adds `span id` and `trace id` to your logs. For example:


```csharp
var hierarchy = (Hierarchy)LogManager.GetRepository();
var logzioAppender = new LogzioAppender();
logzioAppender.AddToken("<<LOG-SHIPPING-TOKEN>>");
logzioAppender.AddListenerUrl("<<LISTENER-HOST>>");
logzioAppender.AddTraceContext(true);
logzioAppender.ActivateOptions();
hierarchy.Root.AddAppender(logzioAppender);
hierarchy.Root.Level = Level.All;
hierarchy.Configured = true;
```

Customize your code by adding the following:


| Why? | What? |
|------|-------|
| Enable proxy routing | `logzioAppender.AddProxyAddress("http://your.proxy.com:port");` |
| Enable sending logs in JSON format | `logzioAppender.ParseJsonMessage(true);` |
| Enable gzip compression | `logzioAppender.AddGzip(true);` , `logzioAppender.ActivateOptions();` , `logzioAppender.JsonKeysCamelCase(false);` |



### Serverless platforms

For serverless functions, call the appender's flush method at the end to ensure logs are sent before execution finishes. Create a static appender in Startup.cs with `UseStaticHttpClient` set to `true` for consistent invocations.



**Azure serverless function code sample**

*Startup.cs*

```csharp
using Microsoft.Azure.Functions.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using log4net;
using log4net.Config;
using System.IO;
using System.Reflection;
using System;
[assembly: FunctionsStartup(typeof(LogzioLoggerFactorySampleApplication.Startup))]

namespace LogzioLoggerFactorySampleApplication
{
    public class Startup : FunctionsStartup
    {
        public static ILoggerFactory LoggerFactory { get; set; }

        public override void Configure(IFunctionsHostBuilder builder)
        {
            var logRepository = LogManager.GetRepository(Assembly.GetEntryAssembly());
            string functionAppDirectory = Environment.GetEnvironmentVariable("AzureWebJobsScriptRoot");

            // Configure log4net here
            XmlConfigurator.Configure(logRepository, new FileInfo(Path.Combine(functionAppDirectory, "log4net.config")));

            var loggerFactory = new LoggerFactory();
            loggerFactory.AddLog4Net(Path.Combine(functionAppDirectory, "log4net.config")); // Use the log4net.config in the function app root directory

            LoggerFactory = loggerFactory;
        }
    }
}
```
*FunctionApp.cs*

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Extensions.Logging;
using log4net;
using System;

namespace LogzioLoggerFactorySampleApplication
{
    public class TimerTriggerCSharpLoggerFactory
    {
        private readonly ILogger _logger = Startup.LoggerFactory.CreateLogger<TimerTriggerCSharpLoggerFactory>();


        [FunctionName("TimerTriggerCSharpLoggerFactory")]
        public void Run([TimerTrigger("*/30 * * * * *")] TimerInfo myTimer)
        {
            _logger.LogInformation($"LoggerFactory C# Timer trigger function executed at: {DateTime.Now}");

            _logger.LogInformation("Hello");
            _logger.LogInformation("Is it me you looking for?");
            
            LogManager.Flush(5000);

            _logger.LogInformation($"LoggerFactory C# Timer trigger function finished at: {DateTime.Now}");

        }
    }
}
```
</TabItem>
  <TabItem value="Serilog" label="Serilog">

:::note
This integration is based on [Serilog.Sinks.Logz.Io repository](https://github.com/serilog-contrib/Serilog.Sinks.Logz.Io). Refer to this repo for further usage and settings information.
:::


**Before you begin, you'll need**:

* .NET Core SDK version 2.0+.
* .NET Framework version 4.6.1+.



### Install the Logz.io Serilog sink

Install `Serilog.Sinks.Logz.Io` via Nuget or by running this command in the Package Manager Console:

```shell
PM> Install-Package Serilog.Sinks.Logz.Io
```


### Configure the sink in a configuration file

Create an `appsettings.json` file and copy this configuration:


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

Replace `<<TYPE>>` with the log type to identify these logs in Logz.io.

Add the following code to use the configuration and create logs with `Serilog.Settings.Configuration` and `Microsoft.Extensions.Configuration.Json` packages:


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


#### Run the code: 


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

### Serverless platforms
For serverless function, create a static appender in Startup.cs to ensure each invocation uses the same appender. For Serilog integration, use `WriteTo.LogzIo()` instead of `WriteTo.LogzIoDurableHttp()` for in-memory buffering, which is best for serverless functions.


**Azure serverless function code sample**

*Startup.cs*
```csharp
using Microsoft.Azure.Functions.Extensions.DependencyInjection;
using Serilog;
using Serilog.Sinks.Logz.Io;

[assembly: FunctionsStartup(typeof(LogzioSerilogSampleApplication.Startup))]

namespace LogzioSerilogSampleApplication
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            var logzioLogger = new LoggerConfiguration()
                .WriteTo.LogzIo("<<LOG-SHIPPING-TOKEN>>", "serilog", dataCenterSubDomain: "listener", useHttps: true)
                .CreateLogger();

            // Assign the logger to the static Log class
            Log.Logger = logzioLogger;
        }
    }
}
```

*FunctionApp.cs*
```csharp
using System;
using Microsoft.Azure.WebJobs;
using Serilog;
using Microsoft.Extensions.Logging;
using MicrosoftLogger = Microsoft.Extensions.Logging.ILogger;
using Serilogger = Serilog.ILogger;
using System.Threading;

namespace LogzioSerilogSampleApplication
{
    public class TimerTriggerCSharpSeriLogzio
    {
        private static readonly Serilogger logzioLogger = Log.Logger;

        [FunctionName("TimerTriggerCSharpSeriLogzio")]
        public void Run([TimerTrigger("*/30 * * * * *")]TimerInfo myTimer, MicrosoftLogger msLog)
        {
            msLog.LogInformation($"Serilog C# Timer trigger function executed at: {DateTime.Now}");
              
            logzioLogger.Information("Hello. Is it me you're looking for?");

            msLog.LogInformation($"Serilog C# Timer trigger function finished at: {DateTime.Now}");
        }
    }
}
```

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

Replace `<<TYPE>>` with the log type to identify these logs in Logz.io.











</TabItem>
  <TabItem value="OpenTelemetry" label="OpenTelemetry">

This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites
    
- [.NET SDK](https://dotnet.microsoft.com/download/dotnet) 6+
- An ASP.NET Core application
- An active account with Logz.io

:::note
If you need an example aplication to test this integration, please refer to our [.NET OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/dotnet/logs).
:::

### Configure the instrumentation

1. Add the packages

   ```bash
   dotnet add package OpenTelemetry.Extensions.Hosting
   dotnet add package OpenTelemetry.Instrumentation.AspNetCore
   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
   ```

2. Setup the OpenTelemetry code in `Program.cs`, by adding the following lines:

   ```csharp
   using OpenTelemetry;
   using OpenTelemetry.Logs;
   using OpenTelemetry.Resources;
   using OpenTelemetry.Exporter;   
   var builder = WebApplication.CreateBuilder(args);   
   const string serviceName = "YOUR-SERVICE-NAME";
   const string logzioEndpoint = "https://otlp-listener.logz.io/v1/logs";
   const string logzioToken = "<LOG-SHIPPING-TOKEN>";   
   builder.Logging.AddOpenTelemetry(options =>
   {
       options
           .SetResourceBuilder(
               ResourceBuilder.CreateDefault()
                   .AddService(serviceName))
           .AddOtlpExporter(otlpOptions =>
           {
               otlpOptions.Endpoint = new Uri(logzioEndpoint);
               otlpOptions.Headers = $"Authorization=Bearer {logzioToken}, user-agent=logzio-dotnet-logs-otlp";
               otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;
           });
   });   
   var app = builder.Build();
   ```
   Replace `YOUR-SERVICE-NAME` with the required service name.

   {@include: ../../_include/log-shipping/log-shipping-token.md}

   Update the `listener.logz.io` parth in `https://otlp-listener.logz.io/v1/logs` with the URL for [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).

3. Run your application.

### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.


  </TabItem>
</Tabs>

## Metrics



<Tabs>
  <TabItem value="Kubernetes" label="Kubernetes" default>

Helm manages packages of preconfigured Kubernetes resources using Charts. This integration allows you to collect and ship diagnostic metrics of your .NET application in Kubernetes to Logz.io, using dotnet-monitor and OpenTelemetry. logzio-dotnet-monitor runs as a sidecar in the same pod as the .NET application.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-helm/)
:::

### Sending metrics from nodes with taints


To ship metrics from nodes with taints, ensure the taint key values are included in your DaemonSet/Deployment configuration as follows:

  
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

:::note
You need to use `Helm` client with version `v3.9.0` or above.
:::

### Standard configuration

 
**1. Select the namespace**

This integration deploys to the namespace specified in values.yaml. The default is logzio-dotnet-monitor.

To use a different namespace, run:



```shell
kubectl create namespace <<NAMESPACE>>
```

* Replace `<<NAMESPACE>>` with the name of your namespace.


**2. Add `logzio-helm` repo**
  
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```


**3. Run the Helm deployment code**

```shell
helm install -n <<NAMESPACE>> \
--set secrets.logzioURL='<<LISTENER-HOST>>:8053' \
--set secrets.logzioToken='<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>' \
--set-file dotnetAppContainers='<<DOTNET_APP_CONTAINERS_FILE>>' \
logzio-dotnet-monitor logzio-helm/logzio-dotnet-monitor 
```

* Replace `<<NAMESPACE>>` with the namespace you selected for this integration. The default value is `default`.
{@include: ../../_include/log-shipping/listener-url.html} {@include: ../../_include/log-shipping/log-shipping-token.html}
* Replace `<<DOTNET_APP_CONTAINERS_FILE>>` with your .NET application containers file. Make sure your main .NET application container has the following volumeMount:

```yaml
volumeMounts:
  - mountPath: /tmp
    name: diagnostics
```


**4. Check Logz.io for your metrics**

Allow some time for data ingestion, then open [Logz.io](https://app.logz.io/). Search for your metrics in Logz.io by searching `{job="dotnet-monitor-collector"}`

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3lGo7AE5839jDfkAYU8r21"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}
 


###  Customizing Helm chart parameters


* **Configure customization options**

    Update the Helm chart parameters using the following options:

    * Specify parameters using the `--set key=value[,key=value]` argument to `helm install` or `--set-file key=value[,key=value]`

    * Edit the `values.yaml`

    * Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

* **Customization parameters**

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

### Uninstalling the Chart

To remove all Kubernetes components associated with the chart and delete the release, use the uninstall command.

To uninstall the `dotnet-monitor-collector` deployment, run:

```shell
helm uninstall dotnet-monitor-collector
```


Encounter an issue? See our [.NET with helm troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/dotnet-helm-troubleshooting/).




</TabItem>
  <TabItem value="SDK" label="SDK">

Send custom metrics from your .NET Core application using Logzio.App.Metrics, an open-source, cross-platform .NET library for recording metrics and forwarding them to Logz.io.

These instructions show you how to:

* Create a basic custom metrics export configuration with a hardcoded Logz.io exporter.
* Create a basic custom metrics export configuration with a Logz.io exporter defined by a configuration file.
* Add advanced settings to the basic custom metrics export configuration.

  

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-app-metrics/)
:::

### Send custom metrics with a hardcoded Logz.io exporter



**Before you begin, you'll need**: 

* An application in .NET Core 3.1+.
* An active Logz.io account.


**1. Install the App.Metrics.Logzio package**


Run the following from the Package Manager Console:

```shell
Install-Package Logzio.App.Metrics
```

For manual installation, download the latest version from the NuGet Gallery.


**2. Create MetricsBuilder**

Copy and paste the following code into the function where you need to export metrics:


```csharp
var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp("<<LISTENER-HOST>>:<<PORT>>", "<<METRICS-SHIPPING-TOKEN>>")
                .Build();
```

{@include: ../../_include/log-shipping/listener-var.html} For HTTPS communication, use port 8053. For HTTP communication, use port 8052.

{@include: ../../_include/metric-shipping/replace-metrics-token.html}


**3. Create Scheduler**

To create the Scheduler, add the following code into the same function as the MetricsBuilder:

```csharp
var scheduler = new AppMetricsTaskScheduler(
                TimeSpan.FromSeconds(15),
                async () => { await Task.WhenAll(metrics.ReportRunner.RunAllAsync()); });
scheduler.Start();
```

**4. Add required metrics to your code**

* [Apdex (Application Performance Index)](https://www.app-metrics.io/getting-started/metric-types/apdex/) - Monitors end-user satisfaction.
* [Counter](https://www.app-metrics.io/getting-started/metric-types/counters/) - Tracks the number of times an event occurs.
* [Gauge](https://www.app-metrics.io/getting-started/metric-types/gauges/) - Provides an instantaneous measurement of a value that can arbitrarily increase or decrease (e.g., CPU usage).
* [Histogram](https://www.app-metrics.io/getting-started/metric-types/histograms/) - Measures the statistical distribution of a set of values.
* [Meter](https://www.app-metrics.io/getting-started/metric-types/meters/) - Measures the rate of event occurrences and the total count.
* [Timer](https://www.app-metrics.io/getting-started/metric-types/timers/) - Combines a histogram and meter to measure event duration, rate of occurrence, and duration statistics.

To use Logzio.App.Metrics, you must include at least one of the above metrics in your code. 

For example, to add a counter metric, insert the following code block into the same function as the MetricsBuilder and Scheduler:


```csharp
var counter = new CounterOptions {Name = "my_counter", Tags = new MetricTags("test", "my_test")};
metrics.Measure.Counter.Increment(counter);
```

In the example above, the metric has a name ("my_counter"), a tag key ("test") and a tag value ("my_test"): These parameters are used to query data from this metric in your Logz.io dashboard.


**5. View your metrics**

Run your application to start sending metrics to Logz.io.

Allow some time for data ingestion, then check your [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).


### Filter metrics by labels

Once the metrics are in Logz.io, you can query them using labels. Each metric includes the following labels:

| App Metrics parameter name | Description | Logz.io parameter name |
|---|---|---|
| Name | The name of the metric. Required for each metric. | Metric name if not stated otherwise |
| MeasurementUnit | The unit you use to measure. By default it is `None`. | `unit` |
| Context | The context which the metric belong to. By default it is `Application`.	 | `context` |
| Tags | Pairs of key and value of the metric. It is not required to have tags for a metric.| Tags keys |

Some of the metrics have custom labels, as described below.

#### Meter

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

#### Histogram

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

#### Timer

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
  
#### Apdex

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Sample Size | [[your_apdex_name]]_sample_size |
| Score | [[your_apdex_name]]_score |
| Frustrating | [[your_apdex_name]]_frustrating |
| Satisfied | [[your_apdex_name]]_satisfied |
| Tolerating | [[your_apdex_name]]_tolerating |

Replace [[your_apdex_name]] with the name that you assigned to the timer metric.

 

Encounter an issue? See our [.NET core troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting/).

 

### Send custom metrics with a Logz.io exporter defined by a config file

**Before you begin, you'll need**: 

* An application in .NET Core 3.1+.
* An active Logz.io account.


 **1. Install the App.Metrics.Logzio package**


Run the following from the Package Manager Console:

```csharp
Install-Package Logzio.App.Metrics
```

For manual installation, download the latest version from the NuGet Gallery.

**2. Create MetricsBuilder**

Copy and paste the following code into the function where you need to export metrics:

```csharp
var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp("<<path_to_the_config_file>>")
                .Build();
```

Add the following to the configuration file:

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


**3. Create Scheduler**

Copy and paste the following code into the same function as the MetricsBuilder:

```csharp
var scheduler = new AppMetricsTaskScheduler(
                TimeSpan.FromSeconds(15),
                async () => { await Task.WhenAll(metrics.ReportRunner.RunAllAsync()); });
scheduler.Start();
```

**4. Add the required metrics to your code**


* [Apdex (Application Performance Index)](https://www.app-metrics.io/getting-started/metric-types/apdex/) - Monitors end-user satisfaction.
* [Counter](https://www.app-metrics.io/getting-started/metric-types/counters/) - Tracks the number of times an event occurs.
* [Gauge](https://www.app-metrics.io/getting-started/metric-types/gauges/) - Provides an instantaneous measurement of a value that can arbitrarily increase or decrease (e.g., CPU usage).
* [Histogram](https://www.app-metrics.io/getting-started/metric-types/histograms/) - Measures the statistical distribution of a set of values.
* [Meter](https://www.app-metrics.io/getting-started/metric-types/meters/) - Measures the rate of event occurrences and the total count.
* [Timer](https://www.app-metrics.io/getting-started/metric-types/timers/) - Combines a histogram and meter to measure event duration, rate of occurrence, and duration statistics.

To use Logzio.App.Metrics, you must include at least one of the above metrics in your code.

For example, to add a counter metric, insert the following code block into the same function as the MetricsBuilder and Scheduler:

```csharp
var counter = new CounterOptions {Name = "my_counter", Tags = new MetricTags("test", "my_test")};
metrics.Measure.Counter.Increment(counter);
```

In the example above, the metric has a name ("my_counter"), a tag key ("test") and a tag value ("my_test"). These parameters are used to query data from this metric in your Logz.io dashboard.


**5. View your metrics**

Run your application to start sending metrics to Logz.io.

Allow some time for data ingestion, then check your [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).

### Filter metrics by labels

Once the metrics are in Logz.io, you can query them using labels. Each metric includes the following labels:

| App Metrics parameter name | Description | Logz.io parameter name |
|---|---|---|
| Name | The name of the metric. Required for each metric. | Metric name if not stated otherwise |
| MeasurementUnit | The unit you use to measure. By default it is `None`. | `unit` |
| Context | The context which the metric belong to. By default it is `Application`.	 | `context` |
| Tags | Pairs of key and value of the metric. It is not required to have tags for a metric.| Tags keys |

Some of the metrics have custom labels as described below.

##### Meter

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
  
##### Histogram

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

##### Timer

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

##### Apdex

| App Metrics parameter name | Logz.io parameter name |
|---|---|
| Sample Size | [[your_apdex_name]]_sample_size |
| Score | [[your_apdex_name]]_score |
| Frustrating | [[your_apdex_name]]_frustrating |
| Satisfied | [[your_apdex_name]]_satisfied |
| Tolerating | [[your_apdex_name]]_tolerating |

Replace [[your_apdex_name]] with the name that you assigned to the apdex metric.

 

Encounter an issue? See our [.NET core troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting/).

  

### Export using ToLogzioHttp exporter

You can configure MetricsBuilder to use ToLogzioHttp exporter, which allows you to export metrics via HTTP using additional export settings. Add the following code block to define the MetricsBuilder:


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

### .NET Core runtime metrics

The runtime metrics include additional parameters sent from your code, such as:


* Garbage collection frequencies, timings by generation/type, pause timings, and GC CPU consumption ratio.
* Heap size by generation.
* Bytes allocated by small/large object heap.
* JIT compilations and JIT CPU consumption ratio.
* Thread pool size, scheduling delays and reasons for growing/shrinking.
* Lock contention.

To enable the collection of these metrics with default settings, add the following code block after the MetricsBuilder:

```csharp
// metrics is the MetricsBuilder
IDisposable collector = DotNetRuntimeStatsBuilder.Default(metrics).StartCollecting();
```

For custom settings, use the following code block after the MetricsBuilder:

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

### Get current snapshot

To enable the current snapshot preview of metrics in Logz.io format, add the following code block to the MetricsBuilder:

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

Encounter an issue? See our [.NET core troubleshooting guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/troubleshooting/dotnet-core-troubleshooting/).
</TabItem>
</Tabs>


## Traces

<Tabs>
  <TabItem value="asp-net-core" label="ASP.NET Core" default>

Deploy this integration to enable automatic instrumentation of your ASP.NET Core application using OpenTelemetry.

### Architecture overview

This integration includes:

* Installing the OpenTelemetry ASP.NET Core instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your ASP.NET Core application in conjunction with the OpenTelemetry instrumentation

On deployment, the ASP.NET Core instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.



### Setup auto-instrumentation for your locally hosted ASP.NET Core application and send traces to Logz.io

**Before you begin, you'll need**:

* An ASP.NET Core application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::


{@include: ../../_include/tracing-shipping/dotnet-steps.md}

#### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your ASP.NET Core application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Start the collector

{@include: ../../_include/tracing-shipping/collector-run.md}


#### Run the application

Run the application to generate traces.


#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


### Setup auto-instrumentation for your ASP.NET Core application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your ASP.NET Core application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.


**Before you begin, you'll need**:

* An ASP.NET Core application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service


{@include: ../../_include/tracing-shipping/dotnet-steps.md}

{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

#### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}



Run the application to generate traces.


#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


</TabItem>
  <TabItem value="asp-net" label="ASP.NET or .NET">

Deploy this integration to enable automatic instrumentation of your ASP.NET Core application using OpenTelemetry.

### Architecture overview

This integration includes:

* Installing the OpenTelemetry ASP.NET Core instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your ASP.NET Core application in conjunction with the OpenTelemetry instrumentation

On deployment, the ASP.NET Core instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.



### Setup auto-instrumentation for your locally hosted ASP.NET Core application and send traces to Logz.io

**Before you begin, you'll need**:

* An ASP.NET Core application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::


{@include: ../../_include/tracing-shipping/dotnet-steps.md}


##### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your ASP.NET Core application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


##### Start the collector

{@include: ../../_include/tracing-shipping/collector-run.md}


##### Run the application

Run the application to generate traces.


##### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).



### Setup auto-instrumentation for your ASP.NET Core application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your ASP.NET Core application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.


**Before you begin, you'll need**:

* An ASP.NET Core application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service


{@include: ../../_include/tracing-shipping/dotnet-steps.md}

{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


##### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}



Run the application to generate traces.


##### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


</TabItem>
  <TabItem value="troubleshooting" label="Troubleshooting">

#### OpenTelemetry instrumentation 

Encounter an issue? See our [OpenTelemetry troubleshooting guide](https://docs.logz.io/docs/user-guide/distributed-tracing/troubleshooting/otel-troubleshooting/).

</TabItem>
</Tabs>