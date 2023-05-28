---
sidebar_position: 2
---


Logz.io Metrics solution is powered by Prometheus. This topic will help you get started with PromQL on Logz.io, and presents some examples and use cases for your environment.

:::note
PromQL does not support the `*` wildcard that Lucene queries use. 
Instead, use `"~"` before the value you want to search, and `".+"` at the end of it.
:::

### Let's query

* To search all of the time series data points in your dashboard, run the following query:
`count({__name__=~".+"}) by (__name__)`

* To search for a specific time series point, add the relevant value to the query:
`{__name__=~"value.+"}` 
    For example, to get all of the time series data points that starts with the value **container**, use the following query:<
`{__name__=~"container.+"}`

![PromQL return container values](https://dytvr9ot2sszz.cloudfront.net/logz-docs/Infrastructure-monitoring/promql-query-container.png)

* Searching a label inside a time series changes the query. You need to add the name of the time series, and the value you're looking for:
`nameOfTimeSeries{label=~"value.+"}`

    For example, if the time series you're querying has the following labels:
    
    * namespace
    * container
    * pod
    * user

    To search for a namespace label that starts with **kub**, run the following query:<br>
    `container_memory_working_set_bytes{namespace=~"kub.+"}`

![PromQL search labels and values](https://dytvr9ot2sszz.cloudfront.net/logz-docs/Infrastructure-monitoring/promql-search-values.png)

### Metrics browser

* If you're not sure what metrics your dashboard contains, which labels it includes, or the values you can search for, click **Metrics browser** to view all of the data, and build the query that fits your needs. 

![PromQL cheatsheet](https://dytvr9ot2sszz.cloudfront.net/logz-docs/Infrastructure-monitoring/query-cheatsheet.png)

### Additional resources

Read more about Prometheus, PromQL, and how you can use it in Logz.io:

* [An Intro to PromQL: Basic Concepts & Examples](https://logz.io/blog/promql-examples-introduction/#promqlintroduction)
* [Basics of querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)
