---
id: GCP-Stackdriver
title: GCP Operation Suite (Stackdriver)
overview: Send Google Cloud Operation Suite (Stackdriver) metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Monitoring']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcp-stackdriver.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Logs

**Default integration**

{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `gce_operation`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

**Integration via Google Cloud Pub/Sub**


Google Cloud Platform (GCP) Stackdriver collects logs from your cloud services.
You can use Google Cloud Pub/Sub to forward your logs from Stackdriver to Logz.io using a continuously runnung Docker container .

**Before you begin, you'll need**:

* [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
* [a GCP project](https://console.cloud.google.com/projectcreate)
* [a GCP Pub/Sub topic and subscribers](https://cloud.google.com/pubsub/docs/quickstart-console) to your GCP project


### Export your logs to Stackdriver

Set up a sink to export your logs to Stackdriver.

For more information, see
[Exporting with the Logs Viewer](https://cloud.google.com/logging/docs/export/configure_export_v2)
from Google Cloud.

### Build your credentials file

Create a working directory for this step and `cd` into it.
You'll need to run this command as root:


```shell
mkdir /etc/logzio-pubsub && cd /etc/logzio-pubsub
```

Next, you'll need to build a credentials file so Pub/Sub can authenticate
and get the right permissions.

You can build it through:

* The command line
* The Cloud console


### Option 1: Build the credentials file from the command line

In this step, you'll build your credentials file using your Google Cloud project ID.

Before you begin, you'll need the gcloud command-line tool (CLI) installed. If it isn't, follow the steps to install it:

  1. [Download](https://cloud.google.com/sdk/docs/quickstarts) the 'google-cloud-sdk' to '/etc/logzio-pubsub'.
  2. Run  ```source '/etc/logzio-pubsub/google-cloud-sdk/path.bash.inc'```.
  If you're are not already logged in to gcloud, you will be requested to login through your browser.

Run the following command for each project you're working with. Replace the placeholder with your project id before running the command:

```shell
wget https://raw.githubusercontent.com/logzio/logzio-pubsub/master/create-credentials.py \
&& python create-credentials.py <<project_id>>
```

If you rename the file, follow these steps as well.



### Option 2: Build the credentials file in the Cloud Console

* In the [GCP Console](https://console.cloud.google.com), go to your project's page.
In the left menu, select **IAM & admin > Service accounts**.

* At the top of the _Service accounts_ page, click **+ CREATE SERVICE ACCOUNT**.

* Give a descriptive **Service account name**, such as "credentials file".
  Click **CREATE** to continue to the _Service account permissions_ page.

* Add the role: 'Pub/Sub Editor'.

* Click **CONTINUE** to _Grant users access to this service account_.
Click **ADD KEY + CREATE NEW KEY** to open the _Create key_ panel.
Select **JSON** and click **CREATE** to save the private key to your machine.

* Click **DONE** to return to the _Service accounts_ page.

* Rename it in the following format: `<project-id>-credentials.json` - replace to your project id.
Move it to the `/etc/logzio-pubsub` folder you've created at the beginning of this step.

#### Variation

* If your credentials file name isn't of the default format `<<project_id>>-credentials.json`, follow the steps below as well.


### Build your Pub/Sub input YAML file

Create a file 'pubsub-input.yml' to hold your Pub/Sub input configuration.
To create the file run the following command as root. Then open the file in your text editor:

```shell
touch /etc/logzio-pubsub/pubsub-input.yml
```

Paste this code block into your file.
Complete configuration instructions are below the code block. 👇

```yaml
listener: <<LISTENER-HOST>>
pubsubs:
- project_id: PROJECT-1_ID
  topic_id: TOPIC-1_ID
  token: <<LOG-SHIPPING-TOKEN>>
  credentials_file: ./credentials-file.json
  subscriptions: [SUB1_ID, SUB2_ID, SUB3_ID]
  type: stackdriver

- project_id: PROJECT-1_ID
  topic_id: TOPIC-2_ID
  token: <<LOG-SHIPPING-TOKEN>>
  credentials_file: ./credentials-file.json
  subscriptions: [SUB1_ID, SUB2_ID, SUB3_ID]
  type: stackdriver

- project_id: PROJECT-3_ID
  topic_id: TOPIC-1_ID
  token: <<LOG-SHIPPING-TOKEN>>
  credentials_file: ./credentials-file.json
  subscriptions: [SUB1_ID, SUB2_ID, SUB3_ID]
  type: stackdriver
```

** Note that YAML files are sensitive to spaces and tabs. We recommend using a YAML validator to make sure that the file structure is correct.

Click here for more information about [filebeat for Google Cloud Pub/Sub](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-input-gcp-pubsub.html#filebeat-input-gcp-pubsub).

### Configuration instructions

| Parameter | Description |
|---|---|
| listener | The Logz.io listener host. {% include log-shipping/listener-var.html %}  |
| pubsubs | This is an array of one or more GCP subscriptions. For each subscription, provide topic and subscription IDs, as given from Pub/Sub. |
| token | Your Logz.io shipping token. For each project under `pubsubs`. Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to. You can send your logs to different accounts that are in the same region, you can do that by inserting a different token per project.  |
| credentials_file (Not required, Default value: `<project_id>-credentials.json`) | This field is only required if your credentials file is named differently than the default value. For an example of adding this field go to [input example file](https://github.com/logzio/logzio-pubsub/blob/master/pubsub-input-example.yml). |

### Pull the Docker image

Download the logzio/logzio-pubsub image:

```shell
docker pull logzio/logzio-pubsub
```

### Run the container

Run the following command after you replace `<<PROJECT_ID>>`  with your details.

```shell
docker run --name logzio-pubsub \
-v /etc/logzio-pubsub/pubsub-input.yml:/logzio-pubsub/pubsub-input.yml \
-v /etc/logzio-pubsub/<<PROJECT_ID>>-credentials.json:/logzio-pubsub/<<PROJECT_ID>>-credentials.json \
logzio/logzio-pubsub
```

### Variations

* If you're working with multiple topics, add this line for every credentials file you've created. Insert your project id instead of the parameters:

    ```
    -v /etc/logzio-pubsub/<<PROJECT_ID>>-credentials.json:/logzio-pubsub/<<PROJECT_ID>>-credentials-file.json \
    ```


* If your credentials file name isn't of the default format `<<project_id>>-credentials.json`, follow the steps below as well.

* If you're using a Mac, you'll need to fix issues with mounting files from root directory.
Add the path '/etc/logzio-pubsub' to your Docker File Sharing. Click [here](https://medium.com/effy-tech/fixing-the-var-folders-error-in-docker-for-mac-v2-2-3-2a40e776132d) for a guide on how to fix this issue - you can use docker desktop or manually edit your Docker configuration file.
For more information about mounting files from the root directory click [here](https://docs.docker.com/docker-for-mac/osxfs/#namespaces).


### Check Logz.io for your logs

Spin up your Docker containers if you haven’t done so already.
Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


####  If you've renamed the credentials file

The default naming convention for the credentials file is: `<<project_id>>-credentials.json`.

When you create the credentials file through the command line, it is automatically named as per the default.

If you create the credentials file using the GCP Console, you'll have the option to select the file name. We strongly recommend that you stick to the default format: `<<project_id>>-credentials.json`.

If you decide to give the credentials file another name, please follow these instructions:

1. On step 3 - building your 'pubsub-input.yml' file, add the field 'credentials_file' with your credentials file's name as the value.

    Go to the github project to see an [example of an input file](https://github.com/logzio/logzio-pubsub/blob/master/pubsub-input-example.yml).

2. On step 5 - running the docker, add the following line for every credentials file you've created:

    `-v /etc/logzio-pubsub/<<credentials-file-name>>.json:/logzio-pubsub/<<credentials-file-name>>.json \`.

    Replace `<<credentials-file-name>>` with your credentials file's name.


**Integration via Filebeat**

Google Workspace is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google. You can ship Google Workspace logs to Logz.io using Filebeat and Google Reports API.


**Before you begin, you'll need**: [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html) installed.

:::note
The GSuite module was [deprecated as of Filebeat 7.12](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-gsuite.html#filebeat-module-gsuite) and has been replaced with the [Google Workspace module](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-google_workspace.html), to align with Google's current naming. The integration remains the same, requiring only that you replace "- module: gsuite" with "- module: google_workspace" in the modules block.
:::


### Google Workspace setup

#### Set up a Service Account


Follow the official Google Workspace [tutorial](https://support.google.com/workspacemigrate/answer/10839762?sjid=10874551070185788155-EU#zippy=%2Cstep-use-google-cloud-to-turn-on-apis) for setting up a service account through IAM.

#### Grant access to the Admin SDK API

Enable access to the following APIs and services. If you can't find the API, specify the API name in **APIs & Services > Library** search box.

* Admin SDK
* People API (If you're using a Google Workspace Migrate version earlier than 2.4.2.0, use the Contacts API instead.)
* Google Workspace Migrate API
* Gmail API
* Google Calendar API
* Google Drive API
* Groups Migration API
* Groups Settings API
* Google Sheets API
* Tasks API

#### Delegate domain-wide authority to your service account

Open your Google Workspace domain’s [Admin console](http://admin.google.com/). Next, navigate to **Main menu** > **Security** > **API controls**.

In the Domain-wide delegation pane, select **Manage Domain Wide Delegation**. 

:::note
If you **can't** find the Manage Domain Wide Delegation option, you will need to **switch to a super-admin** Google Workspace account.
:::

Once you access the **Manage Domain Wide Delegation**, click **Add new**, and fill in the details:

* **Client ID** - Enter the service account's Client ID - you can find it in the service account's details under **Unique ID**. It is also found in the **client_id** field of the credentials file that was auto-downloaded when you created a new key for your service account.
* **OAuth Scopes** - Enter [the admin's API](https://www.googleapis.com/auth/admin.reports.audit.readonly)
* Click **Authorize** to confirm your changes.

#### Filebeat monitoring setup

{@include: ../../_include/log-shipping/certificate.md}


##### Configure Filebeat

Open the Filebeat configuration file (the default path `/etc/filebeat/filebeat.yml`) with your preferred text editor.
Copy and paste the code block below, overwriting the previous contents.

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
### Filebeat


### General
fields:
  logzio_codec: json
  token: <<LOG-SHIPPING-TOKEN>>
  # Replace <<LOG-SHIPPING-TOKEN>> with the token of the account you want to ship to.


  type: google_workspace
fields_under_root: true
encoding: utf-8
ignore_older: 3h

### Modules
filebeat.modules:
- module: google_workspace
  saml:

  # Replace <<PATH_TO_CREDENTIALS_FILE>> with the path to the file. See examples below.
  # Replace <<DELEGATED_ACCOUNT_EMAIL>> with the email address of the Admin (or superadmin) that authorized the domain wide delegation function. 

    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>" 
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  user_accounts:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  login:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  admin:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  drive:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  groups:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"

### Input

### Registry
filebeat.registry.path: /var/lib/filebeat

### Processors
# The following processors are to ensure compatibility with version 7
processors:
- if:
    has_fields: ['gsuite']
  then:
  - rename:
      fields:
      - from: "source"
        to: "gsuite_source"
- rename:
    fields:
    - from: "agent"
      to: "filebeat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source"
    ignore_missing: true
- add_id: ~

### Output 
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"] 
  # Replace <<LISTENER-HOST>> with the host for your region. For example, listener.logz.io if your account is hosted on AWS US East. The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071.


  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

For a full list of available Filebeat configuration options for the Google Workspace module, please see Filebeat's [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-google_workspace.html).


Still in the same configuration file, replace the placeholders to match your specifics.

{@include: ../../_include/log-shipping/certificate.md}

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

* Replace `<<PATH_TO_CREDENTIALS_FILE>>` with the path to the file (for example `./credentials_file.json` with credentials of the service account path that was created on the GCP. It is preferable to use the full path for the file.

* Replace `<<DELEGATED_ACCOUNT_EMAIL>>` with the email address of the Admin (in most cases **superadmin**) that authorized the domain wide delegation function to the service account (GCP) on the **Google Workspace account**.

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).