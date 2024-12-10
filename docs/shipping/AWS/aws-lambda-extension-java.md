---
id: Lambda-extension-java
title: Traces from Java on AWS Lambda using OpenTelemetry
overview: This integration to auto-instrument your Java application running on AWS Lambda and send the traces to your Logz.io account.
product: ["tracing"]
os: ["windows", "linux"]
filters: ["AWS", "Compute"]
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/AWS-Lambda.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Deploy this integration to auto-instrument your Java application running on AWS Lambda and send the traces to your Logz.io account. This is done by adding a dedicated layer for OpenTelemetry collector, a dedicated layer for Java auto-instrumentation and configuring environment variables of these layers. This integration will require no change to your application code.

:::note
This integration only works for the following AWS regions: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`,
`ap-south-1`, `ap-northeast-3`, `ap-northeast-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`,
`eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `eu-north-1`,
`sa-east-1`,
`ca-central-1`.
:::

:::note
If you need an example aplication to test this integration, please refer to our [Java OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/java/traces/lambda-service).
:::

**Before you begin, you'll need**:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Configured [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- A Lambda function with a Java application that is not yet instrumented.

:::note
Using `aws lambda update-function-configuration` with `--layers` replaces all existing layers with the specified ARN(s). To add a new layer without removing existing ones, include all desired layer ARNs in the command, both new and previously attached.
:::

:::note
Adding environmental variables using the AWS CLI commands below, will overwrite all existing variables for your Lambda function.
:::

:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::

**Packaging Your Lambda Function**. Ensure your function is packaged and uploaded as a `.zip` file containing a `lib` directory with the JAR file and the `collector.yaml` file, which will be described later.

**Instrumentation adds overhead.** A 60-second timeout ensures reliable trace exports.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --timeout 60
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of the Lambda function you want to update.

#### Add the OpenTelemetry collector layer to your Lambda function

This layer contains the OpenTelemetry collector that will capture data from your application.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers arn:aws:lambda:<<YOUR-AWS-REGION>>:486140753397:layer:logzio-opentelemetry-collector-<<ARCHITECHTURE>>:<<VERSION>>
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Java application.

Replace `<<YOUR-AWS-REGION>>` with the code of your AWS regions, e.g. `us-east-1`.

Replace `<<ARCHITECTURE>>` with the target architecture for your Lambda function, either `arm64` for ARM-based applications or `amd64` (also known as x86_64) for traditional 64-bit Intel/AMD applications.

Replace `<<VERSION>>` with the latest version of the layer. You can find the latest version number by visiting the [Logz.io OpenTelemetry Lambda Releases page.](https://github.com/logzio/opentelemetry-lambda/releases)

#### Create a configuration file for the OpenTelemetry collector

By default, the OpenTelemetry collector layer exports data to the Lambda console. To customize the collector configuration, you need to add a `collector.yaml` to your function and specifiy its location via the `OPENTELEMETRY_COLLECTOR_CONFIG_URI` environment variable.

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

{@include: ../../\_include/tracing-shipping/replace-tracing-token.html}
{@include: ../../\_include/tracing-shipping/tail-sampling.md}

#### Direct the OpenTelemetry collector to the configuration file

Add `OPENTELEMETRY_COLLECTOR_CONFIG_URI` variable to direct the OpenTelemetry collector to the configuration file:

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_URI=<<PATH_TO_YOUR_COLLECTOR.YAML>>}
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Java application.

Replace `<<PATH_TO_YOUR_COLLECTOR.YAML>>` with the actual path to your `collector.yaml` file.
(If `collector.yaml` is located in the root directory of your application, use the path `/var/task/collector.yaml`.)

#### Activate tracing for your Lambda function

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --tracing-config Mode=Active
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Java application.

#### Add the OpenTelemetry Java Agent layer to your Lambda function

The OpenTelemetry Java Agent layer automatically instruments the Java application in your Lambda function.

Find the latest ARN for the OpenTelemetry Java Agent layer on the [OpenTelemetry Lambda GitHub Releases page](https://github.com/open-telemetry/opentelemetry-lambda/releases) under `layer-java`.

```shell
aws lambda update-function-configuration --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> --layers <LAYER_ARN>

```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Java application.

`<<LAYER_ARN>>` with the latest ARN from the GitHub releases page.

Replace `<<YOUR-AWS-REGION>>` with the code of your AWS regions, e.g. `us-east-1`.

#### Add environment variable

Add the following environment variables to your Lambda function:

- `AWS_LAMBDA_EXEC_WRAPPER` to point to the otel-handler executable
- `OTEL_JAVA_AGENT_FAST_STARTUP_ENABLED` to improve startup performance see [here](https://github.com/open-telemetry/opentelemetry-lambda/tree/main/java#java-agent)
- `OTEL_RESOURCE_ATTRIBUTES` to set a service name

```shell
aws lambda update-function-configuration \
  --function-name <<YOUR-LAMBDA_FUNCTION_NAME>> \
  --environment "Variables={AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-handler,OTEL_JAVA_AGENT_FAST_STARTUP_ENABLED=true,OTEL_RESOURCE_ATTRIBUTES=service.name=my-lambda-function-java}"
```

Replace `<<YOUR-LAMBDA_FUNCTION_NAME>>` with the name of your Lambda function running the Java application.
