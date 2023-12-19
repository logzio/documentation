---
id: Lambda-extension-node
title: Traces from Node.js on AWS Lambda using OpenTelemetry
overview: This integration to auto-instrument your Node.js application running on AWS Lambda and send the traces to your Logz.io account.
product: ['tracing']
os: ['windows', 'linux']
filters: ['AWS', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/AWS-Lambda.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Deploy this integration to auto-instrument your Node.js application running on AWS Lambda and send the traces to your Logz.io account. This is done by adding a dedicated layer for OpenTelemetry collector, a dedicated layer for Node.js auto-instrumentation and configuring environment variables of these layers. This integration will require no change to your application code.

:::note
This integration only works for the following AWS regions: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`,
               `ap-south-1`, `ap-northeast-3`, `ap-northeast-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`,
               `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `eu-north-1`,
               `sa-east-1`,
               `ca-central-1`.
:::

**Before you begin, you'll need**:
  
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* Configured [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
* A Lambda function with a Node.js application that is not yet instrumented.

:::node
Adding environmental variables using the AWS CLI commands below, will overwrite all existing variables for your Lambda function.
:::

:::node
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::


#### Add the OpenTelemetry collector layer to your Lambda function 

This layer contains the OpenTelemetry collector that will capture data from your application.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-opentelemetry-collector-layer:<<LAYER_VERSION>>
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Node.js application.

Replace `<<YOUR-AWS-REGION>>` with the code of your AWS regions, e.g. `us-east-1`.

Replace `<<LAYER_VERSION>>` with the latest stable version for your region.

|Region|logzio-opentelemetry-collector-layer|
|--- |--- |
|us-east-1|14|
|us-east-2|3|
|us-west-1|2|
|us-west-2|2|
|eu-north-1|2|
|eu-west-1|3|
|eu-west-2|3|
|eu-west-3|2|
|ca-central-1|3|
|ap-northeast-1|3|
|ap-northeast-2|3|
|ap-northeast-3|2|
|ap-south-1|2|
|ap-southeast-1|2|
|ap-southeast-2|2|
|sa-east-1|2|


#### Create a configuration file for the OpenTelemetry collector
  
By default, the OpenTelemetry collector layer exports data to the Lambda console. To customize the collector configuration, you need to add a `collector.yaml` to your function and specifiy its location via the `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` environment variable.


The `collector.yaml` file will have the following configuration:
  
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"

exporters:
  logzio/traces:
    account_token: "<<TRACING-SHIPPING-TOKEN>>"
    region: "<<LOGZIO_ACCOUNT_REGION_CODE>>"

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [logzio/traces]
```

  
{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
{@include: ../../_include/tracing-shipping/tail-sampling.md}


#### Direct the OpenTelemetry collector to the configuration file


Add `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` variable to direct the OpenTelemetry collector to the configuration file:

```
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_FILE=/var/task/collector.yaml}
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Node.js application.


#### Activate tracing for your Lambda function

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --tracing-config Mode=Active
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Node.js application.

#### Add the OpenTelemetry Node.js wrapper layer to your Lambda function

The OpenTelemetry Node.js wrapper layer automatically instruments the Node.js application in your Lambda function.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-opentelemetry-nodejs-wrapper:<<LAYER_VERSION>>
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Node.js application.

Replace `<<YOUR-AWS-REGION>>` with the code of your AWS regions, e.g. `us-east-1`.

Replace `<<LAYER_VERSION>>` with the latest stable version for your region.

|Region|logzio-opentelemetry-nodejs-wrapper|
|--- |--- |
|us-east-1|11|
|us-east-2|3|
|us-west-1|2|
|us-west-2|2|
|eu-north-1|2|
|eu-west-1|3|
|eu-west-2|3|
|eu-west-3|2|
|ca-central-1|3|
|ap-northeast-1|3|
|ap-northeast-2|3|
|ap-northeast-3|2|
|ap-south-1|2|
|ap-southeast-1|2|
|ap-southeast-2|2|
|sa-east-1|2|

  
#### Add environment variable for the wrapper
  
Add the `AWS_LAMBDA_EXEC_WRAPPER` environment variable to point to the `otel-handler` executable:

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-handler}
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Node.js application.
