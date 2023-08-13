---
id: AWS-Cost-and-Usage-Reports
title: AWS Cost and Usage Reports
overview: AWS Cost and Usage Reports function tracks your AWS usage and provides estimated charges associated with your account. 
product: ['logs']
os: ['windows', 'linux']
filters: ['AWS', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

AWS Cost and Usage Reports function tracks your AWS usage and provides estimated charges associated with your account. This integration allows you to ship logs from your AWS Cost and Usage Reports to your Logz.io account.

:::caution Important 
Your Lambda function needs to run within the AWS Lambda limits, such as memory allocation and timeout. Make sure you understand these limits. If you can't adjust your settings to stay within the Lambda limits, you can use the AWS [Support Center console](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase) to request an increase. [Learn more about AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).
:::
 
  

## Automated CloudFormation deployment

This deployment will automatically create the following resources:

![Resources](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/Resources.png)

 

### Login to your account

To begin, you need to login to your AWS account.

### Create a new stack

Select the button below to create a new stack dedicated to sending the AWS cost and usage reports to Logz.io.

[![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-cost-usage-auto-deployment/auto-deployment.yaml&stackName=logzio-aws-cost-usage-auto-deployment)

![Create stack](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/create_stack.png)

Keep the default setting in the **Create stack** screen and select **Next**.

### Specify the stack details

![Specify stack details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/specify_stack_details.png)

Specify the stack details as per the table below and select **Next**.

| Parameter | Description |
|---|---|
| Stack name | logzio-cur-auto-deployment |
| CloudWatchEventScheduleExpression | `Default: rate(10 hours)` The scheduling expression that determines when and how often the Lambda function runs. Logz.io recommends to start with 10 hours rate. |
| LambdaMemorySize | `Default: 1024 (MB)` The amount of memory available to the function at runtime. Logz.io recommends to start with 1024 MB. |
| LambdaTimeout | `Default: 300 (seconds)` The amount of time that Lambda allows a function to run before stopping it. Logz.io recommends to start with 300 seconds (5 minutes). |
| LogzioToken | Your Logz.io log shipping token:`<<LOG-SHIPPING-TOKEN>>` {@include: ../_include/log-shipping/log-shipping-token.html} |
| LogzioURL | The Logz.io listener URL: `https://<<LISTENER-HOST>>:8071` {@include: ../_include/log-shipping/listener-var.html} |
| ReportAdditionalSchemaElements | Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase the report size and might affect performance. AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.) This is an optional parameter. |
| ReportName | The name of report that you want to create. |
| ReportPrefix | The prefix that AWS adds to the report name when AWS delivers the report. |
| ReportTimeUnit | The granularity of the line items in the report. Can be Hourly, Daily or Monthly. (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.) |
| S3BucketName | The name for the bucket which will contain the report files. |

### Configure the stack options

![Configure stack options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/specify_stack_details.png)

Specify the **Key** and **Value** parameters for the **Tags** and select **Next**.

### Review the deployment

![Review deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/review_deployment.png)
![Confirm deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/confirm_and_create_stack.png)

Confirm that you acknowledge that AWS CloudFormation might create IAM resources and select **Create stack**.

### Check Logz.io for your logs

Give your logs the time specified in `CloudWatchEventScheduleExpression` to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

All logs that were sent from the Lambda function will be under the type **billing**.
  
To get more out of this functionality, you can enable a dedicated AWS cost and usage dashboard in [ELK Apps](https://app.logz.io/#/dashboard/elk-apps).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

 

## Deployment using a module
  
Deploy this integration to add a module for AWS cost and usage report to your existing stack. This integration uses CloudWatch Public Registry.

:::note
Logz.io Public Registry extensions are currently only available on the AWS region `us-east-1`.
:::
 

{@include: ../_include/log-shipping/note-lambda-test.md}

**Before you begin, you'll need**:

* A CloudFormation stack
* An S3 bucket to store the CloudFormation package

 

### Select the Logz.io AWS Cost and Usage extension

1. Navigate to **CloudFormation > Registry > Public extensions**.
2. Set **Extension type > Modules** and **Publisher > Third party**.
3. Select **Logzio::awsCostAndUsage::cur::MODULE**.


### Activate the Logz.io AWS Cost and Usage extension

1. On the **Logzio::awsCostAndUsage::cur::MODULE** select **Activate**.
2. In the **Extension details** section, select **Use default**.
3. In the **Automatic updates** section, select **On**.
4. Select **Activate extension**.

### Copy the configuration template

On the **Logzio::awsCostAndUsage::cur::MODULE** page, navigate to **Example template** and select **Copy template**.

### Add your stack values to the configuration template

```yaml
{
    "Resources": {
        "MyModule": {
            "Type": "Logzio::awsCostAndUsage::cur::MODULE",
            "Properties": {
                "S3BucketName": "S3BucketName",
                "ReportName": "ReportName",
                "ReportPrefix": "ReportPrefix",
                "ReportTimeUnit": "ReportTimeUnit",
                "ReportAdditionalSchemaElements": "ReportAdditionalSchemaElements",
                "LogzioURL": "https://<<LISTENER-HOST>>:8071",
                "LogzioToken": "<<LOG-SHIPPING-TOKEN>>",
                "LambdaMemorySize": "LambdaMemorySize",
                "LambdaTimeout": "LambdaTimeout",
                "CloudWatchEventScheduleExpression": "CloudWatchEventScheduleExpression"
            }
        }
    }
}
```

Save the template as a yaml file and add the values of your stack to the as per the table below.

| Parameter | Description |
|---|---|
| CloudWatchEventScheduleExpression | `Default: rate(10 hours)` The scheduling expression that determines when and how often the Lambda function runs. Logz.io recommends to start with 10 hours rate. |
| LambdaMemorySize | `Default: 1024 (MB)` The amount of memory available to the function at runtime. Logz.io recommends to start with 1024 MB. |
| LambdaTimeout | `Default: 300 (seconds)` The amount of time that Lambda allows a function to run before stopping it. Logz.io recommends to start with 300 seconds (5 minutes). |
| LogzioToken | Your Logz.io log shipping token:`<<LOG-SHIPPING-TOKEN>>` {@include: ../_include/log-shipping/log-shipping-token.html} |
| LogzioURL | The Logz.io listener URL: `https://<<LISTENER-HOST>>:8071` {@include: ../_include/log-shipping/listener-var.html} |
| ReportAdditionalSchemaElements | Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase the report size and might affect performance. AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.) This is an optional parameter. |
| ReportName | The name of report that you want to create. |
| ReportPrefix | The prefix that AWS adds to the report name when AWS delivers the report. |
| ReportTimeUnit | The granularity of the line items in the report. Can be Hourly, Daily or Monthly. (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.) |
| S3BucketName | The name for the bucket which will contain the report files. |

### Add your stack values to the configuration template

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
            "Type": "Logzio::awsCostAndUsage::cur::MODULE",
            "Properties": {
                "S3BucketName": "S3BucketName",
                "ReportName": "ReportName",
                "ReportPrefix": "ReportPrefix",
                "ReportTimeUnit": "ReportTimeUnit",
                "ReportAdditionalSchemaElements": "ReportAdditionalSchemaElements",
                "LogzioURL": "LogzioURL",
                "LogzioToken": "<<LOG-SHIPPING-TOKEN>>",
                "LambdaMemorySize": "LambdaMemorySize",
                "LambdaTimeout": "LambdaTimeout",
                "CloudWatchEventScheduleExpression": "CloudWatchEventScheduleExpression"
            }
        }
   ```
5. If required, change the module name by editing the `"MyModule"` value.



 