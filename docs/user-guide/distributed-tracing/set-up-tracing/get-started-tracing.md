---
sidebar_position: 1
title: Getting Started with Logz.io Distributed Tracing
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Set up your Logz.io Distributed Tracing solution
keywords: [Tracing, traces, Logz.io tracing, distributed tracing, trace]
---

Get set and get ready: This section describes what you have to do to get set up - before you can use Distributed Tracing in Logz.io.

If you already use Distributed Tracing, you can quickly send your tracing data to Logz.io through your [chosen integration](https://app.logz.io/#/dashboard/integrations/). 


## To set up Distributed Tracing: 


### Get access to Logz.io

Sign up for a [free trial account](https://logz.io/freetrial).
Once you have a Logz.io account, navigate to the [**Distributed Tracing** interface](https://app.logz.io/#/dashboard/jaeger).

![Ready to get some trace data!](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing_activate.png)

### Get credentials to send tracing data

When you configure your system to send tracing data to Logz.io, you need to provide your Logz.io Distributed Tracing token and Region information.

#### Look up your Tracing token

You must have admin permissions for the Logz.io account to view the **Manage tokens** page. If you're not an admin user for the account, consult with an account admin to get the Distributed Tracing token information. 

   1. From the **Tracing** menu, go to **Manage tokens**.

      ![Distributed Tracing tokens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-token_oct2021.gif)

   1. Find the Distributed Tracing account you want to ship to in the table, and copy the token. 

###### Related Links

For information about how to manage your tracing data sources, see the [Manage a Distributed Tracing account](https://docs.logz.io/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts/#tracing) topic.



#### Look up your Region information

If you have admin user permissions, you can clarify the 2-letter code for your region in Settings > General settings > [Account settings](https://app.logz.io/#/dashboard/settings/general).

![Navigate to general settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/general-settings1_sept2021.png)

The list of all the region codes is available in the **Logz.io Docs**, in the **Region code** column of the [Regions and Listener Hosts table](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). The default region is US east.


### Set up instrumentation

Application instrumentation starts with selecting the library based on the programming language that you're using. Logz.io makes the process of collecting data from the software as easy as possible by taking advantage of community-developed plug-ins for the most commonly used libraries and frameworks. 

There’s a growing trend to do this for every type of library, software system, infrastructure component, such as proxies and service meshes, and even for orchestration systems, such as Kubernetes itself.

Logz.io’s distributed tracing solution is designed to support a variety of popular open source instrumentation libraries, including OpenTracing, Jaeger, OpenTelemetry, and Zipkin.    

But instrumentation doesn't *have* to be a huge all-or-nothing effort. It's not mandatory to immediately instrument ALL the code in your environment to start benefitting from Distributed Tracing: You can ramp up your instrumentation gradually, by implementing on a service-by-service basis.  

If you hit a wall, we’ll do our best to provide support to help you solve your instrumentation issues. 

To determine the best instrumentation strategy for your system, start with [**Send your traces**](https://app.logz.io/#/dashboard/integrations/collectors).


### Install and Run the OpenTelemetry Collector

Logz.io captures end-to-end distributed transactions from your applications and infrastructure with trace spans sent directly to Logz.io via the OpenTelemetry collector, which you install inside your environment.

We recommend that you use the OpenTelemetry collector to gather trace transaction data from your system. With the merging of the OpenTracing and OpenCensus projects, OpenTelemetry is the CNCF standard. 

[This link takes you to the OpenTelemetry installation.](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/opentelemetry) 
The information is also available in the **Logz.io Docs**, in [**Ship your data > OpenTelemetry installation**](https://docs.logz.io/shipping/tracing-sources/opentelemetry.html).

If you’re deploying distributed tracing on Kubernetes, we recommend the [Kubernetes deployment reference](https://docs.logz.io/shipping/tracing-sources/otel-traces-helm.html) topic.

For additional insights, check out our [Guide to OpenTelemetry!](https://logz.io/learn/opentelemetry-guide/)