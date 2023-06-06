---
sidebar_position: 3
title: Share OpenSearch Dashboards Objects
---

You can share OpenSearch dashboards, saved searches and visualizations between accounts by exporting and importing them. This is helpful if you have multiple main accounts or accounts on multiple regions. You can also use this process to keep a local backup copy. 


### Export objects from OpenSearch Dashboards 

:::note
You can export data from up to 20 different accounts. To export data from more than 20 accounts, you'll need to add all of your available accounts to the search by clicking `Add all accounts`.
:::

The first step is to export your existing dashboards, searches, and visualizations out of your OpenSearch Dashboards instance.

1. In **Logs > OpenSearch Dashboards**, click the side menu > **<i class="li li-gear"></i> (Management) > Stack Management > Saved objects** 
2. Select **Export xxx objects** (**xxx** is the number of objects available for export).
3. You can un-select any categories you want to exclude from the export. Another way to do this is to hand-pick the objects you want to export, but this is less recommended.
4. Click **Export all**. 
5. A JSON file with your exported objects will be saved to your default location.


![Find saved objects](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/export-objects.gif)

<!-- <video autoplay loop>
  <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-videos/export_kibana_objects1.mp4" type="video/mp4" />
</video> -->

:::note
The full export is highly recommended. That way, you can be sure that you'll have everything, irrespective of any inter-dependencies. For example, if you export a single object that happens to be dependent on another object, the export can fail.
:::


### Import objects from a JSON

**Before you begin, you'll need**:
Make sure that the relevant logs have already shipped to your Logz.io account and refresh the OpenSearch Dashboards mapping.

Assuming you've got a JSON with your exported objects, it's time to import them into your Logz.io account.

1. In **Logs > OpenSearch Dashboards**,  click the side menu > **<i class="li li-gear"></i> (Management) > Stack Management > Saved objects** 
2. Click **Import** and select the relevant JSON file.
3. You can toggle the option to **Automatically overwrite conflicts**. Enable it if you want the export to overwrite existing objects in case of conflict. Select the option that works for you.

You're done! You're all set to use your newly imported OpenSearch dashboards, saved searches, and visualizations.

:::note
If any visualization or dashboard did not import, the issue is likely a field referenced in the visualization but not indexed in your Logz.io account. Check that the relevant logs are already in the account and refresh the OpenSearch Dashboards mapping.
:::


### Sharing objects across versions
 
 Your saved and shared objects can only be imported into the following OpenSearch Dashboards versions: 
 
 * The same release version
 * A newer minor version on the same major version
 * The next major version

Exported shared objects are not backward compatible and thus can’t be imported into an older version of OpenSearch Dashboards.

<!-- 
##### Compatibility examples

The following table provides some compatibility examples:

|Exporting from version: | Importing to version:| Compatible? [Y/N]|
|---|---|---|
| 6.7.0 |6.8.1|Yes|
| 6.8.1 |7.3.0|Yes|
| 7.3.0 |7.11.1|Yes|
| **7.11.1**| **7.6.0**| **No**|
| **6.8.1** | **8.0.0**| **No**|
-->