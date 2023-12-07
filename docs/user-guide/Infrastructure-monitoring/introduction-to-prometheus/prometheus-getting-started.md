---
sidebar_position: 1
title: Getting started with Prometheus
---


Manage your metrics with Logz.io Infrastructure Monitoring, powered by Prometheus.

With our open-source platform, you get enterprise-level user management with role-based access control (RBAC) for Prometheus as a managed service, and you have the option to correlate your metrics with logs and traces, using Logz.io Log Management and Distributed Tracing capabilities.


## Leverage Prometheus with Logz.io

If you're already using Prometheus to pull metrics from your services, you can leverage your current implementation to forward metrics to Logz.io for fast time-to-value: We store your metrics in our managed service, which cuts most of your metrics retention burden. And if you have multiple Prometheus instances, we take on the maintenance tasks to ensure there's enough storage space, as well as upgrading, securing, and in some cases, sharding Prometheus.

You can continue using Prometheus Alert Manager: You'll simply store the metrics on your own servers based on your alerts needs, so your Alert Managers can access the data.

All it takes to ship your metrics data to Logz.io is to use Remote Write on each Prometheus server, with Logz.io configured as the endpoint: By adding a few lines of code, Remote Write ensures that your metrics are written to Logz.io.

<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/w2lic9vv1z" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Your data is formatted as JSON documents by the Logz.io listener.
For the trial program, your incoming raw data has a 30-day retention period.

Once your metrics are flowing, import your existing Prometheus and Grafana dashboards to Logz.io Infrastructure Monitoring as JSON files.

For the record, notification endpoints and dashboard annotations are not imported: You'll need to recreate them in Logz.io.  See [Notification endpoints](../../integrations/notification-endpoints/endpoints/) and [Annotations](../log-correlations/annotations/) for more information.

1. [Configure Remote Write](/docs/user-guide/Infrastructure-monitoring/introduction-to-prometheus/configure-remote-write-prometheus).
1. [Import dashboards](/docs/user-guide/Infrastructure-monitoring/introduction-to-prometheus/importing-dashboards).
1. [Configure notification endpoints](/docs/user-guide/integrations/notification-endpoints/endpoints).
1. [Recreate your dashboard annotations](/docs/user-guide/infrastructure-monitoring/log-correlations/annotations/).
1. [Explore your Prometheus metrics](/docs/user-guide/Infrastructure-monitoring/introduction-to-prometheus/explore-metrics-prometheusZ).




<!--
1. Highlight the value:
Hosted, managed & enterprise grade - Secured, user management etc..
Full system view
Long retention (Will be coming later)
Integrated to the logs management and tracing.

2. Highlight the simplicity in shipping the metrics as well what it means on their environment:  - They will be able to reduce their retention.
implication from resource standpoint : It will require more CPU and memory
 -->
