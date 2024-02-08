---
sidebar_position: 1
title: The Grand Distributed Tracing Tour
description: Monitor your environment's traces with Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, timeline, observability, distributed tracing]
---


Your Distributed Tracing account complements your logging stack. To reach it, log into your Logz.io account and select the **Jaeger** or **Tracing** tab.

By default, your Distributed Tracing account is accessed from your main account. 

![tracing tour](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing_tour-update.png)



### Select a data source for the Distributed Tracing interface 

To display tracing data from a single data source in the Distributed Tracing tab, use the Source selector. 
![Pick a data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-data-source.gif)

You cannot select multiple data sources for an aggregated view.

### Search for traces. 
You search for and view traces on the **Search** page. 
Use the following fields to search for traces: 
![Search traces page](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace-search-fields1.png)



| Field | Description  |
|---------------|---------------|
| Service   |Select a service in your system  |
| Operation | Select an available operation from the list        |
| Tags      | Each span has its own set of tags Use the preconfigured tags that were used to enrich your traces to further refine your trace searches. The added business logic information makes for easier debug processes |
|Lookback                        |Select the time frame for the query|
|Min and Max Duration  |Set the minimum and maximum durations for the traces you want the query to      return Use these parameters to obtain more focused results and reveal performance issues |
| Limit Results                  |Set the maximum number of results for the query Up to 500 traces can be returned|      

    
#### Tag formatting requirements
* Use a space for conjunctions 
* Enclose values that contain whitespace in quotes
* Tag formatting requirements are summarized here: [logfmt <i class="fas fa-external-link-alt"></i>](https://brandur.org/logfmt) 
* A list of recommended tags can be found here: [https://github.com/opentracing/specification/blob/master/semantic_conventions.md <i class="fas fa-external-link-alt"></i>](https://github.com/opentracing/specification/blob/master/semantic_conventions.md)

#### Tag examples

*  `error=true` returns the traces with spans that are tagged as an error
*  `error=true db.statement="select * from User"`  returns the traces with spans that are tagged as `error=true`, which also include the requested db statement.
*  `http.status_code=500` returns the traces with a communication error   

### View trace search results on the Search page.
![Search results](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing_search-results.png)

**Results timeline**

The trace results timeline visualizes traces over the *lookback* period you selected for the search. 

Each circle represents a trace: The larger the circle, the more spans that trace includes. Click a circle to view the trace. A trace that includes fewer spans may indicate a short end-to-end transaction or may be missing information because the [instrumentation ](https://app.logz.io/#/distributed-tracing/tracing-instrumentation/) was incomplete or missing. 
![results timeline1](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/results-timeline1.png)

This view helps you find patterns and identify when the returned results happened.
![results timeline1](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/results-timeline2.png)
Hover over a trace to see the service and operation associated with the trace. 
![results timeline1](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/results-timeline3.png)

**Trace list**

In the trace list, each row represents a single trace and includes the service and operation names, the trace ID, the duration of the trace, and a timestamp of when it occurred.

The colors represent the different services involved in the trace. Each trace shows the number of spans it includes and how many of them were tagged as errors. The trace page shows you the spans that include the errors.

Sort trace results by the time they occured, by duration, or by the number of spans. 
![sort trace list](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/dist_trace-sort_traces.png)

### View a trace on the Trace page.
Click a trace from the trace results timeline or from the trace results list to view its trace page. 

By default, the trace opens in the timeline view. Select an option for different perspectives: 

![pick a trace view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace_view_pick-context.png)

**[What can I do in the Trace Timeline?](/docs/user-guide/distributed-tracing/navigating-tracing/trace-timeline)**

**[What can I do in the Trace Graph?](/docs/user-guide/distributed-tracing/navigating-tracing/trace-graph)**

**[What can I do in the Trace Statistics?](/docs/user-guide/distributed-tracing/navigating-tracing/trace-stats)**

**[What can I do in the Trace Spans Table?](/docs/user-guide/distributed-tracing/navigating-tracing/trace-spands-table)**

**[What can I do in the Trace Flamegraph?](/docs/user-guide/distributed-tracing/navigating-tracing/trace-flamegraph)**


### Find a specific trace. 
After you log in to your Distributed Tracing account, if you need to view a specific trace, you can use trace ID lookup. <!-- or upload a JSON file. -->

* To investigate specific incidents identified by a unique trace ID, use the search box to retrieve the trace data.  Make sure to tag your logs with the proper context to be able to locate the trace ID.
  If data sampling is configured to occur on the collector side, some traces may not be available in the Jaeger UI.  
  ![traceID lookup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/traceid.png)


### Compare traces
[Select traces for comparison](/docs/user-guide/distributed-tracing/navigating-tracing/compare-traces) and find out how they differ.

### View Topology diagrams for your system
Leverage the power of [topology diagrams](/docs/user-guide/distributed-tracing/navigating-tracing/topology) to obtain better observability for your system services and how they interact with each other.
