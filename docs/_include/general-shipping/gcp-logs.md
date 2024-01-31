

**Before you begin, you'll need**:

* Login to your GCP account.

### Run Google Cloud Shell configuration

Use the following link, to clone the solution's repo and use it in your Google Cloud Shell:

```shell
https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/logzio/logzio-google-pubsub
```

You may encounter a pop up window. Check the `Trust repo` checkbox, and press `Confirm`.

### Run setup script in Google Cloud Shell

Copy the following snippet and paste in your Google Cloud Shell:

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
| `telemetry_list` | Will send logs that match the Google resource type. Detailed list you can find [here](https://cloud.google.com/logging/docs/api/v2/resource-list) (ex: `pubsub_topic,pubsub_subscription`). For all services insert `all_services`. |