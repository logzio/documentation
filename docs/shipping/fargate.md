---
id: AWS Fargate
title: AWS Fargate
sidebar_position: 1
overview: AWS Fargate is a serverless compute engine for building applications without managing servers. This integration will create a new container that will run your image to send your AWS ECS Fargate logs to Logz.io using FireLens. The integration will automatically create the replica.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



AWS Fargate is a serverless compute engine for building applications without managing servers. This integration will create a new container that will run your image to send your AWS ECS Fargate logs to Logz.io using FireLens. The integration will automatically create the replica.
 
#### Configuration

 

##### Build the task execution role

[Create a new role](https://console.aws.amazon.com/iam/home#/roles$new?step=type)
in the IAM console.

* Select **AWS service**. It should already be selected by default.
* Under **Choose a use case**:
  * Select **Elastic Container Service**
  * Select **Elastic Container Service Task** (scroll to the bottom of the page to see it.)
  * Click **Next: Permissions** to continue.
* Select **AmazonECSTaskExecutionRolePolicy**.
  * Click **Next: Tags** and then **Next: Review**
* Set **Role name** to `logzioEcsTaskExecutionRole`, then click **Create role** to save.

Your new role should now be created.

* Click the newly created role to go to its **Summary** page.
* Copy the **Role ARN** (at the top of the page) and save it for later. You will need it for the deployment JSON.

##### Create a Fluent Bit task definition

In the ECS console, open the [_Task Definitions_](https://eu-central-1.console.aws.amazon.com/ecs/home?region=eu-central-1#/taskDefinitions)
page.

* Select **Create new Task Definition**.
* Choose **Fargate**, and click **Next step** to continue.
* Scroll to the bottom of the page to the **Volumes** section, and select
**Configure via JSON**.
* Replace the default JSON with this code block:

```json
{
  "family": "logzio-fargate-task",
  "requiresCompatibilities": [ "FARGATE" ],
  "containerDefinitions": [
    {
      "name": "logzio-log-router",
      "image": "amazon/aws-for-fluent-bit:latest",
      "essential": true,
      "firelensConfiguration": {
        "type": "fluentbit",
        "options": { "enable-ecs-log-metadata": "true" }
      },
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/aws/ecs/logzio-fargate-logs",
          "awslogs-region": "<<AWS-REGION>>",
          "awslogs-stream-prefix": "aws/ecs"
        }
      }
    },
    {
      "name": "app",
      "essential": true,
      "image": "<<YOUR-APP-IMAGE>>",
      "logConfiguration": {
        "logDriver": "awsfirelens",
        "options": {
          "Name": "Http",
          "Host": "<<LISTENER-HOST>>",
          "URI": "/?token=<<LOG-SHIPPING-TOKEN>>&type=fargate",
          "Port": "8071",
          "tls": "on",
          "tls.verify": "off",
          "Format": "json_lines"
        }
      }
    }
  ],
  "cpu": "256",
  "executionRoleArn": "arn:aws:iam::<<AWS-ACCOUNT-ID>>:role/logzioEcsTaskExecutionRole",
  "memory": "512",
  "volumes": [ ],
  "placementConstraints": [ ],
  "networkMode": "awsvpc",
  "tags": [ ]
}
```

Replace the placeholders in the code block (indicated by the double angle brackets `<< >>`) using the parameters below: 👇


When you're done, click **Save**,
and then click **Create**.


###### Parameters in logzio-log-router

| Parameter | Description |
|---|---|
| logConfiguration.options.awslogs-group | In the CloudWatch left menu, select **Logs > Log groups**, and then click **Actions > Create log group**. Give the **Log Group Name** `/aws/ecs/logzio-fargate-logs`. |
| logConfiguration.options.awslogs-region | The [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) of your cluster. |
{:.paramlist}


###### Parameters in app

| Parameter | Description |
|---|---|
| image | Replace `<<YOUR-APP-IMAGE>>` with the name of the image you want to ship logs from. |
| logConfiguration.options.Host | {@include: ../_include/log-shipping/listener-var.md} {@include: ../_include/log-shipping/listener-var.html} |
| logConfiguration.options.URI | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html} |
{:.paramlist}



###### Remaining parameters

| Parameter | Description |
|---|---|
| executionRoleArn | Replace `<<AWS-ACCOUNT-ID>>` with your [AWS account Id](https://console.aws.amazon.com/billing/home?#/account). |
{:.paramlist}



##### Run the task on your cluster

Go back to your new task's definition page,
and click **Actions > Run Task**.

Click **Switch to launch type**, and fill in these details:

* For **Launch Type**, select **FARGATE**.
* For **Cluster**, select your cluster.
* For **Subnets**, select a subnet from your cluster.

Click **Run task**.

The logs created by the Fluent Bit shipper are in Cloudwatch
under the `/aws/ecs/logzio-fargate-logs` log group.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

{@include: ../_include//log-shipping/search-log-type.md type="fargate" %}

 

#### Adding extra configuration to your Fluent Bit task

 

##### Create an extra.conf file

Create an `extra.conf` file with the extra configuration. For example:

```conf
[FILTER]
    Name record_modifier
    Match *
    Record app-version ${APP_VERSION}
```

##### Upload the extra.conf file to S3 (if your Fluent Bit is on EC2)

Upload the `extra.conf` file to the S3 bucket.

##### Update the task definition file

Add the path to the extra.conf file to the task definition file as follows:

```json
"firelensConfiguration": {
				"type": "fluentbit",
				"options": {
					"config-file-type": "s3",
					"config-file-value": "arn:aws:s3:::<<PATH-TO-YOUR-EXTRA-CONF>>/extra.conf"
				}
			}
```

Replace `<<PATH-TO-YOUR-EXTRA-CONF>>` with the path to the extra.conf file in your S3 bucket. For example, `yourbucket/yourdirectory/extra.conf`.




 
