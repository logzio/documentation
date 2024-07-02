---
sidebar_position: 5
title: Exceptions
description: Find and highlight exceptions with Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, exceptions, log analysis, observability]
---


Logz.io Exceptions automatically surfaces exceptions and highlights them in your log results.

It's integrated into Explore, where you can easily see the number of exceptions identified in your log results for every query you run. The list is always in-context, and specific to the log results returned by your search.

To review exceptions affecting your environments, click the **Exceptions** button. This will open a quick view menu where you can review and filter the exceptions.

![Exceptions in Explore](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/exceptions-quick-view.png)

### What's an exception?

Logz.io Exceptions Engine scans your log to identify application errors and groups them into a logical unit. Each language has a different exception pattern based on standard libraries, known issues, and best practices.

Each exception is categorized as one of the following:

* **Cognitive insight** - Marked when a log contains specific words linked to known issues. Logz.io provides additional relevant links and metadata related to these exceptions.


* **Application insight** - Also known as Exceptions inside Logz.io's dashboard, these occur when logs contain words indicating errors in user code. For example, when an exception is identified in `thread "main" java.lang.ArrayIndexOutOfBoundsException: 5`, it's marked as an Application insight.


:::note
Logz.io's Exceptions only include **Application insight** exceptions. 
:::

### Find all exceptions

You can find and view all exceptions by using the following query:

`_exists_: _logzio_logceptions OR _exists_:"_logzio_insights"`

![Find exceptions in Explore](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/logzio-insights.png)

Click the **Exceptions** button to see all exceptions related to your current query.


### Investigating an exception

Exceptions may recur in different log lines with slight variations or as duplicates. Logz.io tracks each exception over time, retaining its first occurrence for up to 6 months.

Click the **Exceptions** button to see all exceptions related to your current query, up to 1,000 exceptions. You can filter the list by **Most frequent** or **Most recent** exceptions. Use the toggle to view only new exceptions.

Hover over an exception to open a menu where you can filter it in or out of your view. 

You can also view exceptions directly in the Explore filter as a dropdown list. Search for a specific exception and use the checkboxes to include or exclude it in your search.

**Only one exception can be filtered at a time.**

Each exception includes detailed data:

|Type|Description|
|---|---|
|Exception| Concise title auto-detected by Logz.io based on the content of the logs |
|Trend| A graphical trend of the exception occurrences over time, helping visualize the frequency pattern |
|Count| Shows the total number of times the exception has occurred  |
|Log types| A list of all the log types found to be affected by the exception |
|First occurrence| The earliest time the exception was identified |

![Exceptions quick view inner view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/exceptions-quick-view-focus.png)

