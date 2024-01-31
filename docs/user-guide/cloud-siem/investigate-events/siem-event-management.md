---
sidebar_position: 1
title: Cloud SIEM Event Management
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Manage and Investigate Security Events
keywords: [SIEM, Security, Security events, investigate, Security information]
---

Use Cloud SIEM Event Management to monitor the events triggered by Logz.io Cloud SIEM security rules.

With a single source of truth, you have visibility into the triggered security events in your environment to track triggered event rules, set the event status, assign an event handler, use comments to add information, and prioritize how those issues are handled.

The events are displayed in a table: You can sort the events table by severity, status, handler, last triggering date, and the last time the event was updated or edited. You can also filter and search the events in the table to refine your results further.


## Event Management overview


![Event management](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/main-event-mngmt-jan.png)

The information provided for each event triggered by a Cloud SIEM rule appears in the table. The retention for the Event Management table is two weeks, and the number of triggered rules binds the number of events you can view.

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

In addition, you can **edit** the assignees and comments for each event, **investigate** it, **edit the rule** that triggered the event, and **view the event's history**.

![event management](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/manage-event-mngmt-jan.png)


### Filter events

Filter events by any combination of the available filters. 

:::tip
If you're using filters and no events are displayed, try adjusting your filter choices to find what you're looking for.
:::

![Filter panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/event-mngmt-filter-jan.png)

|Filter| Description| Filter options|
|---|---|---|
|Assigned to| Team member handling event investigation and resolution. You can select all users or pick an investigator from the list. Default = **All Users**|  All Users, Myself, or pick from the list|
|Severity| The triggering conditions defined in the Cloud SIEM rule for a configured event threshold and time period. Default =  **All**| All, Severe, High, Medium,  Low, Info|
|Status|Investigation stage of the triggered event.  Default =  **All**|  All, New, Assigned, In Progress, Waiting for response, False positive, Resolved   |

To reset all the filters to the defaults, click **Clear filters**. 

### Search for events

You can run a free text **Search** on the information in the **Event details** field -  This includes any information in the event title, ID, or **Description**.

:::tip
If you're running a search and no events are displayed, try adjusting your search terms to find what you're looking for.
:::

### Edit an event

You can update the following event fields: 

- The investigation **Status** of the event.
- The investigator the event is **Assigned to**. Once an event is assigned to a team member, the assignment can't be reset to **Unassigned**. 
- Add text to the **Comment** field, to provide information about the event investigation, the handling process, or task priorities. 


After an investigator edits an event, the date and user are automatically displayed in the **Updated** field for the event.  


### Edit an event rule

To fine tune an event, you can edit the rule that triggered it. Find the event you want to edit and click on the three dots menu > **Edit rule**. You can only edit the trigger threshold and notification options in preconfigured rules.

![Edit the event rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/edit-rule-siem-jan.gif)


### Investigate an event

Click the **Investigate** button to open the quick view panel with additional details about the event and when it was triggered. The quick view allows you to assign the event to a team member by choosing the relevant member from the drop-down list. You can dive deeper into each trigger by clicking the **Investigate** button next to it and opening the relevant logs for each event.

![investigate events](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-events-quick-view-jan.png)


### View event history

Click the three dots to access the **View History** option. The popup includes the title and ID of the event, its description, and the timeline of when the event was triggered or modified.


:::info note
The retention period for event history is 2 weeks, and the system saves older event histories as logs on your security account, allowing you to view them from OpenSearch Dashboards.
:::


![event history](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/event-history-siem-jan.png)

### Grouped Events

Events with the same severity and **Group By** field values will be grouped together. For example, suppose multiple rules are triggering for the same use case, authentication fails from a malicious IP, and suspicious activity is detected from the same IP. In that case, the rules are grouped into a single event.

You can see in the table an indication of grouped events and the number of events grouped in this rule.

![Grouped events](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/grouped-events-jan.png)

Some events start as a single event, and as more rules and events occur, they are grouped. This affects the event's history since grouped events display the history from when the events were grouped and not before.

Some events may initially appear as individual events, but as additional rules and events occur, they are combined into a group event. This impacts the event's history because grouped events will display their history from when they are grouped rather than any earlier history of the single event.
