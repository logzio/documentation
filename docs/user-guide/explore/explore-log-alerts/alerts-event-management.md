---
sidebar_position: 5
title: Alerts Event Management
description: Monitoring and Managing Alert Events
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, events, log alerts, log analysis, observability]
---



Use Event Management to monitor the events triggered by your alerts.

Event Management provides a centralized, comprehensive view of the alerts triggered within your environment. This tool allows you to track alert activity, update statuses, add comments and additional details, and prioritize issue handling effectively.

Events are displayed in a sortable table, allowing you to organize them by severity, status, assigned handler, last trigger data, and the most recent update or edit. Additionally, you can filter and search the events to refine your results and focus on the most critical issues.





## Event Management table overview


![Event management](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-management-main.png)

The Event Management table provides a summary of information for each triggered event. The data in this table is retained for two weeks, and the number of events you can view is determined by the total number of triggered alerts.


|Event| Description| 
|---|---| 
|Event details|Includes the title, description, and Event ID of the triggered alert |
|Severity| The triggering conditions defined in the alert for a configured event threshold and time period. The event is labeled with the severity set for the alert:   **Severe > High > Medium > Low > Info**|
|Count| The number of grouped events included in the entry |
|Assigned to| Team member appointed for investigating and resolving the event. |
|Status|Investigation stage of the triggered event:    **- New:** Triggered event not yet assigned **- Assigned:** Investigation pending **- In Progress:** Assigned handler is investigating the event **- Waiting for response:** Investigation on hold, awaiting external stakeholder reply  **- False positive:**  Investigation determined the activity to be benign  **- Resolved:** Investigation complete |
|Last triggered| Date and time of the most recent occurrence of this event within the past 3 days |
|Comment| Additional information added by investigators. Use this field to include handling priority information and any information relevant to the investigation|
|Updated|Date of latest changes made to the event and which user made the changes|


## Filtering events

Use the available filters to refine the events displayed.



:::tip
Tip: If no events are shown when using filters, try adjusting your filter selections.
:::





![Filter panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-filters.png)

|Filter| Description| Filter options|
|---|---|---|
|Assigned to| Team member handling event investigation and resolution. You can select all users or choose an investigator from the list. Default = **All Users**|  All Users, Myself, or select from the list|
|Severity| The conditions specified in the alert that determine the event's threshold and time period for triggering. Default =  **All**| All, Severe, High, Medium,  Low, Info|
|Status|The current stage of the investigation for the triggered event. Default =  **All**|  All, New, Assigned, In Progress, Waiting for response, False positive, Resolved   |


<h3 id="clear"> Clear event filters</h3>

You can easily modify the filters you’ve set. To reset all filters to their default settings, click **Clear filters**.



## Searching for events

You can run a free text **Search** on the information in the **Event details** field -  This includes any of the information in the event title, ID, or **Description**.

:::tip
Tip: If no events are displayed after running a search, try adjusting your search terms for better results.
:::



## Editing an event

You can update the following fields for an event:

- **Status**: Change the investigation status of the event.
- **Assigned to**: Reassign the event to a different investigator. Note that once an event is assigned, it cannot be reset to **Unassigned**.
- **Comments**: Add text to provide details about the investigation, handling process, or task priorities.

After an investigator edits an event, the date and user who made the changes will be automatically displayed in the Updated field.


## Editing an event alert

To fine-tune event management, go back to the source alert and make necessary edits.

![Edit the event alert](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/edit-alert-event.gif)


## Investigating an event

This option opens the Explore interface, allowing you to view related logs for the triggered event within the selected time frame.





## Viewing events history

View the alert information for the triggered event, including the:

- Event title 
- Event ID
- Event description
- Time the event was triggered and subsequent actions

![Event History](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/event-history.png)
