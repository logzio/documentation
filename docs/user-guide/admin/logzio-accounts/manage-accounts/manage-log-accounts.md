---
sidebar_position: 1
title: Manage Log accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your log accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, log, logs]
---

Logz.io **Log Management** is where you can search and query your logs. It is optimized for debugging and troubleshooting issues as quickly and effectively as possible.

If you're an admin for the main account, you can manage the main account and sub accounts from the [**Manage Accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) page (**<i class="li li-gear"></i> > Settings > Manage accounts** in the navigation menu).

The Log Management plan panel is located at the top of the **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** page.

## Manage Log Analytics

### View Log Management plan summary

Your Log account is calculated based on the data you ingest. You can choose to use a [flexible volume to get more control over how you allocate space and data between your accounts.

You can view the total number of daily GB available and the account's retention. This summary also includes a detailed list of the available accounts, their reserved daily GB, and whether these accounts are capped, searchable, and if they include shared objects.

![Log plan overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/log-management-overview.png)

### View and edit account details

To see the detailed information and the configurable options for each account, click the account name in the table or pie chart.

![Log accounts overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/log-management-choose-account.png)

Inside each account, you can view and edit the following details:

* Account name (which you can change by editing it and clicking the **Apply** button)
* Account token
* Account retention duration
* Reserved volume (and whether to cap this account's volume)

You can add the following elements:

* [Save account utilization metrics (and how often)](https://docs.logz.io/docs/user-guide/admin/account-volume-optimization/manage-account-usage/#what-are-account-utilization-metrics)
* Save the account's log size 
* Which accounts/sub accounts have visibility to the data in this account

![Logs accounts details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/log-management-account-inner.png)

### Configure which accounts can access a Logs data source

Each log account can become a data source for other Logz.io Log Management accounts. To manage access to your data, you create an access list of the Logz.io main account and sub accounts that can view the data. 

### To grant access to the data in a Logs account

Users that are logged in to the accounts you add here will be able to read the data in this account.

1. Click the account name to open its account details.

2. To enable access from other accounts, click Add an account and select the relevant accounts.

![Logs add account visibility](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/log-management-add-account.gif)


### Main vs. sub account

If you're on a Pro or Enterprise plan, you can create sub accounts to help manage user access to your data.

Sub accounts help you control data usage and manage user access to your logs.

You can define data volumes and retention periods for independent environments by shipping different logs to different sub accounts.

Sub accounts can also help you control access to sensitive data.

By default, all users of your main account have permission to view the data in other logging sub accounts and timeless accounts. You can route different logs to different sub accounts to limit access to data.

### Add and manage a Log Management sub account

Sub accounts share the same setting options as the main account (See the list above). In addition, sub accounts have settings used to control access to the data.

To add a sub account, navigate to the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page, and click the **Add sub account** button located in the upper left corner of the Log Management account plan panel.

![Add sub account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add-sub-account.png)

Choose the sub account name, retention, and volume options if relevant. On the right hand side, you'll have additional options for this sub account, including:


| Settings | Description |
|---|---|
| **Enable main account users to access this account** | If enabled, all main account users will automatically have user-role permissions to the sub account. This means they can view the log data in the sub account. If disabled, users will need to be explicitly added to the sub account to have access to it. |
| **Searchable from the main account** | If enabled, data stored in the sub account, can be searched directly from the main account in OpenSearch Dashboards. |
| **Save account utilization metrics** | Logs metrics on your account utilization, such as used and expected data volume at current indexing rate (GB). |
| **Save log size** | Adds the logSizeEnabled field to each log, stating the log's size. |
| **Use dashboards, visualizations, and saved searches from these accounts** | Choose the main account from which these elements will be visible on the sub account. Useful if you want to be able to access your main account's data from this sub account. |

Click **Apply** to create the sub account.

If you already have a sub account and you'd like to re-configure it, choose the relevant sub account from the list and click on **Advanced options** to access these settings.

![Manage existing sub accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/manage-sub-accounts.gif)


### No correlation between your logs and usage quota

You or your team see a small number of logs ingested with a high usage quota. 

This happens when you apply the **Today** time frame to view logs and is the result of shipping logs with a date different from today’s date (Also known as sending Back/Future logs).


If you encounter this issue, you can adjust the time frame settings or contact **[Logz.io's Support team](mailto:help@logz.io)** for additional info and assistance.

### Delete a sub account from your plan

Choose the Log Management sub account you want to delete, and click the **Delete** icon located next to its name. 

Then, confirm (or Cancel) the action.

### Change how many GB are reserved for each account within your plan

You can edit the amount of GB reserved for each of your Log Management accounts.

Choose the relevant account you'd like to edit, increase or decrease the reserved volume assigned to it, and click **Apply** to save your changes.
