---
id: AWS-Amplify
title: AWS Amplify
overview: This is an integration that collects Amplify access logs and sends them to Logz.io.
product: ['logs']
os: []
filters: ['AWS', 'CI/CD']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/amplify.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


:::tip
For a much easier and more efficient way to collect and send telemetry, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::

## Logs

This is an AWS Lambda function that collects Amplify access logs and sends them to Logz.io in bulk over HTTP.

## Configuration with a Lambda function


### Create a new Lambda function

1. Open the AWS Lambda Console, and click **Create function**.
2. Choose **Author from scratch**.
3. In **Name**, add the log type to the name of the function.
4. In **Runtime**, choose **Python 3.9**.
5. Click **Create Function**.

After a few moments, you'll see configuration options for your Lambda function. You'll need this page later on, so keep it open.

### Zip the source files

Clone the CloudWatch Logs Shipper - Lambda project from GitHub to your computer,
and zip the Python files in the `src/` folder as follows:

```shell
git clone https://github.com/logzio/logzio_aws_serverless.git \
&& cd logzio_aws_serverless/python3/amplify/ \
&& mkdir -p dist/python3/shipper; cp -r ../shipper/shipper.py dist/python3/shipper; mkdir -p dist/python3/custom_logger; cp -r ../custom_logger/custom_logger.py dist/python3/custom_logger \
&& cp src/lambda_function.py dist \
&& cd dist/ \
&& zip logzio-amplify lambda_function.py python3/shipper/* python3/custom_logger/*
```

### Upload the zip file and set environment variables

1. In the **Code source** section, select **Upload from > .zip file**.
2. Click **Upload**, and choose the zip file you created earlier (`logzio-amplify.zip`).
3. Click **Save**.
4. Navigate to **Configuration > Environment variables**.
5. Click **Edit**.
6. Click **Add environment variable**.
7. Fill in the **Key** and **Value** fields for each variable as per the table below:

| Parameter                                      | Description                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TOKEN (Required)                               | The [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.                                                                                                                                                                                                                                                           |
| LISTENER_URL (Required)                        | Determines protocol, listener host, and port. For example, `https://<<LISTENER-HOST>>:8071`. <br /> Replace `<<LISTENER-HOST>>` with your region's listener host (for example, `https://listener.logz.io:8071`). Use port 8070 for HTTP or 8071 for HTTPS. For more information on finding your account's region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html) . |
| AMPLIFY_DOMAIN (Required)                      | Amplify domain URL can be found in the Amplify admin dashboard in **General** under **Production branch URL**.                                                                                                                                                                                                                                             |
| TYPE (Default: `logzio_amplify_access_lambda`) | The log type you'll use with this Lambda. This can be a [type that supports default parsing](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), or a custom log type. <br /> You'll need to create a new Lambda for each log type you use.                                                                                                |
| AMPLIFY_APP_ID (Required)                      | You can find the app ID in your Amplify admin dashboard in **General** under the **App ARN** field arn:aws:amplify:`REGION`:`AWS_ID`:apps/`APP_ID`.                                                                                                                                                                                                         |
| TIMEOUT                                        | Period in minutes, over which the Lambda function fetches Amplify logs.                                                                                                                                                                                                                                                 |

### Set the EventBridge (CloudWatch Events) trigger

1. Find the **Add triggers** list (left side of the Designer panel) and choose **EventBridge (CloudWatch Events)** from this list.
2. If you don't have a pre-defined schedule type (e.g., 1min), click **Create new rule** in **Rule**.
3. In **Rule name**, enter a name to uniquely identify your rule.
4. In **Rule description**, if required, provide an optional description for your rule.

5. In **Rule type**, choose the schedule expression that is equal to the TIMEOUT of the environment variable (e.g., 5 minutes).

### Update Permissions for Lambda Function

1. Go to **Configuration** in your Lambda function and select the **Permissions** tab.
2. Click the role name shown in the example **lambda-basic**. It will redirect you to the **IAM> Roles> lambda-basic**.
3. On the role page inside the **Permissions** tab, select the dropdown **Add permissions** and click on **Create inline policy**. It will redirect you to the **Create Policy** page.
4. On the **Create Policy** page, select the **JSON** tab.
5. Fill in JSON with your parameters as follows:

```
{
    "Version": "2012-10-17",
    "Statement": [
		{
            "Effect": "Allow",
            "Action": [
                "amplify:GenerateAccessLogs"
            ],
            "Resource": "arn:aws:amplify:AWS_REGION:XXX66029XXXX:apps/XXXXdn0mprXXXX/accesslogs/*"
        }
	]
}
```

* Replace `AWS_REGION` with the AWS region of your Amplify App (e.g.,us-west-2).
* Replace `XXX66029XXXX` with your AWS Account ID.
* Replace `XXXXdn0mprXXXX` with the AWS Amplify App ID.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).
