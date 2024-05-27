---
sidebar_position: 7
title: Terraform Logz.io Provider
description: Build Logz.io integrations with Terraform 
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [integrations, Terraform, API, logz.io, OpenSearch Dashboards, GitHub]
---

:::note
[Project's GitHub repo](https://github.com/logzio/logzio_terraform_provider/)
:::

The Terraform Logz.io provider offers a great way to build integrations using Logz.io APIs.

Terraform is an infrastructure orchestrator written in Hashicorp Language (HCL). It is a popular Infrastructure-as-Code (IaC) tool that does away with manual configuration processes. You can take advantage of the Terraform Logz.io provider to really streamline the process of integrating observability into your dev workflows.

This guide assumes working knowledge of HashiCorp Terraform. If you're new to Terraform, we've got a great [introduction](https://logz.io/blog/terraform-vs-ansible-vs-puppet/) if you're in for one. We also recommend the official [Terraform guides and tutorials](https://www.terraform.io/guides/index.html).

For additional examples, other than those provided here, see our [GitHub project](https://github.com/logzio/logzio_terraform_provider/tree/master/examples).

### Capabilities

You can use the Terraform Logz.io Provider to manage users and log accounts in Logz.io, create and update log-based alerts and notification channels, and more.

The following Logz.io API endpoints are supported by this provider:

* [User management](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/user)
* [Notification channels](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_notification_policy)
* [Sub accounts](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/subaccount)
* [Logs-based alerts v2](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/alert_v2)
* [Log shipping tokens](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/log_shipping_token)
* [Drop filters](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/drop_filter)
* [Archive logs](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/archive_logs)
* [Restore logs](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/restore_logs)
* [Authentication groups](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/authentication_groups)
* [OpenSearch Dashboards objects](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/kibana_object)
* [S3 Fetcher](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/s3_fetcher)
* [Grafana Dashboards](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_dashoboard)
* [Grafana folders](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_folder)
* [Grafana Alert Rules](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_alert_rule)
* [Grafana Contact Point](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_contact_point)
* [Grafana Notification Policy](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/grafana_notification_policy)
* [Metrics Accounts](https://github.com/logzio/terraform-provider-logzio/tree/master/examples/metrics_account)

## Working with Terraform

**Before you begin, you'll need**:

* [Terraform CLI](https://learn.hashicorp.com/tutorials/terraform/install-cli)
* [Logz.io API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api)

### 1. Get the Terraform Logz.io Provider

To install this provider, copy and paste this code into your Terraform configuration:

```hcl
terraform {
  required_providers {
    logzio = {
      source = "logzio/logzio"
    }
  }
}
```

This will install the latest Logz.io provider.
If you wish to use a specific version of the provider, add under `source` the field `version` and specify your preferred version.


### 2. Configuring the provider

The provider accepts the following arguments:

* **api_token** - (Required) The API token is used for authentication. [Learn more about the API token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/).

* **region** - (Defaults to null) The 2-letter region code identifies where your Logz.io account is hosted.
Defaults to null for accounts hosted in the US East - Northern Virginia region. [Learn more about account regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/)


<h4 id="#example1">Example - Pass variables</h4>

You can pass the variables in a bash command for the arguments:

```bash
provider "logzio" {
  api_token = var.api_token
  region= var.your_api_region
}
```


<h4 id="#example3">Example - Create a new alert and a new Slack notification endpoint</h4>


Here's a great example demonstrating how easy it is to get up and running quickly with the Terraform Logz.io Provider.

This example adds a new Slack notification channel and creates a new alert in OpenSearch Dashboards that will send notifications to the newly-created Slack channel.

The alert in this example will trigger whenever Logz.io records 10 loglevel:ERROR messages in 10 minutes.

```
terraform {
  required_providers {
    logzio = {
      source = "logzio/logzio"
    }
  }
}

provider "logzio" {
  api_token = "8387abb8-4831-53af-91de-5cd3784d9774"
  region= "au"
}

resource "logzio_endpoint" "my_endpoint" {
  title = "my_endpoint"
  description = "my slack endpoint"
  endpoint_type = "slack"
  slack {
    url = "${var.slack_url}"
  }
}

resource "logzio_alert" "my_alert" {
  depends_on = [logzio_endpoint.my_endpoint]
  title = "my_other_title"
  query_string = "loglevel:ERROR"
  operation = "GREATER_THAN"
  notification_emails = []
  search_timeframe_minutes = 10
  value_aggregation_type = "NONE"
  alert_notification_endpoints = ["${logzio_endpoint.my_endpoint.id}"]
  suppress_notifications_minutes = 30
  severity_threshold_tiers {
      severity = "HIGH"
      threshold = 10
  }
}
```


<h4 id="#example3">Example - Create user</h4>

This example will create a user in your Logz.io account.

```
terraform {
  required_providers {
    logzio = {
      source = "logzio/logzio"
    }
  }
}

variable "api_token" {
  type = "string"
  description = "Your logzio API token"
}

variable "account_id" {
  description = "The account ID where the new user will be created"
}

provider "logzio" {
  api_token = var.api_token
  region = var.region
}

resource "logzio_user" "my_user" {
  username = "user_name@fun.io"
  fullname = "John Doe"
  roles = [ 2 ]
  account_id = var.account_id
}
```

Run the above plan using the following bash script:

```
export TF_LOG=DEBUG
terraform init
TF_VAR_api_token=${LOGZIO_API_TOKEN} TF_VAR_region=${LOGZIO_REGION} terraform plan -out terraform.plan
terraform apply terraform.plan
```

Before you run the script, update the arguments to match your details.

## Import sub-accounts as resources 

You can import multiple sub-accounts as follows:

```
terraform import logzio_subaccount.logzio_sa_<ACCOUNT-NAME> <ACCOUNT-ID>
```
