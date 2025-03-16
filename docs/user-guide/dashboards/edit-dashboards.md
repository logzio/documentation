---
sidebar_position: 2
title: Manage and configure Unified Dashboards
description: Learn how to utilize Unified Dashboards to monitor your system.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, dashboards, hub, unified dashboards, visualize, visualizations]
toc_max_heading_level: 2
---

Unified Dashboards provide an easy tool for visualizing observable data. Customize layouts, panels, and data sources to create tailored views that enhance monitoring and troubleshooting.


## Create a new dashboard

To create a dashboard, go to **Dashboards Hub**, click **New Dashboard**, and give it a name.

Click **Edit** and add a **Panel Group** to organize panels and improve clarity. This step is required to start adding panels. Then, click **Panel** and configure the following:

* Name – Define a title for the panel.
* Description (optional) – Add context about the panel’s purpose or the data it visualizes.
* Group – Assign the panel to an existing group.
* Type – Choose a visualization format (e.g., Time Series Chart, Gauge, Table).

Next, define the data source and query. Choose **Prometheus Time Series Query** for metrics data or **Logs Lucene Query** for log data. Each query type has its own data source, which you can select based on your needs.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/edit-panel-top.png" alt="panel-top" width="1000"/>

## Edit Panels

### Prometheus Time Series Query

For metric-based visualizations, select **Prometheus Time Series Query** as the query type, and choose a relevant data source based on the metric data you want to use.

For example, to count the number of machines reporting system info for the `ec2` job, use the Jenkins Master Metrics (Prometheus) as the data source, and the following PromQL query:

`count by (machine) (node_uname_info{job="ec2"})`

Once entered, a preview of the visualization appears in the preview section. You can also add a legend for tooltips and labels using `{{label_name}}`, by entering them in the Legend section.

Once you're happy with your visualization, click **Add** to insert the panel into the chosen group.

You can add multiple PromQL expressions per group by clicking the **Add Query** button.

:::note
Make sure your PromQL expression matches the selected visualization type.
:::

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/edit-panel-bottom.png" alt="panel-bottom" width="1000"/>


### Logs Lucene Query

For log-based visualizations, select **Logs Lucene Query** as the query type, and choose the relevant account according to the data you want to use. As you type your Lucene expression, the query builder suggests fields, values, and operators.

For example, to view all logs with `ERROR` log level, choose the relevant account and enter the following Lucene query:

`loglevel:"ERROR"`

You can also use the Group By option to group results. For example, group results by `__overSizedField__.error.code`.

Once you're happy with your visualization, click **Add** to insert the panel into the chosen group.

You can add multiple Lucene expressions per group by clicking the **Add Query** button.

:::note
Make sure your Lucene expression matches the selected visualization type.
:::

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/second-panel-bottom.png" alt="log-panel-bottom" width="1000"/>

### Settings tab

Use the Settings tab to customize panel appearance:

* Legend – Adjust position and display mode.
* Y-Axis – Show/hide values and adjust formatting.
* Thresholds – Define alerting thresholds.
* Visual Settings – Modify line width, opacity, and other styles.
* Query Settings – Change colors and additional parameters as needed.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/settings-tab.png" alt="settings-tab" width="1000"/>


### Adding Links

The Links tab allows you to attach external or internal resources to your panel’s header.

Click the **+** icon and enter a URL. You can add a name or a tooltip to provide added information, render the variable or open it in a new tab. Click the **+** icon again to add multiple links to your panel.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/links-tab.png" alt="links-tab" width="1000"/>

If multiple links are added, they appear as a dropdown when clicking the link icon.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/dropdown-panel.png" alt="links-dropdown-tab" width="1000"/>


### View Panel JSON

The JSON tab displays the panel's raw JSON configuration, useful for:

* Understanding panel settings and structure.
* Sharing panel details with others.
* Troubleshooting queries, panel options, or data sources.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/json-tab.png" alt="json-tab" width="1000"/>


## View and manage your dashboard

Your dashboards display data within a selected time frame. To adjust the view, click the calendar icon and choose a predefined range or set a custom time frame. You can manually refresh the dashboard or temporarily turn off auto-refresh for up to one minute.

Panel groups can be expanded or collapsed to improve readability and organization. Click the arrow icon next to a group name to collapse it, hiding its panels while keeping it accessible. Click it again to expand the group and view all panels. This helps you focus on specific sections without cluttering the dashboard.

To export your dashboard, click the download icon to save it as a JSON or YAML file, or click the brackets **{}** icon to view its JSON configuration.

To edit the dashboard, click **Edit** at the top of the page. You can add new Panel Groups or Panels and modify existing ones using the pencil icon. Each panel’s query and data can be adjusted, and you can expand it for a larger view using the toggle mode icon. To rearrange panel groups, use the arrow icons, or remove them if no longer needed with the trash bin icon.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/unified-dashboards/view-settings-edit.png" alt="view-settings-edit" width="1000"/>
