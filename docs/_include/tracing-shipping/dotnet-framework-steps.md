#### Download instrumentation packages

Run the following command from the application directory:

```shell
dotnet add package OpenTelemetry
dotnet add package OpenTelemetry.Api
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
dotnet add package OpenTelemetry.Instrumentation.AspNet
```

#### Modify the Web.Config file

Add a required HttpModule to the Web.Config file as follows:

```xml
<system.webServer>
    <modules>
        <add
            name="TelemetryHttpModule"
            type="OpenTelemetry.Instrumentation.AspNet.TelemetryHttpModule,
                OpenTelemetry.Instrumentation.AspNet.TelemetryHttpModule"
            preCondition="integratedMode,managedHandler" />
    </modules>
</system.webServer>
```

#### Enable instrumentation in the code

Add the following code to the Global.asax.cs file:

```csharp
using OpenTelemetry;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

public class Global : HttpApplication
{
    private TracerProvider tracerProvider;

    void Application_Start(object sender, EventArgs e)
    {
        this.tracerProvider = Sdk.CreateTracerProviderBuilder()
            .AddAspNetInstrumentation()
            .SetResourceBuilder(
                ResourceBuilder.CreateDefault()
                    .AddService("my-service-name"))
            .AddOtlpExporter(options =>
           {
               options.Endpoint =
                   new Uri("http://localhost:4317");
           })
            .Build();
    }

    void Application_End()
    {
        this.tracerProvider?.Dispose();
    }
}
```
