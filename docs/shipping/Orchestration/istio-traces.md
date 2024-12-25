---
id: Istio-orchestration
title: Istio
overview: Deploy this integration to send traces from your Istio service mesh layers to Logz.io via the OpenTelemetry collector.
product: ['tracing']
os: ['windows', 'linux']
filters: ['Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/istio.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Deploy this integration to send traces from your Istio service mesh layers to Logz.io via the OpenTelemetry collector using **logzio-k8s-telemetry** Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).

**Before you begin, you'll need**:

* An applicaion instrumented by Istio in a Kubernetes cluster
* [Istioctl](https://istio.io/latest/docs/reference/commands/istioctl/) installed on your machine
* An active Logz.io account

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


### 1. Deploy the Helm chart in the same Kubernetes cluster as your application
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

### 2. Run the Helm deployment code

```
helm install -n monitoring \
--set metricsOrTraces.enabled=true \
--set logzio-k8s-telemetry.traces.enabled=true \
--set logzio-k8s-telemetry.secrets.TracesToken="<<TRACING-SHIPPING-TOKEN>>" \
--set logzio-k8s-telemetry.secrets.LogzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set logzio-k8s-telemetry.secrets.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


### 3. Define the service DNS name

You'll need the following service DNS:

`http://<<CHART-NAME>>-otel-collector.<<NAMESPACE>>.svc.cluster.local:<<PORT>>/`.

Replace `<<CHART-NAME>>` with the relevant service you're using (`logzio-k8s-telemetry`).
Replace `<<NAMESPACE>>` with your Helm chart's deployment namespace (e.g., default or monitoring).
Replace `<<PORT>>` with the [port for your agent's protocol](https://github.com/logzio/logzio-helm/blob/master/charts/logzio-telemetry/values.yaml#L249-L267) (Default is 4317).

If you're not sure what your cluster domain name is, you can run the following command to look it up:

```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.<<NAMESPACE>> | grep Name | sed "s/Name:\skubernetes.<<NAMESPACE>>//"'
```

It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name. 

### 4. Set Istio to send traces to Logz.io

Replace `<<logzio-k8s-telemetry-service-name>>` in the command below with the service name obtained in the previous step and run the command.

```
istioctl install --set meshConfig.defaultConfig.tracing.zipkin.address=<<logzio-k8s-telemetry-service-name>>:9411 --set values.pilot.traceSampling=100.0
```

 
:::note
By default, we set the `traceSampling` to 100, which means that Istio will send 100% of the application traces to Logz.io. You can adjust this value as required.
:::
  

### 5. Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).
