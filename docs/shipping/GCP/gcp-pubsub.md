---
id: GCP-PubSub
title: GCP PubSub
overview: Google Pub/Sub is designed to provide reliable, many-to-many, asynchronous messaging between applications. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/pubsub.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Google Pub/Sub provides reliable, many-to-many, asynchronous messaging between applications. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Google Pub/Sub metrics to Logz.io, you need to add the **inputs.stackdriver** and **outputs.http** plug-ins to your Telegraf configuration file.


**Before you begin, you'll need**:

* GCP project
* [gcloud CLI](https://cloud.google.com/sdk/docs/install)
* [jq](https://stedolan.github.io/jq/download/)

## Default configuration

### Connect to the relevant GCP project


Log in to your GCP account:

```shell
gcloud auth login
```

Navigate to the relevant project.

Set the `project id` for the project that you want to send logs from: 

```shell
gcloud config set project <PROJECT_ID>
```

Replace `<PROJECT_ID>` with the relevant project Id.

### Run the logzio-google-pubsub

Donwload and unzip the latest release of [logzio-google-pubsub](https://github.com/logzio/logzio-google-pubsub).

Navigate to the builder folder.

Allow the `sh` file to execute code:

```shell
chmod +x run.sh
```

Run the code:

```shell
./run.sh --listener_url=<listener_url> --token=<token> --gcp_region=<region> --log_type=<type> --function_name=<function_name> --telemetry_list=<telemetry_list>
```

When you run this script, you should choose the project ID where you need to run the integration.

Replace the variables as per the table below:



| Parameter      | Description                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listener_url`   | Use the listener URL specific to the region of your Logz.io account. You can look it up [here](https://docs.logz.io/user-guide/accounts/account-region.html).                                             |
| token          | The logs' shipping token of the account you want to ship to.                                                                                                                                              |
| `gcp_region`     | Region where you want to upload Cloud Function. Requires for Deploy to Cloud option for platform.                                                                                                     |
| `log_type`       | Log type. Help classify logs into different classifications. (Default:`gcp-pubsub`)                                                                                                                       |
| `function_name`  | Function name will be using as Google Cloud Function name. (Default:`logzioHandler`)                                                                                                                      |
| `telemetry_list` | **_Optional_** Will send logs that match the Google resource type. Detailed list you can find [here](https://cloud.google.com/logging/docs/api/v2/resource-list) (ex: `pubsub_topic,pubsub_subscription`) |


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


## Optional configuration with Telegraf

### Set relevant credentials in GCP

1. Navigate to the [Project selector](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create) and choose the project to send metrics from.
2. In the **Service account details** screen, give the service account a unique name and select **Create and continue**.
3. In the **Grant this service account access to project** screen, add the following roles: Compute Viewer, Monitoring Viewer, and Cloud Asset Viewer.
4. Select **Done**.
5. Select your project in the **Service accounts for project** list.
6. Select **KEYS**.
7. Select **Keys > Add Key > Create new key** and choose JSON as the type.
8. Select **Create and Save**.

:::note
You must be a Service Account Key Admin to select Compute Engine and Cloud Asset roles.
:::
 

### Add an environment variable for the key


On your machine, run:

```shell
export GOOGLE_APPLICATION_CREDENTIALS=<<PATH-TO-YOUR-GCP-KEY>>
```

Replace `<<PATH-TO-YOUR-GCP-KEY>>` with the path to the JSON file created in the previous step.


### Set relevant credentials in GCP

1. Navigate to the [Project selector](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create) and choose the project to send metrics from.
2. In the **Service account details** screen, give the service account a unique name and select **Create and continue**.
3. In the **Grant this service account access to project** screen, add the following roles: Compute Viewer, Monitoring Viewer, and Cloud Asset Viewer.
4. Select **Done**.
5. Select your project in the **Service accounts for project** list.
6. Select **KEYS**.
7. Select **Keys > Add Key > Create new key** and choose JSON as the type.
8. Select **Create and Save**.

:::note
You must be a Service Account Key Admin to select Compute Engine and Cloud Asset roles.
:::
 

### Add an environment variable for the key


On your machine, run:

```shell
export GOOGLE_APPLICATION_CREDENTIALS=<<PATH-TO-YOUR-GCP-KEY>>
```

Replace `<<PATH-TO-YOUR-GCP-KEY>>` with the path to the JSON file created in the previous step.




### Configure Telegraf to send your metrics data to Logz.io

**Telegraf version: {@include: ../../_include/metric-shipping/gcp-telegraf-version.md}**

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.stackdriver plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the GCP data from your hosts. To do this, add the below code to the configuration file. 

``` ini
[[inputs.stackdriver]]

  project = "<<YOUR-PROJECT>>"

  metric_type_prefix_include = [
    "pubsub.googleapis.com",
    "pubsublite.googleapis.com",
  ]

  interval = "1m"
```

* Replace `<<YOUR-PROJECT>>` with the name of your GCP project.

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/stackdriver/README.md)
:::
 

#### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}  
  
### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
