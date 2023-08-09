---
id: Alcide-kAudit
title: Alcide kAudit
overview: Alcide kAudit is a security service for monitoring Kubernetes audit logs, and easily identifying abnormal administrative activity and compromised Kubernetes resources.
product: ['logs','siem']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/alcide.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

Alcide kAudit is a security service for monitoring Kubernetes audit logs, and easily identifying abnormal administrative activity and compromised Kubernetes resources.

You can review Alcide kAudit findings in your Logz.io security account, including a pre-configured [Alcide dashboard in Logz.io](https://app.logz.io/#/dashboard/security/research/dashboards?) to get you started.


You can configure an Alcide kAudit integration that uses the Logz.io HTTPS API. The integration can be configured from the kAudit app or kAudit Kubernetes ConfigMap.

Each finding type requires a separate configuration. If you plan to send all kAudit data to Logz.io, you will need to configure 3 HTTPS API integrations, one per finding type.

For more information on exporting kAudit findings, see the official [Alcide docs](https://alcide.atlassian.net/wiki/spaces/PUB/pages/1466728736/Exporting+kAudit+Findings).

**Before you begin, you'll need**:

* Access to [Alcide kAudit](https://github.com/alcideio/kaudit) platform
* A shipping token and listener host information for your [Logz.io Operations account](https://app.logz.io/)


### Configure an Alcide kAudit integration for detections

First, log into your Alcide kAudit console.

1. Select **Integrations** from the left menu.
2. Select **Add New Integration** and select the **HTTPS API** integration from the dropdown menu.
3. Fill in the new integration form:
    1. **Name** - Provide a name for the new HTTPS API integration. For example: Logz.io.
    2. **URL** - Paste the Logz.io webhook URL. {@include: ../_include/log-shipping/listener-var.html}


        ```
        https://<<LISTENER-HOST>>:8071
        ```

3. **Token** - Paste in the log shipping token of the account you want to ship to.

4. **Alert type** - Select **Detections** from the dropdown list.

    Select all available sub-selections:

    * **Entity Type** - select all types: **Cluster**, **User**, **Resource**
    * **Category** - select all categories: **Incident** and **Anomaly**

![Set up an Alcide kAudit integration with Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/security-integrations/alcide-integration.png)

### Configure an Alcide kAudit integration for audit violations

Repeat the above steps, only this time select **Alert type** - **Audit Violations**.

In the field **Report**, select the **Details** option.
Leave all other default configurations.

### Configure an Alcide kAudit integration for audit activity

Repeat the above steps, only this time select **Alert type** - **Audit Activity**.

Leave the default configurations. No sub-selections are required.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search or filter for Alcide logs, under `type:alcide-kaudit`.

If you still don't see your logs, see [log shipping troubleshooting](/user-guide/log-shipping/log-shipping-troubleshooting.html).
