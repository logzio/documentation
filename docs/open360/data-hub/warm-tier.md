---
sidebar_position: 9
title: Warm Tier
description: How warm-tier data behaves in Logz.io Open 360 - searching it from Explore, using it on dashboards, and why results need an explicit Run Query.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, warm tier, data tiers, retention, storage, explore, dashboards, cost optimization, observability]
---

Warm tier keeps older logs searchable at a lower cost than your primary retention. This page covers how warm-tier data behaves when you use it; for what the tier is and how to set it up, see [Warm Tier](https://docs.logz.io/docs/user-guide/admin/data-tiers/warm-tier/).

The practical thing to know is that warm-tier searches are **deliberate rather than automatic**.

## Searching warm data in Explore

When your selected timeframe reaches into warm-tier data, [Explore](/docs/open360/explore/new-explore/) stops re-running the query as you change things. Instead you'll see:

> Current results are outdated — Click **Run Query** to apply new search

This is intentional. Warm-tier queries are heavier than hot-tier ones, so Explore doesn't fire one off every time you adjust a filter or a column. You compose the search you want, then run it.

If results look stale after you've changed something, that banner is why. Select **Run Query**.

## Warm data elsewhere

* **CSV export** — exports include warm-tier data when your timeframe covers it, so you don't need a separate route to get older logs out.
* **Dashboards** — panels can query warm-tier data where their datasource is configured for it.
* **Accounts** — warm tier is configured per account; see the account management docs for enabling and sizing it.

## Practical notes

* Narrow the timeframe before you narrow anything else. On warm data, a smaller window is the difference between a query you wait on and one you don't.
* Expect warm queries to take longer than hot ones. That's the trade you made for the cheaper storage, not a fault.
* Because the query doesn't auto-run, you can safely build up a complex search — filters, columns, group-by — and pay for it once.

## Related

* [Warm Tier setup](https://docs.logz.io/docs/user-guide/admin/data-tiers/warm-tier/)
* [Data tiers overview](https://docs.logz.io/docs/user-guide/admin/data-tiers/data-tiers-intro/)
* [Cost optimization](/docs/open360/data-hub/cost-optimization/)
