---
id: Control-plane
title: Control Plane
overview: Control Plane is a hybrid platform that integrates multiple cloud services, such as AWS, GCP, and Azure, providing a unified and flexible environment for developers to build and manage backend applications and services across various public and private clouds.
product: ['logs']
os: ['windows', 'linux']
filters: ['Containers']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/control-plane.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Logs

Control Plane is a hybrid platform that integrates multiple cloud services, such as AWS, GCP, and Azure, providing a unified and flexible environment for developers to build and manage backend applications and services across various public and private clouds.

Deploy this integration to ship all `Org` logs from your Control Plane account to Logz.io.

**Before you begin, you'll need**:

* Control Plane account



### Store the Logz.io secret as an Opaque Secret

1. Log in to [Control Plane Console UI](https://console.cpln.io/).
2. Navigate to **Secrets**.
3. Create a new secret.
4. Give the secret a name.
5. Select `Opaque` from the **Secret Type list**.
6. Paste `<<LOG-SHIPPING-TOKEN>>` into the content text box. This is the [log shipping token of your Logz.io account](../../user-guide/admin/authentication-tokens/log-shipping-tokens/).
7. Click **Create**.



### Enable Control Plane logging

#### Using the UI Console

1. Open the [Control Plane Console UI](https://console.cpln.io/).
2. Click on **Org** in the left menu.
3. Click **External Logs** in the middle context menu.
4. Select `Logz.io` and fill out the required fields.
5. Select the Opaque secret created to authenticate to Logz.io.
6. Click **Save**.

#### Using the CLI

1. Prepare the YAML manifest:

```yaml
kind: org
name: <<ORG_NAME>>
spec:
  logging:
    logzio:
      credentials: //secret/<<OPAQUE-SECRET-NAME>>
      listenerHost: <<LISTENER-HOST>>
```

Replace `<<ORG_NAME>>` with your organization's name.

Replace `<<OPAQUE-SECRET-NAME>>` with the name of the opaque secret created in the first step of these instructions.

{@include: ../../_include/log-shipping/listener-var.html}

2. Save the file, for example, `logging-config.yaml`.

3. Open your command line interface (CLI) and navigate to the directory where the `logging-config.yaml` file is saved.

4. Execute the following command, replacing `ORG_NAME` with your organization's name:

```shell
cpln org patch ORG_NAME -f logging-config.yaml
```


#### Check Logz.io for your logs

Spin up your Docker containers if you haven't done so already. Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).
