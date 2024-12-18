---
id: Lambda-extensions
title: Lambda Extensions
overview: The Logz.io Lambda extension for logs, uses the AWS Extensions API and AWS Logs API and sends your Lambda Function Logs directly to your Logz.io account.
product: ['logs']
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

Lambda Extensions enable tools to integrate deeply into the Lambda execution environment to control and participate in Lambda’s lifecycle.
To read more about Lambda Extensions, [click here](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html).
The Logz.io Lambda extension for logs, uses the AWS Extensions API and [AWS Logs API](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported), and sends your Lambda Function Logs directly to your Logz.io account.

This repo is based on the [AWS lambda extensions sample](https://github.com/aws-samples/aws-lambda-extensions).
This extension is written in Go, but can be run with runtimes that support [extensions](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html).

## Prerequisites

* Lambda function with [supported runtime](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html) for extensions.
* AWS Lambda limitations: A function can use up to five layers at a time. The total unzipped size of the function and all layers cannot exceed the unzipped deployment package size limit of 250 MB.


## Important notes

* If an extension does not have enough time to receive logs from AWS Logs API, it may send the logs at the next invocation of the Lambda function.
If you want to send all the logs by the time your Lambda function stops running, you will need to add a sleep interval at the end of your Lambda function code. This will give the extension enough time to do the job.
* Due to [Lambda's execution environment lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html), the extension is invoked at two events - `INVOKE` and `SHUTDOWN`.
This means that if your Lambda function goes into the `SHUTDOWN` phase, the extension will start running and send all logs that are in the queue.


## Deploying Logz.io logs extension

You can deploy the extension via the AWS CLI or via the AWS Management Console.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="aws-cli" label="AWS CLI" default>

## Deploying via the AWS CLI

### Deploy the extension and configuration

If you haven't done it already, [install](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) and [configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) the AWS CLI.

Add the layer to your function and configure the environment variables using the following command:

```shell
aws lambda update-function-configuration \
    --function-name <<FUNCTION-NAME>> \
    --layers <<LAYERS>> \
    --environment "Variables={<<ENV-VARS>>}"
```

:::note
This command overwrites the existing function configuration. If you already have your own layers and environment variables for your function, include them in the list.
:::


| Placeholder | Description | Required/Default|
|---|---|---|
| `<<FUNCTION-NAME>>` |  Name of the Lambda Function you want to monitor. |Required|
| `<<LAYERS>>` | A space-separated list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.  For the ARN, see the [**ARNs** table](https://docs.logz.io/docs/shipping/aws/lambda-extensions/#arns) |  |
| `<<ENV-VARS>>`  | Key-value pairs containing environment variables that are accessible from function code during execution. Should appear in the following format: `KeyName1=string,KeyName2=string`.  For a list of all the environment variables for the extension, see the [**Lambda environment variables** table](https://docs.logz.io/docs/shipping/Compute/Lambda-extensions#environment-variables) |  |

#### Command example
```shell
aws lambda update-function-configuration \
    --function-name exampleFunction \
    --layers arn:aws:lambda:us-east-1:486140753397:layer:LogzioLambdaExtensionLogs:14 \
    --environment "Variables={LOGZIO_LOGS_TOKEN=<<LOGZIO_SHIPPING_TOKEN>>,LOGZIO_LISTENER=<<LOGZIO_LISTENER_ADDRESS>>,ENABLE_PLATFORM_LOGS=true,GROK_PATTERNS='{}',LOGS_FORMAT='^\[%{NUMBER:logId}\] %{GREEDYDATA:message}',CUSTOM_FIELDS='fieldName1=fieldValue1,fieldName2=fieldValue2',JSON_FIELDS_UNDER_ROOT=true}"
```

#### Deleting the extension

To delete the extension and its environment variables, use the following command:

```shell
aws lambda update-function-configuration \
    --function-name <<FUNCTION-NAME>> \
    --layers \
    --environment "Variables={}"
```

:::note
This command overwrites the existing function configuration. If you already have your own layers and environment variables for your function, include them in the list.
:::

```shell
aws lambda update-function-configuration \
    --function-name <<FUNCTION-NAME>> \
    --layers [<<LAYERS_TO_KEEP>>] \
    --environment "Variables={<<ENV_VARIABLES_TO_KEEP>>}"
```
:::

 </TabItem>
<TabItem value="aws-console" label="AWS Management Console" default>

## Deploying via the AWS Management Console

### Add the extension to your Lambda Function

1. In the Lambda Functions screen, choose the function you want to monitor.
![Pick lambda function](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lambda_extensions/lambda-x_1-1.jpg)

2. In the page for the function, scroll down to the `Layers` section and choose `Add Layer`.
![Add layer](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lambda_extensions/lambda-x_1-2.jpg)

3. Select the `Specify an ARN` option, then choose the ARN of the extension with the region code that matches your Lambda Function region from the [**ARNs** table](https://docs.logz.io/docs/shipping/aws/lambda-extensions/#arns), and click the `Add` button.

![Add ARN extension](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lambda_extensions/lambda-x_1-3.jpg)

### Configure the extension parameters

Add environment variables to the function, according to the [**Environment variables** table](https://docs.logz.io/docs/shipping/Compute/Lambda-extensions#environment-variables).


#### Deleting the extension

- To delete the **extension layer**: In your function page, go to the **layers** panel. Click `edit`, select the extension layer, and click `save`.
- To delete the extension's **environment variables**: In your function page, select the `Configuration` tab, select `Environment variables`, click `edit`, and remove the variables that you added for the extension.


</TabItem>
</Tabs>


### Check Logz.io for your logs

Give your logs some time to get from your system to ours. It may take more than one run of the function for the logs to start shipping to your Logz.io account.

:::note
Your lambda logs will appear under the type `lambda-extension-logs`.
:::

#### Pre-Built content

Log in to your Logz.io account and navigate to the [current instructions page](https://app.logz.io/#/dashboard/integrations/Lambda-extensions) to install the pre-built dashboard to enhance the observability of your logs.

<!-- logzio-inject:install:grafana:dashboards ids=["4yDXMhmHwfDYvOO8o0SGon"] -->


## Environment Variables

| Name | Description |Required/Default|
| --- | --- | --- |
| `LOGZIO_LOGS_TOKEN` | Your Logz.io log shipping [token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping). | Required |
| `LOGZIO_LISTENER` | {@include: ../../_include/log-shipping/listener-var.md} For example: `https://listener.logz.io:8071`. | Required |
| `LOGS_EXT_LOG_LEVEL` |  Log level of the extension. Can be set to one of the following: `debug`, `info`, `warn`, `error`, `fatal`, `panic`. |Default: `info` |
| `ENABLE_PLATFORM_LOGS` | The platform log captures runtime or execution environment errors. Set to `true` if you wish the platform logs will be shipped to your Logz.io account. | Default: `false` |
| `GROK_PATTERNS` | Must be set with `LOGS_FORMAT`. Use this if you want to parse your logs into fields. A minified JSON list that contains the field name and the regex that will match the field. To understand more see the [parsing logs](https://docs.logz.io/docs/shipping/aws/lambda-extensions/#parsing-logs) section. | - |
| `LOGS_FORMAT` | Must be set with `GROK_PATTERNS`. Use this if you want to parse your logs into fields. The format in which the logs will appear, in accordance to grok conventions. To understand more see the [parsing logs](https://docs.logz.io/docs/shipping/aws/lambda-extensions/#parsing-logs) section. | - |
| `CUSTOM_FIELDS` | Include additional fields with every message sent, formatted as `fieldName1=fieldValue1,fieldName2=fieldValue2` (**NO SPACES**). A custom key that clashes with a key from the log itself will be ignored. | - |
| `JSON_FIELDS_UNDER_ROOT` | If you log Json messages and would like the fields to be nested at the root of the log, instead of under `message_nested`. | Default: `False` |

## ARNs
### AMD64 Architecture
| Region Name               | Region Code      | AWS ARN                                                                        |
|---------------------------|------------------|--------------------------------------------------------------------------------|
| US East (N. Virginia)     | `us-east-1`      | `arn:aws:lambda:us-east-1:486140753397:layer:LogzioLambdaExtensionLogs:16`      |
| US East (Ohio)            | `us-east-2`      | `arn:aws:lambda:us-east-2:486140753397:layer:LogzioLambdaExtensionLogs:16`      |
| US West (N. California)   | `us-west-1`      | `arn:aws:lambda:us-west-1:486140753397:layer:LogzioLambdaExtensionLogs:16`      |
| US West (Oregon)          | `us-west-2`      | `arn:aws:lambda:us-west-2:486140753397:layer:LogzioLambdaExtensionLogs:15`      |
| Europe (Frankfurt)        | `eu-central-1`   | `arn:aws:lambda:eu-central-1:486140753397:layer:LogzioLambdaExtensionLogs:17`   |
| Europe (Ireland)          | `eu-west-1`      | `arn:aws:lambda:eu-west-1:486140753397:layer:LogzioLambdaExtensionLogs:15`      |
| Europe (Stockholm)        | `eu-north-1`     | `arn:aws:lambda:eu-north-1:486140753397:layer:LogzioLambdaExtensionLogs:16`     |
| Asia Pacific (Sydney)     | `ap-southeast-2` | `arn:aws:lambda:ap-southeast-2:486140753397:layer:LogzioLambdaExtensionLogs:16` |
| Canada (Central)          | `ca-central-1`   | `arn:aws:lambda:ca-central-1:486140753397:layer:LogzioLambdaExtensionLogs:17`   |
| South America (São Paulo) | `sa-east-1`      | `arn:aws:lambda:sa-east-1:486140753397:layer:LogzioLambdaExtensionLogs:18`      |
| Asia Pacific (Tokyo)      | `ap-northeast-1` | `arn:aws:lambda:ap-northeast-1:486140753397:layer:LogzioLambdaExtensionLogs:12` |
| Asia Pacific (Singapore)  | `ap-southeast-1` | `arn:aws:lambda:ap-southeast-1:486140753397:layer:LogzioLambdaExtensionLogs:13` |
| Asia Pacific (Mumbai)     | `ap-south-1`     | `arn:aws:lambda:ap-south-1:486140753397:layer:LogzioLambdaExtensionLogs:12`     |
| Asia Pacific (Osaka)      | `ap-northeast-3` | `arn:aws:lambda:ap-northeast-3:486140753397:layer:LogzioLambdaExtensionLogs:13` |
| Asia Pacific (Seoul)      | `ap-northeast-2` | `arn:aws:lambda:ap-northeast-2:486140753397:layer:LogzioLambdaExtensionLogs:13` |
| Europe (London)           | `eu-west-2`      | `arn:aws:lambda:eu-west-2:486140753397:layer:LogzioLambdaExtensionLogs:14`      |
| Europe (Paris)            | `eu-west-3`      | `arn:aws:lambda:eu-west-3:486140753397:layer:LogzioLambdaExtensionLogs:13`      |

### ARM64 Architecture
| Region Name               | Region Code      | AWS ARN                                                                           |
|---------------------------|------------------|-----------------------------------------------------------------------------------|
| US East (N. Virginia)     | `us-east-1`      | `arn:aws:lambda:us-east-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |
| US East (Ohio)            | `us-east-2`      | `arn:aws:lambda:us-east-2:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |
| US West (N. California)   | `us-west-1`      | `arn:aws:lambda:us-west-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |
| US West (Oregon)          | `us-west-2`      | `arn:aws:lambda:us-west-2:486140753397:layer:LogzioLambdaExtensionLogsArm:7`      |
| Europe (Frankfurt)        | `eu-central-1`   | `arn:aws:lambda:eu-central-1:486140753397:layer:LogzioLambdaExtensionLogsArm:7`   |
| Europe (Ireland)          | `eu-west-1`      | `arn:aws:lambda:eu-west-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |
| Europe (Stockholm)        | `eu-north-1`     | `arn:aws:lambda:eu-north-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8`     |
| Asia Pacific (Sydney)     | `ap-southeast-2` | `arn:aws:lambda:ap-southeast-2:486140753397:layer:LogzioLambdaExtensionLogsArm:7` |
| Canada (Central)          | `ca-central-1`   | `arn:aws:lambda:ca-central-1:486140753397:layer:LogzioLambdaExtensionLogsArm:7`   |
| South America (São Paulo) | `sa-east-1`      | `arn:aws:lambda:sa-east-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |
| Asia Pacific (Tokyo)      | `ap-northeast-1` | `arn:aws:lambda:ap-northeast-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8` |
| Asia Pacific (Singapore)  | `ap-southeast-1` | `arn:aws:lambda:ap-southeast-1:486140753397:layer:LogzioLambdaExtensionLogsArm:8` |
| Asia Pacific (Mumbai)     | `ap-south-1`     | `arn:aws:lambda:ap-south-1:486140753397:layer:LogzioLambdaExtensionLogsArm:7`     |
| Asia Pacific (Osaka)      | `ap-northeast-3` | `arn:aws:lambda:ap-northeast-3:486140753397:layer:LogzioLambdaExtensionLogsArm:8` |
| Asia Pacific (Seoul)      | `ap-northeast-2` | `arn:aws:lambda:ap-northeast-2:486140753397:layer:LogzioLambdaExtensionLogsArm:8` |
| Europe (London)           | `eu-west-2`      | `arn:aws:lambda:eu-west-2:486140753397:layer:LogzioLambdaExtensionLogsArm:7`      |
| Europe (Paris)            | `eu-west-3`      | `arn:aws:lambda:eu-west-3:486140753397:layer:LogzioLambdaExtensionLogsArm:8`      |


:::note
If your AWS region is not in the list, please reach out to Logz.io's support or open an issue in the [project's Github repo](https://github.com/logzio/logzio-lambda-extensions).
:::

## Parsing logs

By default, the extension sends the logs as strings.
If your logs are formatted, and you wish to parse them to separate fields, the extension will use the [grok library](https://github.com/vjeantet/grok) to parse grok patterns.
You can see all the pre-built grok patterns (for example `COMMONAPACHELOG` is already a known pattern in the library) [here](https://github.com/vjeantet/grok/tree/master/patterns).
If you need to use a custom pattern, you can use the environment variables `GROK_PATTERNS` and `LOGS_FORMAT`.

### Example

For logs that are formatted like this:

```python
<<timestamp>> <<app_name>>: <<message>>
# Examples
May 04 2024 10:48:34.244 my_app: an awesome message
May 04 2024 10:50:46.532 logzio_sender: Successfully sent bulk to logz.io, size: 472
```

In Logz.io we wish to have `timestamp`, `app_name` and `message` in their own fields.  
To do so, we'll set the environment variables as follows:

#### GROK_PATTERNS

The `GROK_PATTERNS` variable contains definitions of custom grok patterns and should be in a JSON format.   
- key - is the custom pattern name. 
- value - the regex that captures the pattern.

In our example:
- `timestamp` - matching the regex `\w+ \d{2} \d{4} \d{2}:\d{2}:\d{2}\.\d{3}`.
- `app_name` - always non-space character sequence, so matching `\S+`.
- `message` -  have strings containing whitespaces, letters and numbers. So matching `.*`.

For the regex that matches `app_name` and `message` there are built in grok patterns (we'll see in `LOGS_FORMAT` explanation), so we only need to define custom pattern for our `timestamp`.  
Meaning we can set `GROK_PATTERNS` as: 
``` json
{"MY_CUSTOM_TIMESTAMP":"\\w+ \\d{2} \\d{4} \\d{2}:\\d{2}:\\d{2}\\.\\d{3}"}
```

#### LOGS_FORMAT

The `LOGS_FORMAT` variable contains the full grok pattern that will match the format of the logs, using known patterns and the custom patterns that were defined in `GROK_PATTERNS` (if defined).  
The variable should be in a grok format: 
```
%{GROK_PATTERN_NAME:WANTED_FIELD_NAME}
```

:::warning
The `WANTED_FIELD_NAME` cannot contain a dot (`.`).
:::

In our example: 
- `timestamp` - matching the custom pattern we defined previously `MY_CUSTOM_TIMESTAMP`.
- `app_name` - is matching the known grok pattern `NOTSPACE`.
- `message` -  is matching the known grok pattern `GREEDYDATA`.

So we will set `LOGS_FORMAT` as: 
```
^%{MY_CUSTOM_TIMESTAMP:timestamp} %{NOTSPACE:app_name}: %{GREEDYDATA:message}
```

The log example from above: 
```
May 04 2024 10:48:34.244 my_app: an awesome message
```
Will be parsed to look like this:

```
timestamp: May 04 2024 10:48:34.244
app_name: my_app
message: an awesome message
```

This project uses an external module for its grok parsing. To learn more about it, see the [grok library repo](https://github.com/vjeantet/grok).

### Nested fields

**As of v0.2.0** the extension can detect if a log is in a JSON format, and to parse the fields to appear as nested fields in the Logz.io app.
For example, the following log:

```json
{ "foo": "bar", "field2": "val2" }
```

Will appear under the fields:
```
message_nested.foo: bar
message_nested.field2: val2
```

**As of v0.3.3**, to have the fields nested under the root (instead of under `message_nested`), set the `JSON_FIELDS_UNDER_ROOT` environment variable as `true`.  
It is useful in cases where the passed object is in fact meant to be that of a message plus metadata fields.  
For example, the following log:

```json
{ "message": "hello", "foo": "bar" }
```

Will appear under the fields:
```
message: hello
foo: bar
```

**Note:** The user must insert a valid JSON. Sending a dictionary or any key-value data structure that is not in a JSON format will cause the log to be sent as a string.
