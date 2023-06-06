---
sidebar_position: 5
---


# Alerts Event Management



Use Event Management to monitor the events triggered by your alerts.

Event Management offers a single source of truth into triggered alerts in your environment. It allows you to track alerts, set their status, add comments and additional information, and prioritize how those issues are handled.

The events are displayed in a table: You can sort the events table by severity, status, handler (who they’re assigned to), last triggering data, and the last time the event was updated or edited. You can also filter and search the events in the table to further refine your results.

## Event Management table overview


![Event management](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-management-main.png)

The information that is provided for each event triggered is summarized in the table. The retention for the Event Management table is two weeks, and the number of events you can view is bound by the number of triggered alerts.  


|Event| Description| 
|---|---| 
|Event details|This information includes the title, description, and Event ID of the triggered alert |
|Severity| The triggering conditions defined in the alert for a configured event threshold and time period. The event is labeled with the severity set for the alert:   **Severe > High > Medium > Low > Info**|
|Count| The number of grouped events included in the entry |
|Assigned to| Team member handling event investigation and resolution |
|Status|Investigation stage of the triggered event:    **- New:** A triggered event that has not been assigned **- Assigned:** Investigation pending **- In Progress:** The assigned handler is investigating the event **- Waiting for response:** Investigation on hold pending reply from external stakeholders  **- False positive:**  Investigation verified that the detected activity is benign  **- Resolved:** Investigation complete |
|Last triggered| Date and time the alert was last triggered |
|Comment| Additional information added by investigators:  Use this field to include handling priority information and any information relevant to the investigation|
|Updated|Date of latest changes made to the event and which user made the changes|


## Filtering events

Filter events by any combination of the available filters. 

:::tip
If you're using filters and no events are displayed, try adjusting your filter choices to find what you're looking for.
:::


![Filter panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-filters.png)

|Filter| Description| Filter options|
|---|---|---|
|Assigned to| Team member handling event investigation and resolution. You can select all users or pick an investigator from the list. Default = **All Users**|  All Users, Myself, or pick from the list|
|Severity| The triggering conditions defined in the alert for a configured event threshold and time period. Default =  **All**| All, Severe, High, Medium,  Low, Info|
|Status|Investigation stage of the triggered event. Default =  **All**|  All, New, Assigned, In Progress, Waiting for response, False positive, Resolved   |


### Clear event filters
You can always change the filters you've set. 
To reset all the filters to the defaults, click **Clear filters**. 

## Searching for events

You can run a free text **Search** on the information in the **Event details** field -  This includes any of the information in the event title, ID, or **Description**.

:::tip
If you're running a search and no events are displayed, try adjusting your search terms to find what you're looking for. 
:::


## Editing an event

You can update the following event fields: 

- The investigation **Status** of the event.
- The investigator the event is **Assigned to**. Once an event is assigned to a team member, the assignment can't be reset to **Unassigned**. 
- Add text to the **Comment** field, to provide information about the event investigation, the handling process, or task priorities. 

After an investigator edits an event, the date and user are automatically displayed in the **Updated** field for the event.  


## Editing an event alert

To fine tune event management, go back to a source alert and edit it! 

![Edit the event alert](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/edit-alert-event.gif)


## Investigating an event
This option opens the OpenSearch Dashboards interface, where you can view the related logs for the triggered event, according to the time frame you selected to display your events.



## Viewing events history
View the alert information for the triggered event, including the:

- Event title 
- Event ID
- Event description
- Time the event was triggered and subsequent actions

![Event History](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-history.png)
