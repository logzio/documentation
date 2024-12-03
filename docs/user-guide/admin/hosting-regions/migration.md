---
sidebar_position: 2
title: Migrating Accounts Between Hosting Regions
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: How to migrate your Logz.io account between different hosting regions
keywords: [hosting regions, regions, region, migrate, switch region]
---

You can migrate your Logz.io Log Management accounts between hosting regions. We'll be frank - it can take a bit of effort, but with the right scripting and API implementation, can be done fairly quickly.

:::note
Azure Hosting is now deprecated; however, Azure Shipping and Azure Marketplace remain active and will continue to be supported.
:::

## Implications

Before you set out to migrate your account, you will want to take the following implications into consideration:

* Pre-migration data can’t be transferred
* Pre-migration data can't be restored from the archive
* The migration will reset your account's data shipping tokens. Consequently, you will need to update your data shipping configurations with the new token and listener host/region details.
* Logz.io Metrics and Distributed Tracing are subject to availability. If applicable, reach out to your Logz.io Customer Success Manager to verify that they are available on your target region.




## Migration checklist

The following is a comprehensive step-by-step guide for migrating an existing Logz.io Log Management account to a different hosting region.

The guide assumes a robust implementation that makes use of most of Logz.io's offerings. Perform the steps that are relevant **to you**. For example, the sub accounts step is optional, but probably relevant if your pre-migration account has sub-accounts and you want to recreate them in your new, post-migration account.

:::note
The process can be performed by API or manually, as you prefer. You may also consider writing scripts to expedite the process.
:::




### Create a new account in the target region

Open a new Logz.io trial account in your region of choice. Contact your Logz.io Customer Success Manager or Account Manager to request a complimentary upgrade to match your existing account while you are in transition.

:::note
If you have custom parsing, ask your Logz.io Customer Success Manager or Account Manager for assistance migrating your parsing pipelines.
:::


### (Re-)Create your sub-accounts

Retrieve all sub-accounts and re-create them in your new account. You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve the settings for all of your Log Management accounts](https://api-docs.logz.io/docs/logz/get-all-detailed-time-based-account/).
2. In your post-migration account:
    1. [Create a new sub-account](https://api-docs.logz.io/docs/logz/create-time-based-account/) with the matching settings. Repeat for each sub account.
    2. [Update your main account](https://api-docs.logz.io/docs/logz/update-time-based-account/) with the appropriate settings and daily capacity.



### Export & Import your OpenSearch Dashboards objects

Export any and all OpenSearch Dashboards objects you want to keep and import them into your new account. These include saved searches, visualizations, and dashboards.

The process can be performed by API or manually. Export & import guides:

* [Export & import guide](https://docs.logz.io/docs/user-guide/log-management/collaboration/share-import-export/)
* [API guide](https://api-docs.logz.io/docs/logz/import-or-export-kibana-objects/)


### (Re-)Create your archive settings

Retrieve your archive settings and re-create them in your new account. You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve the archive settings](https://api-docs.logz.io/docs/logz/get-settings-for-account/). Repeat for each sub account.
2. In your post-migration account, [set up log archiving](https://api-docs.logz.io/docs/logz/create-settings/). Repeat for each sub account, as necessary.

If you prefer to perform the process manually, see the [archiving guide](https://docs.logz.io/docs/user-guide/data-hub/archive-restore/configure-archiving/).

:::note
Note that only one archive can be active per account.
:::


### (Re-)Create your drop filters

Retrieve all drop filters and re-create them in your new account. You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve the drop filters for all of your Log Management accounts](https://api-docs.logz.io/docs/logz/get-all-for-account/). Repeat for each sub account.
2. In your post-migration account, [create a new drop filter](https://api-docs.logz.io/docs/logz/create/). Repeat for each filter and sub account, as necessary.


If you prefer to perform the process manually, see the [drop filters guide](https://docs.logz.io/docs/user-guide/data-hub/drop-fiters/).

:::caution Important
If the filters were created from the backend, contact your Customer Success Manager for help migrating your drop filters.
:::



### (Re-)Create your Optimizers

In your post-migration account, open your [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts/) page, and create your Timeless account/s. [Learn more](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#timeless)

Re-create your Optimizers manually in your Logz.io account. [Learn more](https://docs.logz.io/docs/user-guide/log-management/long-term-storage/configure-optimizers/).

:::note
Optimizers are currently not supported by the Logz.io API.
:::

### (Re-)Create your endpoints

Retrieve all notification endpoints and re-create them in your new account. You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve all notification endpoints for your main Log Management account](https://api-docs.logz.io/docs/logz/get-all-endpoints/). Repeat for each sub account.
2. In your post-migration account, [create a new endpoint](https://api-docs.logz.io/docs/logz/manage-notification-endpoints/). Repeat for each endpoint and account, as necessary.


If you prefer to perform the process manually, see the [notification endpoints guide](https://docs.logz.io/docs/user-guide/integrations/notification-endpoints/endpoints/).


### Export & import logging alerts

Retrieve all logging alerts you want to keep and re-create them in your new account.
You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve all log alerts](https://api-docs.logz.io/docs/logz/get-all-alerts/). Repeat for each sub account.
2. Update and prepare the alerts with your new, post-migration account information:
    1. Update the account IDs, under the parameter `accountIdsToQueryOn`. If your alerts are set to run on all accounts, this will not be necessary. (That is, if the parameter `QueryOnAllAccounts` is set to true.)
    2. Update the notification endpoints, if relevant, under the parameter `notificationEndpointIds`.
3. In your post-migration account, [create a new alert](https://api-docs.logz.io/docs/logz/create-alert/) with the matching settings. Repeat for each alert and account.

If you prefer to perform the process manually, see the [alert guide](https://docs.logz.io/docs/user-guide/log-management/log-alerts/configure-alert/).


### (Re-)Create your scheduled reports

Re-create your reports manually in your Logz.io account. [Learn more](https://docs.logz.io/docs/user-guide/log-management/reports/).

:::note
Scheduled reports are currently not supported by the Logz.io API.
:::

### (Re-)Create your users

Retrieve all existing users and re-create them in your new account.
You can do so using the Logz.io API endpoints as follows:

1. In your pre-migration account, [retrieve users for all associated accounts](https://api-docs.logz.io/docs/logz/list-all-account-users/).
    * This endpoint returns a list of users in the main account and all associated sub accounts as an array of JSON objects per account.
    * If a user appears in multiple accounts, it will be listed separately under each account.
2. In your post-migration account, [create a new user/admin user](https://api-docs.logz.io/docs/logz/create-user/). Repeat for each user and account.

If you prefer to perform the process manually, see the [user management guide](https://docs.logz.io/docs/user-guide/admin/users/).


### Email Support to enable SSO

If you would like to enable your Single-Sign On (SSO) on the new account, [Email Support](mailto:help@logz.io?subject=Requesting%20help%20enabling%20SSO%20following%20an%20account%20migration) for assistance. [Learn more](https://docs.logz.io/docs/user-guide/admin/sso/single-sign-on/)

