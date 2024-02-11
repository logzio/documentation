---
sidebar_position: 5
title: EasyConnect
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Simplify the process of instrumenting Kubernetes applications
keywords: [Kubernetes, ship kubernetes data, easyconnect, ezkonnect, kubernetes logs, kubernetes metrics, kubernetes tracing]
---


The EasyConnect is a tool that simplifies the process of instrumenting Kubernetes applications with OpenTelemetry auto-instrumentation and adding configurable log types. The EasyConnect is based on the `easy-connect` Helm chart that works in conjunction with the `logzio-monitoring` Helm chart.

EasyConnect comprises three principal components:

* **Kubernetes Instrumentor** - Provides auto-instrumentation and manages log type control for Kubernetes applications.
* **Easy Connect Server** - Facilitates communication between the user and the Kubernetes Instrumentor.
* **Easy Connect UI** - Offers an intuitive graphical interface for managing and viewing your instrumentation data.


Easy Connect supports several programming languages, including:

* Java
* Node.js
* Python
* .NET

### Before you start, you will need:

Opentelemetry collector installed on your cluster. The collector works out of the box with [logzio-monitoring](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring) chart installed with traces and logs enabled (version `0.5.8` or higher for log_type). 

:::note
To send data to a custom collector, change the `kubernetesInstrumentor.env.monitoringServiceEndpoint` value.
:::

## Install EasyConnect

To install the EasyConnect Helm chart, run the following commands:

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
helm install logzio-easy-connect logzio-helm/easy-connect -n monitoring --create-namespace
```

After installing, run `kubectl port-forward` to access the user interface in your browser:

```shell
kubectl port-forward svc/easy-connect-ui -n monitoring 31032:31032
```

The EasyConnect UI is available at http://localhost:31032 

## Using EasyConnect UI

The EasyConnect UI shows a list of all workloads in your account. You can filter the worloads by name, namespace, workload type or language.

### Logs

#### Edit the log type for a workload

If you need to change the log type for a workload:

1. In the row of the required workload, click **Edit**.
2. Click the **Log Type** dropdown.
3. Select the required log type. If the required log type is not available from the selection, manually enter the log type and press **Enter**.
4. Click **Deploy**.

#### Add a log type to a workload

If you need to add a log type to a workload:

1. In the row of the required workload, click the **Log Type** dropdown.
2. Enter the required log type definition.
3. Press **Enter**.
4. Click **Deploy**.


### Traces

#### Add instrumentation to a workload

To add OpenTelemetry instrumentation to a workload:

1. In the row of the required workload, click **Edit**.
2. Enable the selector of **Traces (Service name)**.
3. Click the **Select service name** dropdown.
4. Select the required service name. If the required service name is not available from the selection, manually enter the service name and press **Enter**.
5. Click **Deploy**.

#### Remove instrumentation from a workload

To remove OpenTelemetry instrumentation from a workload:

1. In the row of the required workload, click **Edit**.
2. Disable the toggle switch of **Traces (Service name)**.


:::note
If Opentelemetry is already integrated into your workload, EasyConnect will identify its presence and notify you, preventing any addition or removal of Opentelemetry through EasyConnect.
If your workload's telemetry language is unsupported, EasyConnect will display a notification indicating that auto-instrumentation is not available.
::: 

## Parameters configuration

The EasyConnect chart has several configurable parameters and their default values.

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
| `easyConnectServer.serviceAccount` |	Service account name of the instrumentor deployment |	`"easy-connect-server"`|
|`easyConnectServer.image.repository`|	Repository of the server image|`"logzio/easy-connect-server"`|
|`easyConnectServer.image.tag` | Tag of the server image|`"v1.0.7"`|
|`easyConnectServer.ports.http`	| HTTP port for the server|`8080`|
|`easyConnectServer.service.name` |	Name of the server service|`"easy-connect-server"`|
|`easyConnectServer.service.port` |Service port for the server|`5050`|
|`easyConnectServer.service.targetPort`|Target port for the server service|`5050`|
|`easyConnectUi.image.repository`|Repository of the UI image|`"logzio/easy-connect-ui"`|
|`easyConnectUi.image.tag`|Tag of the UI image|`"v1.0.0"`|
|`easyConnectUi.ports.http`|HTTP port for the UI|`31032`|
|`easyConnectUi.service.name`|Name of the UI service|`"easy-connect-ui"`|
|`easyConnectUi.service.port`|Service port for the UI|`31032`|
|`easyConnectUi.service.targetPort`|Target port for the UI service|`31032`|
|`rbac.clusterRoles...`|Configure the RBAC cluster roles|Refer to `values.yaml`|
|`rbac.clusterRoleBindings...`|Configure the RBAC cluster role bindings|Refer to `values.yaml`|


You can override the default values by creating your own `values.yaml` file and passing the `--values` or `-f` option to the Helm command. For example:

```shell
helm install logzio-easy-connect logzio-helm/easy-connect -n easy-connect --create-namespace --values my_values.yaml
```

Here, `my_values.yaml` is your custom configuration file.

## Manual actions

The `logzio-instrumetor` microservice can be deployed to your cluster to discover applications, inject opentelemetry instrumentation, add log types and more. You can manually control the discovery process with annotations:
- `logz.io/traces_instrument = true` - to instrument the application with OpenTelemetry
- `logz.io/traces_instrument = rollback` - to delete the OpenTelemetry instrumentation
- `logz.io/service-name = <string>` - to set an active service name for your OpenTelemetry instrumentation
- `logz.io/application_type = <string>` - to set the log type to send to logz.io (**dependent on logz.io fluentd helm chart**)
- `logz.io/skip = true` - to skip the application from instrumentation or app detection

## Alternative images

You can find alternative to `dockerhub` images in `public.ecr.aws/logzio/` with the same image name. For example, `public.ecr.aws/logzio/instrumentor`.
