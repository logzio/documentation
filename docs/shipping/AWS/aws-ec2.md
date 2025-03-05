---
id: AWS-EC2
title: AWS EC2
overview: Send your Amazon EC2 logs and metrics to Logz.io.
product: ['logs','metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Compute']
recommendedFor: ['DevOps Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-ec2.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2oLvCy5p914pM9m5pLoD6u', 'YGbSr3PrMIIJanIUb8u24']
metrics_alerts: ['7pnMXCMcUcoERzsIM0nZ9O', '22sfot5B5YjITiWjNrlD9M']
drop_filter: []
---


## Send your AWS EC2 logs and metrics using OpenTelemetry collector service

:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::

Follow these steps to manually configure OpenTelemetry on your Linux machine:

Create a Logz.io directory:

```shell
sudo mkdir /opt/logzio-agent
```

Download OpenTelemetry tar.gz:

```shell
curl -fsSL "https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.111.0/otelcol-contrib_0.111.0_linux_amd64.tar.gz" >./otelcol-contrib.tar.gz
```

Extract the OpenTelemetry binary:

```shell
sudo tar -zxf ./otelcol-contrib.tar.gz --directory /opt/logzio-agent otelcol-contrib
```

Create the OpenTelemetry config file:

```shell
sudo touch /opt/logzio-agent/otel_config.yaml
```

And copy the following OpenTelemetry config content into the config file.

Replace `<<LOG-SHIPPING-TOKEN>>`, `<<LISTENER-HOST>>`, and `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` with the relevant parameters from your Logz.io account.

```yaml
receivers:
  filelog/aws_ec2_system:
    include:
      - /var/log/*.log
    include_file_path: true
    operators:
      - type: move
        from: attributes["log.file.name"]
        to: attributes["log_file_name"]
      - type: move
        from: attributes["log.file.path"]
        to: attributes["log_file_path"]
    attributes:
      type: agent-ec2-linux
  hostmetrics/aws_ec2_system:
    collection_interval: 15s
    scrapers:
      cpu:
        metrics:
          system.cpu.utilization:
            enabled: true
      disk:
      load:
      filesystem:
      memory:
        metrics:
          system.memory.utilization:
            enabled: true
      network:
      paging:
      process:
        mute_process_name_error: true
        mute_process_exe_error: true
        mute_process_io_error: true
processors:
  resourcedetection/system:
    detectors: ["system"]
    system:
      hostname_sources: ["os"]
  resourcedetection/ec2:
    detectors: ["ec2"]
    ec2:
      tags:
        - ^*$
  filter:
    metrics:
      include:
        match_type: strict
        metric_names: ["system.cpu.time", "system.cpu.load_average.1m", "system.cpu.load_average.5m", "system.cpu.load_average.15m", "system.cpu.utilization", "system.memory.usage", "system.memory.utilization", "system.filesystem.usage", "system.disk.io", "system.disk.io_time", "system.disk.operation_time", "system.network.connections", "system.network.io", "system.network.packets", "system.network.errors", "process.cpu.time", "process.memory.usage", "process.disk.io", "process.memory.usage", "process.memory.virtual"]
exporters:
  logging:
  logzio/logs:
    account_token: <<LOG-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>> # Default is US
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    resource_to_telemetry_conversion:
      enabled: true
      target_info:
        enabled: false
service:
  pipelines:
    logs:
      receivers:
        - filelog/aws_ec2_system
      processors:
        - resourcedetection/system
        - resourcedetection/ec2
      exporters: [logzio/logs]
    metrics:
      receivers:
        - hostmetrics/aws_ec2_system
      processors:
        - resourcedetection/system
        - resourcedetection/ec2
        - filter
      exporters: [prometheusremotewrite]
  telemetry:
    logs:
      level: "debug"
    metrics:
      address: localhost:8888
```

:::note
If you already running OpenTelemetry metrics on port 8888, you will need to edit the address field in the config file.
:::

:::caution Important
The IAM role assigned to the EC2 instance must include the `ec2:DescribeTags` permission in its policy.
:::


Create service file:

```shell
sudo touch /etc/systemd/system/logzioOTELCollector.service
```


And copy the service file's content:

```shell
[Unit]

Description=OTEL collector for collecting logs/metrics and exporting them to Logz.io.

[Service]

ExecStart=/opt/logzio-agent/otelcol-contrib --config /opt/logzio-agent/otel_config.yaml

[Install]

WantedBy=multi-user.target
```

### Manage your OpenTelemetry on Linux

To manage OpenTelemetry on your machine, use the following commands:

|Description|Command|
|--|--|
|Start service|`sudo systemctl start logzioOTELCollector`|
|Stop service|`sudo systemctl stop logzioOTELCollector`|
|Service logs|`sudo systemctl status -l logzioOTELCollector`|
|Delete service|`sudo systemctl stop logzioOTELCollector` `sudo systemctl disable logzioOTELCollector` `sudo systemctl reset-failed logzioOTELCollector 2>/dev/null` `sudo rm /etc/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /usr/lib/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /etc/init.d/logzioOTELCollector 2>/dev/null`|


{@include: ../../_include/log-shipping/otel-filter.md}


## Send AWS EC2 metrics to Logz.io via Cloudwatch Metrics Stream


Deploy this integration to send your Amazon EC2 metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon EC2 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.


{@include: ../../_include/metric-shipping/generic-dashboard.html}



{@include: ../../_include/metric-shipping/aws-metrics-new.md}


{@include: ../../_include/metric-shipping/generic-dashboard.html}

