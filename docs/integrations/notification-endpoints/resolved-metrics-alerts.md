---
sidebar_position: 2
---

# Opsgenie notifications for resolved metrics alerts


Change your configuration within Opsgenie to receive notifications for resolved Logz.io metrics alerts.

 This feature is not available on free Opsgenie accounts.
 

### Define or modify a Logz.io integration in Opsgenie

To define a new integration or modify an existing Logz.io integration in Opsgenie:

1.  In Opsgenie, navigate to the **Teams** tab.

    ![Opsgenie teams](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/opsgenie_teams.png)

2.  Select your Logz.io metrics team.

    ![Opsgenie pick team](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/opsgenie_pick_team.png)

3.  Select **Integrations**  in the left menu.

    ![Opsgenie left menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/integrations_left_menu_panel.png)

4.  Select the existing Logz.io metrics integration you want to change, or click **Add integration**, then select and add a Logz.io metrics integration.

    ![Opsgenie integration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/existing_integration.png)

5.  Click **Advanced**.

    ![Opsgenie advanced](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/advanced.png)

    The fields for a metrics resolved alert are filled automatically.

6.  Scroll to the bottom of the page and **Save Integration**.

    ![Opsgenie save](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/save_integration.png)

When updating an existing integration, after clicking **Save integration**, you may be asked to confirm the switch to advanced mode: Click **Proceed**.

![Opsgenie confirm](https://dytvr9ot2sszz.cloudfront.net/logz-docs/opsgenie-resolved-metrics/opsgenie_confirm_advanced.png)

### Logz.io fields shared with Opsgenie
The following fields are sent to Opsgenie when an Opsgenie alert is triggered: 


|Field|Description|
|---|---|
|alert_alias | Unique identifier for a Logz.io alert. Used to close resolved alerts |
|alert_event_type  | Notifies Opsgenie to open or close an alert  |
|alert_details | Specifies account name and alert samples|
|alert_view_link |  Specifies the link to the dashboard where the alert was triggered|
|alert_title| Alert title|
|alert_description| Alert message|
|alert_severity| Alert severity|


###### Field value examples

```
"alert_title": "httpcode200test alert",
"alert_description": "http code is 200",
"alert_severity": "MEDIUM",
"alert_alias": "12345...",
"alert_event_type": "create",
"alert_details": {
	"Account": "Account Name" ,
	"alert_event_samples": "Sample 1 event out of 1"
},  
"alert_view_link": "https://app.logz.io/#/dashboard/metrics/d/..."
```