---
id: synthetic-link-detector
title: Synthetic link detector
overview: Deploy this integration to collect data on broken links in a web page, and to get additional data about the links.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Synthetic Monitoring']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/link.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ["4l4xVZhvqsrJWO7rZwOxgx", "1NiBMzN5DvQZ8BjePpUtvQ"]
metrics_alerts: []
drop_filter: []
---

Deploy this integration to collect data on broken links in a web page, and to get additional data about the links.

<!-- logzio-inject:install:grafana:dashboards ids=["4l4xVZhvqsrJWO7rZwOxgx", "1NiBMzN5DvQZ8BjePpUtvQ"] -->





### Auto-deploy the stack

To deploy this integration, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                       |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)           |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)          |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071) |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/synthetic-link-detector/0.0.3/sam-template.yaml&stackName=logzio-synthetic-link-detector&param_logzioToken=<<LOG-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8071)     |

### Specify stack details

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                    | Description                                                                                                                         | Required/Default                    |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `logzioToken`                | Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to. | **Required**                        |
| `logzioListener`             | Listener host, and port (for example, `https://<<LISTENER-HOST>>:8071`).                                                            | **Required**                        |
| `url`                        | Full URL of the web page you wish to monitor. For example - `https://logz.io`                                                       | **Required**                        |
| `functionInvocationInterval` | The scheduling expression that determines how often the Lambda function runs                                                        | Default: `rate(1 days)`             |
| `logzioCustomFields`         | Enrich the data with custom fields, formatted as `key1=value1,key2=value2`                                                          | -                                   |
| `functionTimeout`            | Timeout for your Lambda function, in seconds                                                                                        | Default: `60`                       |
| `functionMemorySize`         | Memory size (in MB) for your Lambda function                                                                                        | Default: `512`                      |
| `logzioType`                 | The log type you'll use with this Lambda.                                                                                           | Default: `synthetic-links-detector` |


### Check Logz.io for your data

Give the stack a few minutes to be deployed and the data to get to our system, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your data.

<!-- logzio-inject:install:grafana:dashboards ids=["4l4xVZhvqsrJWO7rZwOxgx", "1NiBMzN5DvQZ8BjePpUtvQ"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}





