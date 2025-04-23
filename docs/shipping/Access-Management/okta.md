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

This guide explains two ways to forward Okta logs to Logz.io: via **Event Hooks** or a **legacy Docker-based** solution.

## Okta Event Hook Integration

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

## Legacy Docker-Based Solution

If you prefer using Docker to ship Okta logs, follow this guide. This method collects and forwards logs to Logz.io using Logstash.

You can send logs from multiple Okta tenants and domains.

:::note
If you want to ship from multiple Okta tenants over the same Docker, you'll need to use the latest configuration using a tenants-credentials.yml file. Otherwise, you can continue using the previous configuration without a tenants-credentials.yml.
:::

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-okta/)
:::

### Prerequisites

* Okta administrator privileges
* Port 5050 available - Logz.io Logstash endpoint receives logs from port 5050.

 

**1. Get Okta API Token and Domain**

Navigate to **API → Tokens** in the Okta developer console. Generate a token and save it.

Next, go to **Authorization Servers** and copy your Okta domain from the **Issuer URI** column (e.g., `dev-123456.okta.com`).

**2. Create `tenants-credentials.yml`**

Run the following command as root 

```
mkdir /etc/logzio-okta && touch /etc/logzio-okta/tenants-credentials.yml
```

Open the file in your text editor, and insert your tenants credentials into the YAML file in the following format:

```yml
tenants_credentials:
    - okta_api_key: <<OKTA-API-KEY>>
      okta_domain: <<OKTA-DOMAIN>>
```

Add multiple tenants by repeating the format above. For example:

```yml
tenants_credentials:
    - okta_api_key: 123456a
      okta_domain: logzio-dev-123.okta.com
    - okta_api_key: 123456b
      okta_domain: logzio-dev-123.okta.com
    - okta_api_key: 123456c
      okta_domain: logzio-dev-123.oktapreview.com
```

This shipper supports **up to 50 tenants**.

| Parameter | Description |
|---|---|
| OKTA_API_KEY (Required) | The Okta API key copied in step 1. |
| OKTA_DOMAIN (Required) | The Okta domain copied in step 1. It is found under the **Issuer URI column** in your Okta developer console.    Supports these [Okta domains](https://developer.okta.com/docs/guides/find-your-domain/findorg/):    example.oktapreview.com, example.okta.com, example.okta-emea.com |


:::tip
YAML files are sensitive to spaces and tabs. It's a good idea to run your code through a YAML validator to make sure that its structure is correct. It's a good idea to run it through a YAML validator to rule out indentation errors, clean up extra characters, and check that it is valid. ([Yamllint.com](http://www.yamllint.com/) is a great choice.)
:::
 
Save the file in your working directory. That's the same one you're running the Docker from.


**3. Pull Docker image**

Download the logzio/logzio-okta image:

```shell
docker pull logzio/logzio-okta
```

**4. Run the Docker image**

Replace the placeholders in the code sample below before running it:

```shell
docker run \
--restart always \
--name Okta \
--env LOGZIO_TOKEN=<<LOG-SHIPPING-TOKEN>> \
--env LOGZIO_LISTENER_HOST=<<LISTENER-HOST>> \
-v /etc/logzio-okta/tenants-credentials.yml:/usr/share/logstash/tenants-credentials.yml \
-t logzio/logzio-okta 
```

For macOS users: To resolve issues with mounting files from the root directory, add `/etc/logzio-okta` to your Docker File Sharing settings.

You can follow [this guide](https://medium.com/effy-tech/fixing-the-var-folders-error-in-docker-for-mac-v2-2-3-2a40e776132d) to update the setting via Docker Desktop or by manually editing your Docker configuration file.

For more details on root directory mounting, see [Docker's documentation](https://docs.docker.com/docker-for-mac/osxfs/#namespaces).


| Parameter | Description |
|---|---|
| LOGZIO_TOKEN (Required) | {@include: ../../_include/log-shipping/log-shipping-token.html} |
| LOGZIO_LISTENER_HOST (Required) | {@include: ../../_include/log-shipping/listener-var.html}  |
| LOG_LEVEL (Optional)                                      | Logstash Log Level (deafult: `info`)                                                                                                      |

**5. Confirm logs in Logz.io**

Check [Explore](https://app.logz.io/#/dashboard/explore) to verify incoming logs.

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).