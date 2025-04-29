---
sidebar_position: 1
title: Manage Log accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your log accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, log, logs]
---

Logz.io Log Management gives you the tools to search and query your logs with speed and precision, making it easier to debug, troubleshoot, and quickly get to the root of issues.

If you're an admin of your Logz.io main account, you can manage both the main account and any connected sub accounts from the Manage Accounts page, found under **Settings > Manage Accounts** in the navigation menu.

## Manage your account

Your log account usage is based on the volume of data you ingest. At the top of the page, you'll see an overview of your account, including:

* Daily volume – The maximum daily indexing capacity (in GB) allocated to the account
* Hot Retention – How long logs remain immediately searchable
* Warm Tier (if enabled) – How many days logs are accessible after leaving the Hot Tier
* Cold Tier (if enabled) – How much archived log data is stored each month for long-term retention and compliance
* Sub accounts – The number of active and available sub accounts for this telemetry type

![manage accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/manage-accounts-main-apr7.png)

If flexible volume is enabled, you can share indexing capacity between accounts. This gives you more control over resource allocation, allowing data to be used dynamically instead of reserving volume in advance.

At the bottom of the page, you’ll find a breakdown of all related accounts for this telemetry type. Each row includes:

* Account name – The name of the main or sub-account
* Account ID – The unique identifier for the account
* Vol (GB) – Daily indexing volume allocated to the account
* Retention (days) – How long logs are stored in the hot tier
* Token – The log shipping token used to send data to this account

### Main vs. sub account

If you're on a Pro or Enterprise plan, you can create sub accounts to better manage data usage and control user access to your logs.

Sub accounts allow you to isolate log data by environment (e.g., production, staging, dev), assign separate data volumes and retention periods, and restrict access to sensitive information. You can route specific logs to specific sub accounts to ensure data is only visible to the right teams.

By default, all users in your main account have access to data in all associated logging sub accounts and Timeless accounts. To limit visibility, you can segment data by sub account and manage access through account-level permissions.

## Create an account

Each telemetry type has a predefined limit on how many sub accounts you can create. This limit is visible at the top panel of the Manage Account page. 

To create a new account, click **Create new account**, then enter a name, daily volume (GB), and retention period (in days).

Click **Advanced** to adjust additional settings such as shared asset access, whether to track account utilization, and whether to save log size.

Click **Create** to complete setup and add the account. The account will be visible in the table with all of the relevant data. 

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/create-new-account-apr14.png" alt="create-log-account" width="700"/>

## Edit accounts

To edit an account, click the **⋮** icon next to the account and select **Edit**.

You can update the account name and click **Advanced** to configure additional settings, including which accounts/sub accounts have visibility to the data in this account, log size collection, and [account utilization metrics](https://docs.logz.io/docs/user-guide/admin/account-volume-optimization/manage-account-usage/#what-are-account-utilization-metrics).

Click **Save changes** to apply your updates.

## Manage access to log data across accounts

In Logz.io, each log account can serve as a data source for other accounts—allowing you to centralize data access and reduce duplication. You can control this by configuring which main and sub accounts have access to the data through an access list.

### Grant access to a logs data source

To allow other accounts to view and use shared data—such as dashboards, visualizations, and queries—follow these steps:

1. Open the log account you want to share data from.

2. Click **Advanced**.

3. In the Shared access section, select the accounts you want to grant access to from the dropdown list.

These selected accounts will now be able to use the original log account as a data source, giving them visibility into its logs and shared assets.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add-accounts-log-apr14.png" alt="manage-log-account" width="700"/>


## Delete a sub account 

To delete a sub account, click the **⋮** icon next to the account name and select Remove account.

When deleted, the sub account’s allocated volume (GB) will be returned to the main account, and all data associated with the sub account will be permanently deleted.

This action cannot be undone.


## Troubleshooting 

### Logs and usage quota don’t match

If you notice a small number of logs ingested but a high usage quota, it may be due to logs being sent with a timestamp that doesn’t match the current day—known as backdated or future-dated logs.

This is often seen when viewing logs with the Today time range, while the logs were shipped with a different date.

To resolve this, try adjusting the time range settings. If the issue persists, contact the **[Logz.io's Support team](mailto:help@logz.io)** for help.