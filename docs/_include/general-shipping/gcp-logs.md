
:::note
This integration is based on [`logzio-google-pubsub`](https://github.com/logzio/logzio-google-pubsub).
:::

**Before you begin, you'll need**:

* Login to your GCP account.

### Run Google Cloud Shell configuration

[Click this link](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/logzio/logzio-google-pubsub
) to clone the solution's repo and use it in your Google Cloud Shell.

:::note
If a pop-up window appears, check the `Trust repo` box and press `Confirm`.
:::

### Run setup script in Google Cloud Shell

Copy the following snippet and paste in your Google Cloud Shell:

```shell
./run.sh --listener_url=<<LISTENER-HOST>> --token=<<LOG-SHIPPING-TOKEN>> --gcp_region=<<GCP-REGION>> --log_type=<<LOG-TYPE>> --function_name=<<FUNCTION-NAME>> --telemetry_list=<<TELEMETRY-LIST>>
```

When you run this script, you should choose the project ID where you need to run the integration.

Replace the variables as per the table below:



| Parameter      | Description                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<<LISTENER-HOST>>`   | Use the listener URL specific to the region of your Logz.io account. You can look it up [here](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/).                                             |
| `<<LOG-SHIPPING-TOKEN>>`          | The logs' shipping token of the account you want to ship to.                                                                                                                                              |
| `<<GCP-REGION>>`     | Region where you want to upload Cloud Function. Requires for Deploy to Cloud option for platform.                                                                                                     |
| `<<LOG-TYPE>>`       | Log type. Help classify logs into different classifications. (Default: `gcp-pubsub`)                                                                                                                       |
| `<<FUNCTION-NAME>>`  | Function name will be using as Google Cloud Function name. (Default: `logzioHandler`)                                                                                                                      |
| `<<TELEMETRY-LIST>>` | Will send logs that match the Google resource type. Detailed list you can find [here](https://cloud.google.com/logging/docs/api/v2/resource-list) (ex: `pubsub_topic,pubsub_subscription`). For all services insert `all_services`. |


#### Updating `telemetry_list` after creation

To update the resources that are monitored by the function follow the steps:
1. Go to Log router page.
2. Choose `logzioHandler-sink-logs-to-logzio`.
3. Edit the sink.
4. Update the query which filters for the resource types to monitor.
