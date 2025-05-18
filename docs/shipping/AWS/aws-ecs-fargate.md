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
toc_max_heading_level: 2
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Amazon ECS Fargate is a serverless compute engine for containers that lets you run tasks without managing servers. Use it to send logs, metrics, and traces to Logz.io to monitor your data.

## Send Logs, Metrics, and Traces via OpenTelemetry

### 1. Create an SSM Parameter to store the OTEL configuration

Go to your AWS [System Manager > Parameter Store](https://us-east-1.console.aws.amazon.com/systems-manager/parameters?region=us-east-1&tab=Table):

* Set the **Name** to `logzioOtelConfig.yaml`.
* Keep **Type** as `string` and **Data type** as `text`.
* In the **Value** field, use the following configuration as a starting point, adjusting values as needed for your environment:

```yaml
receivers:
  awsxray:
    endpoint: '0.0.0.0:2000'
    transport: udp
  otlp:
    protocols:
      grpc:
        endpoint: '0.0.0.0:4317'
      http:
        endpoint: '0.0.0.0:4318'
  awsecscontainermetrics: null
  fluentforward:
    endpoint: 'unix:///var/run/fluent.sock'
processors:
  batch:
    send_batch_size: 10000
    timeout: 1s
  tail_sampling:
    policies:
      - name: policy-errors
        type: status_code
        status_code:
          status_codes:
            - ERROR
      - name: policy-slow
        type: latency
        latency:
          threshold_ms: 1000
      - name: policy-random-ok
        type: probabilistic
        probabilistic:
          sampling_percentage: 10
  transform/log_type:
    error_mode: ignore
    log_statements:
      - context: resource
        statements:
          - set(resource.attributes["type"], "ecs-fargate") where resource.attributes["type"] == nil
exporters:
  logzio/traces:
    account_token: '${LOGZIO_TRACE_TOKEN}'
    region: '${LOGZIO_REGION}'
  prometheusremotewrite:
    endpoint: '${LOGZIO_LISTENER}'
    external_labels:
      aws_env: ecs-fargate
    headers:
      Authorization: 'Bearer ${LOGZIO_METRICS_TOKEN}'
    resource_to_telemetry_conversion:
      enabled: true
    target_info:
      enabled: false
  logzio/logs:
    account_token: '${LOGZIO_LOGS_TOKEN}'
    region: '${LOGZIO_REGION}'
service:
  pipelines:
    traces:
      receivers:
        - awsxray
        - otlp
      processors:
        - batch
      exporters:
        - logzio/traces
    metrics:
      receivers:
        - otlp
        - awsecscontainermetrics
      processors:
        - batch
      exporters:
        - prometheusremotewrite
    logs:
      receivers:
        - fluentforward
        - otlp
      processors:
        - transform/log_type
        - batch
      exporters:
        - logzio/logs
  telemetry:
    logs:
      level: info

```

Save the new SSM parameter and keep its ARN handy - you’ll need it for the next step.

### 2. Create IAM Role to allow the ECS task to access the SSM Parameter

Go to [IAM > Policies](https://us-east-1.console.aws.amazon.com/iam/home#/policies).

Click Create policy, choose the **JSON** tab under **Specify permissions**, and paste the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ssm:GetParameters",
      "Resource": [
        "<ARN_OF_SECRET_PARAMETER_FROM_STEP_1>"
      ]
    }
  ]
}
```

Create the policy and give it a name (e.g., `LogzioOtelSSMReadAccess`). 

Go to [IAM > Roles](https://us-east-1.console.aws.amazon.com/iam/home#/roles) and either:

* Attach the new policy to your existing ECS task role, or
* Create a new IAM role for the ECS task and attach the policy during setup.

If you created a new role, save its ARN — you’ll need it in the next step.

### 3. Container per Task Definition

Update your existing ECS tasks to include the OpenTelemetry Collector by:

* Adding a FireLens log configuration to any of your existing task definition
* Adding a sidecar container running the OpenTelemetry Collector


```json
{
  "family": "...",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ecsTaskExecutionRole",
  "taskRoleArn": "<TASK_ROLE_ARN_FROM_STEP_2>",
  "containerDefinitions": [
    {
        … <Existing container definition>,
       "logConfiguration": {
                "logDriver": "awsfirelens",
                "options": {
                    "Name": "opentelemetry"
                }
            }
    },
    {
      "name": "otel-collector",
      "image": "otel/opentelemetry-collector-contrib",
      "cpu": 0,      
      "essential": false,
      "command": [
          "--config",
          "env:OTEL_CONFIG"
      ],
      "environment": [
          {
              "name": "LOGZIO_LOGS_TOKEN",
              "value": "${LOGZIO_LOGS_TOKEN}"
          },
          {
              "name": "LOGZIO_METRICS_TOKEN",
              "value": "${LOGZIO_METRICS_TOKEN}"
          },
          {
              "name": "LOGZIO_TRACE_TOKEN",
              "value": "${LOGZIO_TRACE_TOKEN}"
          },
          {
              "name": "LOGZIO_REGION",
              "value": "${LOGZIO_REGION}"
          },
          {
              "name": "LOGZIO_LISTENER",
              "value": "${LOGZIO_LISTENER}"
          },
      ],
      "secrets": [
          {
              "name": "OTEL_CONFIG",
              "valueFrom": "logzioOtelConfig.yaml"
          }
      ],
      // Optional: Use this to keep logs for debugging and troubleshooting
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/otel-collector",
          "awslogs-region": "<AWS-REGION>",
          "awslogs-stream-prefix": "ecs"
        }
      }
    },
    "firelensConfiguration": {
         "type": "fluentbit"
    }
  ]
}
```

:::note
If you’d like to use a centralized log collection setup instead of the OpenTelemetry Collector, reach out to [Logz.io Support](mailto:help@logz.io) or your Customer Success Manager for guidance.
:::


## Send Logs and Metrics via Kineses Firehose

<Tabs>
  <TabItem value="logs-via-firehose" label="Send Logs" default>


This project deploys instrumentation that allows shipping Cloudwatch logs to Logz.io, with a Firehose Delivery Stream. It uses a Cloudformation template to create a Stack that deploys:

* Firehose Delivery Stream with Logz.io as the stream's destination.
* Lambda function that adds Subscription Filters to Cloudwatch Log Groups, as defined by user's input.
* Roles, log groups, and other resources that are necessary for this instrumentation.


:::note
If you want to send logs from specific log groups, use `customLogGroups` instead of `services`. Since specifying `services` will automatically send all logs from those services, regardless of any custom log groups you define.
:::

### Auto-deploy the Stack


To deploy this project, click the button that matches the region you wish to deploy your stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)      |
| `eu-central-2`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)           |
| `eu-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-south-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)             |
| `eu-south-2`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-south-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-south-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)             |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)             |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `ap-south-2`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-southeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-3.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-southeast-4` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-4#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-4.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs) |
| `ap-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-east-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)     |
| `ca-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-west-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `af-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=af-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-af-south-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `me-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-me-south-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |
| `me-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=me-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-me-central-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)     |
| `il-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=il-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-il-central-1.s3.amazonaws.com/firehose-logs/0.3.2/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs<<LISTENER-HOST>>&param_services=ecs)         |


### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                                  | Description                                                                                                                                                                                                                                              | Required/Default  |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| `logzioToken`                              | The [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship logs to.                                                                                                                                                   | **Required**      |
| `logzioListener`                           | Listener host.                                                                                                                                                                                                                                           | **Required**      |
| `logzioType`                               | The log type you'll use with this Lambda. This can be a [built-in log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), or a custom log type.                                                                                 | `logzio_firehose` |
| `services`                                 | A comma-seperated list of services you want to collect logs from. Supported options are: `apigateway`, `rds`, `cloudhsm`, `cloudtrail`, `codebuild`, `connect`, `elasticbeanstalk`, `ecs`, `eks`, `aws-glue`, `aws-iot`, `lambda`, `macie`, `amazon-mq`. | -                 |
| `customLogGroups`                          | A comma-separated list of custom log groups to collect logs from, or the ARN of the Secret parameter ([explanation below](https://docs.logz.io/docs/shipping/aws/aws-kinesis-firehose/#custom-log-group-list-exceeds-4096-characters-limit)) storing the log groups list if it exceeds 4096 characters. **Note**: You can also specify a prefix of the log group names by using a wildcard at the end (e.g., `prefix*`). This will match all log groups that start with the specified prefix.                                                                                                                                                                                | -                 |
| `useCustomLogGroupsFromSecret`             | If you want to provide list of `customLogGroups` which exceeds 4096 characters, set to `true` and configure your customLogGroups as [defined below](https://docs.logz.io/docs/shipping/aws/aws-kinesis-firehose/#custom-log-group-list-exceeds-4096-characters-limit).                                               | `false`           |
| `triggerLambdaTimeout`                     | The amount of seconds that Lambda allows a function to run before stopping it, for the trigger function.                                                                                                                                                 | `60`              |
| `triggerLambdaMemory`                      | Trigger function's allocated CPU proportional to the memory configured, in MB.                                                                                                                                                                           | `512`             |
| `triggerLambdaLogLevel`                    | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`                                                                                                                                                     | `info`            |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination                                                                                                                                 | `60`              |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination                                                                                                                                | `5`               |


