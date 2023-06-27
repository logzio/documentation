The `tail_sampling` defines the decision to sample a trace after the completion of all the spans in a request. By default, this configuration collects all traces that have a span that was completed with an error, all traces that are slower than 1000 ms, and 10% of the rest of the traces.

You can add more policy configurations to the processor. For more on this, refer to [OpenTelemetry Documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md).

The configurable parameters in the Logz.io default configuration are:

| Parameter | Description | Default |
|---|---|---|
| threshold_ms | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. | 1000 |
| sampling_percentage | Sampling percentage for the probabilistic policy. | 10 |
