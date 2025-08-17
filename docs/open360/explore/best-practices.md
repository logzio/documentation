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

As you type, Lucene displays available fields, values, and operators, helping you construct queries quickly. If your query contains a syntax error, hover over the error indicator to get feedback and fix it easily.

To run a quick search, just type a word or phrase:

`error`

Use field-specific filters:

`logSize:[1200 TO 1500]`

Or combine multiple filters to narrow results:

`LogSize:[2000 TO 3000] AND eventType:MODIFIED`

![numeric filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/logsize-bigger-feb24.png)

Want to get more out of your searches? Learn how to use wildcards, regex, fuzzy logic, proximity matches, field existence checks, and more in our full [Lucene Query Syntax Guide](https://docs.logz.io/docs/user-guide/explore/lucene-best-practices/).

## Keyboard Shortcuts

Explore includes several keyboard shortcuts to help streamline your workflow:

* Control + Enter – Submits the query, even if the suggestion menu is open.
* Shift + Enter – Creates a new line to organize your Lucene query more clearly.
* Command + D – Highlights the next occurrence of the selected word.

Explore uses the same editor as VS Code, so most of its shortcuts will work here. [View the full list here](https://code.visualstudio.com/docs/editor/keybindings#_keyboard-shortcuts-reference).

Looking for a shortcut that isn’t available? [Let us know](mailto:help@logz.io), and we’ll consider adding it!

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