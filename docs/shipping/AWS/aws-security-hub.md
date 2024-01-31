---
id: AWS-Security-Hub
title: AWS Security Hub
overview: This integration ships events from AWS Security Hub to Logz.io. It will automatically deploy resources to your AWS Account.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['AWS', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

 

This integration ships events from AWS Security Hub to Logz.io. It will automatically deploy [resources](#resources) to your AWS Account.

A new event triggers a designated EventBridge rule, which invokes a Lambda function. The function processes the event and sends it to Logz.io.

:::note
Your Lambda function needs to run within the AWS Lambda limits, such as memory allocation and timeout. Make sure you understand these limits. If you can't adjust your settings to stay within the Lambda limits, you can use the AWS [Support Center console](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase) to request an increase. [Learn more about AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).
:::
 

  

## Automated CloudFormation deployment

 

### Login to your account

To begin, you need to login to your AWS account.

### Create a new stack

Select the button below to create a new stack dedicated to sending events from AWS Security Hub to Logz.io.

| AWS Region | Launch a stack |
| --- | --- |
| `us-east-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `us-east-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `us-west-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `us-west-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `eu-central-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `eu-north-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `eu-west-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `eu-west-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `eu-west-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `sa-east-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ca-central-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-south-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=logzio-security-hub-collector&templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/aws-security-hub-collector/0.0.3/template.yaml) |

![Create stack](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/security-hub-step1.png)

Keep the default setting in the **Create stack** screen and select **Next**.

### Specify the stack details

![Specify stack details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/security-hub-step2.png)

Specify the stack details as per the table below and select **Next**.


| Parameter | Description |
| --- | --- |
| `logzioListener` | Your Logz.io [listener url](https://docs.logz.io/user-guide/accounts/account-region.html), followed by port `8070` or `8071`. The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071. For example, `https://listener.logz.io:8071` |
| `logzioLogLevel` | Log level for the Lambda function. Defaults to `info`. Valid options are: `debug`, `info`, `warn`, `error`, `fatal`, `panic`. |
| `logzioOperationsToken` | Your Logz.io [operations token](https://app.logz.io/#/dashboard/settings/general). |

### Configure the stack options

![Configure stack options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/security-hub-step3.png)

Specify the **Key** and **Value** parameters for the **Tags** and select **Next**.

### Review the deployment

![Confirm deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/security-hub-step4b.png)

Confirm that you acknowledge that AWS CloudFormation might create IAM resources and select **Create stack**.

 
### Deployed resources

This deployment will automatically create the following resources:

![Resources](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/resources-security-hub.png)


### Check Logz.io for your events

Give the stack some time to deploy and the resources to get created. Once this is finished, the stack sends a security event to Logz.io as soon as the event is created on the security hub. You can then see the data in [OpenSearch Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your events, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 

  

## Deployment using a module
  
Deploy this integration to add a module for AWS security hub to your existing stack. This integration uses Cloudwatch Public Registry.

:::note
Logz.io Public Registry extensions are currently only available on the AWS region `us-east-1`.
:::
 

{@include: ../../_include/log-shipping/note-lambda-test.md}

**Before you begin, you'll need**:

* A CloudFormation stack

 

### Select the Logz.io AWS Security Hub extension

1. Navigate to **CloudFormation > Registry > Public extensions**.
2. Set **Extension type > Modules** and **Publisher > Third party**.
3. Select **logzio::awsSecurityHub::collector::MODULE**.


### Activate the Logz.io AWS Security Hub extension

1. On the **logzio::awsSecurityHub::collector::MODULE** select **Activate**.
2. In the **Extension details** section, select **Use default**.
3. In the **Automatic updates** section, select **On**.
4. Select **Activate extension**.

### Copy the configuration template

On the **logzio::awsSecurityHub::collector::MODULE** page, navigate to **Example template** and select **Copy template**.

### Add your stack values to the configuration template

```yaml
{
    "Resources": {
        "MyModule": {
            "Type": "logzio::awsSecurityHub::collector::MODULE",
            "Properties": {
                "logzioOperationsToken": "<<LOG-SHIPPING-TOKEN>>",
                "logzioListener": "https://<<LISTENER-HOST>>:8071",
                "logzioLogLevel": "<<LOGZIO-LOG-LEVEL>>"
            }
        }
    }
}
```

Save the template as a yaml file and add the values of your stack to the as per the table below.

| Parameter | Description |
| --- | --- |
| `<<LISTENER-HOST>>` | Your Logz.io [listener url](https://docs.logz.io/user-guide/accounts/account-region.html), followed by port `8070` or `8071`. For example, `https://listener.logz.io:8071` |
| `<<LOGZIO-LOG-LEVEL>>` | Log level for the Lambda function. Defaults to `info`. Valid options are: `debug`, `info`, `warn`, `error`, `fatal`, `panic`. |
| `<<LOG-SHIPPING-TOKEN>>` | Your Logz.io [operations token](https://app.logz.io/#/dashboard/settings/general). |

### Add your stack values to the configuration template

If you are creating a new stack:

1. In step 1 of the **Create stack** process, select **Template is ready**.
2. Select **Upload a template file**.

If you are editing an existing stack:

1. Select the stack.
2. Select **Update**.
3. Select **Edit template in designer**.
4. Paste the content of the yaml file into the **Resources** section of the template as follows:

   ```yaml
   "Resources": {
        "MyModule": {
            "Type": "logzio::awsSecurityHub::collector::MODULE",
            "Properties": {
                "logzioOperationsToken": "<<LOG-SHIPPING-TOKEN>>",
                "logzioListener": "https://<<LISTENER-HOST>>:8071",
                "logzioLogLevel": "<<LOGZIO-LOG-LEVEL>>"
            }
        }
    }
   ```
5. If required, change the module name by editing the `"MyModule"` value.

 
 
