---
sidebar_position: 15
title: Consumption-Based Model
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more about Logz.io's consumption based model
keywords: [account, manage account, payments, consumption, admin controls, admin, access control]
---


Logz.io's consumption-based model allows you to tailor your budget to cover all your data monitoring needs, including logs, metrics, traces, and SIEM. This approach lets you view and analyze various data types within your account, with charges applied based on the volume of GB and Unique Metrics ingested.

Prices per GB and Unique Metrics vary according to your overall budget. You can review the different offerings on [Logz.io’s Pricing page](https://logz.io).

As part of the new model, you can configure the maximum amount of data you want ingested per data type. This can help prevent unexpected data spikes and enable you to prioritize the most relevant data.

If you reach your preconfigured ingestion cap, the system will halt further data intake. However, account admins can modify these limits as needed through the Manage Accounts page.

Once you reach your allocated budget, data ingestion will continue, and additional charges will be calculated using On-Demand rates. 

You can contact your Logz.io account manager or [Logz.io's support team](mailto:help@logz.io) to adjust your budget accordingly.

<h2 id="example"> Consumption-Based Model - Example </h2>

In this example, the user's **budget is $1,000**, and the individual unit prices are:


|Data type                             | Description       | Price |
|--------------------------------------|-------------------|-------|
| Logs                                | Per 1GB per day   | $0.10 |
| Log index + 7 days retention         | Per 1GB per day   | $0.82 |
| Log index retention extension per day| Per 1GB per day   | $0.03 |
| Log cold retention                   | Per 1GB per day   | $0.001 |
| Metrics                              | 1,000 UTM per day | $0.40 |
| Traces                               | Per 1GB per day   | $0.92 |
| Security Monitoring                  | Per 1GB per day   | $0.35 |

Based on these prices, the user will pay $0.92 per 1GB per day for Logs with a 7-day retention period.

For logs with 30 days retention, the user will pay $1.61 per 1GB per day:

`$0.10 + $0.82 + ($0.03 * 23) = $1.61`

$0.10 for Logs, $0.82 for 7 days retention, and $0.69 for the additional 23 days retention.

After one day of use, the user's budget will be updated accordingly:

Budget used per 1 day:

|Data type                             | Data sent      | Price per unit | Budget used per day |
|--------------------------------------|----------------|----------------|---------------------|
| Logs - 7 days retention              | 2GB            | $0.92          | $1.84               |
| Logs - 30 days retention             | 3GB            | $1.61          | $4.83               |
| Metrics                              | 7,000 UTM      | $0.40          | $2.8                |
| Tracing                              | 4GB            | $0.92          | $3.68               |
| Security Monitoring                  | 5GB            | $0.35          | $1.75               | 

At the end of the day, the user spent $14.9, and has the remaining budget of $985.1.