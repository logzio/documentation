---
sidebar_position: 9
title: Explore Best Practices
description: Best practices in Log management and Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, explore, dashboard, log analysis, observability]
---

Once you've sent your data to Logz.io, you can search and query your logs to identify, debug, and monitor issues as quickly and effectively as possible.

## Lucene

Explore supports an enhanced version of Lucene, offering autocomplete suggestions and syntax highlighting to help you build faster, more accurate queries.

As you type, Lucene displays available fields, variables, and operators, making it easier to construct queries. If there's an error in your syntax, hover over the error indicator to get feedback that guides you toward a solution and a valid search.

For example, you can quickly search for logs where `logSize` exceeds a specific value or find messages containing certain words.

![numeric filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/logsize-bigger-feb24.png)


To perform range-based searches, the field must be mapped as a numeric value (e.g., long, float, double). Use the following syntax to find values within a range.

For example, to find all logs where logSize is between 1200 and 1500:

`LogSize:[1200 TO 1500]`

To refine your search further, combine multiple conditions. Find logs where logSize is between 2000 and 3000 and the eventType is MODIFIED:

`LogSize:[2000 TO 3000] AND eventType:MODIFIED`

Find logs where logSize is between 2000 and 3000 and the logzio-signature is in the range 700000000 to 710000000:

`LogSize:[2000 TO 3000] AND logzio-signature:[700000000 TO 710000000]`

To exclude specific values from your search, use the NOT operator. For example, to find logs where `logSize` is between 2000 and 3000, but exclude logs from `agent-k8s`:

`LogSize:[2000 TO 3000] AND type NOT "agent-k8s"`

## Keyboard Shortcuts

Explore includes several keyboard shortcuts to help streamline your workflow:

* Control + Enter – Submits the query, even if the suggestion menu is open.
* Shift + Enter – Creates a new line to organize your Lucene query more clearly.
* Command + D – Highlights the next occurrence of the selected word.

Explore uses the same editor as VS Code, so most of its shortcuts will work here. [View the full list here](https://code.visualstudio.com/docs/editor/keybindings#_keyboard-shortcuts-reference).

Looking for a shortcut that isn’t available? [Let us know](mailto:help@logz.io), and we’ll consider adding it!


## Simple Search

Simple Search offers an autocomplete feature to help you build queries by selecting fields, conditions, and values—similar to Lucene but with a more streamlined approach.

Click the search bar or start typing to see available fields, parameters, and conditions. To add a custom value, type it in and click the + sign. You can also enter free text, which will automatically convert into a Lucene query.

## Filters

Use the side panel to refine your search by selecting specific accounts and exploring all available fields in your logs.

Click a field to view its values:

* **String fields** display unique values along with a percentage indicating how frequently each appears.
* **Numeric fields** allow you to set a range, letting you filter logs based on size or other numerical values.

For example, `LogSize` lets you select the size of the logs you're interested in:

![numeric filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-filters-feb24.png)


## Visualize

The Visualize button provides additional ways to explore your data. Use it to switch to a **group-by** view, **compare data** to a previous time frame, adjust **time intervals**, and add **deployment markers** to track trends after a deployment.

:::note
When using Group by, the graph displays **up to 10 values**. Any additional values are grouped under **Other**.
Entries with empty or undefined values for the selected field will appear under **Missing**.
:::


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

![Time frame options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/adjust-time-explore-feb24.png)