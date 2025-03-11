### Optional - Add basic filtering

You can use the filter processor to remove telemetry data based on OTTL (OpenTelemetry Transformation Language) rules. Any telemetry that meets at least one of the specified conditions will be dropped.

For example, to allow span data from services app1, app2, and app3 and drop data from all other services:

```shell
processors:
  filter/ottl:
    error_mode: ignore
    traces:
      span:
        - |
        resource.attributes["service.name"] != "app1" and
        resource.attributes["service.name"] != "app2" and
        resource.attributes["service.name"] != "app3"
    metrics:
      datapoint:
        - metric.name == "k8s.pod.phase" and value_int == 4
    logs:
      log_record:
        - 'IsMatch(body, ".*password.*")'
        - 'severity_number < SEVERITY_NUMBER_WARN'
```


To only drop spans from a service called service1 while keeping all other spans:

```shell
processors:
  filter/ottl:
    error_mode: ignore
    traces:
      span:
        - resource.attributes["service.name"] == "service1"
```

Learn more about filtering options in OpenTelemetry's [Transforming telemetry documentation](https://opentelemetry.io/docs/collector/transforming-telemetry/#basic-filtering).







