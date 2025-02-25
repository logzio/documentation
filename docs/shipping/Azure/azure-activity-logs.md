---
id: Azure-Activity-logs
title: Azure Activity Logs
overview: Ship your Azure activity logs using an automated deployment process.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Azure', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/azure-monitor.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Automate the deployment of your Azure activity logs. By the end of this process, you will have an event hub namespace, an event hub, and two storage blobs configured.

The deployed resources will collect data from a single Azure region.

:::note
[Project's GitHub repo](https://github.com/logzio/azure-serverless/)
:::

## Configuration via Azure ARM template

### 1. Deploy the Logz.io template 👇

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flogzio%2Fazure-serverless%2Fmaster%2Fdeployments%2Fazuredeploylogs.json)

This deployment will create the following services:
* Serverless Function App (Python-based)
* Event Hubs Namespace
* Event Hubs Instance
* Storage account: 
  - Function's logs containers
  - Failed shipments logs container
* App Service Plan
* Log Analytics Workspace
* Application Insights


### 2. Configure the template

Use these settings when configuring the template:

| Parameter       | Description                                                             |
|-----------------|-------------------------------------------------------------------------|
| Resource group* | Create a new resource group or select an existing one.                  |
| Region*         | Select the region closest to your Azure services.                       |
| LogzioURL*      | Use the listener URL specific to your Logz.io account region.           |
| LogzioToken*    | Your Logz.io logs shipping token.                                       |
| ThreadCount     | Number of threads for the Function App (default: 4).                    |
| bufferSize      | Maximum number of messages to accumulate before sending (default: 100). |
| intervalTime    | Interval time for sending logs in milliseconds (default: 10000).        |
| maxTries        | The maximum number of retries for the backoff mechanism (default: 3).   |
| logType         | The type of the logs being processed (default: eventHub).               |

*Required fields.

At the bottom of the page, click **Review + Create**, then select **Create** to deploy.

Deployment may take a few minutes.

### 3. Stream Azure service data

Once deployment is complete, configure your Azure services to stream logs to the newly created Event Hub. For each service:

1. Create diagnostic settings.
2. Under **Event hub policy name**, select the appropriate policy (e.g., `RootManageSharedAccessKey`).

For more details, see [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-stream-monitoring-data-event-hubs).


### 4. Check Logz.io for your data

Give your data some time to be processed, and then open Logz.io.

If everything went according to plan, you should see logs with the type `eventHub` in Explore.

## Backup for unshipped logs

The deployment includes a backup mechanism for logs that fail to ship to Logz.io. By default, these logs are stored in the **failedlogbackup** blob container, but this can be customized to a different container name of your choice during the setup process.

## Post-deployment configuration

To modify configuration after deployment, go to your Function App's **Configuration** tab. You can adjust settings such as `LogzioURL`, `LogzioToken`, `bufferSize`, and more.

## Configuration via Terraform

You can use Terraform as an alternative to the Azure Template to set up your log shipping environment. The Terraform configuration files are available [here](https://github.com/logzio/azure-serverless/tree/master/deployments). Follow these steps to deploy the integration using Terraform:

### Prerequisites
- Terraform installed on your local machine.
- Azure CLI installed and configured with your Azure account credentials.

### Deploying with Terraform

1. **Download the Terraform Configuration**: Use curl to download only the azuredeploylogs.tf and variables.tf files from the GitHub repository.

   ```bash
    curl -O https://raw.githubusercontent.com/logzio/azure-serverless/master/deployments/azuredeploylogs.tf \
   &&
   curl -O https://raw.githubusercontent.com/logzio/azure-serverless/master/deployments/variables.tf
   ```

2. **Create a `.tfvars` File**: Create a `terraform.tfvars` file in the same folder to specify your configurations, such as your Logz.io token.
    
    ```hcl
    logzio_url = "https://<<LISTENER-HOST>>:8071"
    logzio_token = "<<LOG-SHIPPING-TOKEN>>"
    thread_count = 4
    buffer_size = 100
    interval_time = 10000
    max_tries = 3
    log_type = "eventHub"
    ```
   
3. **Initialize Terraform**: Run the Terraform initialization to install the necessary plugins.
   
   ```bash
    terraform init
   ```

4. **Apply Terraform Configuration**: Deploy the infrastructure using `terraform apply`. You will be prompted to review the proposed changes before applying the configuration.
   
   ```bash
    terraform apply
   ```
    Type **yes** when prompted to confirm the deployment.
    
5. **Verify Deployment**: After successful application of the Terraform configuration, your Azure services will be set up and ready for log shipping.

