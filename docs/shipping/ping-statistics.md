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


### Overview

Deploy this integration to collect metrics of ping statistics collected from your preferred web addresses and send them to Logz.io.

The integration is based on a Lambda function that will be auto-deployed together with the layer [LogzioLambdaExtensionLogs](https://github.com/logzio/logzio-lambda-extensions/tree/main/logzio-lambda-extensions-logs).


<!-- logzio-inject:install:grafana:dashboards ids=["1rNO8llFw8Cm9N8U3M3vCQ"] -->




##### Auto-deploy the Lambda function

👇 To begin, click this button to start the automated deployment. You will need to deploy it in your environment.

[![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/ping-statistics-auto-deployment/auto-deployment.yaml&stackName=logzio-ping-statistics-auto-deployment)


##### Specify the template

![Specify stack template](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ping_statistics/Template.png)

Keep the defaults and click **Next**.


##### Specify the stack details

![Specify stack details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ping_statistics/Stack_details1.png)

Specify the stack details as per the table below and select **Next**.


| Parameter | Description | Required/Optional | Default |
| --- | --- | --- | --- |
| Addresses | The addresses to ping. You can add port for each address (default port for the address is 80). Addresses must be separated by comma. (Example addresses: `www.google.com`, `tcp://www.google.com`, `https://www.google.com`, `http://www.google.com`). | Required | - |
| LogzioListener | The Logz.io listener URL: `https://<<LISTENER-HOST>>:8071` {@include: ../_include/log-shipping/listener-var.html} | Required | `https://listener.logz.io` |
| LogzioLogsToken | Your Logz.io log shipping token:`<<LOG-SHIPPING-TOKEN>>` {@include: ../_include/log-shipping/log-shipping-token.html} | Required | - |
| LogzioMetricsToken | Your Logz.io metrics shipping token:`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Required | - |
| PingCount | The number of pings for each address. | Required | `3` |
| PingInterval | The time to wait (in seconds) between each ping. | Required | `1 (second)` |
| PingTimeout | The timeout (in seconds) for each ping. | Required | `10 (seconds)` |
| SchedulingInterval | The scheduling expression that determines when and how often the Lambda function runs. | Required | `rate(30 minutes)` |


##### Configure the stack options

![Specify stack options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ping_statistics/Stack_option.png)

Keep the defaults and click **Next**.

##### Review the deployment

Confirm that you acknowledge that AWS CloudFormation might create IAM resources and select **Create stack**.


##### Run the tests

Run the ping statistics tests to generate metrics.


##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). All metrics that were sent from the Lambda function will have the prefix `ping_stats` in their name.

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1rNO8llFw8Cm9N8U3M3vCQ"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}



