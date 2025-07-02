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
For a much easier and more efficient way to collect and send telemetry, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
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

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["4pY46CjyNMoHWGB3gjgQWd"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics-new.md}




Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["4pY46CjyNMoHWGB3gjgQWd"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

## Configure AWS to forward traces to Logz.io

**Before you begin, you'll need:**

An application instrumented with an OpenTelemetry instrumentation or any other supported instrumentations based on OpenTracing, Zipkin or Jaeger.

* [Instrument Java application](https://docs.logz.io/docs/shipping/Code/Java/#traces)
* [Instrument Node.js application](https://docs.logz.io/docs/shipping/Code/Node-js/#traces)
* [Instrument Python application](https://docs.logz.io/docs/shipping/Code/Python/)

### Configure the OpenTelemetry Collector

The OpenTelemetry Collector receives traces from the application and exports them to Logz.io.

#### 1. **Create AWS SSM Parameter**

Go to AWS Systems Manager >> Parameter Store >> Create parameter:
- Set **Name** to `logzioOtelConfig.yaml`
- Keep **Type** as `String` and **Data type** as `text`
- In **Value** paste the below configuration:

{@include: ../../_include/tracing-shipping/collector-config.md}

#### 2. **Create Role to allow the ECS task to access the SSM Parameter**

Copy the ARN of the SSM parameter that was created in step [[1]](https://docs.logz.io/docs/shipping/code/java/#1-create-aws-ssm-parameter).
- Create an [IAM Policy](https://us-east-1.console.aws.amazon.com/iam) and add it to the following permissions:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ssm:GetParameters",
      "Resource": [
        "<ARN_FROM_STEP_1>"
      ]
    }
  ]
}
```
- Add the policy to your existing task [IAM Role](https://us-east-1.console.aws.amazon.com/iam) or create a new one and attach the policy to it.
- If you created a new role for the ECS task, copy the Role ARN, as you'll need it later.

#### 3. **Create log groups for your OpenTelemetry Collector in CloudWatch.**

You can either do so from [AWS Console](https://us-east-1.console.aws.amazon.com/cloudwatch), or via AWS CLI:
```shell
aws logs create-log-group --log-group-name /ecs/otel-collector
```

### Define ECS Task

Create a task definition for ECS that defines both your application container and the OpenTelemetry Collector container:
```json
{
  "family": "<APP>-app-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ecsTaskExecutionRole",
  "taskRoleArn": "<TASK_ROLE_ARN>",
  "containerDefinitions": [
    {
        <Your existing application container definitions>
    },
    {
      "name": "otel-collector",
      "image": "otel/opentelemetry-collector-contrib",
      "cpu": 128,      
      "essential": false,
      "command": [
          "--config",
          "env:OTEL_CONFIG"
      ],
      "environment": [],
      "secrets": [
          {
              "name": "OTEL_CONFIG",
              "valueFrom": "logzioOtelConfig.yaml"
          }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/otel-collector",
          "awslogs-region": "<AWS-REGION>",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

:::note
Replace:
- `<AWS-REGION>` with your AWS account region name
- `<AWS_ACCOUNT_ID>` with your AWS account ID
- `<TASK_ROLE_ARN>` with the ARN of the role that was created in step [2]
:::

### Verify Application and Tracing

After deploying, run your application to generate activity that will create tracing data. Wait a few minutes, then check the Logz.io dashboard to confirm that traces are being sent correctly. 