:::caution
AWS limits every log group to have up to 2 subscription filters. If your chosen log group already has 2 subscription filters, the trigger function won't be able to add another one.
:::


### Custom Log Group list exceeds 4096 characters limit
If your `customLogGroups` list exceeds the 4096 characters limit, follow the below steps:

1. Open AWS [Secret Manager](https://console.aws.amazon.com/secretsmanager/)
2. Click `Store a new secret`
   - Choose `Other type of secret`
   - For `key` use `logzioCustomLogGroups`
   - In `value` store your comma-separated custom log groups list
   - Name your secret, for example as `LogzioCustomLogGroups`
   - Copy the new secret's ARN
3. In your stack, Set: 
   - `customLogGroups` to your secret ARN that you copied in step 2
   - `useCustomLogGroupsFromSecret` to `true`

</TabItem>
<TabItem value="metrics-via-firehose" label="Send Metrics" default>


Deploy this integration to send your AWS ECS Metrics via Firehose to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon Kinesis Data Firehose metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.


{@include: ../../_include/metric-shipping/aws-metrics-new.md}


{@include: ../../_include/metric-shipping/generic-dashboard.html}

### Setup Firehose metrics via Terraform

This setup includes creating a Kinesis Firehose delivery stream, CloudWatch metric stream, and necessary IAM roles.

:::note
The setup excludes the Lambda function for adding namespaces, as CloudFormation automatically triggers this during resource creation.
:::


```hcl
locals {
  metrics_namespaces = "CloudWatchSynthetics, AWS/AmazonMQ, AWS/RDS, AWS/DocDB, AWS/ElastiCache"
  logzio_token       = jsondecode(data.aws_secretsmanager_secret_version.logzio_shipping_credentials.secret_string)["LOGZIO_TOKEN"]
}

resource "aws_kinesis_firehose_delivery_stream" "logzio_delivery_stream" {
  name        = "logzio-delivery-stream"
  destination = "http_endpoint"

  http_endpoint_configuration {
    url                = "https://listener-otlp-aws-metrics-stream-us.logz.io"
    name               = "logzio_endpoint"
    retry_duration     = 60
    buffering_size     = 5
    buffering_interval = 60
    role_arn           = aws_iam_role.firehose_logging_role.arn
    s3_backup_mode     = "FailedDataOnly"
    access_key         = local.logzio_token

    request_configuration {
      content_encoding = "NONE"
    }
  }
}

resource "aws_cloudwatch_metric_stream" "logzio_metric_stream" {
  name          = "logzio-metric-stream"
  role_arn      = aws_iam_role.metrics_stream_role.arn
  firehose_arn  = aws_kinesis_firehose_delivery_stream.logzio_delivery_stream.arn
  output_format = "opentelemetry1.0"

  include_filter {
    namespace = "AWS/RDS"
  }
}
```

* Make sure the `URL` matches your region. [View region settings](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#opentelemetry-protocol-otlp-regions).

* Replace `LOGZIO_TOKEN` with your Logz.io shipping token.


Next, deploy your Terraform code to set up the Firehose stream and related resources, and verify that metrics are sent correctly to the Logz.io listener endpoint.

:::note
The Lambda function `logzioMetricStreamAddNamespacesLambda` has been removed from the script as the CloudFormation template automatically triggers it during creation.
:::


For additional namespaces or configurations, adjust the `metrics_namespaces` and `include_filter` fields as needed.

</TabItem>
</Tabs>

## Send Logs and Traces via centeralized container

### 1. Create an SSM Parameter to store the OTEL configuration

Go to your AWS [System Manager > Parameter Store](https://us-east-1.console.aws.amazon.com/systems-manager/parameters?region=us-east-1&tab=Table):

* Set the **Name** to `logzioOtelConfig.yaml`.
* Keep **Type** as `string` and **Data type** as `text`.
* In the **Value** field, use the following configuration as a starting point, adjusting values as needed for your environment:

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
  fluentforward:
    endpoint: 0.0.0.0:24284

processors:
  batch:
    send_batch_size: 10000
    timeout: 1s
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        }, 
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }        
      ]
  transform/log_type:
    error_mode: ignore
    log_statements:
      - context: resource
        statements:
          - set(attributes["type"], "ecs-fargate") where attributes["type"] == nil

