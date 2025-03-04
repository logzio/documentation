---
sidebar_position: 15
title: Consumption-Based Model
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more about Logz.io's consumption based model
keywords: [account, manage account, payments, consumption, admin controls, admin, access control]
---


Logz.io's consumption-based model allows you to tailor your budget to cover all your data monitoring needs, including logs, metrics, traces, and SIEM. This approach lets you view and analyze various data types within your account, with charges applied based on the volume of GB and Unique Metrics ingested.

This model allows you to configure quotas on your end, including the maximum amount of data you want ingested per data type. You pay for the data you ingest.

The cost per GB and Unique Metrics depends on your selected pricing plan. You can review the different offerings on [Logz.io’s Pricing page](https://logz.io).

<h2 id="usage">Usage and limits</h2>

Consumption-based accounts have usage limits that define how much data (GB/UTM) can be ingested per telemetry type (Logs, Metrics, Traces, or SIEM). Instead of reserving a fixed volume of data, your plan is based on a monthly or yearly budget - the total dollar ($) amount allocated for data ingestion.

There are two types of limits in your account:

* Soft Cap (Sub-Account Limit) – Each sub-account has an ingestion limit (GB/UTM) that can be adjusted by account admins in the [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page. If a sub-account reaches its soft cap, data ingestion will stop until the limit is increased.
* Hard Cap (Overall Telemetry Limit) – This is the maximum ingestion limit (GB/UTM) for a specific telemetry type across all sub-accounts. Once this limit is reached, ingestion for that telemetry type will be blocked.

To increase the overall account hard cap, contact the Logz.io [Support team](mailto:help@logz.io).

Account admins can track both budget and ingestion in [Plan and Usage > Usage and Info](https://app.logz.io/#/dashboard/settings/plan-and-billing/usage). The dashboard provides an overview of budget consumption ($ spent), data ingestion (GB/UTM used), and any overages beyond plan limits. Usage data updates once a day.

On-Demand charges apply only when the entire budget has been used.

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

`$0.10 + $0.82 + ($0.03 * 23) = $1.61`

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
