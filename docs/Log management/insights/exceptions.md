---
sidebar_position: 2
---


# Logz.io Exceptions automatically surfaces exceptions and highlights them in your log results.

While troubleshooting in OpenSearch Dashboards, you can easily see the number of exceptions identified in your log results for every query you run. The list is always in-context, and specific to the log results returned by your search.

To review exceptions affecting your environments, switch to the **Exceptions** tab and expand the documents that interest you.

![Exceptions count in OpenSearch Dashboards](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/exceptions.png)

### What's an exception?

Logz.io Exceptions Engine scans your log to identify application errors and groups them into a logical unit. There's a different exception pattern for each language supported in the system, built according to standard libraries, known issues, and best practices.

Each exception is categorized as one of the following:

* **Cognitive insight** - Exceptions are marked as Cognitive insights when a log contains particular words linked to known issues. For these exceptions, Logz.io provides additional relevant links and metadata related to the logged issue.


* **Application insight** - Application insight, also known as Exceptions inside Logz.io's dashboard, are for logs containing words implementing that users have errors in their code. For example, when an exception is identified in `thread "main" java.lang.ArrayIndexOutOfBoundsException: 5`, it's marked as an Application insight.

:::note
Logz.io's Exceptions tab only includes **Application insight** exceptions. 
:::

### Find all exceptions

You can find and view all exceptions by using the following query:

`_exists_: _logzio_logceptions OR _exists_:"_logzio_insights"`

Each exception is grouped into logical units, which you can view under the **Exceptions** tab.

![Exceptions count](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/exception-query.png)

You can also view all exceptions by navigating to **[Log Management](https://app.logz.io/#/dashboard/osd)** > **[Insights](https://app.logz.io/#/dashboard/insights)**. There you can view a summary of your exceptions and filter them according to status, log types, tags, assignees, and date. 

<!-- ![Log management insights](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/logs-insights-exceptions.gif) -->

### Exception count
To help you stay focused, the list is capped and will always show the top 10 exceptions.
If there are more exceptions than can be shown, you can fetch the **Most frequent** or **Most recent** exceptions.

* **Most frequent** - Most frequent number of occurrences in the given time frame.
* **Most recent** - Most recently occurred within your selected time frame.

![Filter exceptions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/exceptions-number.png)

### Investigating an exception

The same exception may recur in different log lines, with slight variations. Sometimes, they may even appear as clones.

Logz.io tracks the recurrence of each exception over time, and retains its **First occurrence**, that is the earliest time the exception was identified. The history of exceptions can date back up to 6 months.

![Expand an exception for more details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/exception-overview.png)

|---|---|
|Exception| Concise title auto-detected by Logz.io based on the content of the logs |
|Tag| Descriptive tags auto-detected by Logz.io that describe the exception type |
|Log types| A list of all the log types found to be affected by the exception |
|# of occurrences| The number of times logs associated with this exception were spotted in the given time frame |
|First occurrence| The earliest time the exception was identified |
| Last seen | Most recent occurrence of the exception, based on your browser's time zone |


### Get your exceptions' insights

You can set an alert to get a digest, including your exceptions insights.

To do so, you'll need to [**configure an alert**](/user-guide/alerts/configure-an-alert.html) with the following query:

`_exists_: _logzio_logceptions OR _exists_:"_logzio_insights"`

And choose the notification endpoint you prefer. You can receive insights to your endpoint of choice, such as an email, Slack channel, logs, and more.

### Sorting & Filtering options

By default, exceptions are sorted by their frequency (that is, their number of occurrences).

To reorder exceptions by **# of occurrences**, **First occurrence**, or **Last seen**, click the column header to sort the data in ascending/descending order. (An arrow indicates the sorting method.)

### New exceptions

Exceptions that occurred for the first time within the search time frame are tagged as **New** exceptions.

![Exception timeframe](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/exceptions-new.png)
