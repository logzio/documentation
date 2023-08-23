---
id: AWS-EC2
title: AWS EC2
overview: Send your Amazon EC2 metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-ec2.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2VNLppOm4XOFwVouv8dorr']
metrics_alerts: ['hWld33IEO6gZMpp2e4vs0']
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::




Deploy this integration to send your Amazon EC2 metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon EC2 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2VNLppOm4XOFwVouv8dorr"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}



**Before you begin, you'll need**:

* An active account with Logz.io



## Manually configure OpenTelemetry on Linux

:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::

Follow these steps to manually configure OpenTelemetry on your Linux machine:

Create a Logz.io directory:

```shell
sudo mkdir /opt/logzio-agent
```

Download OpenTelemetry tar.gz:

```shell
curl -fsSL "https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.82.0/otelcol-contrib_0.82.0_linux_amd64.tar.gz" >./otelcol-contrib.tar.gz
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
    region: us
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    resource_to_telemetry_conversion:
      enabled: true
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


## Configure AWS to forward Cloudwatch metrics to Logz.io
### Create Stack in the relevant region

To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)           |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/EC2)     |

### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                                  | Description                                                                                                                                                                                          | Required/Default |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `logzioListener`                           | The Logz.io listener URL for your region. (For more details, see the [regions page](https://docs.logz.io/user-guide/accounts/account-region.html). For example - `https://listener.logz.io:8053`     | **Required**     |
| `logzioToken`                              | Your Logz.io metrics shipping token.                                                                                                                                                                 | **Required**     |
| `awsNamespaces`                            | Comma-separated list of the AWS namespaces you want to monitor. See [this list](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) of namespaces. If you want to automatically add all namespaces, use value `all-namespaces`. | **Required**     |
| `logzioDestination`                        | Your Logz.io destination URL.                                                                                                                                                                        | **Required**     |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.                                                                            | `60`             |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.                                                                           | `5`              |



### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2VNLppOm4XOFwVouv8dorr"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}