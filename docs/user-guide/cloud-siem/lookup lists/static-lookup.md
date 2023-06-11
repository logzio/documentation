---
sidebar_position: 2
---

# Static Lookups



Static lookup lists include values you define, used as a reference to search and match elements across your code. For example, you can create lookup lists of allowlisted or blocklisted usernames, IP addresses, regions, or domains.

:::note
Lookup list values are only string-based and do not support ranges. OpenSearch Dashboards, however, supports range-based searches, such as IP: [127.0.0.0 TO 127.*].
:::

You can reference lookup tables in a security filter. 

In **Static lookups**, you define fields and values that do not change during the task run.


#### Managing and using lookup lists 

:::tip
To create a large lookup list with up to 200 elements, we recommend that you use a CSV file to upload values. The [lookup lists API endpoints](https://docs.logz.io/api/#tag/Lookup-lists) also let you independently manage lookup lists: To create a new list, you'd use the [Create lookup lists API](https://docs.logz.io/api/#tag/Lookup-lists), and add elements (either via CSV file  or via the [Add element to a lookup list API](https://docs.logz.io/api/#operation/createLookupListElement).
:::


#### Configure the default expiration period for new lookup lists

Time to live (TTL) is the number of days remaining until the lookup list is expired: A lookup list with a TTL of 1 day expires within 24 hours from the time it was created and a list with a TTL of 2 days expires within 48 hours from the creation time.

By default, all new lookup lists are created without an expiration period. To set the Default **Time to live** (**TTL**) for new lookup lists, at the top of the Lookup lists page, click **Change**, select **No expiration** or a period between 1-364 days, and then **Save** your changes to apply them or **Cancel** the change. 
![Configure the default TTL for new lists](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/set-default-ttl_2021.gif)


#### Create or edit a lookup list manually



1. In the [Lookup lists](https://app.logz.io/#/dashboard/security/rules/lookup) page, do one of the following: 
   * Click **+ New lookup** to open **Edit a lookup list**. 
   * For an existing list, hover over the list in the table, and click **edit** <i class="li li-pencil"></i> to open **Edit a lookup list**.   
   ![Create a new lookup list or modify an existing list](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/create-edit-lookup_manual.png) 

1. In the **Edit a lookup list** page, update the **Name** and optional **Description** for the list.
  
1. To add a new line to the list: 

   a. Click **+ New element**. 
    
   ![Lookups](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/add_element-lookup_list.gif)

   b.  Enter a **Value** for the element: For example, an IP address or domain. You can also add an optional note. 

   c.  Set an expiration period (**Time to live**) for the element: Select **No expiration** or select the number of days (1-364) you want the list to be active.

   d. Click **Add** to confirm and save the new element or **Cancel** to discard your changes.

   e. Repeat these steps to continue adding elements to your lookup list.

1. To edit an existing element: 

   a.  Hover over the element in the table, click **edit** <i class="li li-pencil"></i> and update the **Value**, **Comment**, or **Time to live** as needed. 
   b. Click **Save** or **Cancel.**

1. To delete an existing element, hover over the element in the table, click **delete** <i class="li li-trash"></i> , and **Confirm** or **Cancel** the action.    



#### Create or edit a lookup list via CSV file upload


Create a large lookup list of up to 200 elements, or update the elements of an existing list with a CSV file. 

Prepare a CSV file that includes between 1 and 200 elements:  

* An element line can include a single value and an optional comment, but should not be left blank. 
* Don't include header titles for element tables: The headers for the lookup list tables in Cloud SIEM are always **Value** and **Comment**.

If your CSV file includes elements that are already in the lookup list, the values are merged and the comments in the uploaded file overwrite the existing comments.

![CSV files for upload](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/csv-for-upload.png)


1. In the [Lookup lists](https://app.logz.io/#/dashboard/security/rules/lookup) page, click **Upload from CSV file**. 
   ![Upload from CSV ](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-lookups/newlookup-csv.png)
1. In the **Upload records from CSV file** dialog, configure the TTL for the list as needed.
1. Click **Upload CSV file**, select the relevant file, and confirm, or **Cancel** to exit the upload. 
   The **Edit a lookup list** page opens and your new lookup list is displayed with an **Untitledxx** default name (for example, **Untitled20**).
1. Rename your lookup list, add an optional description, and click **Save** to update.



###### Additional resources

Learn how you can use a query to create a [Dynamic lookup list](/user-guide/lookups/dynamic-lookup.html).
