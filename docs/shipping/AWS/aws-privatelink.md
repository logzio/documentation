---
id: AWS-privatelink
title: AWS PrivateLink
overview: Use AWS PrivateLink to securely send logs and metrics to Logz.io over a private network connection.
product: ['logs', 'metrics']
os: []
filters: ['AWS', 'Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/PrivateLink.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

AWS PrivateLink allows you to establish a private and secure connection between your AWS VPC and Logz.io, keeping your data entirely within the AWS network and never exposed to the public internet. This is ideal for isolated environments or organizations with strict compliance and security requirements.

***AWS PrivateLink is available for customers on supported Logz.io plans. To enable the integration, contact your account manager or [support team](mailto:help@logz.io) to request access and receive your PrivateLink service name.***

### How it works

The diagram below shows how data is sent through AWS PrivateLink to Logz.io. Your services in the client VPC route data to a VPC endpoint, which connects to a PrivateLink service managed by Logz.io. From there, traffic is forwarded through a Network Load Balancer (NLB) and ingested via Listener V2 in Logz.io’s infrastructure.

![How it works](https://dytvr9ot2sszz.cloudfront.net/logz-docs/how-it-works.png)

### Prerequisites

Before you begin, ensure you have the following:

* Your AWS Account ID and AWS Region
* The PrivateLink service name provided by Logz.io


### 1. Get service name from Logz.io

To get started, send your AWS Account ID and the region you'll connect from to your Logz.io account manager or [support team](mailto:help@logz.io). You'll receive your PrivateLink service name once access is granted.

### 2. Create a VPC Endpoint in AWS

1. Go to the AWS VPC Console.

    Navigate to **VPC > Endpoints > Create Endpoint**.

    ![Create endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/create-endpoint.png)

2. Configure the Endpoint

    * Under **Name Tag**, enter a meaningful name for your endpoint service.

    * Select **Endpoint services that use NLBs and GWLBs**.

    * Use the **service name** provided by Logz.io.

        * If you're connecting from a different AWS region than your Logz.io account, enable the **cross-region endpoint option**. This is useful for cross-region PrivateLink setups.

    * Select the **VPC** where the endpoint should be established.

    * Choose the **subnets** in which the endpoint will be deployed.

    * Select **security groups**. Make sure they allow outbound traffic for the specific endpoint IPs on the required ports.

### 3. Validate and enable the endpoint

After creating the endpoint, contact [Logz.io support](mailto:help@logz.io) to validate the connection. Confirm the endpoint shows an **Available** status.

Verify PrivateLink connectivity before enabling DNS resolution:

```bash
echo $'{"message":"hello there", "counter": 1}\n{"message":"hello again", "counter": 2}' | curl -XPOST "https://<VPC ENDPOINT IP ADDRESS>:8071?token=<TOKEN>&type=test_http_bulk" --data-binary @-
```

In AWS Endpoints, click **Actions > Modify Private DNS Name**, select **Enable for this endpoint** and click **Save changes**. 

:::note
**The Private DNS Name is critical. Without it enabled, you cannot send data to Logz.io through PrivateLink.**
:::

### 4. Verify the connection

Confirm that the VPC endpoint is active and data is flowing:

```bash
echo $'{"message":"hello world", "counter": 1}\n{"message":"hello there", "counter": 2}' | curl -vvv -XPOST "https://<LOGZ SHIPPING ADDRESS>:8071?token=<TOKEN>&type=test_http_bulk" --data-binary @-
```

![Create endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/vpc-hello-world.png)

In Logz.io, check **[Explore](https://app.logz.io/#/dashboard/explore)** to confirm that logs and metrics are being received through PrivateLink.

## Disable PrivateLink

To temporarily stop sending data through PrivateLink, you don’t need to delete the VPC endpoint, simply disable DNS resolution for it.

Deleting the VPC endpoint is irreversible. If you delete the endpoint, you'll need to request approval from Logz.io again before creating a new one.


If you encounter any issues or need further assistance, contact [Logz.io support](mailto:help@logz.io).
