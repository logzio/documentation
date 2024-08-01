
:::note
This integration is based on [`logzio-google-metrics`](https://github.com/logzio/logzio-google-metrics).
:::

**Before you begin, you'll need**:

* Login to your GCP account.

### Run Google Cloud Shell configuration

[Click this link](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/logzio/logzio-google-metrics
) to clone the solution's repo and use it in your Google Cloud Shell.

:::note
You may encounter a pop up window. Check the `Trust repo` checkbox, and press `Confirm`.
:::

### Run setup script in Google Cloud Shell

Copy the following snippet and paste in your Google Cloud Shell:

```shell
./run.sh --listener_url=<<LISTENER-HOST>> --token=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>> --gcp_region=<<GCP-REGION>> --function_name=<<FUNCTION-NAME-PREFIX>> --telemetry_list=<<TELEMETRY-LIST>>
```

When you run this script, you should choose the project ID where you need to run the integration.

Replace the variables as per the table below:



| Parameter      | Description                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<<LISTENER-HOST>>`   | Use the listener URL specific to the region of your Logz.io account. You can look it up [here](https://docs.logz.io/user-guide/accounts/account-region.html).                                             |
| `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>`          | The metrics' shipping token of the account you want to ship to.                                                                                                                                              |
| `<<GCP-REGION>>`     | Region where you want to upload Cloud Function. Requires for Deploy to Cloud option for platform.                                                                                                     |
| `<<FUNCTION-NAME-PREFIX>>`  | Function name will be using as Google Cloud Function name. (Default: `metrics_gcp`)                                                                                                                      |
| `<<TELEMETRY-LIST>>` | Will send metrics that match the Google metric type. Detailed list you can find [here](https://cloud.google.com/monitoring/api/metrics_gcp) (ex: `cloudfunctions.googleapis.com`) |