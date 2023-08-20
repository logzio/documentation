---
id: cloudwatch-logs
title: CloudWatch Logs with a Firehose Delivery Stream
overview: This project deploys instrumentation that allows shipping Cloudwatch logs to Logz.io, with a Firehose Delivery Stream.
product: ['logs']
os: ['windows', 'linux']
filters: ['AWS', 'Monitoring']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-cloudwatch.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

 This project deploys instrumentation that allows shipping Cloudwatch logs to Logz.io, with a Firehose Delivery Stream. It uses a Cloudformation template to create a Stack that deploys:

* Firehose Delivery Stream with Logz.io as the stream's destination.
* Lambda function that adds Subscription Filters to Cloudwatch Log Groups, as defined by user's input.
* Roles, log groups, and other resources that are necessary for this instrumentation.


##### Auto-deploy the Stack in the relevant region


To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                             |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)     | 
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)         | 
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)           | 
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)         | 
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>) | 
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/firehose-logs/0.0.1/sam-template.yaml&stackName=logzio-firehose&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://aws-firehose-logs-<<LISTENER-HOST>>)     |

##### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                                  | Description                                                                                                                                                                                                                                              | Required/Default  |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| `logzioToken`                              | The [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship logs to.                                                                                                                                                   | **Required**      |
| `logzioListener`                           | Listener host.                                                                                                                                                                                                                                           | **Required**      |
| `logzioType`                               | The log type you'll use with this Lambda. This can be a [built-in log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), or a custom log type.                                                                                 | `logzio_firehose` |
| `services`                                 | A comma-seperated list of services you want to collect logs from. Supported options are: `apigateway`, `rds`, `cloudhsm`, `cloudtrail`, `codebuild`, `connect`, `elasticbeanstalk`, `ecs`, `eks`, `aws-glue`, `aws-iot`, `lambda`, `macie`, `amazon-mq`. | -                 |
| `customLogGroups`                          | A comma-seperated list of custom log groups you want to collect logs from                                                                                                                                                                                | -                 |
| `triggerLambdaTimeout`                     | The amount of seconds that Lambda allows a function to run before stopping it, for the trigger function.                                                                                                                                                 | `60`              |
| `triggerLambdaMemory`                      | Trigger function's allocated CPU proportional to the memory configured, in MB.                                                                                                                                                                           | `512`             |
| `triggerLambdaLogLevel`                    | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`                                                                                                                                                     | `info`            |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination                                                                                                                                 | `60`              |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination                                                                                                                                | `5`               |


AWS limits every log group to have up to 2 subscription filters. If your chosen log group already has 2 subscription filters, the trigger function won't be able to add another one.
{:.info-box.important}





##### Send logs

Give the stack a few minutes to be deployed.

Once new logs are added to your chosen log group, they will be sent to your Logz.io account.

If you've used the `services` field, you'll have to **wait 6 minutes** before creating new log groups for your chosen services. This is due to cold start and custom resource invocation, that can cause the Lambda to behave unexpectedly.
{:.info-box.important}

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).