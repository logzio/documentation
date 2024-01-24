---
sidebar_position: 2
title: Configure Optimizers
description: How to use and configure optimizers in Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, optimizers, log analysis, observability]
---

Configure optimizers to store logs and aggregations to a timeless account for extended retention, retaining critical data for long-term visibility.


:::info note
You need a timeless account to configure optimizers. [Learn more](https://docs.logz.io/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts) about timeless accounts. A log can take up to **2 hours** to appear in your timeless account.
:::

Open OpenSearch Dashboards and run your query of choice. 


Review the results in the histogram and the document table,
and make sure your query returns the expected results.


![OSD query bar](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/query-to-optimizer.png)

### Create an optimizer

Click **Create optimizer** (above the query bar) to open the **Create an optimizer** page.

![Configure an Optimizer](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/create-optimizer_aug2021.png)



### Name the optimizer

Type a **Name** and a detailed **Description**.

<h3 id="edit-search"> <i>(Optional)</i> Edit the optimizer's search settings</h3>

If you need to, change your optimizer **Query** and the **Accounts** that the query searches.


:::caution
If you use an invalid query, the optimizer will automatically be disabled.

Run your query in OpenSearch Dashboards to ensure you're getting the expected results. 
The filter tags displayed in the optimizer **Query** section indicate which filters you used for the query in **Discover**. 
To update the filters, you'll need to add them to your search in **Discover**.
:::


<h3 id="edit-search"> <i>(Optional)</i> Edit the optimizer's group-by settings</h3>

To store aggregate results, group your search fields.

![Group optimizer fields](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/optimizer-groupby_aug2021.png)

Click **Group by** to add up to 3 groups.

In the **Choose fields** list,
choose a field to group by.

To limit the available fields,
choose a log type from the **Filter by type** list.
To show fields for all log types,
choose **Clear filter**.

### Set optimizers' trigger

In the **Trigger** section, choose how often this optimizer should run.

### Choose the relevant timeless account

In the **Action** section, choose a timeless account to send to.

### Choose the optimizer's output format

Choose an **Output**.


To send the raw JSON documents to your timeless account, choose **Full log**.


To send a summary table, choose **Aggregations**.

:::note
If you added any groups, the aggregations table will show the aggregated fields you used. To change these fields, you'll need to change your Group by selection.
:::


If you choose **Aggregations**, click +<i class="li li-plus"></i> to add a column to the table, and then select a field to show in the new column.

![Optimizer aggregation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/optimizr-aggreg2_aug2021.png)

Click **Save** to save your optimizer. Logz.io will start sending your logs to the configured timeless account.
