---
sidebar_position: 2
---

# Create an integration with StatusPage



Use this StatusPage integration to notify StatusPage when there are service issues that impact your platform. 

To implement the integration, you will:

1. Create a pair of alerts: 
   + An alert configured with a condition to trigger a StatusPage update
   + An alert configured with the opposite trigger condition, to update the StatusPage when the conditions return to normal

2. Create a pair of custom endpoints to update a specific component, then attach each endpoint to the relevant alert:
   + An endpoint to update the component with the triggered status 
   + An endpoint to update the component with the status **_Operational_** 




#### Creating a custom endpoint to update StatusPage components

 

##### Look up your `page_id`
1. Log in to your StatusPage account.
2. Click your profile picture.
3. Select **API info** from the menu.
4. Find your `page_id`.

##### Look up your `component_id`
1. Log in to your StatusPage account.
2. In the left menu, click  `Components` and select the component you want to update.
3. Scroll to the bottom to see your **Component API ID**.

##### Look up your StatusPage API key
1. Log in to your StatusPage account.
2. Click your profile picture.
3. Select **API info** from the menu.
4. Find your account `API key`.

##### Create the endpoint
The endpoint makes use of the StatusPage API, which can be found [here](https://developer.statuspage.io/#operation/putPagesPageIdComponentsComponentId).


1. To add a new custom endpoint, click **Add endpoint**.
1. **Type**: Select the option **Custom**.
1. **URL**: Use the following StatusPage API URL and replace the placeholder values in the URL for `[page_id]` and `[component_id]` with the values that you looked up in the previous steps: **https://api.statuspage.io/v1/pages/`[page_id]`/components/`[component_id]`**. 
1. **Method**: Select the **PUT** method. 
1. **Headers**: Add `Authorization=OAuth {[API key]}` and replace the `[API key]` placeholder with the StatusPage API key you determined in step 3.
1. **Body**: Add your body message. See the next step for details.

![StatusPage custom endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/statuspage-custom-endpoint.png) 

##### Add your message

Use the following code and replace the placeholder with the relevant status parameter.

###### Message body structure

```yml
{
    "component": {
        "status": "{placeholder value}"  # replace with the relevant option from the list of status parameters
    }
}
```

###### Status parameter options


+ `operational`
+ `degraded_performance`
+ `partial_outage`
+ `major_outage`
+ `under_maintenance`

######  Payload example


```json
{
    "component": {
        "status": "partial_outage"  
    }
}
```






##### Test the endpoint (_optional_)

Click **Run the test** to verify your endpoint. Logz.io shows if the message was successfully sent.

Check that the message arrived at the target endpoint.

##### Save the endpoint

**Save** your endpoint.
 