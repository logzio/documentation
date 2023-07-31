---
id: GuardDuty
title: GuardDuty
overview: This integration sends GuardDuty logs.
product: ['logs']
os: ['windows', 'linux']
filters: ['AWS', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-guardduty.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---

 

#### Manual Lambda configuration

{@include: ../_include/log-shipping/note-lambda-test.md}


 

##### Create a new Kinesis data stream

If you're not already sending your GuardDuty logs through a Kinesis data stream, create one using the [Kinesis console](https://console.aws.amazon.com/kinesis).

Save the name of the data stream—you'll need this in the next step.

##### Configure CloudWatch Events

In the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) left menu, click **Events > Rules**, and then click **Create rule**.

In the Event Source panel (on the left), set these options:

* Choose **Event Pattern**.
* In the **Build event pattern** section, choose **GuardDuty** from the **Service Name** list.
  You can choose any **Event Type** that you need.

In the Targets panel (on the right), click **Add target**, and choose **Kinesis stream**.
Choose the Kinesis data stream from step 1 from the **Stream** list.

Click **Configure details** (lower right corner).

##### Create a new IAM role

Create a new IAM role and attach the **AWSLambdaKinesisExecutionRole** policy to the new role.

##### Create a new Lambda function

This Lambda function will collect CloudWatch logs and sends them to Logz.io in bulk over HTTP.

Open the AWS Lambda Console, and click **Create function**.
Choose **Author from scratch**, and use this information:

* **Name**:
  We suggest adding the log type to the name, but you can name this function whatever you want.
* **Runtime**:
  Choose **Python 3.7**
* **Role**:
  Select **Use an existing role**.
  Then, select the role that you created in the previous step. It should have the **AWSLambdaKinesisExecutionRole** policy.
   
Click **Create Function** (bottom right corner of the page).
After a few moments, you'll see configuration options for your Lambda function.

You'll need this page later on, so keep it open.

##### Download the Kinesis stream shipper

Download the latest Kinesis stream shipper zip file from the [Logz.io GitHub page](https://github.com/logzio/logzio_aws_serverless/releases).

By default, the zip file will be named `logzio-kinesis-0.0.2.zip`.

##### Upload the zip file

In the _Function_ code section of Lambda, open the **Code entry type** list and select **Upload a .ZIP file**.

Click **Upload** and select the zip file you created in the previous step (`logzio-kinesis-0.0.2.zip`).

##### Set environment variables

In the _Environment variables_ section, set your Logz.io account token, URL, and log type, and any other variables that you need to use.

###### Environment variables

| Parameter | Description | Required/Default |
|---|---|---|
| TOKEN (Required) | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html} | Required  |
| REGION | Two-letter region code, or blank for US East (Northern Virginia). This determines your listener URL (where you're shipping the logs to) and API URL.    You can find your region code in the [Regions and URLs](https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls) table. | Default: *blank* (US East)|
| URL  (Deprecated)| Use REGION instead. Protocol, listener host, and port (for example, `https://<<LISTENER-HOST>>:8071`). {@include: ../_include/log-shipping/listener-var.html}  | Required |
| TYPE | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type.    You should create a new Lambda for each log type you use. | `"guardduty"` |
| FORMAT | `"json"` or `"text"`. If `"json"`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `"text"` |
| COMPRESS | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `false` |


##### Configure the function's basic settings

In Basic settings, we recommend starting with these settings:

* **Memory**: 512 MB
* **Timeout**: 1 min 0 sec

:::note
These default settings are just a starting point. Check your Lambda usage regularly, and adjust these values if you need to.
:::
 

##### Set the Kinesis event trigger

Find the **Add triggers** list (left side of the Designer panel).
Choose **Kinesis** from this list.

Below the Designer, you'll see the Configure triggers panel.
Choose the **Kinesis stream** that the Lambda function will watch.

Click **Add**, and then click **Save** at the top of the page.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 

#### Automated CloudFormation deployment

{@include: ../_include/log-shipping/note-lambda-test.md}


**Before you begin, you'll need**:
AWS CLI,
an S3 bucket to store the CloudFormation package

 

##### Create a new Kinesis data stream

If you're not already sending your GuardDuty logs through a Kinesis data stream, create one using the [Kinesis console](https://console.aws.amazon.com/kinesis).

Select the button below according to the region where you need to deploy the stack.

| REGION           | DEPLOYMENT                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/template?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/template?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)           |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)         |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/template?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/aws-kinesis/0.0.2/auto-deployment.yaml&stackName=guardduty-log-shipper&param_LogzioTOKEN=<<LOG-SHIPPING-TOKEN>>) |

![Create stack](https://dytvr9ot2sszz.cloudfront.net/logz-docs/guardduty/first.png)

Keep the default setting in the **Create stack** screen and select **Next**.

##### Specify the stack details

![Specify stack details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/guardduty/second.png)


Specify the stack details as per the table below and select **Next**.


| Parameter                     | Description                                                                                                                                                                                                                                                                                        | Required/Default           |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| LogzioTOKEN                   | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html}                                                                                                                                                                                                                     | Required                   |
| KinesisStream                 | The name of the Kinesis stream where this function will listen for updates.                                                                                                                                                                                                                        | Required                   |
| LogzioREGION                  | Two-letter region code, or blank for US East (Northern Virginia). This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the [Regions and URLs](https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls) table. | Default: _blank_ (US East) |
| LogzioURL (Deprecated)        | Use LogzioREGION instead. Protocol, listener host, and port (for example, `https://<<LISTENER-HOST>>:8071`). {@include: ../_include/log-shipping/listener-var.html}                                                                                                                                          | Required                   |
| LogzioTYPE                    | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type. You should create a new Lambda for each log type you use.                                                                     | `guardduty`                |
| LogzioFORMAT                  | `"json"` or `"text"`. If `"json"`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.                                                                                                                                         | `"text"`                   |
| LogzioCOMPRESS                | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs.                                                                                                                                                                                                      | `false`                    |
| KinesisStreamBatchSize        | The largest number of records to read from your stream at one time.                                                                                                                                                                                                                                | `100`                      |
| KinesisStreamStartingPosition | The position in the stream to start reading from. For more information, see [ShardIteratorType](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) in the Amazon Kinesis API Reference.                                                                            | `"LATEST"`                 |

##### Configure the stack options

![Configure stack options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/guardduty/third.png)

Specify the **Key** and **Value** parameters for the **Tags** and select **Next**.

##### Review the deployment

![Review deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/guardduty/fourth.png)

Confirm that you acknowledge that AWS CloudFormation might create IAM resources and select **Create stack**.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
  