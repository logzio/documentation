---
sidebar_position: 6
title: Explore Best Practices
description: Best practices in Log management and Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, explore, dashboard, log analysis, observability]
---

Once you've sent your data to Logz.io, you can search and query your logs to identify, debug, and monitor issues as quickly and effectively as possible.

Explore supports a few query methods, including:


## Simple Search

Logz.io offers an intuitive and easy way to build your query. You can build queries easily by selecting fields, conditions, and values.

Click the search bar or start typing to see the available fields, parameters, and conditions. To add a custom value, type its name and click the + sign. You can also add free text to your search, converting it into a Lucene query.

## Lucene 

Logz.io supports Lucene for more advanced queries.

Type the string or query you want to find. For example, `error` will return all words containing this string, and using quotation marks, `"error"`, will return only the specific word you're searching for.


![See error](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/explore-error-oct21.png)

Search for a value in a specific field:

`log_level:ERROR`

Use the boolean operators AND, OR, and NOT to create more complex searches. For example, to search for a specific status that doesn't contain a certain word:

`log_level:ERROR AND Kubernetes`

To perform **range-related searches**, fields must be mapped as numbers (long, float, double, etc.). Then, you can use the following syntax. For example, you can use it to find all status codes between 400-499:

`LogSize:[2000 TO 3000]`

To make your search more complex, you can find status codes 400-499 with the extension php:

`LogSize:[2000 TO 3000] AND eventType:MODIFIED`

Or, find status codes 400-499 with the extension php or html:

`LogSize:[2000 TO 3000] AND logzio-signature:[700000000 TO 710000000]`

To exclude a term from your search, you can use the following syntax:

`LogSize:[2000 TO 3000] AND type NOT (name:"agent-k8s")`


## Filters

Use the filters to refine your search, whether you're using Simple or Lucene. Open string fields to view its related values, and open numeric fields to choose a range. For example, `LogSize` lets you select the size of the logs you're interested in:

![numeric filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/logsize-oct21.png)



## Regex in Lucene

:::caution
Using regex can overload your system and cause performance issues in your account. If regex is necessary, applying filters and using shorter timeframes is best.
:::

Logz.io uses Apache Lucene's regular expression engine to parse regex queries, supporting regexp and query_string.

While Lucene's regex supports all Unicode characters, several characters are reserved as operators and cannot be searched on their own:

`. ? + * | { } [ ] ( ) " \`

Some additional characters may also be reserved depending on the optional operators enabled. These characters are:

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


## Edit log table view

You can add additional columns to your logs table view.

Find the field you'd like to add, hover over it and click the **Toggle column in table** button (table icon).

![Add field](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/toggle-explore-oct21.png)

Once added, you can drag it to reposition it, or click the **X** to remove it.

## Save Searches

Save your current query or filtered view to quickly access it whenever needed. Click on the Save icon > Save Search and name your search. The query is saved while the results change according to your chosen time frame. 

![Save field](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/save-search-oct21.png)


## Select logs' time frame

The default period to display results is 15 minutes. You can edit this time frame by clicking on the time picker. Choose an option from the quick menu, or switch to the absolute view to select a specific time frame. You can type the time frame you want to view using this option.

![Time frame options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/timepicker-oct21.png)