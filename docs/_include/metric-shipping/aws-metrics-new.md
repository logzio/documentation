**Before you begin, you'll need**:

* An active Logz.io account

 

### Configure AWS to forward metrics to Logz.io

**1. Set the required minimum IAM permissions**

configured the minimum required IAM permissions as follows:

* **Amazon S3**:
   - `s3:CreateBucket`
   - `s3:DeleteBucket`
   - `s3:PutObject`
   - `s3:GetObject`
   - `s3:DeleteObject`
   - `s3:ListBucket`
   - `s3:AbortMultipartUpload`
   - `s3:GetBucketLocation`
* **AWS Lambda**:
   - `lambda:CreateFunction`
   - `lambda:DeleteFunction`
   - `lambda:InvokeFunction`
   - `lambda:GetFunction`
   - `lambda:UpdateFunctionCode`
   - `lambda:UpdateFunctionConfiguration`
   - `lambda:AddPermission`
   - `lambda:RemovePermission`
   - `lambda:ListFunctions`
* **Amazon CloudWatch**:
   - `cloudwatch:PutMetricData`
   - `cloudwatch:PutMetricStream`
   - `logs:CreateLogGroup`
   - `logs:CreateLogStream`
   - `logs:PutLogEvents`
   - `logs:DeleteLogGroup`
   - `logs:DeleteLogStream`
* **AWS Kinesis Firehose**:
   - `firehose:CreateDeliveryStream`
   - `firehose:DeleteDeliveryStream`
   - `firehose:PutRecord`
   - `firehose:PutRecordBatch`
* **IAM**:
   - `iam:PassRole`
   - `iam:CreateRole`
   - `iam:DeleteRole`
   - `iam:AttachRolePolicy`
   - `iam:DetachRolePolicy`
   - `iam:GetRole`
   - `iam:CreatePolicy`
   - `iam:DeletePolicy`
   - `iam:GetPolicy`
* **Amazon CloudFormation**:
   - `cloudformation:CreateStack`
   - `cloudformation:DeleteStack`
   - `cloudformation:UpdateStack`
   - `cloudformation:DescribeStacks`
   - `cloudformation:DescribeStackEvents`
   - `cloudformation:ListStackResources`


**2. Create Stack in the relevant region**

To deploy this project, click the button that matches the region you wish to deploy your Stack to:

| Region           | Deployment                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `us-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `us-east-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-east-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `us-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `us-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-us-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `eu-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)     |
| `eu-central-2`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-central-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)     |
| `eu-north-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-north-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `eu-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-2`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `eu-west-3`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-west-3.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)           |
| `eu-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `eu-south-2`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-south-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-eu-south-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `sa-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-sa-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `ap-northeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-northeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-northeast-3.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `ap-south-2`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-south-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `ap-southeast-1` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-southeast-2` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-2.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-southeast-3` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-3#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-3.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-southeast-4` | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-4#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-southeast-4.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053) |
| `ap-east-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-east-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ap-east-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `ca-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)     |
| `ca-west-1`      | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-west-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-ca-west-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `af-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=af-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-af-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `me-south-1`     | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-me-south-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |
| `me-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=me-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-me-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)     |
| `il-central-1`   | [![Deploy to AWS](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lights/LightS-button.png)](https://console.aws.amazon.com/cloudformation/home?region=il-central-1#/stacks/create/review?templateURL=https://logzio-aws-integrations-il-central-1.s3.amazonaws.com/metric-stream-helpers/aws/1.3.4/sam-template.yaml&stackName=logzio-metric-stream&param_logzioToken=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>&param_logzioListener=https://<<LISTENER-HOST>>:8053)         |


**3. Specify stack details**

Specify the stack details as per the table below, check the checkboxes and select **Create stack**.

| Parameter                                  | Description                                                                                                                                                                                          | Required/Default |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `logzioListener`                           | Logz.io listener URL for your region. (For more details, see the [regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/). e.g., `https://listener.logz.io:8053`     | **Required**     |
| `logzioToken`                              | Your Logz.io metrics shipping token.                                                                                                                                                                 | **Required**     |
| `awsNamespaces`                            | Comma-separated list of AWS namespaces to monitor. See [this list](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) of namespaces. Use value `all-namespaces` to automatically add all namespaces. | At least one of `awsNamespaces` or `customNamespace` is required    |
| `customNamespace`                          | A custom namespace for CloudWatch metrics. Used to specify a namespace unique to your setup, separate from the standard AWS namespaces.                                                                                                                                   | At least one of `awsNamespaces` or `customNamespace` is required  |
| `logzioDestination`                        | Your Logz.io destination URL.                                                                                                                                                                        | **Required**     |
| `httpEndpointDestinationIntervalInSeconds` | Buffer time in seconds before Kinesis Data Firehose delivers data.                                                                            | `60`             |
| `httpEndpointDestinationSizeInMBs`         | Buffer size in MBs before Kinesis Data Firehose delivers data.                                                                           | `5`              |
| `debugMode` |	Enable debug mode for detailed logging (true/false).	| false |






**4. View your metrics**


Allow some time for data ingestion, then open your [Logz.io metrics account](https://app.logz.io/#/dashboard/metrics/).


