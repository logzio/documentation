#### Configuring a correlated rule


To correlate events, we need to configure 2 search queries, each with its own trigger condition. For the rule to trigger, both conditions must be satisfied.

If you opt to join the queries, you must also select aggregation criteria and fields to join. When the queries are joined, the values of the join fields must match for the rule to trigger.

This tutorial assumes you are familiar with the process of configuring a rule.
It explains what's different when correlating queries.

##### Name the rule

The name should convey the significance of the combined event for both queries together.

For example, "Brute-force attack from malicious address followed by malware download".

##### Add another query

Click **+ Add another query** to add the option to correlate queries.

![Add another query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/add-another-query.png)

##### Query 1 & Query 2

The form now has 2 sections: Query 1 & Query 2.

There is no significance to their order. If Query 1 and Query 2 are interchanged, the results will be the same.

The following criteria are similar for both the single-query and multi-query rule:

* Fill in the free search and filtering criteria as usual.
* If you are only using filters, leave a wildcard **asterisk (*)** in the free search box.
* You have the option to aggregate results for as many as 3 fields. Select **group by** fields from the dropdown list.
* Select the **Accounts to search**.
* You can preview the results in OpenSearch Dashboards for each query independently. Click **Preview in OpenSearch Dashboards** to open the results for the past 24 hours in another tab.
* If you change your mind, you can delete either of the queries. Click **X Delete query** to return to a single-query form.

![empty alert form with 2 queries](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/multiple-queries.png)

##### Joining the queries (_optional_)

If you opt to join the queries, you must first add **group by** fields that will aggregate results by values. When the queries are joined, the values of the join fields must match for the rule} to trigger.

* First, select the **group by** fields for each of the queries.
  * You can select as many as 3 fields.
  * The number of **group by** fields can differ between the queries.
* **Group by** fields provide criteria for count aggregations.

  As a result, the rule will count the query results returned per value of the **group by** field. This allows you to join the results by searching for overlapping values that are the same for the join field pairs.

:::note
**Grouped fields** limitation: You cannot use the **group by** feature on analyzed fields (_Text_ data type).
:::

* Select the join pairs you want to enable. You can enable as many as 3 pairs.

  Available join options are automatically determined by the order of your **group by** fields. The suggestions are ordered pairs of the **group by** ields.

  You do not have to join all of the **group by** fields, and the queries can have a different number of **group by** fields.

![name with 2 queries](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/both-queries.png)

When joined, the rule looks for values that are common to the field pairs selected for joining the queries. This means the rule will only trigger if it finds matching values for the join field pairs.

![Add a group by field function for both queries](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/group-by-join.png)

Joined fields are indicated by the **link icon <i class="fas fa-link"></i>**.

When the rule triggers, the event log will specify the matching values that triggered the rule in the field `logzio-alert-join-values`.

For example, if we enable 2 joins: by the fields hostname and then IP address, the field `logzio-alert-join-values` will contain comma-separated pairs, such as `Host1, 247.23.11.58`, `Host2, 44.76.131.4`.


##### Trigger conditions

When the rule has 2 queries, you can set a single condition for each of your queries, and a single severity.

As usual, each query can take a different condition for a field of your choice.

![Conditions and severity for correlated rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/join-trigger.png)

The rule conditions are evaluated over regular intervals. The time frame for evaluating the conditions is the same for both queries. It can range between a minimum of 5 minutes and a maximum of 24 hours/1 day.

##### Notification description

It's a good idea to add a description that works for both queries and what they capture together. As usual, best practice is to include a playbook that covers the steps needed to investigate and remediate the incident.

##### Configure output per query

You have the option to send notification sample data in **JSON** or **Table** format.
Toggle the button to select your preferred format.

Next, select the output fields for each query, as applicable. As usual, if the query has aggregations (or group-by fields) definted, the output will be auto-selected, and the aggregated results will be sent by default. Otherwise, you can select which fields to include. [Learn more](/user-guide/alerts/configure-an-alert.html#output-format--content).

![Notifications are auto-configured](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/join-notification.png)

##### Save it!

Click **Save** at the top of the form to save your rule.


