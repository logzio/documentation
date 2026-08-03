---
sidebar_position: 8
title: Import Dashboards
description: Import a dashboard into Logz.io Unified Dashboards, including converting Grafana and OpenSearch Dashboards definitions and mapping their datasources.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboards, unified dashboards, import, export, grafana, opensearch dashboards, migration, datasource mapping, library panels, observability]
---

You can import a dashboard definition into Unified Dashboards, either one exported from Logz.io or one from Grafana or OpenSearch Dashboards, which is converted on the way in.

The part that decides whether an import is useful or broken is **datasource mapping**: the source dashboard points at datasources that don't exist in your account, and you have to say what they correspond to here.

## Import a dashboard

From the Dashboards Hub, choose to import a dashboard, then:

1. **Dashboard JSON** — paste the definition.
2. **Dashboard Name** — filled in automatically once a valid dashboard is pasted, and editable.
3. **Folder** — select an existing folder or type a new name to create one. A folder is required.

If the JSON isn't a definition Logz.io can read, the import reports that it couldn't convert it rather than importing something half-formed.

## Map the datasources

For each datasource the source dashboard references, pick the target it should use in this account. Prometheus-style datasources map to a metrics datasource; Lucene datasources map to a **Logz.io account**, since that's what holds the logs.

Each mapping row shows which dashboards and panels use that datasource, so you can tell an important mapping from an incidental one.

When nothing suitable exists, the target list reports **No `<type>` datasource in account** and offers **Skip & import anyway**. That does what it says: the dashboard imports and the items relying on that datasource load broken until you fix them. It's a reasonable choice when you're importing a dashboard ahead of shipping the data, and a bad one if you're expecting it to work now.

## What conversion handles

Grafana and OpenSearch Dashboards definitions are converted to the Unified Dashboards format on import. Conversion covers panels, queries, variables and layout, and resolves **library panel** references by expanding them into the dashboard — a Grafana dashboard stores those as references rather than panel definitions, so they'd otherwise arrive empty. References that can't be resolved are reported instead of silently dropped.

Conversion is a translation between two products that don't have identical features, so treat an imported dashboard as a strong starting point rather than a finished result. Check it before you rely on it:

* Panels whose visualization has no direct equivalent.
* Queries using functions or transformations specific to the source product.
* Variables, especially ones whose values are populated from a datasource.
* Anything that looked right in the source because of a default that differs here.

## After importing

Open the dashboard and check each panel returns data. A panel with **No data** after an import is usually a datasource mapping or a query-syntax difference, not missing telemetry — the quickest test is to run the panel's query directly and see whether it returns anything at all.

Imported dashboards are editable and removable like any other, so you can fix rather than re-import.

## Related

* [Dashboards Hub](/docs/open360/dashboards/dashboards-hub/)
* [Panel Types](/docs/open360/dashboards/panel-types/) — what the converted panels map onto
* [Dashboards Configuration Guide](/docs/open360/dashboards/edit-dashboards/)
