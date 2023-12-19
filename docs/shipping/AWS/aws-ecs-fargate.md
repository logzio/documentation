---
id: AWS-ECS-Fargate
title: AWS ECS Fargate 
overview: AWS Fargate is a serverless compute engine for building applications without managing servers.
product: ['logs','metrics','tracing']
os: []
filters: ['AWS', 'Compute', 'Containers']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-fargate.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


AWS Fargate is a serverless compute engine for building applications without managing servers.
This template will create a new collector container to send your AWS ECS Fargate traces and metrics to Logz.io using AWS OTel Collector.
ECS logs will be sent to logz.io with aws firehose

**Only `awsecscontainermetrics` receiver metrics are collected by default**

**Make your ecs fargate logs are being sent to cloudwatch**

### Before you begin
These are the prerequisites you’ll need before you can begin:

* An Amazon ECS Fargate cluster
* Applications instrumented with OpenTelemetry SDK (for Traces)

Next, you'll need to configure your CloudFormation template and point the OTLP exporter.

#### Deploy the CloudFormation template

**Note**: We support two different types of CloudFormation stacks. Option 1 collects all logs from ECS clusters and also gathers metrics and traces from one cluster. For collecting metrics and traces from multiple clusters without logs, deploy multiple instances of Option 2, which is exclusively designed for metrics and traces.

##### (Option 1) Cloudformation template for logs, metrics and traces:

Click on the **Launch Stack** button below to deploy the CloudFormation template. This template will create the required resources and configurations for the AWS OTel Collector.

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                           |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/ecs-fargate/ecs-fargate-0.0.2/sam-template.yaml&stackName=logzio-ecs-fargate&param_logzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)     |

##### (Option 2) Cloudformation template for metrics and traces only:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                           |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)           |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/ecs-fargate/ecs-fargate_collector-0.0.1/sam-template.yaml&stackName=logzio-ecs-fargate&param_LogzioTracingToken=<<TRACING-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<METRICS-SHIPPING-TOKEN>>&param_LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>>&param_LogzioListenerUrl=https://<<LISTENER-HOST>>:8053)     |

#### Point the OTLP exporter to the new collector container

Update the OTLP exporter configuration in your applications to point to the new collector container running in your ECS Fargate tasks.

### Check Logz.io for your data

Give your data some time to get from your system to ours.


### Parameters

The CloudFormation template requires the following parameters:
#### Traces and metrics
| Parameter            | Description                                                                                                            |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| `ClusterName`        | The name of your ECS cluster from which you want to collect metrics.                                                   |
| `TaskRoleArn`        | Specifies whether to create default IAM roles (True or False).                                                         |
| `ExecutionRoleArn`   | The role ARN you want to use as the ECS task role. (Optional, only required if you set `CreateIAMRoles` to False)      |
| `SecurityGroups`     | The role ARN you want to use as the ECS execution role. (Optional, only required if you set `CreateIAMRoles` to False) |
| `Subnets`            | The list of SecurityGroupIds in your Virtual Private Cloud (VPC).                                                      |
| `LogzioTracingToken` | Your Logz.io tracing account token.                                                                                    |
| `LogzioMetricsToken` | Your Logz.io metrics account token.                                                                                    |
| `LogzioRegion`       | Your Logz.io region. for example: `us`                                                                                 |
| `LogzioListenerUrl`  | Your Logz.io listener URL. for example: `https://listener.logz.io:8053`                                                |
#### Logs
| Parameter                                  | Description                                                                                                                |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `logzioLogsToken`                          | Your Logz.io logs account token.                                                                                           |
| `LogzioListener`                           | Your Logz.io listener URL. for example: `https://aws-firehose-logs-listener.logz.io`                                       |
| `logzioType`                               | The log type you'll use with this shipping method. This can be a built-in log type, or your custom log type.               |
| `services`                                 | A comma-separated list of services you want to collect logs from.                                                          |
| `customLogGroups`                          | A comma-separated list of custom log groups you want to collect logs from.                                                 |
| `triggerLambdaTimeout`                     | The amount of seconds that Lambda allows a function to run before stopping it, for the trigger function.                   |
| `triggerLambdaMemory`                      | Trigger function's allocated CPU proportional to the memory configured, in MB.                                             |
| `triggerLambdaLogLevel`                    | Log level for the Lambda function. Can be one of: debug, info, warn, error, fatal, panic.                                  |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.  |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. |


