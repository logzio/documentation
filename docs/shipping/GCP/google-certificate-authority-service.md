---
id: google-certificate-authority-service
title: Google Certificate Authority Service
overview: Google Certificate Authority Service is a highly available, scalable Google Cloud service that enables you to simplify, automate, and customize the deployment, management, and security of private certificate authorities (CA). Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/certmanager.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---

Google Certificate Authority Service is a highly available, scalable Google Cloud service that enables you to simplify, automate, and customize the deployment, management, and security of private certificate authorities (CA). Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Google Certificate Authority Service metrics to Logz.io, you need to add the **inputs.stackdriver** and **outputs.http** plug-ins to your Telegraf configuration file.


**Before you begin, you'll need**:
 GCP project

 

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

### Configuring Telegraf to send your metrics data to Logz.io


**Telegraf version: {@include: ../../_include/metric-shipping/gcp-telegraf-version.md}**

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.stackdriver plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the GCP data from your hosts. To do this, add the below code to the configuration file. 

``` ini
[[inputs.stackdriver]]

  project = "<<YOUR-PROJECT>>"

  metric_type_prefix_include = [
    "privateca.googleapis.com",
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


 
