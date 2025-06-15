---
id: uptime-data
title: Uptime
overview: Monitor website and API uptime with global coverage and forward alerts directly to Logz.io for unified observability.
product: ['metrics', 'logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/uptime-logo.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Uptime.com is a comprehensive website monitoring service that provides real-time alerts and detailed performance analytics for your web applications and APIs across 80+ probe servers in six continents. You can forward alert notifications from Uptime.com directly to your Logz.io account. This integration allows you to monitor and analyze uptime incidents alongside the rest of your observability data in Logz.io.

### Prerequisites

Before you begin, you'll need:

* An active Uptime.com account
* A name for the new Uptime.com integration
* A Logs shipping token from Logz.io
* A Metrics shipping token from Logz.io

### Integration functionality

Integration with Uptime.com allows for the following:

* Uptime.com alerts are sent to Logz.io as Logs
* Uptime.com response times are sent to Logz.io as Metrics

## Integration setup

1. Log in to your [Logz.io account](https://app.logz.io/#/login).

2. Navigate to [Settings > Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs), click Data shipping tokens, and copy the **Listener URL**. 

![Copy listener URL](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/data-shipping-listener-url.png)

3. Log in to your [Uptime.com account](https://uptime.com/accounts/login).

4. Navigate to [Notifications > Integrations](https://app.uptime.com/integrations/manage/) and click Add Integration.

5. Select Logz.io as the integration type and paste your Listener URL.

:::note
When creating a new Logz.io integration, the Listener URL field is pre-filled with the default value listener.logz.io. If the default URL is not shown, enter the correct URL manually.
:::

![Enter listener URL](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/uptime-enter-listener-url.png)

6. Go back to Logz.io [Settings > Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs), and click Data shipping tokens. Copy both the **Log** and **Metrics** shipping tokens.

:::note
If you do not have a Metrics token in Logz.io, navigate to [Settings > Manage Accounts](https://app.logz.io/#/dashboard/settings/manage-accounts?product=Logs) and create a Metrics account. For further assistance, contact [Logz.io support team](mailto:help@logz.io).
:::

![data shipping token in Logz](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/shipping-tokens-logz.png)

7. In Uptime.com, paste the shipping tokens into the appropriate fields:

![data shipping token](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/data-shipping-tokens.png)

8. Save the new Uptime.com integration. It may take a few minutes for data to appear in Logz.io.

Once set up, response time metrics appear as `uptime_response_time` in Logz.io, including labels for checks and locations.

![metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/metrics.png)

## Testing the integration

Test your integration with one of the following two options:

* In Uptime.com, force the check assigned to your integration to fail by altering it (for example, by misspelling the domain in an HTTPS check).
* Navigate to [Notifications > Contacts](https://app.uptime.com/contact-groups), then click Actions > Test to send a test alert to the Contact.

## Managing Uptime.com contacts

### Assign the integration to an existing contact

To add your integration to an existing contact in Uptime.com, click on or type the name of the contact into the **Assign to Contacts** field within the integration setup screen.

![assign a contact](https://dytvr9ot2sszz.cloudfront.net/logz-docs/uptime/image7.png)

## Create a new contact

Adding a dedicated or a new contact cannot be done within the integrations screen.

To add a new contact, navigate to [Notifications > Contacts](https://app.uptime.com/contact-groups). You can create a **New Contact** or add the integration to an existing contact. In both cases, select the Logz.io option from the Integrations dropdown.


## Assign Integration Contact to a Check

To receive alerts, the contact linked to your Logz.io integration must be assigned to a check.

If the contact is already assigned to one or more checks, no action is needed.

If not, open the **Check’s Edit** screen and add the contact to the **Contacts** field. This ensures real-time alert notifications are sent during downtime events.