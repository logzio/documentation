## Introduction

Logz.io recommends that you use OpenTelemetry to gather trace transaction data from your system. Because of its versatility, OpenTelemetry has been widely adopted as the industry standard: OpenTelemetry can be equipped with many additional functionalities, one of which is collecting aggregated trace data. Beyond that, [OpenTelemetry](https://github.com/open-telemetry) is set to be the best production-ready solution going forward.

However, if you already have Jaeger deployed in your local environment, to quickly move from your local Jaeger installation to Logz.io,  the simplest solution is to replace the Jaeger collector with the Logz.io version of the Jaeger collector. The Logz.io collector makes sure that your tracing data and spans are sent to the Logz.io backend instead of to the local Jaeger installation. 

Over time, should you decide to change to the OpenTelemetry collector, please feel free to explore the topic [_Installing the OpenTelemetry Collector for Distributed Tracing_](https://docs.logz.io/shipping/tracing-sources/opentelemetry) for the procedure to configure and deploy the OpenTelemetry collector. You can always return to the Jaeger collector as a secondary option if you experience issues with the OpenTelemetry collector. 

This topic explains how to set up the Logz.io Jaeger collector. For an overview of the process to send traces to Logz.io, see [Getting started with Logz.io Distributed Tracing](https://docs.logz.io/user-guide/distributed-tracing/getting-started-tracing/). 


#### Deploy the Jaeger collector with the Logz.io exporter

The Logz.io integration builds on the Jaeger collector base image and uses the gRPC plugin framework to enable communication between the collector and Logz.io.

Wherever you reference the Jaeger collector image in your Kubernetes configuration file or Docker script, all you need to do is replace it with the Logz.io image and include the relevant Logz.io parameters. 

The Logz.io collector image is available via the Docker hub, [here.](https://hub.docker.com/r/logzio/jaeger-logzio-collector)


##### Update collector references to the Logz.io image in your configuration

###### Example

If you were using Jaeger collector version 1.22, in your Kubernetes config file or your Docker script, wherever `jaegertracing/jaeger-collector:1.22` appears, replace it with the latest version of the Logz.io collector:  `logzio/jaeger-logzio-collector:latest`.


##### Configure the Logz.io Jaeger Collector image with the required parameters

Update the Logz.io image with the relevant shell or environment variables. 
The required ports are described [here](https://www.jaegertracing.io/docs/latest/deployment/#collectors), and the complete list of Logz.io collector parameters is presented below. 

In addition to these parameters, you can also use [Jaeger's collector parameters](https://www.jaegertracing.io/docs/latest/cli/#jaeger-collector-grpc-plugin). 
You'll need to select the Jaeger version page for your deployment. 


{@include: ./tracing-shipping/tracing-parameters.md}


|GRPC_STORAGE_PLUGIN_LOG_LEVEL| The lowest log level to send.  From lowest to highest, log levels are: **trace, debug, info, warn, error**.  Controls logging only for the Jaeger Logz.io Collector.  Does not affect Jaeger components.|DEFAULT: **warn** |