---
sidebar_position: 2
title: Warm Tier
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Everything you need to know about Logz.io's Warm Tier solution
keywords: [manage, log redaction, admin controls, account administration, access control, warm, warm tier, warm logs, archive]
---

Warm tier is a storage option designed for data that is not frequently accessed but still needs to be readily available for analysis and troubleshooting. It provides a practical solution for mid-term storage ensuring you can retrieve historical data when required.

:::info note
Warm tier configuration can be set up by contacting the [Sales team](https://logz.io/contact-us/).
:::

Prerequisites

Data gets to warm only after it's been to hot. All hot data goes to warm data according to the retention period configured by you. When you enable Warm Tier, the retention minimum for Hot tier is 4 days.

## Setting Up the Warm Tier

Once Warm Tier has been enabled on your Logz.io account, you can assign it to one or more of your sub-accounts. To do so, navigate to [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts), select the sub account you want to configure, choose the desired Warm Tier retention period, and click **Apply** to save your changes.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/data-tiers/warm-tier-configuration-nov29.png" alt="warm-tier-button" width="700"/>

Data transitions to the Warm Tier **only after** stored in the Hot Tier. All Hot Tier data moves to the Warm Tier based on the retention period you configure. When enabling the Warm Tier, the minimum retention period for the Hot Tier is set to 4 days.


## Accessing Warm Tier Data

After activation, all sub account users can access Warm Tier data through [Explore](https://app.logz.io/#/dashboard/explore).

:::tip
When querying Warm Tier data, limit the time range, use filters, and focus on key information to improve speed. Warm Tier data has a 5-minute timeout; you'll be notified if retrieval fails.
:::

Open the time picker, where indicators show the availability of Warm or Hot data. 

When selecting a date containing Warm Tier data, a notification will inform you that retrieval may take several minutes. To proceed, confirm your date selection by clicking **Apply** in the time picker, then click **Run Query** in the main Explore query bar. This manual step ensures intentional data retrieval, as Warm Tier data may take longer to load and incur additional costs.


![warm data activate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/data-tiers/both-times-warm-data.png)

While waiting for results, you can navigate away from Explore. You’ll receive an in-app notification once the data is ready.
