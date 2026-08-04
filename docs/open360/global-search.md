---
sidebar_position: 9
title: Global Search
description: Find pages, saved searches, dashboards and alerts across Logz.io from one search box.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, global search, search, navigation, saved searches, dashboards, alerts, open 360, observability]
---

Global search finds things across your account from the search control in the top bar — pages, saved searches, dashboards and alerts, without you having to remember which section each lives in.

It's the fastest way to reach a dashboard whose exact name you've half-forgotten, and it beats navigating by menu once an account has more than a handful of saved objects.

## Open it with a shortcut

Press **Ctrl + K** to open global search from anywhere in the product.

Note that it's `Ctrl` on every platform, including macOS — `Cmd + K` won't open it.

The shortcut also works while you're inside the embedded open-source apps, such as OpenSearch Dashboards and Grafana, so you don't have to click out of them first to go somewhere else.

## What it searches

Results are grouped by where they came from:

| Group | What's in it |
|---|---|
| **Pages** | Product pages and settings screens — a way to jump straight to a page by name. |
| **Explore saved searches** | Saved searches from [Explore](/docs/open360/explore/new-explore/). |
| **Unified dashboards** | Your [Unified Dashboards](/docs/open360/dashboards/dashboards-hub/). |
| **OpenSearch Dashboards** | Saved objects from OpenSearch Dashboards. |
| **Logs alerts** | Log alert definitions. |
| **Metrics** | Metrics objects and alerts. |
| **Other** | Anything that doesn't fall into the groups above. |

Each group is labelled with its own icon, so you can tell a dashboard from a saved search from an alert at a glance rather than reading every result.

## Filtering results

Use the filter control to restrict the search to particular groups. When a filter is active it's indicated on the control, so you don't spend time wondering why an object you know exists isn't appearing.

That's worth knowing because it's the most common source of confusion: a filtered search that looks like a missing object.

## Notes

* Each source is searched independently with its own timeout, so a slow or unavailable source doesn't hold up the rest of the results. A group can therefore come back empty because it timed out rather than because it had no matches — searching again usually resolves it.
* Results respect your permissions and the account you're currently in. Switching accounts changes what global search can find.
