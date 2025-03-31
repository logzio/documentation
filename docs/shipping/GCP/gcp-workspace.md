---
id: GCP-Workspace
title: GCP Workspace
overview: Send Google Cloud Workspace metrics to your Logz.io account.
product: ['logs', 'metrics', 'siem']
os: ['windows', 'linux']
filters: ['GCP', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/google-workspace.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Google Workspace is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Logs
You can send your data to Logz.io using one of the following methods:

<Tabs>
 <TabItem value="GCP-Pubsub" label="Google Pub\Sub" default>

### Google Cloud Pub/Sub
Forward Google Workspace Logs to Google Cloud Platform (GCP) and use Logz.io’s Pub/Sub integration to forward the data to Logz.io.

{@include: ../../_include/general-shipping/gcp-logs.md}

  </TabItem>
  <TabItem value="API-Fetcher" label="Google API" default>

### Google Workspace API
Extract data directly from the Google Workspace API and forward it to Logz.io using the Logz.io API Fetcher.

### Prerequisites

Please follow [Google guide to enable Google Workspace API](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs#before-you-begin) under `Before you begin` section to configure the below:

#### Enable the APIs
Enable the following APIs in your Google Cloud project:

- [Google Workspace Admin SDK](https://developers.google.com/admin-sdk/admin-settings)
- [Alert Center API](https://developers.google.com/admin-sdk/alertcenter/quickstart/java#turn_on_the_api)

#### Create a Service account
To allow [Service-to-Service interactions](https://developers.google.com/identity/protocols/oauth2#serviceaccount) to authenticate with the Google API, [create a service account](https://cloud.google.com/iam/docs/service-accounts-create#creating) for your Google Cloud project.

#### Create a delegated user
[Create a Super Admin user](https://support.google.com/search?q=workspace+how+to+assign+a+super+admin+role) that impersonates the service account, and assign it to a new role which holds the [privalages to the APIs you'd like to access](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs#:~:text=Privileges%20%3E%20Reports,Privileges%20%3E%20Groups%20%3E%20Read).

#### Create a Service account key
[Create a Service account Key](https://cloud.google.com/iam/docs/keys-create-delete#creating) for the Service account you created at step 2. Save the key JSON file in the same path where you'll sav the API Fetcher configuration (and run the program from) later on.

#### Setup Domain wide delegations
[Setup Domain wide delegations](https://support.google.com/a/answer/162106?=en#zippy=%2Cset-up-domain-wide-delegation-for-a-client) so the Service account can access the APIs you'd like to access.

:::note
For Google Workspace Activity logs, the scope `https://www.googleapis.com/auth/admin.reports.audit.readonly` is enough.
:::

### Pull Docker Image
Download the logzio-api-fetcher image:

```sh
docker pull logzio/logzio-api-fetcher
```

### Configuration
Create a local config file `config.yaml`. Save it in the same path where you saved your Google Workspace Service Account Key JSON.

```yaml
apis:
  - name: google saml
    type: google_activity
    google_ws_sa_file_name: credentials_file.json
    google_ws_delegated_account: user@example.com
    application_name: saml
    additional_fields:
      type: google_activity
    days_back_fetch: 7
    scrape_interval: 5

  - name: google user accounts
    type: google_activity
    google_ws_sa_file_name: credentials_file.json
    google_ws_delegated_account: user@example.com
    application_name: user_accounts
    additional_fields:
      type: google_activity
    days_back_fetch: 7
    scrape_interval: 5

  - name: google login
    type: google_activity
    google_ws_sa_file_name: credentials_file.json
    google_ws_delegated_account: user@example.com
    application_name: login
    additional_fields:
      type: google_activity
    days_back_fetch: 7
    scrape_interval: 5

  - name: google admin
    type: google_activity
    google_ws_sa_file_name: credentials_file.json
    google_ws_delegated_account: user@example.com
    application_name: admin
    additional_fields:
      type: google_activity
    days_back_fetch: 7
    scrape_interval: 5

  - name: google groups
    type: google_activity
    google_ws_sa_file_name: credentials_file.json
    google_ws_delegated_account: user@example.com
    application_name: groups
    additional_fields:
      type: google_activity
    days_back_fetch: 7
    scrape_interval: 5

logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>
```

:::note
You can customize the endpoints to collect data by adding or modifying the configurations under the apis section. Refer to the [relevant API documentation](https://developers.google.com/workspace/admin/reference-overview) for more details.
:::

#### Google Workspace Activity Configuration Options

To send [Google Activity](https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list#Activity) logs, use `google_activity` API type.

| Parameter Name              | Description                                                                                                                                                                                                                                         | Required/Optional | Default                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------------------|
| name                        | Name of the API (custom name)                                                                                                                                                                                                                       | Optional          | `Google Workspace`                      |
| google_ws_sa_file_name      | The name of the service account credentials file. **Required unless** `google_ws_sa_file_path` is set.                                                                                                                                              | Required*         | `""`                                    |
| google_ws_sa_file_path      | The path to the service account credentials file. **Required unless** `google_ws_sa_file_name` is set. Use this if mounting the file to a different path than the default.                                                                          | Optional*         | `./src/shared/<google_ws_sa_file_name>` |
| google_ws_delegated_account | The email of the user for which the application is requesting delegated access                                                                                                                                                                      | Required          | -                                       |
| application_name            | Specifies the [Google Workspace application](https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list#applicationname) to fetch activity data from (e.g., `saml`, `user_accounts`, `login`, `admin`, `groups`, etc). | Required          | -                                       |
| user_key                    | The unique ID of the user to fetch activity data for                                                                                                                                                                                                | Optional          | `all`                                   |
| additional_fields           | Additional custom fields to add to the logs before sending to logzio                                                                                                                                                                                | Optional          | -                                       |
| days_back_fetch             | The amount of days to fetch back in the first request                                                                                                                                                                                               | Optional          | 1 (day)                                 |
| scrape_interval             | Time interval to wait between runs (unit: `minutes`)                                                                                                                                                                                                | Optional          | 1 (minute)                              |


#### Google Workspace General Configuration Options

To configure a [different Google Workspace API](https://developers.google.com/workspace/admin/reference-overview) as source, use `type` as `google_workspace`, and configure it as necessary.

By default `google_workspace` API type has built in pagination settings and sets the `response_data_path` to `items` field.

| Parameter Name              | Description                                                                                                                                                                | Required/Optional | Default                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------|
| name                        | Name of the API (custom name)                                                                                                                                              | Optional          | `Google Workspace`                                                 |
| google_ws_sa_file_name      | The name of the service account credentials file. **Required unless** `google_ws_sa_file_path` is set.                                                                     | Required*         | `""`                                                               |
| google_ws_sa_file_path      | The path to the service account credentials file. **Required unless** `google_ws_sa_file_name` is set. Use this if mounting the file to a different path than the default. | Optional*         | `./src/shared/<google_ws_sa_file_name>`                            |
| google_ws_delegated_account | The email of the user for which the application is requesting delegated access                                                                                             | Required          | -                                                                  |
| scopes                      | The OAuth 2.0 scopes that you might need to request to access Google APIs                                                                                                  | Optional          | `["https://www.googleapis.com/auth/admin.reports.audit.readonly"]` |
| data_request                | Nest here any detail relevant to the data request. (Options in [General API](https://docs.logz.io/docs/log-management/api-fetcher/#configure-your-apis))                                                                        | Required          | -                                                                  |
| additional_fields           | Additional custom fields to add to the logs before sending to logzio                                                                                                       | Optional          | -                                                                  |
| days_back_fetch             | The amount of days to fetch back in the first request                                                                                                                      | Optional          | 1 (day)                                                            |
| scrape_interval             | Time interval to wait between runs (unit: `minutes`)                                                                                                                       | Optional          | 1 (minute)                                                         |


#### Logzio output configuration options

:::note
To configure multiple outputs (in order to send different API data to different Logz.io accounts), please refer to [the linked docs](https://docs.logz.io/docs/log-management/api-fetcher/#add-your-logzio-listener-and-token).
:::

| Parameter Name | Description                 | Required/Optional | Default                         |
|----------------|-----------------------------|-------------------|---------------------------------|
| url            | The logzio Listener address | Optional          | `https://listener.logz.io:8071` |
| token          | The logzio shipping token   | Required          | -                               |

### Run The Docker Container
In the path where you saved your `config.yaml` and your Google Workspace Service account key JSON, run:
```sh
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

### Check Logz.io for your logs


Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).
 

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
