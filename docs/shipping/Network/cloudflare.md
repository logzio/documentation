---
id: Cloudflare-network
title: Cloudflare
overview: The Cloudflare web application firewall (WAF) protects your internet property against malicious attacks that aim to exploit vulnerabilities such as SQL injection attacks, cross-site scripting, and cross-site forgery requests.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cloudflare.svg 
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


The Cloudflare web application firewall (WAF) protects your internet property against malicious attacks that aim to exploit vulnerabilities such as SQL injection attacks, cross-site scripting, and cross-site forgery requests.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
 <TabItem value="use-s3" label="Send logs using S3" default>


For an overview of Cloudflare logs, and the related S3 and Logpush configuration procedures, click [here](https://developers.cloudflare.com/logs/).


To send firewall event logs to Logz.io Cloud SIEM, you'll first configure a Logpush job to send your Cloudflare data to a dedicated S3 bucket, then configure Logz.io to collect and ingest that data from the S3 bucket. 

### Prerequisites

Before you begin, ensure that you have: 

+ Admin access to Cloudflare.
+ Enterprise account with Cloudflare.
+ Admin access to your AWS environment.
+ Configured an S3 bucket for your Cloudflare logs.
  To create an S3 bucket, see the [instructions from Amazon.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
+ Logs of your HTTP requests uploaded to Amazon S3.
+ [Enabled the Cloudflare Logppush service](https://developers.cloudflare.com/logs/get-started/logpush-dashboard) for the assets you want to monitor in Cloudflare, via **Analytics > Logs > Connect a service**.


##### Configure Logpush to send logs to the S3 bucket

To configure Logpush to stream logs of Cloudflare's datasets to your cloud service in batches, follow the [Cloudflare procedure](https://developers.cloudflare.com/logs/get-started/enable-destinations/aws-s3/) to enable the Logpush service to access Amazon S3. <!--  deprecated link (https://developers.cloudflare.com/logs/logpush/aws-s3  -->

For an overview of the Logpush service, [click here](https://developers.cloudflare.com/logs/about)

##### Configure Logz.io to collect logs from the S3 bucket. 

Use [our procedure](https://docs.logz.io/docs/shipping/aws/aws-s3-bucket/#configure-logzio-to-fetch-logs-from-an-s3-bucket) to configure Logz.io to fetch logs from your S3 bucket.


  </TabItem>
  <TabItem value="use-cf-api" label="Send logs using Cloudflare API" default>

You can send available logs from the Cloudflare API with Logzio API fetcher.

## Pull Docker Image
Download the logzio-api-fetcher image:

```shell
docker pull logzio/logzio-api-fetcher
```

## Configuration
Create a local config file `config.yaml`.  

```yaml
apis:
  - name: cloudflare example
    type: cloudflare
    cloudflare_account_id: <<CLOUDFLARE_ACCOUNT_ID>>
    cloudflare_bearer_token: <<CLOUDFLARE_BEARER_TOKEN>>
    url: https://api.cloudflare.com/client/v4/accounts/alerting/v3/history
    next_url: https://api.cloudflare.com/client/v4/accounts/{account_id}/alerting/v3/history?since={res.result.[0].sent}
    days_back_fetch: 7
    additional_fields:
      type: cloudflare

logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOGZIO_SHIPPING_TOKEN>>
```

:::note
You can customize the endpoints to collect data by adding or modifying the configurations under the `apis` section. Refer to the [relevant API documentation](https://developers.cloudflare.com/api/) for more details.
:::

### Cloudflare configuration options
| Parameter Name          | Description                                                                                                                                 | Required/Optional | Default           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|
| name                    | Name of the API (custom name)                                                                                                               | Optional          | the defined `url` |
| cloudflare_account_id   | The CloudFlare Account ID                                                                                                                   | Required          | -                 |
| cloudflare_bearer_token | The Cloudflare Bearer token                                                                                                                 | Required          | -                 |
| url                     | The request URL                                                                                                                             | Required          | -                 |
| next_url                | If needed to update the URL in next requests based on the last response. Supports using variables. | Optional          | -                 |
| additional_fields       | Additional custom fields to add to the logs before sending to logzio                                                                        | Optional          | -                 |
| days_back_fetch         | The amount of days to fetch back in the first request. Applies a filter on `since` parameter.                                               | Optional          | -                 |
| scrape_interval         | Time interval to wait between runs (unit: `minutes`)                                                                                        | Optional          | 1 (minute)        |
| pagination_off          | True if builtin pagination should be off, False otherwise                                                                                   | Optional          | `False`           |

### Logzio output configuration options
| Parameter Name | Description                 | Required/Optional | Default                         |
|----------------|-----------------------------|-------------------|---------------------------------|
| url            | The logzio Listener address (You can find the relevant `<<LISTENER-HOST>>` [here](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs).) | Optional          | `https://listener.logz.io:8071` |
| token          | The logzio shipping token   | Required          | -                               |


## Run The Docker Container
In the path where you saved your `config.yaml`, run:
```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher 
```

:::note
To run in Debug mode add `--level` flag to the command:
```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher \
--level DEBUG
```
Available Options: `INFO`, `WARN`, `ERROR`, `DEBUG`
:::

### Stopping the container
When you want to stop the container, to make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the docker stop command:

```shell
docker stop -t 30 logzio-api-fetcher
```


  </TabItem>
</Tabs>


##### Check Logz.io for your logs

Give your Cloudflare data some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your data, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 

