---
id: GuardDuty
title: GuardDuty
overview: This integration sends GuardDuty logs.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['AWS', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-guardduty.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

 
## Logs

### Create an EventBridge rule

You'll need to create a new EventBridge rule that will send your GuardDuty findings to a Cloudwatch Log Group.

1. In your **AWS Console**, go to ** Amazon EventBridge** service.
2. In the left menu of Amazon EventBridge, choose **Rules**, then click on **Create rule**.
3. Enter the name of your new rule, and click **Next**.
4. Scroll down to the **Event pattern** panel. In the **AWS service** field, choose **GuardDuty**. In the **Event type** field choose **All Events**, and click **Next**.
5. For the **Select a target** field, choose **CloudWatch log group**. In the **Log Group** field, choose the first option (`/aws/events`) and enter the name you'd like for your new log group. Click **Next**.
6. Optionally, add tags to your event rule. Click **Next**.
7. Review the details and click **Create rule**.


### Auto-deploy the Stack in the relevant region

This integration will deploy a Firehose connection with your AWS services to forward logs to Logz.io
To deploy this project, click the button that matches the region you wish to deploy your stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                             |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)     | 
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)         | 
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)         | 
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/firehose-logs/0.3.3/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)     |

#### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.
Add the CloudWatch log group name you created in the first step to field `customLogGroups`.

| Parameter                                  | Description                                                                                                                                                                                                                                              | Required/Default  |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| `logzioToken`                              | The [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship logs to.                                                                                                                                                   | **Required**      |
| `logzioListener`                           | Listener host.                                                                                                                                                                                                                                           | **Required**      |
| `logzioType`                               | The log type you'll use with this Lambda. This can be a [built-in log type](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types), or a custom log type.                                                                                 | `logzio_firehose` |
| `services`                                 | A comma-seperated list of services you want to collect logs from. Supported options are: `apigateway`, `rds`, `cloudhsm`, `cloudtrail`, `codebuild`, `connect`, `elasticbeanstalk`, `ecs`, `eks`, `aws-glue`, `aws-iot`, `lambda`, `macie`, `amazon-mq`. | -                 |
| `customLogGroups`                          | A comma-separated list of custom log groups to collect logs from, or the ARN of the Secret parameter ([explanation below](https://docs.logz.io/docs/shipping/aws/guardduty/#custom-log-group-list-exceeds-4096-characters-limit)) storing the log groups list if it exceeds 4096 characters. **Note**: You can also specify a prefix of the log group names by using a wildcard at the end (e.g., `prefix*`). This will match all log groups that start with the specified prefix.                                                                                                                                                                                | -                 |
| `useCustomLogGroupsFromSecret`             | If you want to provide list of `customLogGroups` which exceeds 4096 characters, set to `true` and configure your customLogGroups as [defined below](https://docs.logz.io/docs/shipping/aws/guardduty/#custom-log-group-list-exceeds-4096-characters-limit).                                               | `false`           |
| `triggerLambdaTimeout`                     | The amount of seconds that Lambda allows a function to run before stopping it, for the trigger function.                                                                                                                                                 | `60`              |
| `triggerLambdaMemory`                      | Trigger function's allocated CPU proportional to the memory configured, in MB.                                                                                                                                                                           | `512`             |
| `triggerLambdaLogLevel`                    | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`                                                                                                                                                     | `info`            |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination                                                                                                                                 | `60`              |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination                                                                                                                                | `5`               |


:::caution Important
AWS limits every log group to have up to 2 subscription filters. If your chosen log group already has 2 subscription filters, the trigger function won't be able to add another one.
:::

##### Custom Log Group list exceeds 4096 characters limit
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

#### Send logs

Give the stack a few minutes to be deployed.

Once new logs are added to your chosen log group, they will be sent to your Logz.io account.

Your GuardDuty logs will be sent in accordance with your GuardDuty configuration.
GuardDuty publishes its findings to EventBridge every 6 hours. If you want to configure it differently:
1. Go to your GuardDuty settings.
2. Scroll down to **Findings export options**. Click on **Edit** of **Frequency**.
3. Choose your prefered frequency to export GuardDuty findings.

You can export a sample finding by going to GuardDuty **settings** and clicking the **Generate sample findings**.


:::caution Important
If you've used the `services` field, you'll have to **wait 6 minutes** before creating new log groups for your chosen services. This is due to cold start and custom resource invocation, that can cause the Lambda to behave unexpectedly.
:::

#### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).
