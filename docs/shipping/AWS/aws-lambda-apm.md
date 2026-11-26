---
id: AWS-Lambda-APM
title: AWS Lambda APM (Node.js)
overview: Send traces, APM metrics, function logs and AWS service metrics from your Node.js Lambda functions to Logz.io with one CloudFormation stack. No code changes.
product: ['tracing', 'metrics', 'logs']
os: []
filters: ['AWS', 'Compute']
recommendedFor: ['DevOps Engineer', 'Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/lambda-nodejs2.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Monitor your Node.js Lambda functions in Logz.io APM. One CloudFormation stack instruments your functions and sends their data to Logz.io. You don't change your code, and you don't run a script per function.

## What you get

* **APM service pages** for your functions: request rate, errors and latency per route, dependencies (databases, queues, AWS services) and cold starts.
* **End-to-end traces** across API Gateway, Lambda, SQS, SNS, EventBridge, Kinesis, DynamoDB, Aurora/RDS and HTTP calls. Trace context is carried through SQS, EventBridge, Kinesis and IoT Core, so one request shows as one trace.
* **Function logs linked to traces.** Anything your function writes with `console.log` arrives with its trace ID, so you can jump from a log line to its trace.
* **AWS service metrics** from CloudWatch: Lambda invocations, errors, throttles, duration and concurrency, plus the AWS services you choose (SQS, DynamoDB, Kinesis, API Gateway and more).

## How it works

The stack deploys three parts in your AWS account and region:

1. **The Logz.io Lambda layer**, added to the functions you choose. It contains OpenTelemetry for Node.js and a small collector extension. The stack keeps it on your functions: when a function is created, redeployed or reconfigured, the layer is added back automatically. The stack also re-checks every function every 30 minutes.
2. **A gateway collector** (one ECS Fargate task) that receives your functions' traces, computes the APM metrics and forwards everything to Logz.io.

    :::note
    The gateway collector is needed today to compute APM metrics. It will not be needed in a future release; this page will say when.
    :::

3. **A CloudWatch metric stream** that sends the AWS service metrics you select.

Deleting the stack removes all three and restores your functions' original configuration.

## Before you begin

* An active Logz.io account, and these shipping tokens from **Settings > Data shipping tokens**:
  * Tracing token
  * Metrics token (the metrics account your APM uses)
  * Logs token, if you send function logs
* Node.js Lambda functions (Node.js 18, 20 or 22, x86_64 or arm64). Other runtimes are skipped.
* A VPC with at least two private subnets that have outbound internet access (through a NAT gateway) for the gateway collector.
* Permission to create CloudFormation stacks with IAM roles in the target account.
* An AWS CloudTrail trail that records management events in the region (most accounts have one). Without it, new and redeployed functions are picked up by the 30-minute re-check instead of right away.

## Choose what to send

Each data type can be turned on or off. Turn off anything you already send to Logz.io another way, so it doesn't arrive twice.

| Data | Parameter | What it adds |
| --- | --- | --- |
| Traces and APM | `SendTraces` | The layer on your functions and the gateway collector. Needed for APM service pages. |
| Function logs | `SendLogs` | `console` output with trace IDs, plus Lambda init and error records. Turn it off if you already ship your Lambda logs to Logz.io (for example with the CloudWatch logs integration). Logs shipped another way don't carry trace IDs. |
| AWS service metrics | `SendAwsMetrics` | The CloudWatch metric stream for the namespaces in `AwsNamespaces`. Turn it off if you already stream these metrics to Logz.io. |

## Deploy the stack

Pick one way. All three deploy the same stack.

<Tabs>
<TabItem value="console" label="AWS console (Launch stack)" default>

Click the button for the region your functions run in, fill in the parameters, select the IAM acknowledgement, and choose **Create stack**.

| Region | Deploy |
| --- | --- |
| `us-east-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml&stackName=logzio-lambda-apm&param_TracesToken=<<TRACING-SHIPPING-TOKEN>>&param_MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogsToken=<<LOG-SHIPPING-TOKEN>>) |
| `us-east-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml&stackName=logzio-lambda-apm&param_TracesToken=<<TRACING-SHIPPING-TOKEN>>&param_MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogsToken=<<LOG-SHIPPING-TOKEN>>) |
| `us-west-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml&stackName=logzio-lambda-apm&param_TracesToken=<<TRACING-SHIPPING-TOKEN>>&param_MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogsToken=<<LOG-SHIPPING-TOKEN>>) |
| `eu-west-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml&stackName=logzio-lambda-apm&param_TracesToken=<<TRACING-SHIPPING-TOKEN>>&param_MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogsToken=<<LOG-SHIPPING-TOKEN>>) |
| `eu-central-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml&stackName=logzio-lambda-apm&param_TracesToken=<<TRACING-SHIPPING-TOKEN>>&param_MetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogsToken=<<LOG-SHIPPING-TOKEN>>) |

For other regions, open the `us-east-1` link and change the region in the URL (both the `region=` value and the bucket name).

</TabItem>
<TabItem value="terraform" label="Terraform">

Deploy the stack from Terraform with the AWS provider:

```hcl
resource "aws_cloudformation_stack" "logzio_lambda_apm" {
  name         = "logzio-lambda-apm"
  template_url = "https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/lambda-apm/1.0.0/template.yaml"
  capabilities = ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]

  parameters = {
    LogzioRegion     = "us"
    TracesToken      = var.logzio_tracing_token
    MetricsToken     = var.logzio_metrics_token
    LogsToken        = var.logzio_logs_token
    EnvironmentId    = "production"
    SendTraces       = "true"
    SendLogs         = "true"
    SendAwsMetrics   = "true"
    FunctionSelector = "all"
    VpcId            = "vpc-0123456789abcdef0"
    PrivateSubnetIds = "subnet-0aaa1111bbbb2222c,subnet-0ddd3333eeee4444f"
  }
}
```

Match the bucket region in `template_url` to the region the provider deploys to.

To deploy to many accounts and regions at once, use `aws_cloudformation_stack_set` and `aws_cloudformation_stack_set_instance` with the same template URL and parameters. Each account and region gets its own gateway collector and metric stream.

Store the tokens as sensitive Terraform variables or in your secrets manager, not in plain text.

</TabItem>
<TabItem value="own-iac" label="Add the layer in your own IaC">

Use this if you want your infrastructure code to own the layer instead of the stack. Deploy the stack with `FunctionSelector` set to `none`: it creates the gateway collector and metric stream but doesn't change any function. Then add the following to each function in your IaC (SAM, CDK, Serverless Framework, Terraform).

**Layer**: `arn:aws:lambda:<<REGION>>:486140753397:layer:otel-nodejs-extension-<<ARCH>>-1_1_0:1`, where `<<ARCH>>` is `amd64` (x86_64 functions) or `arm64`. See the [Logz.io Lambda layer releases](https://github.com/logzio/opentelemetry-lambda/releases) for newer versions.

**Environment variables**:

| Variable | Value |
| --- | --- |
| `AWS_LAMBDA_EXEC_WRAPPER` | `/opt/otel-handler` |
| `OPENTELEMETRY_COLLECTOR_CONFIG_URI` | `/opt/collector-config/config.gateway.yaml` (traces and logs) or `/opt/collector-config/config.gateway-traces.yaml` (traces only) |
| `LOGZIO_GATEWAY_ENDPOINT` | The stack output `PrivateEndpoint` (functions in the stack's VPC) or `PublicEndpoint` |
| `LOGZIO_GATEWAY_TOKEN` | The value of the secret in the stack output `GatewayTokenSecret` |
| `OTEL_LOGS_EXPORTER` | `none`, only with the traces-only collector config |
| `OTEL_SERVICE_NAME` | The service name to show in APM (optional). Defaults to the function name. |
| `OTEL_RESOURCE_ATTRIBUTES` | `service.version=<<VERSION>>` (optional) |

In SAM, put these under `Globals.Function` to apply them to every function at once:

```yaml
Globals:
  Function:
    Layers:
      - arn:aws:lambda:<<REGION>>:486140753397:layer:otel-nodejs-extension-amd64-1_1_0:1
    Environment:
      Variables:
        AWS_LAMBDA_EXEC_WRAPPER: /opt/otel-handler
        OPENTELEMETRY_COLLECTOR_CONFIG_URI: /opt/collector-config/config.gateway.yaml
        LOGZIO_GATEWAY_ENDPOINT: <<GATEWAY-ENDPOINT>>
        LOGZIO_GATEWAY_TOKEN: '{{resolve:secretsmanager:<<GATEWAY-TOKEN-SECRET-ARN>>}}'