## Resources and Configuration

The CloudFormation template creates several resources to set up the AWS OTel Collector and send metrics and traces to Logz.io. Here is a summary of the resources created by the template and the permissions granted to the IAM policies:

### AWS::ECS::TaskDefinition
The `ECSTaskDefinition` resource defines the container properties, such as the image, command, environment variables, and log configuration for the AWS OTel Collector container. It also sets the task and execution roles, network mode, and required compatibilities.

### AWS::ECS::Service
The `ECSReplicaService` resource creates an Amazon ECS service with the specified task definition, desired count, scheduling strategy, and network configuration. It associates the service with the provided ECS cluster.

### AWS::SSM::Parameter
The `CollectorConfigParameter` resource creates an AWS Systems Manager (SSM) parameter to store the collector's configuration. The configuration defines the receivers, processors, exporters, and service pipelines for traces and metrics. The applied configuration will be:

```yaml
receivers:
  awsxray:
    endpoint: 0.0.0.0:2000
    transport: udp
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"
  awsecscontainermetrics:
processors:
  batch:
    send_batch_size: 10000
    timeout: 1s
exporters:
  logzio/traces:
    account_token: ${LOGZIO_TRACING_TOKEN}
    region: ${LOGZIO_REGION}
  prometheusremotewrite:
    endpoint: ${LOGZIO_LISTENER_URL}
    external_labels:
      aws_env: fargate-ecs
    headers:
      Authorization: "Bearer ${LOGZIO_METRICS_TOKEN}"
    resource_to_telemetry_conversion:
      enabled: true
service:
  pipelines:
    traces:
      receivers: [ awsxray,otlp ]
      processors: [ batch ]
      exporters: [ logzio/traces ]
    metrics:
      receivers: [ otlp, awsecscontainermetrics ]
      exporters: [ prometheusremotewrite ]
  telemetry:
    logs:
      level: "debug"
```
### AWS::Lambda::Function
The `logzioFirehoseSubscriptionFiltersFunction` Lambda function is designed to handle the process of filtering log data for Logz.io, and add and remove cloudwatch logs subscription filters

### AWS::Events::Rule
The `logGroupCreationEvent` rule listens for AWS API calls via CloudTrail, specifically focusing on CreateLogGroup events from the logs.amazonaws.com event source. When such an event occurs, it triggers the Logz.io subscription filter function.

### AWS::KinesisFirehose::DeliveryStream
A Kinesis Firehose delivery stream configured to send logs to Logz.io. Logs that fail to deliver are backed up to an S3 bucket.

### AWS::S3::Bucket
An S3 bucket used to store backup logs that fail to deliver via Kinesis Firehose.

### IAM Roles
1.  **ECSTaskRole**: This role is assumed by the ECS tasks and allows them to call AWS services on your behalf. The role is created with the following properties:
    *   RoleName: AWSOTelRole
2.  **ECSExecutionRole**: The ECS container agent assumes this role, allowing it to make calls to the Amazon ECS API on your behalf. The role is created with the following properties:
    *   RoleName: AWSOTelExecutionRole
3. **firehoseSubscriptionFilterLambdaRole**: This IAM role is assumed by the Lambda function when it runs. It has permissions to:
    * Create, access, and manage CloudWatch logs.
    * Manage CloudWatch Logs Subscription Filters.
    * Assume other roles.
4. **logzioS3DestinationFirehoseRole**: IAM role assumed by Kinesis Firehose when interacting with the S3 bucket for backup purposes. The role has permissions to perform basic S3 operations like `PutObject`, `GetObject`, and `ListBucket`.

