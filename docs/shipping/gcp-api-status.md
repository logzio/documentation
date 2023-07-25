---
id: API-status-metrics
title: API status metrics
overview: Deploy this integration to collect API status metrics of user API and send them to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/apii.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1RCzCjjByhyz0bJ4Hmau0y']
metrics_alerts: []
---

### Overview

Deploy this integration to collect API status metrics of user API and send them to Logz.io.

The integration is based on a Lambda function that will be auto-deployed together with the layer [LogzioLambdaExtensionLogs](https://github.com/logzio/logzio-lambda-extensions/tree/main/logzio-lambda-extensions-logs).


<!-- logzio-inject:install:grafana:dashboards ids=["1RCzCjjByhyz0bJ4Hmau0y"] -->









##### Auto-deploy the stack

To deploy this integration, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                               |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)           |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/api-status-auto-deployment/1.1.2/sam-template.yaml&stackName=logzio-api-status-auto-deployment&param_LogzioLogsToken=<<LOG-SHIPPING-TOKEN>>&param_LogzioMetricsToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_LogzioListener=https://<<LISTENER-HOST>>)     |

##### Specify the stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.


| Parameter | Description | Required/Optional | Default |
| --- | --- | --- | --- |
| ApiURL | Your API URL to collect status from (for example: https://example.api:1234). | Required | - |
| Method | Your API HTTP request method. Can be `GET` or `POST` | Required | `GET` |
| ApiResponseTimeout | Your API response timeout (seconds). | Required | `10 (seconds)` |
| ExpectedStatusCode | The expected HTTP response status code your API should return. | Required | `200` |
| ExpectedBody | The expected HTTP response body your API should return (leave empty if your API HTTP response body is empty). | Required | ` ` |
| LogzioListener | The Logz.io listener URL: `https://<<LISTENER-HOST>>:8071` {@include: ../_include/log-shipping/listener-var.html} | Required | `https://listener.logz.io` |
| LogzioMetricsToken | Your Logz.io metrics shipping token:`<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` | Required | - |
| LogzioLogsToken | Your Logz.io log shipping token:`<<LOG-SHIPPING-TOKEN>>` {@include: ../_include/log-shipping/log-shipping-token.html} | Required | - |
| SchedulingInterval | The scheduling expression that determines when and how often the Lambda function runs. | Required | `rate(30 minutes)` |
| Headers | Your API headers separated by comma and each header's key and value are separated by `=` (`header_key_1=header_value_1,header_key_2=header_value_2`). | Optional | - |
| Body | Your API HTTP request body. | Optional | - |
| BearerToken | Your API bearer token. | Optional | - |
| Username | Your API username. | Optional | - |
| Password | Your API password. | Optional | - |


##### Run the tests

Run the ping statistics tests to generate metrics.


##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). All metrics that were sent from the Lambda function will have the prefix `api_status` in their name.

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1RCzCjjByhyz0bJ4Hmau0y"] -->

{@include: ../_include/metric-shipping/generic-dashboard.html}





