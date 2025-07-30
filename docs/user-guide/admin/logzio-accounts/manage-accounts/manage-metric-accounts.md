---
sidebar_position: 2
title: Manage Metric accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your metric accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, metrics, metric]
---

Logz.io Metrics provides powerful tools to monitor your data with precision, helping you debug, troubleshoot, and resolve issues faster.

If you're an admin of your Logz.io main account, you can manage your Metrics setup from the Manage Accounts page under **Settings > Manage Accounts**, then navigate to the Metrics tab.

## Manage your account

Your Metrics usage is calculated based on the number of Unique Time Series (UTSs), which represent the distinct metric streams collected using PromQL. These include counters, gauges, histograms, and summaries.

At the top of the page, you'll see a summary of your account, including:

* Allowed unique metrics – The maximum number of daily UTSs allocated to the account
* Sub accounts – The number of active and available sub accounts for this telemetry type
* Retention - The retention period indicating how long your metric data is stored

![Metrics account overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-account-main-apr8.png)

Below that, you’ll find a detailed table listing all related accounts for this telemetry type. Each row includes:

* Account name – Name of the account. Special characters such as `<`, `>`, `:`, `\"`, `/`, `\\`, `|`, `?`, `*` are not supported.
* Account ID – A unique identifier for the account
* Plan - The daily UTS allocation for the account
* Token – The token used to ship metrics data to this account

## Create an account

You can add up to 5 metric accounts by default. If you need the ability to add more accounts, contact your account manager or reach out to [Logz.io Sales team](mailto:sales@logz.io).

To create a new account, click **Create new account**, then enter the account name, the number of allocated UTSs, and select which accounts should have read access to this account's data.

Click **Create** to complete the setup. The new account will appear in the table with its associated details.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-new-account.png" alt="create-metric-account" width="700"/>


## Edit accounts

To make changes to an account, click the **⋮** icon next to it and select **Edit**. You can update the account name, adjust its UTS allocation, and modify which accounts can access its data.

Click **Save changes** to apply the updates.

## Delete an account 

To delete an account, click the **⋮** icon and select **Remove account**.

Deleting an account will return its UTS allocation to the main account. All data associated with the deleted account will be permanently removed.

This action cannot be undone.

## Configure your account limits

You can adjust your account’s daily volume and data retention period to fit your current monitoring needs.

To make changes, go to the [Plan and usage](https://app.logz.io/#/dashboard/settings/plan-and-billing/plan) page, select the telemetry type you want to update, and click **Update plan**.

To edit your metrics account, select Infrastructure Monitoring. From there, you can modify the Time series (TS) and billing cycle (monthly or yearly). When you're ready, click **Proceed to checkout** to apply the changes.