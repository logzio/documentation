---
sidebar_position: 1
---
Get set and get ready: This section describes what you have to do to get set up - before you can use Distributed Tracing in Logz.io.

If you already use Distributed Tracing, refer to our [guides on how to get connected to Logz.io](https://app.logz.io/#/dashboard/send-your-data/collection?tag=existing-instrumentation&collection=tracing-sources). 
This information is also available in the [**Logz.io Docs**](https://docs.logz.io/shipping/#tracing-sources), via the **My code is instrumented** filter.

#### To set up Distributed Tracing: 


##### Get access to Logz.io

Sign up for a [free trial account](https://logz.io/freetrial).
Once you have a Logz.io account, navigate to the [**Distributed Tracing** interface](https://app.logz.io/#/dashboard/jaeger). 
![Ready to get some trace data!](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing_activate.png)

##### Get your credentials to send tracing data

When you configure your system to send tracing data to Logz.io, you need to provide your Logz.io Distributed Tracing token and Region information.

###### Look up your Tracing token

You must have admin permissions for the Logz.io account to view the **Manage tokens** page. If you're not an admin user for the account, consult with an account admin to get the Distributed Tracing token information. 

   1. From the **Tracing** menu, go to **Manage tokens**.

      ![Distributed Tracing tokens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-token_oct2021.gif)

   1. Find the Distributed Tracing account you want to ship to in the table, and copy the token. 

   *Related Links*

   + For information about how to manage your tracing data sources, see the [Manage a Distributed Tracing account](https://docs.logz.io/user-guide/accounts/manage-the-main-account-and-sub-accounts.html#tracing) topic.



###### Look up your Region information


##### Set up instrumentation

Application instrumentation starts with selecting the library based on the programming language that you're using. Logz.io makes the process of collecting data from the software as easy as possible by taking advantage of community-developed plug-ins for the most commonly used libraries and frameworks. 

There’s a growing trend to do this for every type of library, software system, infrastructure component, such as proxies and service meshes, and even for orchestration systems, such as Kubernetes itself.

Logz.io’s distributed tracing solution is designed to support a variety of popular open source instrumentation libraries, including OpenTracing, Jaeger, OpenTelemetry, and Zipkin.    

But instrumentation doesn't *have* to be a huge all-or-nothing effort. It's not mandatory to immediately instrument ALL the code in your environment to start benefitting from Distributed Tracing: You can ramp up your instrumentation gradually, by implementing on a service-by-service basis.  

If you hit a wall, we’ll do our best to provide support to help you solve your instrumentation issues. 

To determine the best instrumentation strategy for your system, start with [**Tracing > Send your traces**](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=tracing-sources&accountIds=true), and then select the relevant filter in the **Tracing** tab, depending on whether or not your code is already instrumented: Either **My code is instrumented** or **My code is not instrumented**.  

This information is also available in the **Logz.io Docs**, in [**Send your data > Tracing**](https://docs.logz.io/shipping/#tracing-sources).


##### Install and Run the OpenTelemetry Collector

Logz.io captures end-to-end distributed transactions from your applications and infrastructure with trace spans sent directly to Logz.io via the OpenTelemetry collector, which you install inside your environment.

We recommend that you use the OpenTelemetry collector to gather trace transaction data from your system. With the merging of the OpenTracing and OpenCensus projects, OpenTelemetry is the CNCF standard. 

[This link takes you to the OpenTelemetry installation.](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/opentelemetry) 
The information is also available in the **Logz.io Docs**, in [**Ship your data > OpenTelemetry installation**](https://docs.logz.io/shipping/tracing-sources/opentelemetry.html).

If you’re deploying distributed tracing on Kubernetes, we recommend the [Kubernetes deployment reference](https://docs.logz.io/shipping/tracing-sources/otel-traces-helm.html) topic.

For additional insights, check out our [Guide to OpenTelemetry!](https://logz.io/learn/opentelemetry-guide/)