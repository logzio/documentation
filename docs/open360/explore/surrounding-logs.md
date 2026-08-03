---
sidebar_position: 12
title: Surrounding Logs
description: See what happened immediately before and after a log in Logz.io Explore, loading more context in either direction as you need it.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, explore, surrounding logs, context, log context, troubleshooting, investigation, observability]
---

A single log line rarely explains itself. **Surrounding Logs** takes one log and shows you what happened either side of it, so you can read the sequence instead of the snapshot.

Use it the moment a search result looks relevant but not sufficient — an error with no cause, a timeout with no origin, a success that shouldn't have happened.

<img src="/img/open360/surrounding-logs.png" alt="Surrounding logs view with the anchor log and context either side" width="900"/>

## Open the context view

From a log in Explore, open **Surrounding logs**. The view opens with the log you selected anchored in place and **25 logs either side** of it.

Your query, selected accounts, and table columns carry over, so the context is shown the way you were already reading logs.

## Load more context

The bars above and below the results extend the window:

* **Newer logs** — load more from after the anchor.
* **Older logs** — load more from before it.

Each load fetches up to **250** logs, and you can build up to **1,000** in a direction. Start small: the answer is usually within a few lines, and a smaller window is far easier to read than a thousand-row wall.

## A note on filters

Surrounding Logs keeps your query applied. That's usually what you want — context from the same service or component — but it also means a narrow query can hide the very line that explains the problem.

If the context looks suspiciously clean, clear the query and reload. Widening from "logs matching my search around this moment" to "everything around this moment" is often what reveals the cause, especially when the cause came from a different service than the symptom.

## Related

* [Intro to Explore](/docs/open360/explore/new-explore/)
* [Trace View](/docs/open360/explore/trace-view/) — when the log carries a trace ID, the trace often explains more than the neighbouring logs
* [Live Tail](/docs/open360/explore/live-tail/)
