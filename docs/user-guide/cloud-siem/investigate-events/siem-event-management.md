---
sidebar_position: 1
title: Cloud SIEM Event Management
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Manage and Investigate Security Events
keywords: [SIEM, Security, Security events, investigate, Security information]
---

Use Cloud SIEM Event Management to monitor the events triggered by Logz.io Cloud SIEM security rules.

With a single source of truth, you have visibility into the triggered security events in your environment, to track triggered event rules, set the event status, assign an event handler, and use comments to add information, and prioritize how those issues are handled.

The events are displayed in a table: You can sort the events table by severity, status, handler, last triggering date, and the last time the event was updated or edited. You can also filter and search the events in the table, to further refine your results. 


## The Event Management table


![Event management](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-event-management.png)

The information that is provided for each event triggered by a Cloud SIEM rule is summarized in the table below. The retention for the Event Management table is two weeks, and the number of events you can view is bound by the number of triggered rules.  


|Event| Description| 
|---|---| 
|Event details|This information includes the title, description, and Event ID of the triggered Cloud SIEM rule |
|Severity| The triggering conditions defined in the Cloud SIEM rule for a configured event threshold and time period. The event is labeled with the severity set for the rule:   **Severe > High > Medium > Low > Info**|
|Count| The number of grouped events included in the entry |
|Status|Investigation stage of the triggered event:  **- New:** A triggered event that has not been assigned **- Assigned:** Investigation pending **- In Progress:** The assigned handler is investigating the event **- Waiting for response:** Investigation on hold pending reply from external stakeholders **- False positive:**  Investigation verified that the detected activity is benign **- Resolved:** Investigation complete |
|Assigned to| Team member handling event investigation and resolution |
|Last triggered| Date and time the rule was last triggered |
|Comment| Additional information added by investigators:  Use this field to include handling priority information and any information relevant to the investigation|
|Updated|Date of latest changes made to the event and which user made the changes|


## Event filtering 

Filter events by any combination of the available filters. 

:::tip
If you're using filters and no events are displayed, try adjusting your filter choices to find what you're looking for.
:::

![Filter panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-filter-event-management.png)

|Filter| Description| Filter options|
|---|---|---|
|Assigned to| Team member handling event investigation and resolution. You can select all users or pick an investigator from the list. Default = **All Users**|  All Users, Myself, or pick from the list|
|Severity| The triggering conditions defined in the Cloud SIEM rule for a configured event threshold and time period. Default =  **All**| All, Severe, High, Medium,  Low, Info|
|Status|Investigation stage of the triggered event.  Default =  **All**|  All, New, Assigned, In Progress, Waiting for response, False positive, Resolved   |


### Clear filters
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


## Editing an event rule

To fine tune event management, go back to a source rule and edit it! 

![Edit the event rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-edit-rule.gif)


## Investigating an event
This option opens the OpenSearch Dashboards interface, where you can view the related logs for the triggered event, according to the time frame you selected to display your events.


## Viewing the event history
View the rule information for the triggered event, including the:

- Event title 
- Event ID
- Event description
- Time the event was triggered and subsequent actions

![Event History](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-event-history.png)

