---
sidebar_position: 2
title: Sharing Links
description: Use shared tokens to share dashboards and visualizations
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, collaboration, sharing, log analysis, observability]
---

You can use shared tokens to share objects and visualizations with stakeholders who don't have access to your Logz.io account. This is particularly useful for communicating with clients outside your organization or with other teams internally.

### Configuring a shared token

To share objects, queries, and dashboards, you need to configure a shared token. Only account admins can create, delete, or manage tokens.


To create a token, navigate to [Settings > Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared), select **+ New shared token**, configure an expiration date, add any necessary filters, and save the token.


Learn more about the different [types of tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/tokens/).


### Choosing a Dashboard to Share

Open the dashboard or saved query you would like to share. When you share an item, you can decide whether to share it as a snapshot or a saved object.

* **Snapshot** - Converts the time selection to absolute dates, allowing recipients to view the exact data you're seeing. For example, if you send a snapshot for the last 24 hours, recipients will receive a dashboard with a fixed date range. Note that this link is short-lived based on your log retention policy; once the logs expire, the dashboard will no longer display data.

* **Saved object** - Shares the dashboard with a relative time selection, meaning the dashboard will load with its default time selection and filters. This option keeps the link updated automatically if changes are made to the dashboard, so recipients always see the latest version without needing a new link.

![Share your dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/dashboard-to-share.gif)


### How recipients will view shared dashboards

When you select **Share Public**, you'll choose the relevant [shared token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/shared-tokens/), and recipients will receive a link to the shared dashboard. The dashboard will appear without the top and side navigation bars and without the OpenSearch Dashboards time filtering options.

To **include the time frame** and search functionality in the shared link, add the following string to the end of the URL:

`&forceShowQueryBar=true`

For example, the original link:

`https://app.logz.io/?embed=true&shareToken=8d90-fbe1c84836d3#/dashboard/osd/discover/?=&_a=(columns%3A...15m%2Cto%3Anow))`

This is how users will see it:

![public share no time](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sharing-logs/share-public-link.png)


With the time frame string added:

`https://app.logz.io/?embed=true&shareToken=8d90-fbe1c84836d3#/dashboard/osd/discover/?=&_a=(columns%3A...15m%2Cto%3Anow))&forceShowQueryBar=true`

![public share with time](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sharing-logs/share-with-time.png)

### Testing your sharing permalink

To verify that your sharing link works as expected, you can open it in an incognito browser window.