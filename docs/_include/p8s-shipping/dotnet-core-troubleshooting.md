This section contains some guidelines for handling errors that you may encounter when trying to collect .NET metrics.


#### Problem: No metrics received

No metrics are observed in your Logz.io account.

##### Possible cause - Incorrect token and/or listener URL


Your Logz.io token and/or listener URL may be incorrect.

###### Suggested remedy


1. Navigate to  **[Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) > [Data shipping tokens - Metrics](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics)** and verify your account's metrics token and listener URL.

2. Check in the integration code whether the token and listener URL are specified correctly.

### Possible cause - Shipper connectivity failure

Your host/server may not be connected to your Logz.io listener.


###### Suggested remedy


Verify connectivity of your Logz.io listener as follows.

* For Linux and Mac servers, use `telnet`:

  ```shell
  telnet listener.logz.io <<PORT>>
  ```


* For Windows servers running Windows 8/Server 2012 and later, use the following command in PowerShell:

  ```shell
  Test-NetConnection listener.logz.io -Port <<PORT>>
  ```

  Replace `<<PORT>>` with the appropriate port nummber. For HTTPS communication use port 8053. For HTTP communication use port 8052.


##### Possible cause - Incorrect listener endpoint

Your Logz.io listener may not be using the correct endpoint.

###### Suggested remedy

Change the endpoint of your listener from `https://<<LISTENER-HOST>>:<<PORT>>` to `http://<<LISTENER-HOST>>:<<PORT>>` or from `http://<<LISTENER-HOST>>:<<PORT>>` to `https://<<LISTENER-HOST>>:<<PORT>>`


* Use the listener URL specific to the region where your Logz.io account is hosted. [Click to look up your listener URL](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions). The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071.


##### Possible cause - Kubernetes environment - prometheus.io/scrape is not set

If you're running .NET on Kubernetes, the `prometheus.io/scrape` may not be enabled.

###### Suggested remedy


Make sure you have the scrape setting enabled as follows: `prometheus.io/scrape: true`.


##### Possible cause - Code needs debugging

If all the above causes are not applicable, the code may need debugging.


###### Suggested remedy


Check if the following code works with your integration:

```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using App.Metrics.Counter;
using App.Metrics.Scheduling;

namespace App.Metrics.Logzio
{
    class Program
    {
        static void Main(string[] args)
        {
            var metrics = new MetricsBuilder()
                .Report.ToLogzioHttp("[[logzio_endpoint]]", "[[metrics_token]]")
                .Build();

            var scheduler = new AppMetricsTaskScheduler(
                TimeSpan.FromSeconds(5),
                async () => { await Task.Run(() => metrics.ReportRunner.RunAsync<LogzioMetricsReporter>()); });
            scheduler.Start();

            var counter = new CounterOptions {Name = "my_counter", Tags = new MetricTags("test", "my_test")};
            metrics.Measure.Counter.Increment(counter);

            Thread.Sleep(10000);

            metrics.Measure.Counter.Increment(counter);

            Thread.Sleep(100000); // Lets the program to continue running so that the scheduler wiil be able to continue sending metrics to Logz.io 
        }
    }
}
```

If this code is not working, we need to start debugging the integration.

[App Metrics](https://www.app-metrics.io/) supports the following .NET logging providers:

* Serilog
* NLog
* log4net
* EntLib
* Loupe

To see in-app logs, configure your desired log provider and change the properties of your config file as follows:

* `Copy to output directory` to `Copy if newer` or `Copy always`.