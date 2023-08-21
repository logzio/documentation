---
id: AWS-ECS
title: AWS ECS
overview: Send your Amazon ECS logs and metrics to Logz.io.
product: ['logs','metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Compute', 'Containers']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-ecs.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['4pY46CjyNMoHWGB3gjgQWd']
metrics_alerts: []
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send telemetry, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::


## Configure AWS to forward logs to Logz.io

This integration uses Fluentd in a Docker container to forward logs from your Amazon Elastic Container Service (ECS) cluster to Logz.io.

:::note
This integration refers to an EC2-based cluster. For Fargate-based cluster see [our Fargate documentation](https://docs.logz.io/shipping/log-sources/fargate.html).
:::
 

:::caution Important
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::

### Automated CloudFormation deployment
 
  
#### Configure and create your stack

Click the button that matches your AWS region, then follow the instructions below:

| AWS Region | Launch button |
| --- | --- |
| `us-east-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/logzio-aws-ecs/1.0.0/auto-deployment.json&stackName=logzio-aws-ecs-auto-deployment) |

:::note
If your region is not on the list, let us know in the [repo's issues](https://github.com/logzio/logzio-aws-ecs/issues), or reach out to Logz.io support team!
:::
 

####### In screen **Step 1 Specify template**:

Keep the defaults and click **Next**.

![Screen_1](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ecs/screen_01.png)

####### In screen **Step 2 Specify stack details**:

1. For **Stack name** you can either keep the default, or change the stack name.

2. For **LogzioListener** - choose your Logz.io listener from the list.

3. For **LogzioToken** - insert your Logz.io logs shipping token.

4. Click **Next**.

![Screen_2](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ecs/screen_02.png)

####### In screen **Step 3 Configure stack options** (Optional):

If you want to, you can add your custom tags, or not. Click on **Next**.

####### In screen **Step 4 Review**:

Scroll down and click on **Create stack**.

**Give your stack a few moments to launch.**

#### Run the task

1. Go to your AWS ECS page, and on the left menu, click on **Task Definitions**, then choose the task you just created.

2. Click on the **Actions** button, then choose **Run Task**.

3. In the **Run Task** screen, choose **EC2** as your **Launch type**.

4. Choose the cluster you want to ship logs from.

5. For **Placement Templates** choose **One Task Per Host**.

6. Click on **Run Task**.

#### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).
  

### Manual deployment (AWS Classic Console)

 
#### Download the task definition JSON

```shell
wget https://raw.githubusercontent.com/logzio/logzio-aws-ecs/master/task-definition.json
```

#### Configure the task

In your prefered text editor, open the JSON you downloaded in the previous step and replace the following:

| Paramater | Details |
|---|---|
| `<<LOG-SHIPPING-TOKEN>>` | **Required**. Your Logz.io account token. Replace with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to. |
| `<<LISTENER-HOST>>` | **Required**. Your Logz.io listener URL. Replace with your region's listener URL.|


#### Advanced settings (optional)

Since the Docker image is based on Logz.io's [fluentd-docker-logs](https://github.com/logzio/fluentd-docker-logs) image, any of the environment variables mentioned [here](https://github.com/logzio/fluentd-docker-logs#parameters) can be added to the task definition JSON.


#### Add your task definition

1. In your [Amazon ECS Classic Console](https://console.aws.amazon.com/ecs/) menu, go to **Task Definitions** and click on **Create new Task Definition**.

2. In the **Step 1: Select launch type compatibility** screen, choose **EC2** and click **Next step**.

3. In the **Step 2: Configure task and container definitions** screen, scroll down and click on the **Configure via JSON** button.

4. In the text-box, delete the existing text and paste your configured task definition JSON. Press **Save**, then press **Create**.

#### Run the task

1. After the task creation, click on the **Actions** button, then choose **Run Task**.

2. In the **Run Task** screen, choose **EC2** as your **Launch type**.

3. Choose the cluster you want to ship logs from.

4. For **Placement Templates**, choose **One Task Per Host**.

5. Click on **Run Task**.

#### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).



## Configure AWS to forward metrics to Logz.io


Deploy this integration to send your Amazon ECS metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon ECS metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["4pY46CjyNMoHWGB3gjgQWd"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


**Before you begin, you'll need**:

* An active account with Logz.io


### Create Stack in the relevant region

To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)           |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.2.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053&param_awsNamespaces=AWS/ECS)     |

### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                                  | Description                                                                                                                                                                                          | Required/Default |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `logzioListener`                           | The Logz.io listener URL for your region. (For more details, see the [regions page](https://docs.logz.io/user-guide/accounts/account-region.html). For example - `https://listener.logz.io:8053`     | **Required**     |
| `logzioToken`                              | Your Logz.io metrics shipping token.                                                                                                                                                                 | **Required**     |
| `awsNamespaces`                            | Comma-separated list of the AWS namespaces you want to monitor. See [this list](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) of namespaces. If you want to automatically add all namespaces, use value `all-namespaces`. | **Required**     |
| `logzioDestination`                        | Your Logz.io destination URL.                                                                                                                                                                        | **Required**     |
| `httpEndpointDestinationIntervalInSeconds` | The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.                                                                            | `60`             |
| `httpEndpointDestinationSizeInMBs`         | The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.                                                                           | `5`              |



### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["4pY46CjyNMoHWGB3gjgQWd"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}