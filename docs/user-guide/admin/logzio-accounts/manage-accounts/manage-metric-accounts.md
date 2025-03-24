---
sidebar_position: 5
title: Manage Metric accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your metric accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, metrics, metric]
---

## Manage your Infrastructure Monitoring account

### View plan summary

Your Metrics account is calculated according to the unique metrics (UMs) you're using. These metrics are a combination of the metric type queries by PromQL, including counters, gauges, histograms, and summaries.

You can view your daily and monthly available UMs, and a breakdown of each account’s current month’s allocations and usage percentages.

![Metrics plan overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-plan-overview.png)

### View details and abilities for a specific account

To see the detailed information and the configurable options for each account, click the account name in the table or pie chart.

![Metrics accounts overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/view-metrics-accounts.png)

Inside each account you can view the following details:

* Account name (which you can change by editing it and clicking the **Apply** button)
* Account creation date
* Account token
* Summary and breakdown of the unique metrics sent to the account over the last 7 days

You can edit the following elements:

* Which accounts/sub accounts have visibility to the data in this account
* Total unique metrics allocated to this specific data source, which defines how many daily unique metrics can be ingested into this data source

![Metrics accounts details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-account-details.png)

### Configure which accounts can access a Metrics data source

Each Metrics account can become a data source for other Logz.io Metrics accounts. To manage access to your metrics data, you create an access list of the Logz.io main account and sub accounts that can view the data for each Metrics account. In the account selector, you can see the list of all the sub accounts (and main account) in the top right of the application page.

#### To grant access to the data in a Metrics account

If users are logged in to the accounts you add here, they'll be able to read the metrics in this account.

1. Click the account name to open its account details.

2. To enable access to a Metrics data source for other accounts, click Add an account and select the relevant accounts in the field below the Metrics account name.

![Metrics add account visibility](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-visibility.gif)


### Add a Metrics account to your plan

You can add up to 5 Metrics accounts for your Infrastructure Monitoring plan. If you need the ability to add more accounts, reach out to your account manager or [Logz.io's Sales team](mailto:sales@logz.io).


**To create a new account**

1. Click **Add metrics account** in the upper left of the Infrastructure Monitoring account plan panel.
2. Name the new account.
3. Set which accounts can use it as a data source.
4. Configure the **total monthly UMs** you want to allocate to the new account. If you don’t have UMs available, you’ll be prompted to reduce the allocation of another account.
5. Click **Apply** to apply your changes.

### Delete a Metrics account from your plan

Choose the Metrics account you want to delete, and click the **Delete** icon located next to its name. 

Then, confirm (or Cancel) the action.

### Change how many UMs are allocated to each account within your plan

Set how many unique metrics (UMs) are allocated to each account from the overall Infrastructure Monitoring plan. 

Choose the relevant account you'd like to edit, increase or decrease the Unique metrics assigned to it, and click **Apply** to save your changes.

![Allocate metrics ums](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/allocate-metrics-data.gif)
