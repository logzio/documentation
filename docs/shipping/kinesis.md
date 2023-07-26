---
id: Kinesis
title: Kinesis
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/Amazon-Kinesis-Data-Firehose.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
 

#### Manual configuration with a Lambda function

{@include: ../_include/log-shipping/note-lambda-test.md}

 

##### Create a new Lambda function

This Lambda function will consume a Kinesis data stream and sends the logs to Logz.io in bulk over HTTP.

Open the AWS Lambda Console, and click **Create function**.
Choose **Author from scratch**, and use this information:

* **Name**: We suggest adding the log type to the name, but you can name this function whatever you want.
* **Runtime**: Choose **Python 3.7**
* **Role**: Use a role that has `AWSLambdaKinesisExecutionRole` permissions.

Click **Create Function** (bottom right corner of the page). After a few moments, you'll see configuration options for your Lambda function.

You'll need this page later on, so keep it open.

##### Download the Kinesis stream shipper

Download the [latest Kinesis stream shipper](https://github.com/logzio/logzio_aws_serverless/releases). It is a zip file.


##### Upload the zip file and set environment variables

In the _Function_ code section of Lambda, find the **Code entry type** list.
Choose **Upload a .ZIP file** from this list.

Click **Upload**, and choose the zip file you created earlier (`logzio-kinesis.zip`).

In the _Environment variables_ section, set your Logz.io account token, URL, and log type, and any other variables that you need to use.

###### Environment variables

| Parameter | Description | Required/Default |
|---|---|---|
| TOKEN | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html}  | Required |
| REGION | Logz.io 2-letter region code. {@include: ../_include/log-shipping/listener-var.html} | Required |
| URL (_Deprecated_) | Use REGION instead.  | -- |
| TYPE | The log type you'll use with this Lambda. You should create a new Lambda for each log type you use. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type. | `kinesis_lambda` |
| FORMAT | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| COMPRESS | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `true` |
| MESSAGES_ARRAY (_Optional_) | Name the field containing a JSON array that will be used to split the log document. [Learn more]({{site.baseurl}}/user-guide/mapping-and-parsing/split-json-array.html). **Note**: This option only works if the `FORMAT` is set to `json`. | -- |


##### Configure the function's basic settings

In Basic settings, we recommend starting with these settings:

* **Memory**: 512 MB
* **Timeout**: 1 min 0 sec

:::note
These default settings are just a starting point. Check your Lambda usage regularly, and adjust these values if you need to.
:::
 

##### Set the Kinesis event trigger

Find the **Add triggers** list (left side of the Designer panel). Choose **Kinesis** from this list.

Below the Designer, you'll see the Configure triggers panel. Choose the **Kinesis stream** that the Lambda function will watch.

Click **Add**, and then click **Save** at the top of the page.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 

#### Automated CloudFormation deployment

{@include: ../_include/log-shipping/note-lambda-test.md}

**Before you begin, you'll need**:

* AWS CLI
* An S3 bucket to store the CloudFormation package

 

##### Download the Kinesis stream shipper

Download the [latest Kinesis stream shipper](https://github.com/logzio/logzio_aws_serverless/releases). It is a zip file.

##### Create the CloudFormation package and upload to S3

Create the CloudFormation package using the AWS CLI.
Replace `<<YOUR-S3-BUCKET>>` with the S3 bucket name where you'll be uploading this package.

```shell
curl -o sam-template.yaml https://raw.githubusercontent.com/logzio/logzio_aws_serverless/master/python3/kinesis/sam-template.yaml
aws cloudformation package \
  --template sam-template.yaml \
  --output-template-file kinesis-template.output.yaml \
  --s3-bucket <<YOUR-S3-BUCKET>>
```

##### Deploy the CloudFormation package

Deploy the CloudFormation package using AWS CLI.

For a complete list of options, see the configuration parameters below the code block. 👇

```shell
aws cloudformation deploy \
--template-file $(pwd)/kinesis-template.output.yaml \
--stack-name logzio-kinesis-logs-lambda-stack \
--parameter-overrides \
  LogzioTOKEN='<<LOG-SHIPPING-TOKEN>>' \
  KinesisStream='<<KINESIS-STREAM-NAME>>' \
--capabilities "CAPABILITY_IAM"
```

###### Parameters

| Parameter | Description |  Required/Default |
|---|---|---|
| LogzioTOKEN | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html} | Required  |
| KinesisStream | The name of the Kinesis stream where this function will listen for updates. | Required  |
| LogzioREGION | Two-letter region code, or blank for US East (Northern Virginia). Logz.io 2-letter region code. {@include: ../_include/log-shipping/listener-var.html} | Required | 
| LogzioURL (Deprecated) | Use LogzioREGION instead. | -- |
| LogzioTYPE | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type.    You should create a new Lambda for each log type you use. | `kinesis_lambda` |
| LogzioFORMAT  | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| LogzioCOMPRESS | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `true` |
| KinesisStreamBatchSize | The largest number of records to read from your stream at one time. | `100` |
| KinesisStreamStartingPosition | The position in the stream to start reading from. For more information, see [ShardIteratorType](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) in the Amazon Kinesis API Reference. | `LATEST` |


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 
#### Deployment using a module
  
