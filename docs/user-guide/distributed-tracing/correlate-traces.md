---
sidebar_position: 7
title: Correlate Logs and Traces
description: Connect your traces and logs into a unified dashboard with Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, trace dashboard, dashboard, logs, observability, distributed tracing]
---


## What can I do with my trace and span data in OpenSearch Dashboards?

Make the Jaeger-OpenSearch Dashboards connection: Harness the power of OpenSearch Dashboards and Jaeger for more context and insights with Logz.io Distributed Tracing when you correlate traces with logs in OpenSearch Dashboards.

We’ve put together examples of visualizations over distributed tracing telemetry that we think you’ll find helpful. 

## Telemetry correlation

If you’re using Logz.io for both Log Analytics and Distributed Tracing, you can correlate logs with their corresponding traces and spans.

To search for the logs related to a specific trace or the request transaction which generated the trace, you’ll need to enrich your logs with the trace ID and span ID. These log fields will let you drill down via a link that opens the specific trace in Jaeger from within OpenSearch Dashboards Discover, or within an OpenSearch Dashboards Dashboard.

Enriching logs with trace ID and span ID must be performed before or during the data collection process, and before sending the data to Logz.io.

<!--The enrichment process depends on the language and log type: You will have to [configure your deployment](/user-guide/distributed-tracing/deploying-components) to perform these actions _before_ the data is ingested into Logz.io, because retroactive correlation is not available.  -->

Contact <a class="intercom-launch" href="mailto:help@logz.io">the Support team for additional information on enriching your logs. </a>

### How to correlate Logs and Traces

1. Once the trace ID is part of the log attributes, open the OpenSearch Dashboards left menu, and select **Stack Management**.
2. To manage log index patterns, click **Index patterns** and go to your default index pattern settings.
    ![Go to index pattern settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/index-pattern-main.png)
3. Search for the trace ID field you want to correlate with your logs and select **Edit**. In this example, the field name is **traceID**.
    ![search for and edit the traceID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/logs-traceid-edit.png)
4. Change the **Format** to **URL** and enable **Open in a new tab**.
    ![Change format and open](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/logs-edit-traceid.png)
5. Using your main account, insert the following template in the **URL template** field of the Jaeger user interface (UI), add `{% raw %}{{value}}{% endraw %}` to **Label template** and **Save field**.
  
`{% raw %}https://app.logz.io/#/dashboard/jaeger/trace/{{value}}{% endraw %}`


Each traceID attribute functions as a drill down link that leads you to the correlated trace view in Jaeger. 

![traceID to Trace view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/log_trace5-new.png)

:::note
The Trace ID identifies logs related to traces, and it should be a part of the log. If you're using OpenTelemetry as instrumentation, you can get the Trace ID in context from the OTEL library and attach it to the log on creation. 
:::

### From traceID to OpenSearch Dashboards
You can jump from a trace in Jaeger to view it in OpenSearch Dashboards: 

![traceID lookup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/view-in-kibana-new.png)
