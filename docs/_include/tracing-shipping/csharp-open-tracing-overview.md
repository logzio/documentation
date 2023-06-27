## OpenTracing Instrumentation for C\#

This article describes how to extract traces from your C#-based application with OpenTracing instrumentation.

### OpenTracing and Jaeger

OpenTracing is an API standard of instrumentation for distributed tracing.
Jaeger is one implementation of that standard and our most recommended practice for C#. It has a set of libraries and tools to provide open source implementation for distributed tracing

### Requirements
Add the following packages to your solution:

* OpenTracing.Contrib.NetCore
* OpenTracing
* Jaeger

### Examples

To see an actual example, head to our [examples repository](https://github.com/logzio/Integrations_examples/tree/main/Tracing/cs_client_instrumentaion).
