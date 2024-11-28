---
sidebar_position: 2
title: Warm Tier
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Everything you need to know about Logz.io's Warm Tier solution
keywords: [manage, log redaction, admin controls, account administration, access control, warm, warm tier, warm logs, archive]
---

Warm tier is a storage option designed for data that is not frequently accessed but still needs to be readily available for analysis and troubleshooting. It provides a practical solution for mid-term storage ensuring you can retrieve historical data when required.

:::info note
Warm tier configuration can be set up by contacting the [Sales team](mailto:sales@logz.io).
:::

## Setting Up the Warm Tier

Once Warm Tier has been enabled on your Logz.io account, you can assign it to one or more of your sub-accounts. To do so, navigate to [Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts), select the sub account you want to configure, choose the desired Warm Tier retention period, and click **Apply** to save your changes.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/data-tiers/warm-tier-activate-nov28.png" alt="warm-tier-button" width="700"/>


## Accessing Warm Tier Data

After activation, all users can access Warm Tier data through [Explore](https://app.logz.io/#/dashboard/explore).

Open the time picker, where indicators show the availability of Warm or Hot data. Hover over specific dates to view a tooltip specifying the type of data available.

When selecting a date with Warm Data, a notification will inform you that retrieval may take several minutes. To proceed, manually apply the query by clicking **Apply Query** in the top-right corner. This step ensures intentional data retrieval, as Warm Data may take longer to load and incur additional costs.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/data-tiers/warm-data-date-picker-nov.png" alt="warm-data-tooltip" width="500"/>

While waiting for results, you can navigate away from Explore. You’ll receive an in-app notification once the data is ready.
