---
sidebar_position: 1
title: Distributed Tracing Troubleshooting
description: Common questions and use cases when setting up your Logz.io tracing account
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, trace dashboard, dashboard, troubleshoot, logs, observability, distributed tracing]
---


Setting up a Distributed Tracing account might require some additional help. In this doc, we'll walk through troubleshooting some common issues. 



## Distributed Tracing is not showing data in Service/Operations dropdown lists

You’ve logged into your Distributed Tracing search screen, and you can’t see any data in Service and Operation lists.

![No service or operation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/no-service-or-operation.png)

Several scenarios can cause this:


### Account token misconfiguration in OTEL collector

Distributed Tracing spans are sent to Logz.io and indexed in a Distributed Tracing account the same way as logs. If the spans are sent as expected, you should be able to see them in Open Search Dashboards, the same way you search for logs.

To troubleshoot this issue, you first need to verify that the Tracing account has indexed the data.

Navigate to [Open Search Dashboards](https://app.logz.io/#/dashboard/osd) > Choose the **Tracing account you’re trying to troubleshoot**, and hit the Refresh button on the right side of the screen.

![Logs showing tracing data](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace-and-refresh-in-logs.png)

If there are no results and you can't see any logs, you’ll need to ensure the correct token is used to send the spans.

Head over to **[Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) > [Data shipping tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs) > [Tracing](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing)**. Copy the token of the Tracing account you’re troubleshooting, re-configure your collector or make sure it matches, and restart the collector.

Head back to **[Open Search Dashboards](https://app.logz.io/#/dashboard/osd)** and check whether you can now see logs in the Tracing account you're trying to troubleshoot.

If you still can't see any logs, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.

Once your logs appear in Open Search Dashboards, navigate to **Distributed Tracing > [Search](https://app.logz.io/#/dashboard/jaeger/)**.

If there's no data in the Service/Operation dropdown lists, continue to the next step:

### Lost Service and Operation data

Service and Operation data reach Logz.io separately from your spans. That's why you might see data in your Tracing account in Open Search Dashboards (as explained in the previous step), but you won't be able to see data in your Service and Operation lists.

**Restart your collector** to recover this lost data and make sure spans are flowing into your account.

After restarting the collector, navigate back to **Distributed Tracing > [Search](https://app.logz.io/#/dashboard/jaeger/)** and verify that you can see the data in both the Service and Operation dropdown lists.

If you still can't see data in the Service and Operation lists, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.

### Distributed Tracing Search screen not showing search results

When you're trying to search any combination of parameters in **[Distributed Tracing > Search](https://app.logz.io/#/dashboard/jaeger/),** and the search screen does not yield any results, follow these steps to resolve the issue:

**1.** Make sure only **Service**, **Loopback**, and **Limit Results** fields have values, while Tags, Max Duration, and Min Duration are empty.
  ![Service field value](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/just-these-fields-jaeger.png)

**2.** If you still can't see any results, navigate to **[Open Search Dashboards](https://app.logz.io/#/dashboard/osd)** > Choose the **Tracing account you’re trying to troubleshoot**, and check whether you can see logs in the Tracing account you're trying to troubleshoot.

**3.** If you can't see any logs, follow the previous steps to check the token configuration. 

**4.** If you can see logs, make sure their indicated type is jaegerSpan:

  ![Trace logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/trace-fields-log.png)

**5.** If you still can’t see any search results after following all of these steps, contact [Logz.io's Support team](mailto:help@logz.io) for additional help.



## Service Performance Monitoring dashboard showing no data

Your Service Performance Monitoring dashboard shows a **No Data** message across all elements in your dashboard.

![Query of Metrics account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/spm-no-data-showing.png)

This occurs when the Metrics account attached to the Tracing data is not receiving any data. It’s possible you have not completed the collector configuration changes required to operate your Service Performance Monitoring dashboard.

Let's verify this. Navigate to **[Metrics](https://app-uk.logz.io/#/dashboard/metrics) > [Explore](https://app.logz.io/#/dashboard/metrics/explore)** and choose the relevant data source connected to your Service Performance Monitoring dashboard from the dropdown list.

To confirm that the data is available and accessible, type `calls_total` and run the query.

![Query of calls total](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/calls-total-tracing.png)

If there are no results, go through the **[Set up your Service Performance Monitoring dashboard](https://docs.logz.io/docs/user-guide/distributed-tracing/setup-spm/)** guide again to confirm that  the collector is properly configured to send the data.

If you can see the query's results, but the data is not visible in your Service Performance Monitoring dashboard, contact the [Logz.io Support team](mailto:help@logz.io) for additional help.