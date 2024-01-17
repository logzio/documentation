---
sidebar_position: 3
title: Add Drilldown Links
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Add drilldown links in Cloud SIEM
keywords: [SIEM, drilldown, drilldown links, Security information]
---

A drilldown link is a redirect link that takes users directly from an informative log field to another dashboard, already filtered by the selected field.

When investigating a security incident through the logs, drilldown links make it possible to simply click on an informative field (such as an IP address, username, or hostname) to open a related dashboard, filtered by the selected field, and review the event in a wider context.

Adding Drilldown links to your security account will help you speed up and streamline investigations and structure your team's workflows and processes.

Drilldown links are configurable via your security account. To open the **Drilldown settings**,
navigate to [**SIEM > Drilldowns**](https://app.logz.io/#/dashboard/settings/drilldowns).

![Security drilldown links](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/drilldown-links-jan.png)

### Add a drilldown link

1. Click **+ Add drilldown**.
2. Select the **Source field** from the dropdown list. This will be your drilldown starting point, and the field will become a hyperlink.
3. Select a **Dashboard** from the dropdown list. This is the target destination of the drilldown link. When users click the log field in a dashboard or OpenSearch Dashboards, it will direct them to this dashboard.
4. Click **Save drilldown** to confirm the new drilldown link.


![Add drilldown](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/create-drilldown-jan.png)

### Edit or delete a drilldown link

* To edit a drilldown link, hover over the drilldown, click **Edit**, make your changes, and click **Save** to confirm the changes.

* To delete a drilldown link, hover over the drilldown and click **Delete** to delete it. You'll be asked to confirm the deletion.


<h3 id="#example">Example</h3>

Your Logz.io Security account comes with a few drilldown links preconfigured by default.

For example, IP addresses in the [Threat Overview dashboard](https://app.logz.io/#/dashboard/security/threats/overview) function as drilldown links that direct you to the **IP Investigation** dashboard in your account. This helps to speed up the investigation and to structure your team's workflow.

Drilldown links maintain context, such that any filters and time range settings already applied, will be kept.

![IP addresses function as drilldown links](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/drilldown-example.png)