### IAM Policies
1.  **AWSOpenTelemetryPolicy**: This policy is attached to the ECSTaskRole and grants the following permissions:
    *   Allows the collector to create, describe, and put log events into CloudWatch Logs.
    *   Allows the collector to send trace data to AWS X-Ray using PutTraceSegments and PutTelemetryRecords actions.
    *   Allows the collector to fetch sampling rules, targets, and statistic summaries from AWS X-Ray.
    *   Allows the collector to get parameters from AWS Systems Manager (SSM) Parameter Store.
2.  **AmazonECSTaskExecutionRolePolicy**: This managed policy is attached to the ECSExecutionRole and grants the following permissions:

    *   Allows the collector to register and deregister tasks and task definitions in Amazon ECS.
    *   Allows the collector to access and manage container instances, clusters, and services.
    *   Allows the collector to access and manage Elastic Load Balancing resources.
3.  **CloudWatchLogsFullAccess**: This managed policy is attached to the ECSExecutionRole and grants full access to Amazon CloudWatch Logs.

4.  **AmazonSSMReadOnlyAccess**: This managed policy is attached to the ECSExecutionRole and grants read-only access to the AWS Systems Manager services and resources.


By creating and attaching these IAM roles and policies, the AWS OTel Collector is granted the necessary permissions to collect and send metrics and traces from your ECS Fargate cluster to Logz.io. The template also configures the collector to use the specified Logz.io tokens, region, and listener URL.

## Ensuring Connectivity Between the Application Containers and the Collector Container

To ensure seamless connectivity between your application containers and the AWS OTel Collector container, you need to properly configure your Amazon VPC, subnets, and security groups.

### Amazon VPC and Subnets
The application containers and the AWS OTel Collector container must be launched in the same Amazon VPC and share at least one common subnet. This ensures that they can communicate with each other using private IP addresses. When deploying the CloudFormation template, make sure to provide the correct VPC subnet IDs in the `Subnets` parameter.

### Security Groups
To allow your application containers to send traces and metrics to the AWS OTel Collector container, you need to configure the security groups for both sets of containers.

1.  **Application Containers Security Group**: Modify the security group associated with your application containers to allow outbound traffic to the OTel Collector's ports (4317 for gRPC and 4318 for HTTP). Ensure that the rules are restricted to the IP address range of the VPC or the security group associated with the OTel Collector container. This configuration allows your application containers to send data to the collector container.

2.  **AWS OTel Collector Container Security Group**: Create or modify the security group for the AWS OTel Collector container to allow inbound traffic on ports 4317 (gRPC) and 4318 (HTTP) from the application containers' security group. This configuration ensures the collector container accepts incoming data from your application containers.


When deploying the CloudFormation template, provide the collector container's security group ID in the `SecurityGroups` parameter.

By properly configuring your Amazon VPC, subnets, and security groups, you can ensure that your application containers can send metrics and traces to the AWS OTel Collector container, which in turn forwards the data to Logz.io.


## Alternative: Configure AWS Fargate task Manually to send logs to Logz.io

### Build the task execution role

