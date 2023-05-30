---
sidebar_position: 4
---


# Understanding Log Patterns

The Logz.io Patterns Engine runs advanced clustering algorithms to automatically group logs with similar message fields by their frequency of occurrence.

As you’re troubleshooting in OpenSearch Dashboards, you can easily see the number of Patterns identified in your log results for every query you run. The list is always in-context, and specific to the log results returned by your search.

Patterns can help you isolate unusual events from a mass of repetitive events, identify frequent errors, and spot bulky uninteresting logs that can be dropped.

![Log patterns](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/patterns-in-discover.png)

To review your log results clustered into Patterns, switch to the **Patterns** tab in OpenSearch Dashboards and filter Patterns in/out of your results.

### Understanding log patterns

![Log patterns](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/log-patterns-table-1.png)

Time
: The earliest log that matches the pattern for the log results returned by your search.

Count
: The number of logs matching the pattern for the log results returned by your search.

Ratio
: The ratio of logs matching the pattern,
  relative to the total logs in the dataset.

Estimated size
: A raw estimate in GBs of the capacity taken up by the log pattern.

Pattern
: The patterns identified in the message fields.

Filters
: Filter a pattern in/out. You'll be taken to the **Logs** tab, where you'll see the filtered log results.


### Split logs to optimize pattern view

Patterns are specific to your log results. For optimal pattern recognition, we recommend **splitting your logs into multiple types** to allow you to see the different patterns more clearly. Combining many logs into one type may result in many unidentified patterns.


Log Patterns is an alternative view to the log document table. It shows the same logs organized in a different way. As you adjust your search and query parameters, filters, and time frame - Patterns are recalculated in sync with your log results.

### Filtering by log patterns

Pattern filters can be used in saved searches, visualizations, and dashboards. They can also be pinned across all apps, inverted, and temporarily disabled. Unlike other filters, Pattern filters cannot be edited.
  
![Patterns filter](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/patterns-filter1.png)

### Sorting by log patterns

The default sorting for your log document table is chronological, with the newest logs at the top. In contrast, Patterns are organized by default by frequency with the most common patterns at the top.

If you are looking for rare or infrequent logs, click the **Count** or **Ratio** column headers to sort the table by the least common logs.

You can sort your log patterns by their time of first occurrence, ratio, count, and estimated size.

### Log pattern variables: Categories vs. Wildcards

The log pattern reduces specifics in the log message field to generic _variables_.

Variables come in 2 forms: 

* Typical data categories, such as: **Date**, **Ip**, **Email**, **Url**, **Number**, **Path**, **Guid**, **Hash**, **Syslogtimestamp**, or similar.

  Variables are highlighted and easy to spot. Here's an example of a pattern that has identified 2 variables: Email and GUID.

  ![Duplicate entry `Email` for session `Guid`](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/sample-pattern1.png)

  If you filter for this pattern, the document table will return all of the logs that match this pattern in their original format, with the email and GUID information.

* Wildcard variables, indicated by an **<i class="fas fa-asterisk"></i>** to replace any number of characters (even 0). These variables are less intuitive and don't belong to any standard category. 

  ![reloading account `.*`log patterns matcher](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/sample-pattern2.png)

### Log pattern limitations

Unidentified size
: Estimated size calculations depend on a enabling the log size field in the [Manage accounts page](https://app.logz.io/#/dashboard/settings/manage-accounts). [Learn more](https://docs.logz.io/user-guide/accounts/manage-account-usage.html#enabling-account-utilization-metrics-and-log-size)

Unidentified patterns 
: Logs that don't fall under any pattern are grouped under the unidentified pattern category.


![Log pattern limitations](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/log-pattern-limitations_aug2021.png)