exporters:
  logzio/traces:
    account_token: ${LOGZIO_TRACE_TOKEN}
    region: ${LOGZIO_REGION}
  logzio/logs:
    account_token: ${LOGZIO_LOGS_TOKEN}
    region: ${LOGZIO_REGION}

service:
  pipelines:
    traces:
      receivers: [ awsxray, otlp ]
      processors: [ batch ]
      exporters: [ logzio/traces ]
    logs:
      receivers: [ fluentforward, otlp ]
      processors: [ transform/log_type, batch ]
      exporters: [ logzio/logs ]
  telemetry:
    logs:
      level: "info"

```

Save the new SSM parameter and keep its ARN handy - you’ll need it for the next step.


### 2. Create IAM Role to allow the ECS task to access the SSM Parameter

Go to [IAM > Policies](https://us-east-1.console.aws.amazon.com/iam/home#/policies).

Click Create policy, choose the **JSON** tab under **Specify permissions**, and paste the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ssm:GetParameters",
      "Resource": [
        "<ARN_OF_SECRET_PARAMETER_FROM_STEP_1>"
      ]
    }
  ]
}
```

Create the policy and give it a name (e.g., `LogzioOtelSSMReadAccess`). 

Go to [IAM > Roles](https://us-east-1.console.aws.amazon.com/iam/home#/roles) and either:

* Attach the new policy to your existing ECS task role, or
* Create a new IAM role for the ECS task and attach the policy during setup.

If you created a new role, save its ARN — you’ll need it in the next step.

### 3. Create a ceneralized container

Create a new ECS task for the OpenTelemetry Collector 



```json
{
  "family": "...",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ecsTaskExecutionRole",
  "taskRoleArn": "<TASK_ROLE_ARN_FROM_STEP_2>",
  "containerDefinitions": [
     {
      "name": "otel-collector",
      "image": "otel/opentelemetry-collector-contrib",
      "cpu": 0,
     "portMappings": [
{
    "name": "otel-collector-4317",
    "hostPort": 4317,
    "protocol": "tcp",
    "containerPort": 4317,
    "appProtocol": "grpc"
},
{
    "name": "otel-collector-4318",
    "hostPort": 4318,
    "protocol": "tcp"
    "containerPort": 4318,
}
      ],      
      "essential": false,
      "command": [
          "--config",
          "env:OTEL_CONFIG"
      ],
      "environment": [
          {
              "name": "LOGZIO_LOGS_TOKEN",
              "value": "${LOGZIO_LOGS_TOKEN}"
          },
          {
              "name": "LOGZIO_METRICS_TOKEN",
              "value": "${LOGZIO_METRICS_TOKEN}"
          },
          {
              "name": "LOGZIO_TRACE_TOKEN",
              "value": "${LOGZIO_TRACE_TOKEN}"
          },
          {
              "name": "LOGZIO_REGION",
              "value": "${LOGZIO_REGION}"
          },
          {
              "name": "LOGZIO_LISTENER",
              "value": "${LOGZIO_LISTENER}"
          },
      ]
      "secrets": [
          {
              "name": "OTEL_CONFIG",
              "valueFrom": "logzioOtelConfig.yaml"
          }
      ],
      // Optional: Use this to keep logs for debugging and troubleshooting
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/otel-collector",
          "awslogs-region": "<AWS-REGION>",
          "awslogs-stream-prefix": "ecs"
        }
      }
    },
    "firelensConfiguration": {
         "type": "fluentbit"
    }
  ]
}

```

When enabling debugging, you may need to create a CloudWatch log group for your OpenTelemetry Collector.

You can do this via the AWS Console or using the AWS CLI:

`aws logs create-log-group --log-group-name /ecs/otel-collector`

### 4. Configure FireLens per container for Logs or Traces

To enable telemetry collection, you’ll need to add a FireLens log configuration to each relevant container in your ECS task definition.

#### For Logs

For every container you want to collect **logs** from, add the following `logConfiguration` block to its task definition:

```json
 "logConfiguration": {
                "logDriver": "awsfirelens",
                "options": {
                    "Name": "opentelemetry",
                    "Host": "<CENTRAL_COLLECTOR_HOST_OR_IP>",
                    "Port": "24284",
                    "TLS": "off"
                }
            },

```

#### For Traces

For each application you want to collect **traces** from, configure the instrumentation to send trace data to the centralized OpenTelemetry Collector container as its endpoint.