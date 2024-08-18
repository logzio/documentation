---
sidebar_position: 5
---

# Configure an Endpoint for Microsoft Teams

:::warning note
Starting August 15th, 2024, new Microsoft Teams endpoints must be configured using the **Workflows** app. [Read more on Microsoft's blog](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/).
:::



Integrate with Microsoft Teams using a Logz.io custom webhook to receive Logz.io notifications in your Microsoft Teams workspace.


## Adding your Microsoft Teams endpoint

 
### 1. Allow firewall access

See [Custom Endpoints](https://docs.logz.io/docs/user-guide/integrations/notification-endpoints/custom-endpoints/) for general instructions on setting up firewall access for Logz.io notifications.

This may include whitelisting Logz.io IPs and/or creating a verification token.



### 2. Add the endpoint

1. To add a new custom endpoint, click **Add endpoint**.
2. **Type**: Select the option **Custom**.
3. **URL**: See [MS docs](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook) for instructions on creating the webhook URL.
4. **Method**: Select the **POST** method. 
5. **Headers**: Add `Content-Type=application/json`.
6. **Payload**: Add your payload message. See the next step for details.

![Configure a custom endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/ms-teams-endpoint.png)


### 3. Add your payload

Microsoft Teams requires that you send either the `text` or `summary` properties. [Learn more from Microsoft.](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#office-365-connector-card)


#### Example payload

To use this example in your own endpoint, copy the payload. Note that double-brackets indicate parameters that will be auto-populated by Logz.io.

<!--{% raw %}-->

```
{
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "themeColor": "0072C6",
    "title": "{{alert_severity}}: {{alert_title}}",
    "summary": "{{alert_description}}",
    "text": "{{alert_samples}}",
    "potentialAction": [
        {
            "@type": "OpenUri",
            "name": "View in OpenSearch Dashboards",
            "targets": [
                {
                    "os": "default",
                    "uri": "{{alert_app_url}}#/view-triggered-alert?from={{alert_timeframe_start_epoch_millis}}&to={{alert_timeframe_end_epoch_millis}}&definitionId={{alert_definition_id}}&switchToAccountId={{account_id}}"
                }
            ]
        }
    ]
}
```
<!-- {% endraw %}-->


### 4. Test the endpoint (_Optional_)

Click **Run the test** to test your endpoint. Logz.io shows if the message was successfully sent.

Check that the message arrived at the target endpoint.

### 5. Save the endpoint

**Save** your endpoint.
