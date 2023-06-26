To make your search engine queries and analytics are more effective, OpenSearch Dashboards maps each field by a data type, so it knows how to display it according to its capabilities. There are two types of mapping fields:

* **Dynamic** - This is the default mapping type, determined by the value of the log fields mapped at the beginning of each day.
* **Explicit** - This is a forced mapping type, and when chosen, OpenSearch will always map this field as the same data type.

For example, if the value of the log field is `"yourField":123`, OpenSearch will map it as a **number (Long)**.

`“yourField”:”abc”` will be mapped as a **Keyword (String)**.

`“yourField”:{“someField”:”someValue”}` will be mapped as an **Object**.

`yourField.someField` will be mapped as a **Keyword (String)**.

If a field is mapped as a string, OpenSearch won’t allow you to run any mathematical queries on the field.
If it's an analyzed field, such as `message`, `tags`, or `geoip_location`, OpenSearch won't let you use it in an alert, a visualization, or a `group by` rule.

Field data type determines how each field is indexed and shown in OpenSearch Dashboards. Account admins can change the data types according to a predefined set of options:

![Choose field data type](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-mapping/mapping-fields-main-.png)

Changing a field's data type may affect any dashboards, visualizations, searches, alerts, optimizers, and integrations using that field.