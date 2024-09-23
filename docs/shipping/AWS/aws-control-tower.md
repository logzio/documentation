---
id: AWS-Control-Tower
title: AWS Control Tower
overview: AWS Control Tower is a tool to control a top-level summary of policies applied to the AWS environment.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-control-tower.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---




:::note
This integration is currently released as a beta version.
:::
 


AWS Control Tower is a tool to control a top-level summary of policies applied to the AWS environment. This integration sends logs from S3 buckets that the AWS Control Tower automatically creates in your AWS environment.

 

## Deploy an S3 Hook Lambda function

### Create Stack in the relevant region

:::note
The stacks must be deployed in the same region as the S3 buckets.
:::
 

To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                       |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)     | 
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)         | 
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)           | 
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook) | 
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook) | 
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook) | 
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)         | 
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook) | 
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook) | 
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/s3-hook/0.4.2/sam-template.yaml&stackName=logzio-s3-hook)     | 

### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter        | Description                                                                                                                                                                                                                                                         | Required/Default   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| `logzioListener` | The Logz.io listener URL for your region. (For more details, see the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/)                                                                                                                   | **Required**       |
| `logzioToken`    | Your Logz.io log shipping token.                                                                                                                                                                                                                                    | **Required**       |
| `logLevel`       | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`.                                                                                                                                                               | Default: `info`    |
| `logType`        | The log type you'll use with this Lambda. This is shown in your logs under the type field in Kibana. Logz.io applies parsing based on the log type.                                                                                                                 | Default: `s3_hook` |
| `includePathsRegexes`   | Comma-seperated list of regexes that match the paths you'd like to pull logs from. That field is mutually exclusive with the `excludePathsRegexes` field.                                                                                                                                                                                 | -                  |
| `excludePathsRegexes`   | Comma-seperated list of regexes that match the paths that won't pull logs from. That field is mutually exclusive with the `includePathsRegexes` field.                                                                                                                                                                                    | -                  |
| `pathToFields`   | Fields from the path to your logs directory that you want to add to the logs. For example, `org-id/aws-type/account-id` will add each of the fields `org-id`, `aws-type` and `account-id` to the logs that are fetched from the directory that this path refers to. | -                  |


### Add trigger

Give the stack a few minutes to be deployed.

Once your Lambda function is ready, you'll need to manually add a trigger. This is due to Cloudformation limitations.

Go to the function's page, and click on **Add trigger**.

![Step 5 screenshot](https://dytvr9ot2sszz.cloudfront.net/logz-docs/control-tower/s3-hook-stack-05.png)

Then, choose **S3** as a trigger, and fill in:

- **Bucket**: Your bucket name.
- **Event type**: Choose option `All object create events`.
- Prefix and Suffix should be left empty.

Confirm the checkbox, and click **Add*.

![Step 5 screenshot](https://dytvr9ot2sszz.cloudfront.net/logz-docs/control-tower/s3-hook-stack-06.png)


### Deploy the Control Tower stack

This stack creates a Lambda function, an EventBridge rule and IAM roles to automatically add triggers to the S3 Hook Lambda function as the Control Tower is creating new buckets. 



:::note
The stacks must be deployed in the same region as the S3 buckets.
:::
 


To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                           |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     | 
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         | 
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         | 
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/s3-hook/control-tower/0.0.3/sam-template.yaml&stackName=logzio-control-tower&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     | 


### Specify stack details

Specify the stack details as per the table below, check the checkboxes, and select **Create stack**.

| Parameter   | Description                                                                                           | Required/Default |
|-------------|-------------------------------------------------------------------------------------------------------|------------------|
| `logLevel`  | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`. | Default: `info`  |
| `s3HookArn` | The ARN of your S3 Hook Lambda function.                                                              | **Required**     |


:::note
It can take a few minutes after the stack creation for EventBridge rule to be triggered.
:::
 

:::caution Important
To delete the S3 Hook Stack - you'll need to detach the policy "LambdaAccessBuckets" first.
:::
 

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).



 

## Advanced settings

### Automatic parsing

S3 Hook will automatically parse logs in the following cases:

- The object's path contains the phrase `cloudtrail` (case insensitive).

### Filtering files

If you wish to extract logs from specific paths within the bucket, utilize the includePathsRegexes variable. Conversely, if there exist specific paths within the bucket from which you would prefer not to extract logs, the excludePathsRegexes variable should be employed. These variables are mutually exclusive.

Both variables ought to contain a comma-separated list of regular expressions, corresponding either to the paths from which you aim to extract logs (includePathsRegexes), or to the paths you aim to exclude during log extraction (excludePathsRegexes).

:::caution Important
Each time a new object is added to your bucket, this will trigger your Lambda function. Nonetheless, if the key fails to match the regexes, the function will terminate without sending the logs.
:::
 


### Adding object path as logs field

In case you want to use your objects' path as extra fields in your logs, you can do so by using `pathToFields`.

For example, if your objects are under the path: `oi-3rfEFA4/AWSLogs/2378194514/file.log`, where `oi-3rfEFA4` is org id, `AWSLogs` is aws type, and `2378194514` is account id. 

Setting `pathToFields` with the value: `org-id/aws-type/account-id` will add to logs the following fields:
`org-id: oi-3rfEFA4`, `aws-type: AWSLogs`, `account-id: 2378194514`.

:::note
* If you use `pathToFields`, you need to add a value for each subfolder in the path. Otherwise there will be a mismatch and the logs will be sent without fields.
* This will override a field with the same key, if it exists.
* In order for the feature to work, you need to set `pathToFields` from the root of the bucket.
:::
 

 
