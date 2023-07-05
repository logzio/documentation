---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---

 

Real-time log collection is the recommended method, as it sends logs immediately as they are generated. However, if you prefer to collect logs at specific time intervals, please refer to the [Logs at user-defined intervals](#intervals) for configuring this option.

#### Logs in realtime

This project will create 2 Lambda functions:

- **Shipper function**: this function is responsible for processing and shipping the Cloudwatch logs to Logz.io. [See here the function's repo](https://github.com/logzio/logzio_aws_serverless/tree/master/python3/cloudwatch).

- **Trigger function**: this function is responsible for adding subscription filters to the desired Cloudwatch log groups, to trigger the shipper function.

When the Trigger function is run for the first time, it will add subscription filters to the log groups chosen by the user. If the user chose a service, the Trigger function will also get triggered whenever a log group is created to check if this log group is for a service that is one of the services that the user has selected. If yes, it will add a subscription filter to it.

 

##### Auto-deploy the Lambda function

👇 To begin, click this button to start the automated deployment. You will need to deploy it in your region.

| REGION           | DEPLOYMENT                                                                                                                                                                                                                                                                                                                                                     |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     | 
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         | 
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           | 
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         | 
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) | 
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/cloudwatch-shipper-trigger/1.1.1/sam-template.yaml&stackName=logzio-cloudwatch&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     |



##### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

###### Shipper config

| Parameter              | Description                                                                                                                                                                                                                             | Required/Default                  |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `logzioToken`          | Replace `<<SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.                                                                                                     | **Required**                      |
| `logGroup\*`                                     | CloudWatch Log Group name from where you want to send logs.                                                                                                                                                                             |
| `logzioListener`       | Listener host, and port (for example, `https://<<LISTENER-HOST>>:8071`).                                                                                                                                                                | **Required**                      |
| `logzioType`           | The log type you'll use with this Lambda. This can be a [built-in log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), or a custom log type. <br> You should create a new Lambda for each log type you use. | `logzio_cloudwatch_logs` |
| `logzioFormat`         | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.                                                                                    | `text`                   |
| `logzioCompress`       | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs.                                                                                                                                           | `true`                   |
| `logzioEnrich`         | Enrich CloudWatch events with custom properties, formatted as `key1=value1;key2=value2`.                                                                                                                                                | -                                 |
| `shipperLogLevel`              | Log level for the shipper function. Possible values are: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.                                                                                                                               | `INFO` |
| `shipperRequestTimeout`                 | Timeout in seconds for each http request for sending logs into logz.io.                                                                                                                                                                 | `15` |

###### Trigger config

| Parameter               | Description                                                                                                                                                                                                                                              | Required/Default |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `services`              | A comma-seperated list of services you want to collect logs from. Supported options are: `apigateway`, `rds`, `cloudhsm`, `cloudtrail`, `codebuild`, `connect`, `elasticbeanstalk`, `ecs`, `eks`, `aws-glue`, `aws-iot`, `lambda`, `macie`, `amazon-mq`. | -                |
| `customLogGroups`       | A comma-seperated list of custom log groups you want to collect logs from                                                                                                                                                                                | -                |
| `triggerLambdaTimeout`  | The amount of seconds that Lambda allows a function to run before stopping it, for the trigger function.                                                                                                                                                 | `60`             |
| `triggerLambdaMemory`   | Trigger function's allocated CPU proportional to the memory configured, in MB.                                                                                                                                                                           | `512`            |
| `triggerLambdaLogLevel` | Log level for the Lambda function. Can be one of: `debug`, `info`, `warn`, `error`, `fatal`, `panic`                                                                                                                                                     | `info`           |

:::note
AWS limits every log group to have up to 2 subscription filters. If your chosen log group already has 2 subscription filters, the trigger function won't be able to add another one.
:::
 


##### Send logs

Give the stack a few minutes to be deployed.

Once new logs are added to your chosen log group, they will be sent to your Logz.io account.

:::note
If you've used the `services` field, you'll have to **wait 6 minutes** before creating new log groups for your chosen services. This is due to cold start and custom resource invocation, that can cause the cause Lambda to behave unexpectedly.
{:.info-box.important}
 

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


 
  
#### Logs at user-defined intervals

By using this integration, you can easily deploy Logz.io's Cloudwatch Fetcher to your K8S cluster. With the Cloudwatch Fetcher, you can define a specific time interval for fetching logs from AWS Cloudwatch and ship them to Logz.io.

Cloudwatch-fetcher's code can be found in the [cloudwatch-fetcher](https://github.com/logzio/cloudwatch-fetcher) Github repo.

* [Using Helm](#using-helm)
* [Using Docker](#using-docker)

##### Using Helm


**Before you begin, you'll need**:

AWS access keys with permissions to:

* `logs:FilterLogEvents`
* `sts:GetCallerIdentity`


:::note
The solution can handle only one AWS account per container. If you want to monitor multiple accounts, you'll need to create multiple deployments, one for each AWS account.
{:.info-box.important}
 



 


##### Add Logz.io Helm repo:

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### Create a configuration file

Create a configuration file for the Cloudwatch fetcher. For example:

```yaml
log_groups:
  - path: '/aws/lambda/my-lambda'
    custom_fields:
      key1: val1
      key2: val2
  - path: 'some-log-group'
  - path: 'newloggroup'
    custom_fields:
      hello: world
aws_region: 'us-east-1'
collection_interval: 10
```

| Field                      | Description                                                                                      | Required/Default |
|----------------------------|--------------------------------------------------------------------------------------------------|------------------|
| `log_groups`               | An array of log group configuration                                                              | **Required**     |
| `log_groups.path`          | The AWS Cloudwatch log group you want to tail                                                    | **Required**     |
| `log_groups.custom_fields` | Array of key-value pairs, for adding custom fields to the logs from the log group                | -                |
| `aws_region`               | The AWS region your log groups are in. **Note** that all log groups should be in the same region | **Required**     |
| `collection_interval`      | Interval **IN MINUTES** to fetch logs from Cloudwatch                                            | Default: `5`     |

##### Deploy the Chart

Use the following command, and replace the placeholders with your parameters:

```shell
helm install -n monitoring --create-namespace \                 
--set secrets.logzioShippingToken="<<LOG-SHIPPING-TOKEN>>" \
--set secrets.logzioListener="<<LISTENER-HOST>>" \
--set secrets.awsAccessKey="<<AWS-ACCESS-KEY>>" \
--set secrets.awsSecretKey="<<AWS-SECRET-KEY>>" \
--set-file fetcherConfig=<<CONFIG-PATH>> \
cloudwatch-fetcher logzio-helm/cloudwatch-fetcher
```

| Parameter | Description |
| --- | --- |
| `<<LOG-SHIPPING-TOKEN>>` | {@include: ../_include/log-shipping/log-shipping-token.html} |
| `<<LISTENER-HOST>>` | {@include: ../_include/log-shipping/listener-var.html}  |
| `<<AWS-ACCESS-KEY>>` | Your AWS access key |
| `<<AWS-SECRET-KEY>>` | Your AWS secret key |
| `<<CONFIG-PATH>>` | Path to the Cloudwatch Fetcher configuration file you created in the previous step |


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Logz.io](https://app.logz.io/).

:::note
Note that the logs will have the original timestamp from Cloudwatch, so when you're searching for them, make sure that you're viewing the relevant time frame.
{:.info-box.important}
 


###### Further Configuration

The above helm install command will deploy a standard configuration version of the Chart.

However, you can modify the Chart by using the --set flag in your helm install command:

| Parameter | Description | Default |
| --- | --- | --- |
| `image` | Container image | `logzio/cloudwatch/fetcher` |
| `imageTag` | Container image tag | `0.0.1` |
| `secrets.enabled` | Specifies whether to create a secret for the deployment | `true` |
| `secrets.name` | Name of the secret | `"logzio-logs-secret-cloudwatch"` |
| `secrets.logzioShippingToken` | Your [Logz.io logs shipping token](https://app.logz.io/#/dashboard/settings/general) | `""`
| `secrets.logzioListener` | Your logz.io [listener url](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs), for example: `listener.logz.io` | `""` (defaults to us region) |
| `secrets.awsAccessKey` | Your AWS access key | `""` |
| `secrets.awsSecretKey` | Your AWS secret key | `""` |
| `persistentVolume.enabled` | Specifies whether to create a persistent volume and persistent volume claim for this release. Disabling will not allow the fetcher to continue from the last time it ran, in case the pod will be stopped | `true` |
| `persistentVolume.storageClassName` | Storage class name | `"logzio-cloudwatch-fetcher"` |
| `persistentVolume.capacity.storage` | Storage requirement for the PV | `50Mi` |
| `persistentVolume.accessModes` | Access modes for the PV | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/cloudwatch-fetcher/values.yaml) |
| `persistentVolume.resources.requests.storage` | Storage request for the PVC | `30Mi` |
| `loggingConfig` | Configuration for the logging of the fetcher | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/cloudwatch-fetcher/values.yaml) |
| `fetcherConfig` | Configuration for the fetcher | `""` |
| `resetPositionFile` | Delete current position file | `false` |


###### Presistent volume

By default, this Helm Chart creates a Persistent Volume (PV) and a Persistent Volume Claim (PVC). These resources enable the Fetcher to save a position file, which records the last time the fetcher extracted logs from Cloudwatch. This is essential to prevent data loss in case the pod stops. If you choose to disable these resources or if your cluster does not allow their creation, some data may be lost if the pod stops.

###### Uninstalling the Chart

To uninstall the Cloudwatch Fetcher release:

```shell
helm uninstall -n monitoring cloudwatch-fetcher
```

 

##### Using Docker


 


##### Pull Docker image

```shell
docker pull logzio/cloudwatch-fetcher:latest
```

##### Create a data volume directory

This directory will store the configuration and position files for the fetcher. The position file enables the fetcher to resume from the last point it fetched in the event that the container was stopped.

```shell
mkdir logzio-cloudwatch-fetcher \
&& cd logzio-cloudwatch-fetcher
``` 

##### Create a configuration file

In the directory you created in the previous step, create a configuration file and name it `config.yaml`.

| Field                      | Description                                                                                      | Required/Default |
|----------------------------|--------------------------------------------------------------------------------------------------|------------------|
| `aws_region`               | The AWS region your log groups are in. **Note** that all log groups should be in the same region. | **Required**     |
| `log_groups`               | An array of log group configuration                                                              | **Required**     |
| `log_groups.path`          | The AWS Cloudwatch log group you want to tail                                                    | **Required**     |
| `log_groups.custom_fields` | Array of key-value pairs, for adding custom fields to the logs from the log group                | -                |
| `collection_interval`      | Interval **IN MINUTES** to fetch logs from Cloudwatch                                            | Default: `5`     |


###### Configuration example

**See this [config sample](https://github.com/logzio/cloudwatch-fetcher/blob/master/config.yaml) for example.**

##### Run the docker container

```shell
 docker run --name logzio-cloudwatch-fetcher \
-e AWS_ACCESS_KEY_ID=<<AWS-ACCESS-KEY>> \
-e AWS_SECRET_ACCESS_KEY=<<AWS-SECRET-KEY>> \
-e LOGZIO_LOG_SHIPPING_TOKEN=<<LOG-SHIPPING-TOKEN>> \
-e LOGZIO_LISTENER=https://<<LISTENER-HOST>>:8071 \
-v "$(pwd)":/logzio/src/shared \
logzio/cloudwatch-fetcher:latest
```

Replace the following:

| Parameter                        | Description                                                                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `<<AWS-ACCESS-KEY>>`             | Your AWS access key                                                                                                                             |
| `<<AWS-SECRET-KEY>>`             | Your AWS secret key                                                                                                                             |
| `<<LOG-SHIPPING-TOKEN>>` | Your [Logz.io logs shipping token](https://app.logz.io/#/dashboard/settings/general)                                                            |
| `<<LISTENER-HOST>>`            | Your logz.io [listener url](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs), for example: `listener.logz.io` |

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Logz.io](https://app.logz.io/).

**NOTE** that the logs will have the original timestamp from Cloudwatch, so when you're searching for them, make sure that you're viewing the relevant time frame.

 

##### Stop docker container

Upon stopping the container, the code will continue to run until the completion of the current iteration. To ensure the iteration finishes on time, please provide a grace period of 30 seconds when executing the 'docker stop' command:

```shell
docker stop -t 30 logzio-cloudwatch-fetcher
```

##### Position file

After each successful iteration for every log group, the latest timestamp and next token obtained from AWS will be written to a file named position.yaml.

You can locate this file within the mounted host directory that you created.

If the container is stopped, the file enables the fetcher to resume from the exact point at which it was interrupted.



 

The advanced configuration settings for this integration include:


* [Manual configuration with a Lambda function](#manual-configuration-with-a-lambda-function)
* [Deployment using a module](#deployment-using-a-module)
* [Terraform deployment](#terraform-deployment)
* [Working with test events](#working-with-test-events)
* [Multiline support](#multiline-support)



#### Manual configuration with a Lambda function

 

##### Create a new Lambda function

This Lambda function will collect CloudWatch logs and sends them to Logz.io in bulk over HTTPS.

Open the AWS Lambda Console, and click **Create function**.
Choose **Author from scratch**, and use this information:

* **Name**: We suggest adding the log type to the name, but you can name this function whatever you want.
* **Runtime**: Choose **Python 3.9**

Click **Create Function** (bottom right corner of the page). After a few moments, you'll see configuration options for your Lambda function.

You'll need this page later on, so keep it open.

##### Zip the source files

Clone the CloudWatch Logs Shipper - Lambda project from GitHub to your computer,
and zip the Python files by running the following command:

```shell
git clone https://github.com/logzio/logzio_aws_serverless.git \
&& cd logzio_aws_serverless/python3/cloudwatch/ \
&& mkdir -p dist/python3/shipper; cp -r ../shipper/shipper.py dist/python3/shipper \
&& cp src/lambda_function.py dist \
&& cd dist/ \
&& zip logzio-cloudwatch lambda_function.py python3/shipper/*
```

:::note
You can alternatively zip the required files manually. To do this, zip folders `cloudwatch` and `shipper` in `python3` directory.
:::
 

You'll upload `logzio-cloudwatch.zip` in the next step.

##### Upload the zip file and set environment variables

1. In the **Code source** section, select **Upload from > .zip file**.
2. Click **Upload**, and choose the zip file you created earlier (`logzio-cloudwatch.zip`).
3. Click **Save**.
4. Navigate to **Configuration > Environment variables**.
5. Click **Edit**.
6. Click **Add environment variable**.
7. Fill in the **Key** and **Value** fields for each variable as per the table below:

###### Environment variables

| Parameter | Description | Required/Default |
|---|---|---|
| TOKEN | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html}  | Required  |
| LISTENER_URL |  Determines protocol, listener host, and port. For example, `https://<<LISTENER-HOST>>:8071`. <br > Replace `<<LISTENER-HOST>>` with your region's listener host (for example, `listener.logz.io`). For more information on finding your account's region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html) . |
| URL (Deprecated) | Use REGION instead. | -- |
| TYPE | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type.    You should create a new Lambda for each log type you use. | `logzio_cloudwatch_lambda` |
| FORMAT | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| COMPRESS | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `false` |
| ENRICH | Enrich CloudWatch events with custom properties, formatted as `key1=value1;key2=value2`. | -- |






##### Configure the function's basic settings

In Basic settings, we recommend starting with these settings:

* **Memory**: 512 MB
* **Timeout**: 1 min 0 sec

:::note
These default settings are just a starting point.
Check your Lambda usage regularly, and adjust these values if you need to.
:::
 


{@include: ../_include/log-shipping/cloudwatch-defaults.md}


##### Set the CloudWatch Logs event trigger

1. Find the **Add triggers** list (left side of the Designer panel) and choose **CloudWatch Logs** from this list.
2. In the **Log group** field, select the applicable log group.
3. Type a **Filter name** (required) and **Filter pattern** (optional).
4. Click **Add**, and then click **Save** at the top of the page.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 



#### Deployment using a module

Deploy this integration to add a module for CloudWatch to your existing stack. This integration uses CloudWatch Public Registry.
  
:::note
Logz.io Public Registry extensions are currently only available on the AWS region `us-east-1`.
:::
 

**Before you begin, you'll need**:

* A CloudFormation stack
* An S3 bucket to store the CloudFormation package

 

##### Select the Logz.io AWS Cloudwatch extension

1. Navigate to **CloudFormation > Registry > Public extensions**.
2. Set **Extension type > Modules** and **Publisher > Third party**.
3. Select **logzio::autoDeploymentLogzio::CloudWatch::MODULE**.


##### Activate the Logz.io AWS Cloudwatch extension

1. On the **logzio::autoDeploymentLogzio::CloudWatch** select **Activate**.
2. In the **Extension details** section, select **Use default**.
3. In the **Automatic updates** section, select **On**.
4. Select **Activate extension**.

##### Copy the configuration template

On the **logzio::autoDeploymentLogzio::CloudWatch** page, navigate to **Example template** and select **Copy template**.

##### Add your stack values to the configuration template

```yaml
{
    "Resources": {
        "MyModule": {
            "Type": "logzio::autoDeploymentLogzio::CloudWatch::MODULE",
            "Properties": {
                "LogzioListenerUrl": "https://<<LISTENER-HOST>>:8071",
                "LogzioToken": "<<LOG-SHIPPING-TOKEN>>",
                "LogzioType": "LogzioType",
                "LogzioFormat": "LogzioFormat",
                "LogzioCompress": "LogzioCompress",
                "LogzioSendAll": "LogzioSendAll",
                "LogzioEnrich": "LogzioEnrich",
                "LogGroup": "LogGroup"
            }
        }
    }
}
```

Save the template as a yaml file and add the values of your stack to the as per the table below.


| Parameter | Description | Required/Default |
|---|---|---|
| LogzioListenerUrl |  {@include: ../_include/log-shipping/listener-var.md} | |
| LogzioToken | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html}  | Required  |
| LogzioType | The log type you'll use with this Lambda. This can be a [built-in log type]({{site.baseurl}}/user-guide/log-shipping/built-in-log-types.html), or a custom log type.    You should create a new Lambda for each log type you use. | `logzio_cloudwatch_lambda` |
| LogzioFormat | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| LogzioCompress | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `false` |
| LogzioSendAll | Set to `true` to send all logs |  |
| LogzioEnrich | Enrich CloudWatch events with custom properties, formatted as `key1=value1;key2=value2`. | -- |
| LogGroup | CloudWatch log group. | -- |
  
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
            "Type": "logzio::autoDeploymentLogzio::CloudWatch::MODULE",
            "Properties": {
                "LogzioListenerUrl": "https://<<LISTENER-HOST>>:8071",
                "LogzioToken": "<<LOG-SHIPPING-TOKEN>>",
                "LogzioType": "LogzioType",
                "LogzioFormat": "LogzioFormat",
                "LogzioCompress": "LogzioCompress",
                "LogzioSendAll": "LogzioSendAll",
                "LogzioEnrich": "LogzioEnrich",
                "LogGroup": "LogGroup"
            }
        }
   ```
5. If required, change the module name by editing the `"MyModule"` value.



 



#### Terraform deployment

You can deploy this integration using Terraform with [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).

 

##### Zip the source files
Clone the CloudWatch Logs Shipper - Lambda project from GitHub to your computer, and zip the Python files in the src/ folder as follows:

```bash
git clone https://github.com/logzio/logzio_aws_serverless.git \
&& cd logzio_aws_serverless/python3/cloudwatch/ \
&& mkdir -p dist/python3/shipper; cp -r ../shipper/shipper.py dist/python3/shipper \
&& cp src/lambda_function.py dist \
&& cd dist/ \
&& zip logzio-cloudwatch lambda_function.py python3/shipper/* \
&& mv logzio-cloudwatch.zip ../../../.. \
&& cd ../../../.. \
&& rm -rf logzio_aws_serverless
```

The above script will create `logzio-cloudwatch.zip` that contains the source code for your lambda function.

##### Set AWS credentials

Create environment variables that contain your AWS credentials:

```bash
export AWS_ACCESS_KEY_ID="<<AWS-ACCESS-KEY>>"
export AWS_SECRET_ACCESS_KEY="<<AWS-SECRET-KEY>>"
export AWS_DEFAULT_REGION="<<AWS-REGION>>"
```

:::note
This configuration uses AWS keys credentials.
If you're using another authentication method for AWS, see [here](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#shared-credentials-file) how to configure your provider accordingly.
:::
 

##### Configure Terraform

Use the following configuration to create the necessary AWS resources to ship Cloudwatch logs to Logz.io.
Make sure you replace within the configuration to your details, where applicable:


```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.65.0"
    }
  }
}

resource "aws_iam_role" "iam_lambda_cw_to_logzio" {
  name = "lambda_cw_to_logzio"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "policy_cw_to_logzio" {
  name        = "policy_cw_to_logzio"
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:PutResourcePolicy",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
})
}

resource "aws_iam_policy_attachment" "attach_cw_to_logzio" {
  name       = "attach_cw_to_logzio"
  roles      = [aws_iam_role.iam_lambda_cw_to_logzio.name]
  policy_arn = aws_iam_policy.policy_cw_to_logzio.arn
}

resource "aws_lambda_function" "lambda_cloudwatch_to_logzio" {
  # Change to your path of the zip file you created in the 1st step
  filename      = "/path/to/your/logzio-cloudwatch.zip"

  function_name = "cloudwatch_to_logzio"
  role          = aws_iam_role.iam_lambda_cw_to_logzio.arn
  runtime = "python3.9"
  handler = "lambda_function.lambda_handler"

  # These default settings are just a starting point. Check your Lambda usage regularly, and adjust these values if you need to.
  timeout = 60
  memory_size = 512

  environment {
    variables = {
      # Required variables:
      TOKEN = "<<LOG-SHIPPING-TOKEN>>" # Your Logz.io shipping token
      LISTENER_URL = "https://<<LISTENER-HOST>>:8071" # Your Logz.io listener host (for example, listener.logz.io)

      # To learn more about all the environment variables for this function, see the parameters table in the documentation.
    }
  }
}

# Log group for the lambda function we create
resource "aws_cloudwatch_log_group" "log_group_cw_to_logzio" {
  name = "/aws/lambda/${aws_lambda_function.lambda_cloudwatch_to_logzio.function_name}"

  # You can add retention days for the function's log group
  # retention_in_days = 5
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_cloudwatch_to_logzio.function_name
  principal     = "logs.amazonaws.com"
}

# Subscription filter to the log group you wish to subscribe to.
# Create a seperate "aws_cloudwatch_log_subscription_filter" resource for every log group you want to subscribe to.
resource "aws_cloudwatch_log_subscription_filter" "cw_to_logzio_subscription" {
  name            = "cw_to_logzio_subscription"
  # Change "log_group_name" to the log group name you want to subscribe to. For example - /aws/lambda/my_lambda_function
  log_group_name  = "<<LOG-GROUP-TO-READ-FROM>>"
  filter_pattern  = ""
  destination_arn = "${aws_lambda_function.lambda_cloudwatch_to_logzio.arn}"
}

```

{@include: ../_include/log-shipping/cloudwatch-parameters.md}

##### Create Terraform execution plan

The following command will create a Terraform execution plan out of your configuration

```bash
terraform plan -out terraform.plan
```

##### Apply the plan

The following command will apply the execution plan you've created in the previous step, meaning that Terraform will create the resources you described in the configuration:

```bash
terraform apply terraform.plan  
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


##### Destroying the resources

To destroy the resources, use the following:

```bash
terraform destroy
```
 


#### Working with test events

You can generate test events using the Logz.io Lambda test events generator and add these events to your Lambda function. This functionality is currently only available on Linux & macOS.


 

##### Generate a test event

1. In your terminal, run the following command:
  
   ```shell
   bash <(curl -s https://raw.githubusercontent.com/logzio/logzio_aws_serverless/master/python3/cloudwatch/test_events/test_event_generator.sh)      
   ```
               
   This script generates a test event with a UTC timestamp of the moment you run the script.
               
2. Copy the output JSON.

##### Add the generated test event to your Lambda function

1. Select the Lambda function that you need to add the test event to.
2. Open the **Test** tab.
3. Select **New event**.
4. In the **Template** field, select **CloudWatch Logs**.
5. In the **Name** field, enter a name for the test event. No specific naming convention is required. 
6. Populate the body field with the output JSON of the test event generated in the previous step.
7. Select **Format** to format the test event.
8. Select **Save changes**.

##### Run the test event

To run the test event, select **Test** in the **Test** tab. The Lambda function will run and generate the following two logs in your account:
`[ERROR] Logz.io cloudwatch test log1` `[ERROR] Logz.io cloudwatch test log2`

 

#### Multiline support


AWS Lambda treats each log line as a separate event. However, you can use JSON in your logs as a workaround to help you gain multiline support.

JSON can be used regardless of the language you're currently using, and you'll need to replace `/n` with `/r` when printing the log message. This will replace the new lines generated with a return action, allowing you to view multiline log events. 

 
