`tail_sampling` defines which traces to sample after all spans in a request are completed. By default, it collects all traces with an error span, traces slower than 1000 ms, and 10% of all other traces.


Additional policy configurations can be added to the processor. For more details, refer to the [OpenTelemetry Documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md).

The configurable parameters in the Logz.io default configuration are:

| Parameter | Description | Default |
|---|---|---|
| threshold_ms | Threshold for the span latency - traces slower than this value will be included. | 1000 |
| sampling_percentage | Percentage of traces to sample using the probabilistic policy. | 10 |