[Create a new role](https://console.aws.amazon.com/iam/home#/roles$new?step=type)
in the IAM console.

* Select **AWS service**. It should already be selected by default.
* Under **Choose a use case**:
  * Select **Elastic Container Service**
  * Select **Elastic Container Service Task** (scroll to the bottom of the page to see it.)
  * Click **Next: Permissions** to continue.
* Select **AmazonECSTaskExecutionRolePolicy**.
  * Click **Next: Tags** and then **Next: Review**
* Set **Role name** to `logzioEcsTaskExecutionRole`, then click **Create role** to save.

Your new role should now be created.

* Click the newly created role to go to its **Summary** page.
* Copy the **Role ARN** (at the top of the page) and save it for later. You will need it for the deployment JSON.

### Create a Fluent Bit task definition

In the ECS console, open the [_Task Definitions_](https://eu-central-1.console.aws.amazon.com/ecs/home?region=eu-central-1#/taskDefinitions)
page.

* Select **Create new Task Definition**.
* Choose **Fargate**, and click **Next step** to continue.
* Scroll to the bottom of the page to the **Volumes** section, and select
**Configure via JSON**.
* Replace the default JSON with this code block:

```json
{
  "family": "logzio-fargate-task",
  "requiresCompatibilities": [ "FARGATE" ],
  "containerDefinitions": [
    {
      "name": "logzio-log-router",
      "image": "amazon/aws-for-fluent-bit:latest",
      "essential": true,
      "firelensConfiguration": {
        "type": "fluentbit",
        "options": { "enable-ecs-log-metadata": "true" }
      },
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/aws/ecs/logzio-fargate-logs",
          "awslogs-region": "<<AWS-REGION>>",
          "awslogs-stream-prefix": "aws/ecs"
        }
      }
    },
    {
      "name": "app",
      "essential": true,
      "image": "<<YOUR-APP-IMAGE>>",
      "logConfiguration": {
        "logDriver": "awsfirelens",
        "options": {
          "Name": "Http",
          "Host": "<<LISTENER-HOST>>",
          "URI": "/?token=<<LOG-SHIPPING-TOKEN>>&type=fargate",
          "Port": "8071",
          "tls": "on",
          "tls.verify": "off",
          "Format": "json_lines"
        }
      }
    }
  ],
  "cpu": "256",
  "executionRoleArn": "arn:aws:iam::<<AWS-ACCOUNT-ID>>:role/logzioEcsTaskExecutionRole",
  "memory": "512",
  "volumes": [ ],
  "placementConstraints": [ ],
  "networkMode": "awsvpc",
  "tags": [ ]
}
```

Replace the placeholders in the code block (indicated by the double angle brackets `<< >>`) using the parameters below: 👇


When you're done, click **Save**,
and then click **Create**.


### Parameters in logzio-log-router

| Parameter | Description |
|---|---|
| logConfiguration.options.awslogs-group | In the CloudWatch left menu, select **Logs > Log groups**, and then click **Actions > Create log group**. Give the **Log Group Name** `/aws/ecs/logzio-fargate-logs`. |
| logConfiguration.options.awslogs-region | The [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) of your cluster. |


### Parameters in app

| Parameter | Description |
|---|---|
| image | Replace `<<YOUR-APP-IMAGE>>` with the name of the image you want to ship logs from. |
| logConfiguration.options.Host | {@include: ../../_include/log-shipping/listener-var.md} Replace `<<LISTENER-HOST>>` with the host for your region. For example, listener.logz.io if your account is hosted on AWS US East, or listener-nl.logz.io if hosted on Azure West Europe. The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071.|
| logConfiguration.options.URI | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html} |



### Remaining parameters

| Parameter | Description |
|---|---|
| executionRoleArn | Replace `<<AWS-ACCOUNT-ID>>` with your [AWS account Id](https://console.aws.amazon.com/billing/home?#/account). |



### Run the task on your cluster

Go back to your new task's definition page,
and click **Actions > Run Task**.

Click **Switch to launch type**, and fill in these details:

* For **Launch Type**, select **FARGATE**.
* For **Cluster**, select your cluster.
* For **Subnets**, select a subnet from your cluster.

Click **Run task**.

The logs created by the Fluent Bit shipper are in Cloudwatch
under the `/aws/ecs/logzio-fargate-logs` log group.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

You'll be able to find these logs by searching for `type:{{fargate}}`.

 

## Adding extra configuration to your Fluent Bit task

 

### Create an extra.conf file

Create an `extra.conf` file with the extra configuration. For example:

```conf
[FILTER]
    Name record_modifier
    Match *
    Record app-version ${APP_VERSION}
```

### Upload the extra.conf file to S3 (if your Fluent Bit is on EC2)

Upload the `extra.conf` file to the S3 bucket.

### Update the task definition file

Add the path to the extra.conf file to the task definition file as follows:

```json
"firelensConfiguration": {
				"type": "fluentbit",
				"options": {
					"config-file-type": "s3",
					"config-file-value": "arn:aws:s3:::<<PATH-TO-YOUR-EXTRA-CONF>>/extra.conf"
				}
			}
```

Replace `<<PATH-TO-YOUR-EXTRA-CONF>>` with the path to the extra.conf file in your S3 bucket. For example, `yourbucket/yourdirectory/extra.conf`.

