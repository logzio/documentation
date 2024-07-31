---
sidebar_position: 6
title: Configuring Grafana Datasource for Logz.io Metrics
description: This guide provides step-by-step instructions for configuring Grafana to query Prometheus metrics stored in Logz.io. If you have your own Grafana instance and want to use it to visualize metrics from Logz.io, follow the steps below.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, Prometheus, monitoring, dashboard, observability, logz.io]
---

### Request Metric API Endpoint Enablement

To enable Metric API access for your accounts, contact your account manager or the [Logz.io support team](mailto:help@logz.io) with your **Metric Account ID**.

### Create API Token for the Metrics Account

1. **Create an API Token:**  
   Generate an [API token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/) from your Main Log Management account or Log Management sub-account. You will need this token as the `X-API-TOKEN` header in the next step.

2. **Generate a Metric Account Token:**  
   Use the [Create a sub-account API token](https://api-docs.logz.io/docs/logz/create-api-token-request/) endpoint to generate a new token for the metrics account. Include the **Metrics Account ID** in the request body.

### Configure Logz.io Metric Endpoint as a Local Grafana Datasource

To configure the Logz.io metric endpoint as a Prometheus datasource in your Grafana instance:

1. **Navigate to Data Source Configuration:**  
   Add a new datasource of type **Prometheus**.

2. **Configure the Datasource:**
   - **URL:** Set the URL to `https://api.logz.io/v1/metrics/prometheus` (adjust according to your region).
   - **Access:** Select **Server (default)** as the access type.
   - **Custom Headers:** Add a custom header named `X-API-TOKEN` and set its value to the Metric Account API token generated in the previous step.

### Query and Create Dashboards

Once the datasource is configured, you can start creating queries and dashboards.

To use the Prometheus Query API, utilize the endpoints (according to your region) provided under `{LOGZIO_API_URL}/v1/metrics/prometheus`. The supported query APIs are:

- **[Instant Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#instant-queries):**  
  Supports both GET and POST requests to `{LOGZIO_API_URL}/v1/metrics/prometheus/api/v1/query`.

- **[Range Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries):**  
  Supports both GET and POST requests to `{LOGZIO_API_URL}/v1/metrics/prometheus/api/v1/query_range`.

- **[Series Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#finding-series-by-label-matchers):**  
  Supports both GET and POST requests to `{LOGZIO_API_URL}/v1/metrics/prometheus/api/v1/series`.

- **[Getting Label Names](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names):**  
  Supports both GET and POST requests to `{LOGZIO_API_URL}/v1/metrics/prometheus/api/v1/labels`.

- **[Getting Label Values](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names):**  
  Supports GET requests to `{LOGZIO_API_URL}/v1/metrics/prometheus/api/v1/label/<label_name>/values`.
