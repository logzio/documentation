---
sidebar_position: 2


---


# What can I do in the Trace Graph?


The trace graph shows you the sequence of requests, with spans grouped into node blocks that include parent and child spans. 

You can display the graph color-coded by service, duration time, or by parent span self time. 
Hover over a span in the graph to see its details. 

![trace graph key](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace_graph-key.png)

- Click <i class="fas fa-question-circle"></i> to view the graph legend. Each box includes the following information: 
  - Total time shows the duration of parent and child spans and presents the span time as a percentage of total trace duration
  - Selftime shows the duration for the parent span and presents the parent span selftime as a percentage of span total time
  - Count/Error shows the total call count vs. the total error count

- Click the options to see the trace graph colored by:
    - Service - default view
    - Total time - Total duration of the span, including the time spent waiting on child spans
    - Self time - Trace duration of the span, not including the time spent waiting on child spans

Comparing the time and selftime for a span may provide insights into latency issues for child spans.

The default for Trace Graph mode is the Service view, which displays the services in the trace. ![service graph - service](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace_graph1.png)

You can: 

* Search for text in any view.
<video autoplay loop>
  <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/srch-trace-grph2.mp4" type="video/mp4" />
</video>

* Select the Time view to highlight the longest durations for parent spans. This view includes the time spent waiting for child spans. ![service graph total time](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace_graph3-time.png)

* Select the Selftime view to highlight the longest times for parent spans when they are not waiting on child spans. 
**Example**: A 10ms span that includes two 4ms non-overlapping children will have a self-time = 10ms - (2 x 4ms) = 2ms

![Service graph self time](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace_graph4-self-time.png)
 
The darker the highlight color in the Time and Selftime views, the longer the span duration. 
