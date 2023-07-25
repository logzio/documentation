---
id: Azure-Native
title: Azure Native logs
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/Azure-native-integration2.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

 

You can use Logz.io's Cloud-Native Observability Platform to monitor the health and performance of your Azure environment through the Azure portal.

To learn more about this solution, refer to [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/partner-solutions/logzio/overview).

### Enable single sign-on

You can use Security Assertion Markup Language (SAML) SSO feature within the Logz.io resource to directly access Logz.io's Cloud-Native Observability Platform in your portal.

To learn more about this solution, refer to [Logz.io documentation on SSO](https://docs.logz.io/user-guide/users/single-sign-on/azure_marketplace_liftr.html) and [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/partner-solutions/logzio/setup-sso).


### Manage the platform options

Purchases using CSP subscriptions are not supported at the moment.
:::

Logz.io's Cloud-Native Observability Platform provides a variety of different options to manage the monitoring of your Azure environment.

To learn more about this, refer to [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/partner-solutions/logzio/manage).

### Start your own Logz.io observability journey

Start your journey with Logz.io in Azure [here](https://portal.azure.com/#create/logz.logzio_via_liftr/preview).

 

You can create a Logz.io account in Azure using Terraform.


**Before you begin, you'll need**:

* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
* Azure subscription


 

##### Connect to your Azure account

Login to Azure first:

```shell
az login
```

Then connect to your account subscription:


```shell
az account set --subscription="<<SUBSCRIPTION_ID>>"
```

* Replace `<<SUBSCRIPTION_ID>>` with the Subscription ID where you want to create your Logz.io resources.

##### Configure Terraform to login to your Azure subscription

Create a Terraform script with the following configuration:

```
# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.46.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  subscription_id = "<<SUBSCRIPTION_ID>>"
}
```

* Replace `<<SUBSCRIPTION_ID>>` with the Subscription ID where you want to create your Azure account.


##### Configure Logz.io monitor

Add the following code block to the same Terraform script:

```
resource "azurerm_resource_group" "logzio_resource_group" {
  name     = "<<RESOURCE-GROUP-NAME-AZURE>>"
  location = "<<RESOURCE-GROUP-REGION>>"
}

resource "azurerm_logz_monitor" "logzio_account" {
  name                = "<<LOGZIO-RESOURCE-NAME>>"
  resource_group_name = azurerm_resource_group.logzio_resource_group.name
  location            = azurerm_resource_group.logzio_resource_group.location
  plan {
    billing_cycle  = "MONTHLY"
    effective_date = "<<EFFECTIVE-DATE>>"
    plan_id        = "100gb14days"
    usage_type     = "PAYG"
  }

  user {
    email        = "<<USER-EMAIL>>"
    first_name   = "<<USER-FIRST-NAME>>"
    last_name    = "<<USER-LAST-NAME>>"
    phone_number = "<<USER-PHONE-NUMBER>>"
  }
}
```

Define the parameters as per the table below:

| Parameter | Description |
|---|---|
| `<<RESOURCE-GROUP-NAME-AZURE>>` | Name for your resource group in Azure. |
| `<<RESOURCE-GROUP-REGION>>` | Azure region for your resource group. |
| `<<LOGZIO-RESOURCE-NAME>>` | Name for your Logz.io account and resource in your Azure resource group. |
| `<<EFFECTIVE-DATE>>` | Current date in `yyyy-mm-ddThh:mm:ss.s+zzzzzz` format. |
| `<<USER-EMAIL>>` | Email address attached to the Azure account where you need to create the Logz.io resource group. |
| `<<USER-FIRST-NAME>>` | Account user's first name. |
| `<<USER-LAST-NAME>>` | Account user's last name. |
| `<<USER-PHONE-NUMBER>>` | Account user's phone number. |



##### Configure the tag rule

Add the following code block to the same Terraform script:

```
resource "azurerm_logz_tag_rule" "logzio_tags" {
  logz_monitor_id = azurerm_logz_monitor.logzio_tags.id
  tag_filter {
    name   = "<<TAG-FILTER-NAME>>"
    action = "<<TAG-FILTER-ACTION>>"
    value  = "<<TAG-VALUE>>"
  }

  send_aad_logs          = <<boolean>>
  send_activity_logs     = <<boolean>>
  send_subscription_logs = <<boolean>>
```

Define the parameters as per the table below:

| Parameter | Description |
|---|---|
| `<<TAG-FILTER-NAME>>` | Name for the tag filter. |
| `<<TAG-FILTER-ACTION>>` | The action for a filtering tag. Possible values are `Include` and `Exclude`. `Exclude` takes priority over the `Include`. |
| `<<TAG-VALUE>>` | Optional. The value of the tag filter. |
| send_aad_logs | (Optional) Whether AAD logs should be sent to the Monitor resource. |
| send_activity_logs | (Optional) Whether activity logs from Azure resources should be sent to the Monitor resource. |
| send_subscription_logs | (Optional) Whether subscription logs should be sent to the Monitor resource. |

  
  

##### Initialize a working directory

Run the following command from the directory of your Terrafrom script:

```shell
terraform init
```

##### Create the Terraform execution plan

```shell
terraform plan -out terraform.plan
```

##### Execute the Terraform plan

```shell
terraform apply terraform.plan
```


  