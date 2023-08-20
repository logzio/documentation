#### Install general Python OpenTelemetry instrumentation components

Run the following commands:

```shell
pip3 install opentelemetry-distro
pip3 install opentelemetry-instrumentation
opentelemetry-bootstrap --action=install
pip3 install opentelemetry-exporter-otlp
```

#### Set environment variables 

After installation, configure the exporter by running the following command:

```shell 
export OTEL_TRACES_EXPORTER=otlp
export OTEL_RESOURCE_ATTRIBUTES="service.name=<<YOUR-SERVICE-NAME>>"
```

Replace `<<YOUR-SERVICE-NAME>>` with the name of your tracing service defined earlier.