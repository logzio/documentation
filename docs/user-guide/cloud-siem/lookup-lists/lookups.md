---
sidebar_position: 1
title: Lookup Lists
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn about Logz.io's lookup lists
keywords: [SIEM, rules, correlated rules, managing threats, Security information]
---



Lookup lists are custom lists that you can use for simpler, easier query filtering in OpenSearch Dashboards. 
Instead of adding a long list of elements to your query, you can create lookup lists and use them to filter results by adding the operator `in lookups` or `not in lookups`. For example, you can create lookup lists of allowlisted or blocklisted usernames, IP addresses, regions, or domains. 

:::note
Lookup list values are only string-based and do not support ranges. OpenSearch Dashboards, however, supports range-based searches, such as IP: [127.0.0.0 TO 127.*].
:::

Each list you create is added to the main Lookup lists library: Because the lookup lists are centrally managed, any list can be easily updated and changed without requiring manually updating multiple dashboards, saved searches, security rules, and so on.

To view and create lookup lists, from the **Cloud SIEM** menu, go to [**Lookups**](https://app.logz.io/#/dashboard/security/lookups).

<!--![Open Lookup lists](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/lookuplist-nav.gif) -->

![Lookup list](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/siem-lookups-jan.png)

## Static and Dynamic lookups

Logz.io offers two main lookup lists, Static and Dynamic. 

A **Static lookup list** is created by adding individual values or uploading a CSV file with the different fields and values you want to track. While you can update the list, it has to be done manually and maintained by you.

A **Dynamic lookup list** uses a query as its source of data. The query's results fill the list with the different fields and values, updating and maintaining it independently.

* **[Create a Static lookup](/docs/user-guide/cloud-siem/lookup-lists/static-lookup/)**
* **[Create a Dynamic lookup](/docs/user-guide/cloud-siem/lookup-lists/dynamic-lookup)**

## Filter by lookup lists in OpenSearch Dashboards

You can filter by lookup lists in OpenSearch Dashboards, security rules, and searches.

For example, go to the SIEM [OpenSearch Dashboards](https://app.logz.io/#/dashboard/security/research) page or open a Dashboard. Click **Add a filter** to show the filter dialog box.

![Filter by lookup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/siem-osd-filter.png)

* **Field** - Select a field to filter by.
* **Operator** - Select the operator **in lookups** or **not in lookups**.
* **Value** - Select the lookup you want to filter by.

## Add a lookup list filter to a security rule

If you want to use your lookup lists as a reference when creating security rules, navigate to the [Create a rule](https://app.logz.io/#/dashboard/security/rules/v2019/new) page, and select **Add a filter**.

Select the field you want to filter by, and select whether it's included or excluded from a lookup.

Next, select the lookup list you'd like to refer to from the dropdown menu.

![Select a filter](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/filter-in-lookup.png)

**Save** your filter, and continue editing the rule.

[Learn more about managing security rules](/docs/user-guide/cloud-siem/security-rules/manage-security-rules/)

## Delete a lookup list

To delete a lookup, hover over the item and click **delete**. You'll be asked to confirm the deletion.

