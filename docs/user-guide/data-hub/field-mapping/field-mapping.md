---
sidebar_position: 1
---
# Field Mapping



Field mapping is the process of defining how a value and the fields it contains are stored and indexed. 

OpenSearch mappings are important whenever you want to perform any action on a field, such as visualize it, aggregate by it, or use it in an alert.




## Default mapping

You might have noticed that the particular fields mapped by OpenSearch Dashboards tend to vary. This is because mapping is dynamic and responds to the particular dataset you've selected. The larger the dataset, the more likely it is for fields to be unmapped by OpenSearch Dashboards.

By default, OpenSearch Dashboards maps only 1,000 fields to keep querying and filtering performance at top speed.

Here's how OpenSearch Dashboards does it. First, it finds every field that your account is actively using - in visualizations, dashboards, saved searches, alerts, and optimizers - and makes sure that those fields are mapped.

Let's say you have 10k fields in your database index, but are actively using 300 fields. Then OpenSearch Dashboards will first map your 300 required fields and then map another 700 random fields.

OpenSearch Dashboards will always make sure that all of your required fields are mapped by default. So even if you have more than 1,000 required fields, OpenSearch Dashboards will cover them all and ensure that _all_ of them are mapped every time.




## Field mapping types

{@include: ../../../_include/rules-alerts/field-mapping-types.md}

## Managing field mappings

Use field mapping to override dynamic mapping and resolve mapping errors for your ingested logs.
The changes you make on the **Field mappings** page won't affect the logs that are already ingested.

You can make **up to 5 mapping changes in a day**, but be cautious. 
Changing a field mapping may impact the components and integrations that use the field: Your dashboards, visualizations, searches, alerts, and optimizers may not perform as expected if you change field mappings. 

If you’re not sure of the impact of changing a mapping, contact the **[Logz.io Support team](mailto:help@logz.io)** for advice.


### *Date* data fields

:::note
Before you change, edit, and send `date` data fields, contact the **[Logz.io Support team](mailto:help@logz.io)**.
:::

There are additional restrictions for `date` data field types:

* Automatic date detection is disabled by default in dynamic mapping, which detects values as `string` instead of `date`.
* To avoid conflict between the mapping of `date` fields, the data type **must** be identical across all indices.

Therefore, to change the mapping of any field to a `date` field, contact **[Logz.io Support team](mailto:help@logz.io)** before sending the fields.

### How to identify when a field is not mapped

If you are trying to filter by a field but the field doesn't appear in the dropdown list, this is a good indication that the field is not mapped in OpenSearch Dashboards. 

OpenSearch's capabilities are most powerful for mapped fields. 
Fields that aren't mapped can be searched and queried. 
But they will not appear in filters and do not support 1-click visualizations.

| Action | Mapped field | Unmapped field |
|---|---|---|
| Filtering | ✔ | ✖️ |
| Appears in filtering menu | ✔ | ✖️ |
| Can be visualized | ✔ | ✖️ |
| Searchable | ✔ | ✔ |



{@include: ../../../_include/arrays_in_kibana/array_note.md}

## Manage your mapping




### Refresh mapping

If you find that many of the fields you are interested in exploring aren't mapped, you can refresh your mapping via the navigation menu. Click [<i class="li li-gear"></i> Settings> General settings > Refresh mapping](https://app.logz.io/#/dashboard/settings/general).


### Add specific fields to your default mapping

Instead of refreshing the mapping in bulk, you can add specific fields to your default mapping. Click **Field not indexed** on an unmapped field. [Learn more](/user-guide/logs/mapping/field-not-indexed/)

### Explicitly map a field 

To manually edit a field mapping,
Select [Data Hub > Field mappings](https://app.logz.io/#/dashboard/tools/field-mapping)
from the navigation menu. 

To change the field mapping type, hover over the field, click **edit** <i class="li li-pencil"></i>, make your changes, and click **Save**.



## Resolving mapping errors 

If you encounter an issue or an error when mapping your fields, check out the **[common mapping errors and why they happen](https://docs.logz.io/user-guide/invalid_logs/#mapping-errors)**.