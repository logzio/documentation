---
sidebar_position: 6
title: Explore Best Practices
description: Best practices in Log management and Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, explore, dashboard, log analysis, observability]
---

Once you've sent your data to Logz.io, you can search and query your logs to identify, debug, and monitor issues as quickly and effectively as possible.

Explore supports a few query methods, including:


## Simple

Logz.io offers an intuative and easy way to build your query. Click the search bar or start typing to find and select fields, conditions, and values. 

Build your query by selecting fields, parameters, and conditions. Start typing to see all the relevant fields available, add an operator, and select the value. To add a custom value that doesn't appear in your logs, type its name and click on the + sign to apply it.

Click Enter to apply the query, or tab to build the next condition. 

You can also type free text in your search, which will convert it into a Lucene query.

## Lucene 

Logz.io supports Lucene, an open-source search engine software library.

With Lucene, you can search for free text by typing the text string you want to find; for example, `error` will return all words containing this string, and using quotation marks, `"error"`, will return only the specific word you're searching for.

//![See error](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/best-error-aug27.png)

Use the filters to refine your search. For example, you can filter out all `log_type:info` to focus your search on relevant finds.

//![Filter out](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/isnot-filter-aug27.png)

The filters include numeric based fields, such as `LogSize`. Choose the operator and value to view the relevant results. 

![numeric filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/logsize-explore-aug27.png)

To search for a value in a specific field, use the following syntax:

`log_level:ERROR`

Use the boolean operators AND, OR, and NOT to create more complex searches. For example, to search for a specific status that doesn't contain a certain word:

`log_level:ERROR AND Kubernetes`

If you want to perform **range-related searches**, the fields must be mapped as numbers (long, float, double, etc.). Then, you can use the following syntax. For example, you can use it to find all status codes between 400-499:

`LogSize:[2000 TO 3000]`

To make your search more complex, you can find status codes 400-499 with the extension php:

`LogSize:[2000 TO 3000] AND eventType:MODIFIED`

Or, find status codes 400-499 with the extension php or html:

`LogSize:[2000 TO 3000] AND logzio-signature:[700000000 TO 710000000]`

To exclude a term from your search, you can use the following syntax:

`LogSize:[2000 TO 3000] AND type NOT (name:"agent-k8s")`


### Apply regex to search

:::caution
Using Regex can overload your system and cause performance issues in your account. If Regex is necessary, it's best to apply filters and use shorter timeframes.
:::

Logz.io uses Apache Lucene's regular expression engine to parse regex queries, supporting regexp and query_string.

While Lucene's regex supports all Unicode characters, several characters are reserved as operators and cannot be searched on their own:

`. ? + * | { } [ ] ( ) " \`

Depending on the optional operators enabled, some additional characters may also be reserved. These characters are:

`# @ & < >  ~`

However, you can still use reserved characters by applying a backslash or double-quotes. For example:

`\*` will render as a * sign.

`\#` will render as a # sign.

`\()` will render as brackets.


To use Regex in a search query in OpenSearch, you'll need to use the following template:

`fieldName:/.*value.*/`.

For example, you have a field called `sentence` that holds the following line: "The quick brown fox jumps over the lazy dog".

To find one of the values in the field, such as `fox`, you'll need to use the following query:

`sentence:/.*fox.*/`.

// DIDNT EDIT BELOW THIS LINE

## Edit log view

You can add additional columns to your logs table view.

Find the field you'd like to add, hover over it and click the **Toggle column in table** button.



//![Add field](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/add-field-discover.png)

Once added, you can drag it to reposition it, or click the **X** to remove it.


//![Edit field](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/add-field-overview.gif)

Finally, you can save your search and its view by clicking on the **Save** option, at the top navigation bar.

//![Save field](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/save-your-fields.png)

## Filter log results

To narrow down your search, click the **Add filter** option underneath the search bar.

Choose the field, operator, and value you'd like to apply in your filter, and click save. You can also create a custom label to rename the filter for better identification.

![Apply a filter](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/add-a-filter.png)

Once you've set your filter, clicking on it will open additional abilities such as pinning it across all apps, excluding results, temporarily disabling it, editing, or deleting it.

## Select logs' time frame

The default period to display results is 15 minutes. You can edit this time frame by clicking on the **Show dates** link or clicking on the calendar icon.

The calendar icon offers popular time frames for you to choose from and lets you select the refresh rate of your data.

![Time frame options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/quick-time-edits.png)

The **Show dates** option lets you set a start and end time. In the popup, select between the following options:

* **Relative** - Set a start and end date to view your data
* **Now** - Get real-time troubleshooting and monitoring of your logs
* **Absolute** - Browse the calendar view and choose any time frame to view your data. In this option, you can type the time frame you want to view

![Choose time frame](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/time-settings-gif.gif)

## Create Log Visualizations

In the following video, you'll be able to see how to create a visualization dashboard based on your logs:


<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/videos/log-visualizations-velcfd5tpr.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>



<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/velcfd5tpr" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Divide your log data

You can divide logs from different environments by type, by utilizing Logz.io's sub accounts option.

Create a sub account and configure it to receive the same logs as an existing account, mapping it as a different data type.

For example, if a `metadata` field is assigned as an `Object` in your production environment, you can assign it as a `String` in your testing environment by creating a sub account to which you’ll send the same logs.

You can also send data from each environment to a dedicated sub account to monitor them individually.

Learn more about [creating and managing sub accounts](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts) and about [field mapping](/docs/user-guide/data-hub/field-mapping/) in your account.

## Additional resources

* [Configure an alert](https://docs.logz.io/docs/user-guide/log-management/log-alerts/configure-alert/)
* [Use Insights to detect new exceptions and critical errors](https://docs.logz.io/docs/user-guide/log-management/insights/ai-insights/)
* [Use Live tail to get a live view of your logs](https://docs.logz.io/docs/user-guide/log-management/live-tail/)

