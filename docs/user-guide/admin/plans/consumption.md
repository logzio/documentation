---
sidebar_position: 1
title: Consumption-Based Model
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more about Logz.io's consumption based model
keywords: [account, manage account, payments, consumption, admin controls, admin, access control]
---

Logz.io offers a consumption-based pricing plan that lets you to set a budget to cover all of your data monitoring needs, including logs, metrics, traces, and SIEM. 

Logz.io consumption plans allow you to control your spending based on actual usage rather than a fixed data allocation. You set your budget in advance, and charges apply based on your data volume (GB) and Unique Metrics (UTM) consumed. You can set ingestion caps to control how much data is ingested per telemetry type (logs, metrics, traces, and SIEM).

The cost per GB and UTM depends on your selected pricing plan. You can review the different offerings on [Logz.io’s Pricing page](https://logz.io).

<h2 id="start">Getting started with a consumption-based plan</h2>

To activate a consumption plan, you can either:

* Contact your account manager
* [Purchase an account via AWS](/docs/admin/plans/aws-consumption/)

<h2 id="limit">Managing consumption limits</h2>

Consumption-based plans use budgets instead of reserved volumes. Your account includes a monthly or yearly budget and associated ingestion limits (GB/UTM). Limits help prevent unexpected overages.

Your account has two types of ingestion limits:

* **Soft Cap** (Sub-Account Limit) - Each sub-account has a daily ingestion limit (GB/UTM) that can be adjusted by account admins on the [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page. If a sub-account reaches this soft cap, data ingestion pauses for that sub-account until the limit is increased.

* **Hard Cap** (Overall Product Limit) - The hard cap is the total daily ingestion limit (GB/UTM) for each telemetry type across all sub-accounts combined. The sum of all sub-account soft caps cannot exceed this hard cap. Once the hard cap is reached, further ingestion for that telemetry type stops until the limit is adjusted.

_For example, if your Logs Hard Cap is set to 100 GB and you have three sub-accounts sending log data, the combined ingestion from these sub-accounts cannot exceed 100 GB._

The default hard cap is 300 GB for logs, 300,000 UTMs for metrics, and 150GB for tracing data. To request an increase, contact [Logz.io Support](mailto:help@logz.io).



Administrators can track the budget and ingestion usage from the [Plan and Usage > Usage and Info](https://app.logz.io/#/dashboard/settings/plan-and-billing/usage) page. This dashboard provides:

* Current budget consumption (dollars spent)
* Data ingestion amounts (GB/UTM used)
* Information about overages beyond your defined plan limits

Usage data is updated daily.

:::tip note
On-demand charges apply only after your entire allocated budget has been consumed. They are not relevant for Pay As You Go plans. 
:::


<h2 id="usage">Manage accounts overview</h2>

Account admins can monitor and configure account-specific settings via the [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page.

![manage consumption account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/consumption/consumption-manage-accounts.png)

At the top of the page, you'll find a graph displaying your current usage alongside key details:

* Total budget consumption breakdown
* Estimated daily maximum cost if usage reaches the limit (Soft Cap)
* Contract start and end dates

The second half of the page includes a table that provides an overview of all accounts, including:

* Account name
* Account ID
* Telemetry data type
* Usage limit – The maximum amount of telemetry data you can ingest per account
* Unit price (per GB/UTM)
* Daily max price – The highest possible charge if usage reaches the limit (Soft Cap)
* Retention period per account
* Advanced settings – Indicates whether the account can access shared assets, have account utilization metrics, present log size, and more

To create a new account, click **Create New Account**, then select the telemetry type, name, usage limit, retention, and any other required settings.

To edit an account, click the **⋮** menu next to it. You can modify all settings except the telemetry type.

<h2 id="example"> Consumption-Based Model - Example </h2>

In this example, the **budget is $1,000**, and the individual unit prices are:


|Data type                                      | Description       | Price |
|-----------------------------------------------|-------------------|-------|
| Open 360 logging ingestion                    | Per 1GB per day   | $0.10 |
| Open 360 logging index + 7 days hot retention | Per 1GB per day   | $0.82 |
| Open 360 logging hot retention extension      | Per 1GB per day   | $0.03 |
| Open 360 logging cold tier retention          | Per 1GB per day   | $0.001 |
| Open 360 metrics + 18 months retention        | 1,000 UTM per day | $0.40 |
| Open 360 traces                               | Per 1GB per day   | $0.92 |
| Open 360 security addon                       | Per 1GB per day   | $0.35 |

Based on these prices, the cost is $0.92 per 1GB per day for Open 360 logging index + 7 days hot retention period.

For Open 360 logging index + 30 days hot retention, the cost will be $1.61 per 1GB per day:

`$0.10 + $0.82 + ($0.03 x 23) = $1.61`

$0.10 for log ingestion, $0.82 for 7 days retention, and $0.69 for the additional 23 days retention.

After one day of use, the budget will be updated accordingly:

Budget used per 1 day:

|Data type                                        | Data sent      | Price per unit | Budget used per day |
|-------------------------------------------------|----------------|----------------|---------------------|
| Open 360 logging index + 7 days hot retention   | 2GB            | $0.92          | $1.84               |
| Open 360 logging index + 30 days hot retention  | 3GB            | $1.61          | $4.83               |
| Open 360 metrics                                | 7,000 UTM      | $0.40          | $2.8                |
| Open 360 tracing                                | 4GB            | $0.92          | $3.68               |
| Open 360 security addon                         | 5GB            | $0.35          | $1.75               | 

At the end of the day, $14.9 was spent, leaving a remaining budget of $985.1.


<h2 id="table">Which plan is right for you?</h2>

Logz.io offers two types of consumption plans:

- **Pay as You Go** - You’re billed based on your actual usage (GB or UTM), without upfront commitment.
- **Budget + On-demand** - You set a prepaid budget for GB or UTM usage. Once your daily limit is reached, additional usage is billed on-demand.

Availability by payment method:

|                       | AWS (Marketplace) | Credit Card | Wire Transfer |
|-----------------------|-------------------|-------------|---------------|
| **Pay as You Go**     | ✔️                 | ✖️           | ✖️             |
| **Budget + On-Demand**| ✔️                 | ✖️           | ✔️             |






