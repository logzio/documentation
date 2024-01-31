---
sidebar_position: 5
---

# Using Inspect Feature on OpenSearch Dashboards UI



If you want to search logs using our [Search API](https://api-docs.logz.io/docs/category/logz-api), an easy way to construct your query is to use the OpenSearch Dashboards UI.


 
### Construct the search query

Enter the search query into the search bar on your OpenSearch Dashboards UI.

For example, you can filter by the log type: `type:payment`. This search query will retrieve all log entries that match the log type.

![Search](https://dytvr9ot2sszz.cloudfront.net/logz-docs/api-cookbook/search-api.png)



### Navigate to the Inspect window

Select **Inspect** to open the inspection window.

In the inspection window, select **Request**.

![request](https://dytvr9ot2sszz.cloudfront.net/logz-docs/api-cookbook/inspect-osd.png)


### Copy the query object

The `query` object of the JSON file displayed, contains the query that you can use in your request via our [Search API](https://api-docs.logz.io/docs/category/logz-api).

![JSON object](https://dytvr9ot2sszz.cloudfront.net/logz-docs/api-cookbook/query-osd.png)

 