---
sidebar_position: 2
---


# Configure Optimizers


To create a new optimizer, start in OpenSearch Dashboards so you can test the query you want to use.

Before creating an optimizer, you'll need a timeless account to send the data to. If you need help setting up a timeless account, see [Manage timeless accounts](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts).

After you've created your account, navigate back to **OpenSearch Dashboards** > **Create an optimizer**, where you can configure the optimizer settings.

:::note
Once a log is pulled to your Logz.io account, it takes up to **2 hours** until it appears in your timeless account.
:::


If you want help updating an existing optimizer, you can [skip the first part of this page](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts).

### Create an optimizer:

#### Set your query in OpenSearch Dashboards

In OpenSearch Dashboards, type a query in the query bar
and press **Enter**.


![OSD query bar](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/query-to-optimizer.png)

Review the results in the histogram and the document table,
and make sure your query returned the expected results.

Click **Create Optimizer** (above the query bar) to open the **Create an optimizer** page.


### Configure an optimizer:

![Configure an Optimizer](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/create-optimizer_aug2021.png)



#### Name the optimizer

Type a **Name** and a detailed **Description**.

#### _(Optional)_ Edit the optimizer's search settings

If you need to, change your optimizer **Query** and the **Accounts** that the query searches.


:::caution
If you use an invalid query, the optimizer will automatically be disabled.

Run your query in OpenSearch Dashboards so you can be sure you're getting the expected results. 
The filter tags that are displayed in the Optimizer **Query** section indicate which filters you used for the query in **Discover**. 
To update the filters, you'll need to add them to your search in **Discover**.
:::


#### _(Optional)_ Edit the optimizer's group-by settings

To store aggregate results, group your search fields.

![Group optimizer fields](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/optimizer-groupby_aug2021.png)

Click **Group by** to add up to 3 groups.

In the **Choose fields** list,
choose a field to group by.

To limit the available fields,
choose a log type from the **Filter by type** list.
To show fields for all log types,
choose **Clear filter**.

#### Set optimizers' trigger

In the **Trigger** section, choose how often this optimizer should run.

#### Choose the relevant timeless account

In the **Action** section, choose a timeless account to send to.

#### Choose the optimizer's output format

Choose an **Output**.


To send the raw JSON documents to your timeless account, choose **Full log**.


To send a summary table, choose **Aggregations**.

:::note
If you added any groups (in step 3), the aggregations table will show the aggregated fields that you used. To change these fields, you'll need to change your Group by selection.
:::


If you choose **Aggregations**, click +<i class="li li-plus"></i> to add a column to the table, and then choose a field to show in the new column.

![Optimizer aggregation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/optimizr-aggreg2_aug2021.png)

Click **Save** to save your optimizer. Logz.io will start sending your logs to the configured timeless account.
