---
id: Azure-Diagnostic-Logs
title: Azure Diagnostic Logs
overview: Ship your Azure diagnostic logs using an automated deployment process.
product: ['logs']
os: ['windows', 'linux']
filters: ['Azure', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/azure-monitor.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Ship your Azure diagnostic logs using an automated deployment process.
At the end of this process, your Azure function will forward logs from an Azure Event Hub to your Logz.io account.


![Overview of Azure Diagnostic Logz.io integration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure-diagnostic-logs/logzio-eventhub-diagram.svg)s

:::note
[Project's GitHub repo](https://github.com/logzio/azure-serverless/)
:::


## Setting up Log Shipping from Azure

### Deploy the Logz.io Python Template👇 

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

### Configure the Template

Use these settings when configuring the template:

| Parameter       | Description                                                             |
|-----------------|-------------------------------------------------------------------------|
| Resource group* | Create a new resource group or select an existing one.                  |
| Region*         | Select the region closest to your Azure services.                       |
| LogzioURL*      | Select a predefined listener URL for your region, or choose CUSTOM to specify your own. |
| CustomLogzioURL | Custom listener URL (e.g., https://listener-custom.logz.io:8071). Required only when LogzioURL is set to CUSTOM. |
| UseKeyVaultForToken | If true, read LogzioToken from an existing Key Vault secret reference (default: false). |
| LogzioTokenSecretUri | Full Key Vault Secret URI (prefer versioned), e.g., https://kv-name.vault.azure.net/secrets/secret-name/version. Required when UseKeyVaultForToken is true. |
| KeyVaultResourceId | Resource ID of the existing Key Vault, e.g., /subscriptions/sub-id/resourceGroups/rg-name/providers/Microsoft.KeyVault/vaults/kv-name. Required when UseKeyVaultForToken is true. |
| LogzioToken     | Your Logz.io logs shipping token. Leave empty if UseKeyVaultForToken is true. |
| ThreadCount     | Number of threads for the Function App (default: 4).                    |
| bufferSize      | Maximum number of messages to accumulate before sending (default: 100). |
| intervalTime    | Interval time for sending logs in milliseconds (default: 10000).        |
| maxTries        | The maximum number of retries for the backoff mechanism (default: 3).   |
| logType         | The type of the logs being processed (default: eventHub).               |


*Required fields (LogzioURL and Region are always required; either LogzioToken OR the Key Vault parameters are required).

After setting the parameters, click **Review + Create**, and then **Create** to deploy.

#### Using Azure Key Vault for Token Storage

For enhanced security, you can store your Logz.io token in an existing Azure Key Vault instead of providing it directly as a parameter:

* **Prerequisites**:
   - An existing Azure Key Vault with your Logz.io logs token stored as a secret
   - The deploying user/service principal must have permissions to assign roles on the Key Vault (e.g., "User Access Administrator" or "Owner" role)

* ***Configuration**:
   - Set `UseKeyVaultForToken` to `true`
   - Provide the `LogzioTokenSecretUri` (full secret URI, preferably versioned for deterministic behavior)
   - Provide the `KeyVaultResourceId` (full resource ID of your Key Vault)
   - Leave `LogzioToken` empty

* ***What happens during deployment**:
   - The Function App is created with a system-assigned managed identity
   - The managed identity is automatically granted the "Key Vault Secrets User" role on your Key Vault
   - The Function App's `LogzioToken` setting is configured as a Key Vault reference

* ***Example values**:
   ```
   UseKeyVaultForToken: true
   LogzioTokenSecretUri: https://my-keyvault.vault.azure.net/secrets/logzio-token/abc123def456
   KeyVaultResourceId: /subscriptions/12345678-1234-1234-1234-123456789abc/resourceGroups/my-rg/providers/Microsoft.KeyVault/vaults/my-keyvault
   LogzioToken: "" # leave empty when using Key Vault
   ```

#### Using Custom Listener URLs

If your Logz.io account uses a custom listener URL not available in the predefined list:

- **ARM Template**: Select "CUSTOM" from the `LogzioURL` dropdown, then provide your full custom URL in the `CustomLogzioURL` field (e.g., `https://listener-custom.logz.io:8071`).

- **Terraform**: Set the `logzio_url` variable directly to your custom URL in your `.tfvars` file.


### Stream Azure Service Data

Configure your Azure services to stream logs to the newly created Event Hub. For each service:

1. Create diagnostic settings.
2. Under **Event hub policy name**, select the appropriate policy (e.g., 'RootManageSharedAccessKey').

For more details, see [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-stream-monitoring-data-event-hubs).

#### Verify Data Reception in Logz.io

Allow some time for data to flow from Azure to Logz.io, then check your Logz.io account. You should see logs of the type `eventHub` in Logz.io.

#### Backup for Unshipped Logs

The deployment includes a backup mechanism for logs that fail to ship to Logz.io. By default, these logs are stored in the **failedlogbackup** blob container, but this can be customized to a different container name of your choice during the setup process.

#### Post-Deployment Configuration

To modify configuration after deployment, visit your Function App's **Configuration** tab. You can adjust settings such as `LogzioURL`, `LogzioToken`, `bufferSize`, and more.

### Check Logz.io for your logs

Give your data some time to get from your system to ours, and then open your [Logz.io Open Search Dashboards account](https://app.logz.io/#/dashboard/osd/discover?).
If everything went according to plan, you should see logs of the `type:eventHub` in Open Search Dashboards.

If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).


## Alternative Setup using Terraform

As an alternative to the Azure Template, you can use Terraform to set up your log shipping environment. The Terraform configuration files are located in the **deployments** folder of this repository. Follow the instructions below to deploy this integration using Terraform.

### Prerequisites

- Terraform installed on your local machine.
- Azure CLI installed and configured with your Azure account credentials.

### Steps to Deploy using Terraform

1. **Obtain the Terraform Configuration**: Use curl to download only the `azuredeploylogs.tf` and `variables.tf` files from the GitHub repository.

   ```bash
    curl -O https://raw.githubusercontent.com/logzio/azure-serverless/master/deployments/azuredeploylogs.tf \
   &&
   curl -O https://raw.githubusercontent.com/logzio/azure-serverless/master/deployments/variables.tf
   ```

2. **Create a `.tfvars` File**: Create a `terraform.tfvars` file in the same folder to specify your configurations, such as your Logz.io token.
    ```hcl
    logzio_url = "https://<<LISTENER-HOST>>:8071" # Replace with your actual listener URL
    logzio_token = "<<LOG-SHIPPING-TOKEN>>"
    thread_count = 4
    buffer_size = 100
    interval_time = 10000
    max_tries = 3
    log_type = "eventHub"
   
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


### Check Logz.io for your logs

Give your data some time to get from your system to ours, and then open your [Logz.io Open Search Dashboards account](https://app.logz.io/#/dashboard/osd/discover?).
If everything went according to plan, you should see logs of the `type:eventHub` in Open Search Dashboards.

If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

### Migration to Log Analytics Workspace-Based Model

For users currently on the Classic Application Insights, it's essential to migrate to the Log Analytics workspace-based model. To do this:

1. Navigate to your Application Insights resource that hasn't been migrated yet.
2. Click on the notification that states "Classic Application Insights is deprecated."
3. A "Migrate to Workspace-based" dialog will appear. Here, confirm your preferred Log Analytics Workspace and click 'Apply'.

:::caution important
Be aware that once you migrate to a workspace-based model, the process cannot be reversed.
:::