Deploy this integration to add a module for Kinesis to your existing stack. This integration uses Cloudwatch Public Registry.

:::note
Logz.io Public Registry extensions are currently only available on the AWS region `us-east-1`.
:::
 

{@include: ../_include/log-shipping/note-lambda-test.md}

**Before you begin, you'll need**:

* A CloudFormation stack
* An S3 bucket to store the CloudFormation package

 

##### Select the Logz.io Kinesis extension

1. Navigate to **CloudFormation > Registry > Public extensions**.
2. Set **Extension type > Modules** and **Publisher > Third party**.
3. Select **Logzio::KinesisShipper::KinesisShipper::MODULE**.


##### Activate the Logz.io Kinesis extension

1. On the **Logzio::KinesisShipper::KinesisShipper::MODULE** select **Activate**.
2. In the **Extension details** section, select **Use default**.
3. In the **Automatic updates** section, select **On**.
4. Select **Activate extension**.

##### Copy the configuration template

On the **Logzio::KinesisShipper::KinesisShipper::MODULE** page, navigate to **Example template** and select **Copy template**.

##### Add your stack values to the configuration template

```yaml
{
    "Resources": {
        "MyModule": {
            "Type": "Logzio::KinesisShipper::KinesisShipper::MODULE",
            "Properties": {
                "LogzioTOKEN": "<<LOG-SHIPPING-TOKEN>>",
                "LogzioFORMAT": "LogzioFORMAT",
                "LogzioREGION": "LogzioREGION",
                "LogzioCOMPRESS": "LogzioCOMPRESS",
                "LogzioMessagesArray": "LogzioMessagesArray",
                "KinesisStreamBatchSize": "KinesisStreamBatchSize",
                "LogzioURL": "https://<<LISTENER-HOST>>:8071",
                "KinesisStreamStartingPosition": "KinesisStreamStartingPosition",
                "LogzioTYPE": "LogzioTYPE",
                "KinesisStream": "KinesisStream"
            }
        }
    }
}
```

Save the template as a yaml file and add the values of your stack to the as per the table below.

| Parameter | Description |  Required/Default |
|---|---|---|
| LogzioTOKEN | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html} | Required  |
| KinesisStream | The name of the Kinesis stream where this function will listen for updates. | Required  |
| LogzioREGION | Two-letter region code, or blank for US East (Northern Virginia). Logz.io 2-letter region code. | Required | 
| LogzioURL | {@include: ../_include/log-shipping/listener-var.html} | -- |
| LogzioTYPE | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type.    You should create a new Lambda for each log type you use. | `logzio_kinesis_stream` |
| LogzioFORMAT  | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| LogzioCOMPRESS | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `true` |
| KinesisStreamBatchSize | The largest number of records to read from your stream at one time. | `100` |
| KinesisStreamStartingPosition | The position in the stream to start reading from. For more information, see [ShardIteratorType](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) in the Amazon Kinesis API Reference. | `LATEST` |
| LogzioMessagesArray | Set this variable to split the a record into multiple logs based on a field containing an array |  |

##### Add your stack values to the configuration template

If you are creating a new stack:

1. In step 1 of the **Create stack** process, select **Template is ready**.
2. Select **Upload a template file**.

If you are editing an existing stack:

1. Select the stack.
2. Select **Update**.
3. Select **Edit template in designer**.
4. Paste the content of the yaml file into the **Resources** section of the template as follows:

   ```yaml
   "MyModule": {
               "Type": "Logzio::KinesisShipper::KinesisShipper::MODULE",
               "Properties": {
                   "LogzioTOKEN": "<<LOG-SHIPPING-TOKEN>>",
                   "LogzioFORMAT": "LogzioFORMAT",
                   "LogzioREGION": "LogzioREGION",
                   "LogzioCOMPRESS": "LogzioCOMPRESS",
                   "LogzioMessagesArray": "LogzioMessagesArray",
                   "KinesisStreamBatchSize": "KinesisStreamBatchSize",
                   "LogzioURL": "https://<<LISTENER-HOST>>:8071",
                   "KinesisStreamStartingPosition": "KinesisStreamStartingPosition",
                   "LogzioTYPE": "LogzioTYPE",
                   "KinesisStream": "KinesisStream"
               }
           }
   ```
5. If required, change the module name by editing the `"MyModule"` value.



  