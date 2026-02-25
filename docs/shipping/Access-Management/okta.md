---
id: Okta
title: Okta
overview: Okta is an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/okta.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Okta is an enterprise-grade identity management service built for the cloud, and it integrates with both cloud and on-premises applications.

This guide explains how to forward Okta logs to Logz.io: via **Event Hooks**.

## Okta Event Hook Integration

:::note
[Project's GitHub repo](https://github.com/logzio/okta-events-hook)
:::

This section walks you through setting up an Okta Event Hook that sends selected System Log events to Logz.io. The integration uses custom headers (`logzio_token`, `logzio_region`) for authentication and region routing.

### Prerequisites

- **Okta Admin Access** – To configure event hooks
- **Logz.io shipping token** (32 characters) 
- **Logz.io region** – e.g., `us`, `au`, `eu`, `uk`, `ca`

### Configure Okta Event Hook for Logz.io

**1. Create the Event Hook in Okta**

Sign in to the Okta Admin Console and navigate to **Workflow → Event Hooks**.

Click **Create Event Hook** and enter the following:

* Set the **Name** to something like `LogzIoEventHook`
* Use this **Endpoint URL**:
   ```
   https://okta.listener-logz.io
   ```

Next, add **Authentication & Headers**:

* `logzio_token`: your Logz.io shipping token
* `logzio_region`: your Logz.io region (`us`, `au`, `eu`, `ca`, `uk`)

Choose one or more **events to subscribe** to, e.g., `user.lifecycle.deactivate` or `user.session.start`.

**Save** the Events Hook. Okta will send a one-time GET request with an `x-okta-verification-challenge` header to verify the endpoint and ownership.

**2. Preview & Test the Hook**

Use Okta's **Preview** feature to simulate an event and inspect the payload.

**Trigger** an actual event in Okta and confirm it appears in your Logz.io dashboard.

