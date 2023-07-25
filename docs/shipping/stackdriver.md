---
id: Stackdriver
title: GCP Stackdriver
overview: Google Cloud Platform (GCP) Stackdriver collects logs from your cloud services. You can use Google Cloud Pub/Sub to forward your logs from Stackdriver to Logz.io using a continuously runnung Docker container.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



Google Cloud Platform (GCP) Stackdriver collects logs from your cloud services.
You can use Google Cloud Pub/Sub to forward your logs from Stackdriver to Logz.io using a continuously runnung Docker container .

#### Configuration

**Before you begin, you'll need**:

* [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
* [a GCP project](https://console.cloud.google.com/projectcreate)
* [a GCP Pub/Sub topic and subscribers](https://cloud.google.com/pubsub/docs/quickstart-console) to your GCP project



##### Export your logs to Stackdriver

Set up a sink to export your logs to Stackdriver.

For more information, see
[Exporting with the Logs Viewer](https://cloud.google.com/logging/docs/export/configure_export_v2)
from Google Cloud.

##### Build your credentials file

Create a working directory for this step and `cd` into it.
You'll need to run this command as root:


```shell
mkdir /etc/logzio-pubsub && cd /etc/logzio-pubsub
```

Next, you'll need to build a credentials file so Pub/Sub can authenticate
and get the right permissions.




###### Option 1: Build the credentials file from the command line

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





###### Option 2: Build the credentials file in the Cloud Console

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

###### Variation

* If your credentials file name isn't of the default format `<<project_id>>-credentials.json`, follow [the steps below](#cred-info) as well.




##### Build your Pub/Sub input YAML file

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

###### Configuration instructions

| Parameter | Description |
|---|---|
| listener | The Logz.io listener host. {@include: ../_include/log-shipping/listener-var.html}  |
| pubsubs | This is an array of one or more GCP subscriptions. For each subscription, provide topic and subscription IDs, as given from Pub/Sub. |
| token | Your Logz.io shipping token. For each project under `pubsubs`. Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to. You can send your logs to different accounts that are in the same region, you can do that by inserting a different token per project.  |
| credentials_file (Not required, Default value: `'<project_id>-credentials.json'`) | This field is only required if your credentials file is named differently than the default value. For an example of adding this field go to [input example file](https://github.com/logzio/logzio-pubsub/blob/master/pubsub-input-example.yml). |
{:.paramlist}

##### Pull the Docker image

Download the logzio/logzio-pubsub image:

```shell
docker pull logzio/logzio-pubsub
```

##### Run the container

Run the following command after you replace `<<PROJECT_ID>>`  with your details.

```shell
docker run --name logzio-pubsub \
-v /etc/logzio-pubsub/pubsub-input.yml:/logzio-pubsub/pubsub-input.yml \
-v /etc/logzio-pubsub/<<PROJECT_ID>>-credentials.json:/logzio-pubsub/<<PROJECT_ID>>-credentials.json \
logzio/logzio-pubsub
```

###### Variations

* If you're working with multiple topics, add this line for every credentials file you've created. Insert your project id instead of the parameters:

```
-v /etc/logzio-pubsub/<PROJECT_ID>-credentials.json:/logzio-pubsub/<PROJECT_ID>-credentials-file.json \
```


* If your credentials file name isn't of the default format `<<project_id>>-credentials.json`, follow [the steps below](#cred-info) as well.

* If you're using a Mac, you'll need to fix issues with mounting files from root directory.
Add the path '/etc/logzio-pubsub' to your Docker File Sharing. Click [here](https://medium.com/effy-tech/fixing-the-var-folders-error-in-docker-for-mac-v2-2-3-2a40e776132d) for a guide on how to fix this issue - you can use docker desktop or manually edit your Docker configuration file.
For more information about mounting files from the root directory click [here](https://docs.docker.com/docker-for-mac/osxfs/#namespaces).


##### Check Logz.io for your logs

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

`-v /etc/logzio-pubsub/<<credentials-file-name>>.json:/logzio-pubsub/<<credentials-file-name>>.json \`

Replace `<<credentials-file-name>>` with your credentials file's name.




