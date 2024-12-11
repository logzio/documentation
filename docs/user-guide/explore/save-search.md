---
sidebar_position: 7
title: Saved Search
description: Save your search to easily access and share them
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, save search, explore, logs, saved search, save query, save, observability]
---

Saved Searches allow you to save specific sets of search queries and filters, making it easy to reuse them in future searches. This is particularly useful for consistently monitoring certain logs or data without manually re-entering the search parameters each time. By saving and reusing your searches, you can quickly access and apply complex search queries, thereby saving time and ensuring consistency in your data analysis.

This functionality is handy for users who need to perform repetitive searches, monitor specific data patterns, or collaborate with others on data analysis.

## Save your search

Navigate to [Explore](https://app.logz.io/#/dashboard/explore) and enter a query using either Simple or Advanced search.

Click the **Save** icon to open the Saved Search menu. Here, you can see all saved searches within your account created by you or your teammates.

Click **Save Search**; give your search a meaningful name that you and your team will easily understand, then click **Save** to confirm.

![saved search save](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/save-search-oct21.png)

Once saved, your search name will appear in the page's breadcrumbs. 

Any changes to the query or addition of filters will **not** be automatically saved. A draft label will appear in the breadcrumbs to indicate unsaved modifications.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/saved-draft-oct21.png" alt="draft-label" width="500"/>



To update the current search, open the Saved Search menu and click **Update Search**. You can save it as a new search by clicking **Save as New**.

To return to the main view and exit the current search view, click on **Explore** in the breadcrumbs.



## Manage saved searches

You can change the Saved Search viewing ordering by choosing ascending, descending, or last created. Use the search bar to find specific Saved Searches.

Once you find a Saved Search you want to manage, hover over it to view an additional menu where you can delete it, edit its name, or add it to your favorites, pinning it to the top of the list. 

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/saved-search-sub-menu.png" alt="saved-sub-menu" width="500"/>

## Import Saved Searches from OpenSearch Dashboards

Logz.io automatically imports all Saved Searches from OpenSearch Dashboards to Explore.

To manually import your saved searches from OpenSearch Dashboards to the new Explore dashboard, follow these steps:

* **Generate an Empty State**: In the Saved Search search bar, enter a search query that you know will return no results, for example, `jjjjj`.

* **Trigger the Import Prompt**: When no saved searches are found, you'll see a message indicating this and a button to import your saved searches.

* **Import Saved Searches**: Click the button to import all your saved searches from OpenSearch Dashboards into Explore. This process automatically imports all of your Saved Searches.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/saved-search/import-saved-search.png" alt="import-saved-searches" width="500"/>
