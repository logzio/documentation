---
sidebar_position: 9
title: SIEM Event Management
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Manage and filter security events in Logz.io
keywords: [SIEM, security event, events, cloud security, Security information and event management, Security information]

---

Event management is an integrated platform to monitor and manage security events. The table provides an overview of all security events in your environment, where you can view the event's history, investigate it, edit the rule related to the event, and assign the event to one of your team members.

## Event Management Overview

![Event management table](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/main-event-mngmt-jan.png)

The event management table presents your latest events with useful information, including:

* **Event details**, such as event ID, title, and description of the triggered event
* Each event **severity level**, as defined in the rule that triggered it
* Relevant **status** for each event. The status can be:
   * **New** - A triggered event that has not been assigned
   * **Assigned** - Assigned to a handler and is pending investigation
   * **In progress** - The assigned handler is actively investigating the event
   * **Waiting for response** - Investigation is on hold pending a reply from external stakeholders
   * **False positive** - Investigation verified that the detected activity is benign
   * **Resolved** - The investigation is complete
* **Assigned to** show the handler handling event investigation and resolution. Once assigned to a team member, you cannot reset the event to `Unassigned`
* The date and time when the event was last **triggered**
* You and your team members can add **comments** to each event, which will show in the table
* Indicated when an event was last **updated** if a team member updated it


In addition, you can **edit** the assignees and comments for each event, **investigate** it, **edit the rule** that triggered the event, and **view the event's history**. 

![Event management manage](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/manage-event-mngmt-jan.png)

:::info note
The event manager has a retention period of 2 weeks. Older events are **saved as logs** on your security account and can be viewed from OpenSearch Dashboards.
:::

## Investigate Events


Click the **Investigate** button to open the quick view panel with additional details about the event and when it was triggered. The quick view allows you to assign the event to a team member by choosing the relevant memebr from the drop down list. You can dive deeper into each trigger by clicking the **Investigate** button next to it, and opening the relevant logs for each event. 

![Edit management quick view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-events-quick-view-jan.png)

### View Event History

Click the three dots to access the **View History** option. The popup includes the event's ID, description, and timeline.

Event history helps you keep track of what happened to it during the last 2 weeks, including when it was created, who the handler is, and updates regarding its status.

![Event history overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/event-history-siem-jan.png)

### Grouped Events

Events with the same severity and the same Group By field values, will be grouped together. For example, suppose multiple rules are triggering for the same use case, authentication failed from a malicious IP, and suspicious activity is detected from the same IP. In that case, they will be grouped into a single event.

You can see in the table an indication of grouped events and the number of events grouped in this rule. 

![Grouped events](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/grouped-events-jan.png)

Some events start as a single event, and as more rules and events occur, they will be grouped. This affects the event's history since grouped events display the history from when the events were grouped and not before.

Some events may initially appear as individual events, but as additional rules and events occur, they will be combined into a group event. This impacts the event's history because grouped events will display their history from when they were grouped rather than any earlier history of the single event.