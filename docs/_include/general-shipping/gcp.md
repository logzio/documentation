

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
