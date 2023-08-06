---
sidebar_position: 5
title: EZKonnect
---


EZKonnect is a deployment and configuration tool designed to assist you in effectively instrumenting Kubernetes applications with OpenTelemetry auto-instrumentation and configurable log types.

At the heart of EZKonnect is the `logzio-ezkonnect` Helm chart, which functions synergistically with the `logzio-monitoring` Helm chart.

EZKonnect comprises three principal components:

* **Kubernetes Instrumentor** - Provides auto-instrumentation and manages log type control for Kubernetes applications.
* **EZKonnect Server** - Facilitates communication between the user and the Kubernetes Instrumentor.
* **EZKonnect UI** - Offers an intuitive graphical interface for managing and viewing your instrumentation data.


EZKonnect supports several programming languages, including:

* Java
* Node.js
* Python
* .NET

### Before you start you will need:
- Opentelemetry collector installed on your cluster
  - works out of the box with [logzio-monitoring](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring) chart installed with traces and logs enabled (version `0.5.8` or higher for log_type)
  - to send the data to a custom collector change the `kubernetesInstrumentor.env.monitoringServiceEndpoint` value

## Install EZKonnect

To install the EZKonnect Helm chart, run the following commands:

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
helm install logzio-ezkonnect logzio-helm/ezkonnect -n ezkonnect --create-namespace
```

Afterwards, use `kubectl port-forward` to access the user interface in your browser:

```shell
kubectl port-forward svc/ezkonnect-ui -n ezkonnect 31032:31032
```

Go to http://localhost:31032 

## Using EZKonnect UI


The EZKonnect UI shows when you access the deployment at `http://localhost:8080`.


### Logs

![UI](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ezkonnect/ezkonnect-logs.png)

#### Edit a log type of a log

If you need to change a log type of a log collected by EZKonnect:

1. In the row of the required log, click the **Log Type** dropdown.
2. Select the required log type.
3. Click **Deploy**.

#### Add a log type

If you need to add a log type to a log collected by EZKonnect:

1. In the row of the required log, click the **Log Type** dropdown.
2. Type in the required log type definition.
3. Press Enter.
4. Click **Add log type**.

#### Remove a log type from a log

If you need to change a log type of a log collected by EZKonnect:

1. In the row of the required log, click the **Remove log type**.

### Traces

![UI](https://dytvr9ot2sszz.cloudfront.net/logz-docs/ezkonnect/ezkonnect-traces.png)

#### Add instrumentation to a pod

To add OpenTelemetry instrumentation to a pod:

1. Select the required pod. The source code detected on the pod will be shown on the UI. THe instrumentation will be installed for this code.
2. Click **Add instrumentation**. 
3. Click **Deploy**.

#### Remove instrumentation from a pod

To remove OpenTelemetry instrumentation from a pod:

1. Select the required pod.
2. Click **Rollback**. 


## Parameters configuration

The EZKonnect chart has several configurable parameters and their default values. Below is a table detailing these parameters:

| Parameter | Description | Default |
| --- | --- | --- |
| `kubernetesInstrumentor.serviceAccount` | Service account name of the instrumentor deployment | `"kubernetes-instrumentor"` |
| `kubernetesInstrumentor.image.repository` | Repository of the instrumentor image | `"logzio/instrumentor"` |
| `kubernetesInstrumentor.image.tag` | Tag of the instrumentor image | `"v1.0.5"` |
| `kubernetesInstrumentor.instrumentationDetectorImage.repository` | Repository of the instrumentation detector image | `"logzio/instrumentation-detector"` |
| `kubernetesInstrumentor.instrumentationDetectorImage.tag` | Tag of the instrumentation detector image | `"v1.0.5"` |
| `kubernetesInstrumentor.javaAgentImage.repository` | Repository of the Java agent image | `"logzio/otel-agent-java"` |
| `kubernetesInstrumentor.javaAgentImage.tag` | Tag of the Java agent image | `"v1.0.5"` |
| `kubernetesInstrumentor.dotnetAgentImage.repository` | Repository of the .Net agent image | `"logzio/otel-agent-dotnet"` |
| `kubernetesInstrumentor.dotnetAgentImage.tag` | Tag of the .Net agent image | `"v1.0.5"` |
| `kubernetesInstrumentor.nodejsAgentImage.repository` | Repository of the Node.js agent image | `"logzio/otel-agent-nodejs"` |
| `kubernetesInstrumentor.nodejsAgentImage.tag` | Tag of the Node.js agent image | `"v1.0.5"` |
| `kubernetesInstrumentor.pythonAgentImage.repository` | Repository of the Python agent image | `"logzio/otel-agent-python"` |
| `kubernetesInstrumentor.pythonAgentImage.tag` | Tag of the Python agent image | `"v1.0.5"` |
| `kubernetesInstrumentor.ports.metricsPort` | Metrics port for the instrumentor | `8080` |
| `kubernetesInstrumentor.ports.healthProbePort` | Health probe port for the instrumentor | `8081` |
| `kubernetesInstrumentor.resources.limits.cpu` | CPU limit for the instrumentor | `"500m"` |
| `kubernetesInstrumentor.resources.limits.memory` | Memory limit for the instrumentor | `"128Mi"` |
| `kubernetesInstrumentor.resources.requests.cpu` | CPU request for the instrumentor | `"10m"` |
| `kubernetesInstrumentor.resources.requests.memory` | Memory request for the instrumentor | `"64Mi"` |
| `kubernetesInstrumentor.env.monitoringServiceEndpoint` | Endpoint of the monitoring service | `"logzio-monitoring-otel-collector.monitoring.svc.cluster.local"` |
| `kubernetesInstrumentor.service.name` | Name of the instrumentor service | `"kubernetes-instrumentor-service"` |
| `kubernetesInstrumentor.service.port` | Service port for the instrumentor | `8080` |
| `kubernetesInstrumentor.service.targetPort` | Target port for the instrumentor service | `8080` |
| `ezkonnectServer.serviceAccount` | Service account name of the instrumentor deployment | `"ezkonnect-server"` |
| `ezkonnectServer.image.repository` | Repository of the server image | `"logzio/ezkonnect-server"` |
| `ezkonnectServer.image.tag` | Tag of the server image | `"v1.0.6"` |
| `ezkonnectServer.ports.http` | HTTP port for the server | `8080` |
| `ezkonnectServer.service.name` | Name of the server service | `"ezkonnect-server"` |
| `ezkonnectServer.service.port` | Service port for the server | `5050` |
| `ezkonnectServer.service.targetPort` | Target port for the server service | `5050` |
| `ezkonnectUi.image.repository` | Repository of the UI image | `"logzio/ezkonnect-ui"` |
| `ezkonnectUi.image.tag` | Tag of the UI image | `"v1.0.0"` |
| `ezkonnectUi.ports.http` | HTTP port for the UI | `31032` |
| `ezkonnectUi.service.name` | Name of the UI service | `"ezkonnect-ui-service"` |
| `ezkonnectUi.service.port` | Service port for the UI | `31032` |
| `ezkonnectUi.service.targetPort` | Target port for the UI service | `31032` |
| `rbac.clusterRoles...` | Configure the RBAC cluster roles | Refer to `values.yaml` |
| `rbac.clusterRoleBindings...` | Configure the RBAC cluster role bindings | Refer to `values.yaml` |


You can override the default values by creating your own `values.yaml` file and passing the `--values` or `-f` option to the Helm command. For example:

```shell
You can override the default values by creating your own values.yaml file and passing the --values or -f option to the Helm command. For example:
```