```

</TabItem>
</Tabs>

### Stack parameters

| Parameter | Description | Default |
| --- | --- | --- |
| `LogzioRegion` | The region of your Logz.io account: `us`, `eu`, `uk`, `ca` or `au`. | `us` |
| `TracesToken` | Your Logz.io tracing shipping token. | Required |
| `MetricsToken` | Your Logz.io metrics shipping token, for APM metrics and AWS service metrics. | Required |
| `LogsToken` | Your Logz.io logs shipping token. Needed only when `SendLogs` is `true`. | |
| `EnvironmentId` | The environment name shown in Logz.io APM, for example `production` or `staging`. | `production` |
| `SendTraces` | Send traces and APM metrics. | `true` |
| `SendLogs` | Send function logs. | `true` |
| `SendAwsMetrics` | Stream AWS service metrics from CloudWatch. | `true` |
| `AwsNamespaces` | The CloudWatch namespaces to stream, comma-separated. | `AWS/Lambda,AWS/ApiGateway,AWS/SQS,AWS/SNS,AWS/Kinesis,AWS/DynamoDB,AWS/RDS,AWS/Events` |
| `FunctionSelector` | Which functions to instrument: `all` (every Node.js function in the region), `prefix`, `tag`, or `none` (instrument them in your own IaC). | `all` |
| `FunctionPrefix` | With `prefix`: instrument functions whose name starts with this value, for example `orders-`. | |
| `FunctionTag` | With `tag`: instrument functions that have this tag, as `key=value`, for example `apm=enabled`. | |
| `VpcId` | The VPC for the gateway collector. Functions in this VPC reach it privately. | Required |
| `PrivateSubnetIds` | Two or more private subnets with outbound internet access, comma-separated. | Required |
| `VpcCidr` | The address range allowed to send data to the gateway: your VPC range, or a wider private range if functions run in peered VPCs. | `10.0.0.0/8` |
| `PublicEndpoint` | Also create a public HTTPS endpoint, for functions that don't run in this VPC. It is protected by a generated token. | `false` |
| `LayerVersion` | The Logz.io layer release. | `1.1.0` |
| `LayerVersionNumber` | The AWS version number of that layer release. | `1` |
| `LayerAccount` | The AWS account that publishes the Logz.io layer. | `486140753397` |

To leave a single function out, tag it `logzio:apm=off`. The stack skips it, and removes the layer if it was added.

## Check Logz.io for your data

Send a few requests to your functions, then wait about 3 minutes.

* **APM**: go to **APM** and select your environment. Each instrumented function appears as a service, named after its function, or after `OTEL_SERVICE_NAME` if the function sets one.
* **Traces**: open **Explore** and switch to **Spans**, or open a trace from an APM service page.
* **Logs**: open **Explore** and search `faas.name:"<<FUNCTION-NAME>>"`. Lines written with `console` have a trace link.
* **AWS service metrics**: CloudWatch metrics start with `aws_`, for example `aws_lambda_invocations_sum`. They can take up to 10 minutes to appear.

## What is collected

**Traces** include:

* The invocation of each function, named by API route for API Gateway functions (for example `POST /orders`).
* A `cold start` span inside the first request of each new function instance, showing how long initialization took.
* Calls to AWS services through the AWS SDK, HTTP and `fetch` calls, and calls to PostgreSQL, MySQL, Redis, MongoDB and other common clients.
* For functions triggered by Kinesis, SQS, SNS or DynamoDB Streams, the stream, queue or topic that triggered them. They show as dependencies in APM.

**Labels on APM metrics** include the function name (`faas_name`), AWS account (`cloud_account_id`), region (`cloud_region`), environment (`env_id`), version (`service_version`) and whether the request was a cold start (`faas_coldstart`). The version defaults to the function's code hash, so it changes only when you deploy new code. Set `service.version` in `OTEL_RESOURCE_ATTRIBUTES` to use your own release numbers.

**Logs** include each line your function writes with `console`, with its level and trace ID, and Lambda init and error records. Lambda's per-invocation START and END lines are dropped to keep log volume down.

**AWS service metrics** carry the AWS `account` and `region` and the resource name in lower case (for example `functionname`, `queuename`).

## Update or remove

* **Update** to a new layer release by updating the stack's `LayerVersion`. The stack moves every instrumented function to the new layer.
* **Remove** by deleting the stack. Your functions return to their original configuration: the layer and environment variables are removed.

## Troubleshooting

**A function doesn't appear in APM**
* Check that its runtime is Node.js and that it matches `FunctionSelector`.
* Check that it isn't tagged `logzio:apm=off`.
* Lambda allows 5 layers per function. If a function already has 5, the stack skips it and logs the reason in the log group `/aws/lambda/<<STACK-NAME>>-instrumenter`.
* A new function can take up to 30 minutes to be instrumented if the account has no CloudTrail trail.
* A function outside the gateway's VPC can't reach the private endpoint. Set `PublicEndpoint` to `true`, or deploy the gateway in that function's VPC.

**Another APM vendor's layer is on the function**
Remove the other vendor's layer and its environment variables (for example `AWS_LAMBDA_EXEC_WRAPPER` pointing to another wrapper) before you instrument the function. Two tracing layers on one function interfere with each other.

**Traces disappear for a short time after a deploy**
When your IaC or CI redeploys a function without the layer, the stack adds it back, usually within a few minutes (the time CloudTrail takes to report the change). Requests in between aren't traced. To avoid the gap, add the layer in your own IaC (see **Add the layer in your own IaC** above).

**Logs arrive twice**
You ship Lambda logs another way too (for example the CloudWatch logs integration). Set `SendLogs` to `false`, or stop the other shipping for these functions.
