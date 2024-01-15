---
sidebar_position: 2
title: Static Lookups
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn about Logz.io's Static lookups and how you can utilize them
keywords: [SIEM, rules, lookup list, lookups, Static lookups]
---



Static lookup lists include values you define and are used as a reference to search and match elements across your code. For example, you can create lookup lists of allowlisted or blocklisted usernames, IP addresses, regions, or domains.

:::note
Lookup list values are only string-based and do not support ranges. OpenSearch Dashboards, however, supports range-based searches, such as IP: [127.0.0.0 TO 127.*].
:::

You can reference lookup tables in a security filter. 

In **Static lookups**, you define fields and values that do not change during the task run.



:::tip
To create an extensive lookup list with up to 200 elements, we recommend using a CSV file to upload values. The [lookup lists API endpoints](https://api-docs.logz.io/docs/logz/update-lookup-list/) also let you independently manage lookup lists: To create a new list, you'd use the [Create lookup lists API](https://api-docs.logz.io/docs/logz/create-lookup-list), and add elements via CSV file or the [Add element to a lookup list API](https://api-docs.logz.io/docs/logz/create-lookup-list).
:::


## Configure TTL for new lookup lists

Time to live (TTL) is the number of days remaining until the lookup list is expired: A lookup list with a TTL of 1 day expires within 24 hours from the time it was created, and a list with a TTL of 2 days expires within 48 hours from the creation time.

By default, all new lookup lists are created without an expiration period. To set the Default **Time to live** (**TTL**) for new lookup lists, at the top of the Lookup lists page, click **Change**, select **No expiration** or a period between 1-364 days, and then **Save** your changes to apply them or **Cancel** the change.

![Add values to lookup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/edit-static-lookup-jan.png)

## Create a lookup list manually

Navigate to [Lookup lists](https://app.logz.io/#/dashboard/security/rules/lookup) and click on New lookup. Select the type of list you want to create, in this case, Static lookup.

To edit an existing list, hover over the relevant list in the table and click the pencil icon to **Edit** it.

In the **Edit a lookup** page, update the **Name** and optional **Description** for the list.

To add a new line to the list: 

   * Click **+ New element**. 

   *  Enter a **Value** for the element: For example, an IP address or domain. You can also add an optional note. 

   * Set an expiration period (**Time to live**) for the element: Select **No expiration** or select the number of days (1-364) you want the list to be active.

   * Click **Add** to confirm and save the new element or **Cancel** to discard your changes.

   * Repeat these steps to continue adding elements to your lookup list.

![Add values to lookup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/edit-static-lookup-jan.png)

## Edit a lookup list manually

Hover over the element in the table, click **edit** and update the **Value**, **Comment**, or **Time to live** as needed.

Click **Save** to apply the changes.

To delete an existing lookup, hover over the element in the table, click **delete**, and **Confirm** the process.



## Create a lookup list via CSV

You can create a large lookup list of up to 200 elements, or update the elements of an existing list with a CSV file. 

Prepare a CSV file that includes between 1 and 200 elements:  

* An element line can include a single value and an optional comment but should not be left blank. 
* Don't include header titles for element tables: The headers for the lookup list tables in Cloud SIEM are always **Value** and **Comment**.

If your CSV file includes elements already in the lookup list, the values are merged and the comments in the uploaded file overwrite the existing comments.

![CSV files for upload](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/csv-for-upload.png)

Navigate to [Lookup lists](https://app.logz.io/#/dashboard/security/rules/lookup) and click on New lookup. Select the type of list you want to create, in this case, Upload from CSV.

Set the expiration period (**Time to live**) for the element: Select **No expiration** or select the number of days (1-364) you want the list to be active.

Click **Upload CSV file** and select the file from your computer.

The list will be auto-added to Logz.io with the relevant values. You can review the different values and edit them if necessary.

Rename your lookup list, add an optional description, and click **Save** to apply the changes.


<h3 id="additional">Additional resources</h3>

Learn how you can use a query to create a [Dynamic lookup list](/docs/user-guide/cloud-siem/lookup-lists/dynamic-lookup/).
