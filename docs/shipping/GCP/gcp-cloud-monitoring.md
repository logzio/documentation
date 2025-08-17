---
id: GCP-Cloud-Monitoring
title: GCP Monitoring
overview: Send Google Cloud Monitoring metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Monitoring']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cloudmonitoring.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Cloud Monitoring provides visibility into the performance, uptime, and overall health of cloud-powered applications. 

## Logs 

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `metric`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="telegraf" label="Telegraf" default>

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `monitoring.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

  </TabItem>
  <TabItem value="opentelemetry" label="OpenTelemetry">

Use the OpenTelemetry Collector or the Logz.io Telemetry Helm chart and configure `googlecloudmonitoring` receiver to pull metrics from Google Cloud Monitoring and ship them to Logz.io via Prometheus Remote Write.

<Tabs>
  <TabItem value="local" label="Local/Native (Collector)">

Run the OpenTelemetry Collector on a host (VM, server, or workstation) to pull metrics from Google Cloud Monitoring using your service account credentials and forward them to Logz.io.

### Prerequisites

- OpenTelemetry Collector Contrib v0.131.0+ installed on your host
- Google Cloud project with Monitoring enabled
- Service account JSON key with `roles/monitoring.viewer`
- Logz.io Metrics shipping token and listener host

### Step 1: Install OpenTelemetry Collector

Download the OpenTelemetry Collector Contrib binary for your operating system from the [releases page](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases).

For example, on Linux:

```bash
# Download the latest version (replace with actual version)
wget https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.131.0/otelcol-contrib_0.131.0_linux_amd64.tar.gz
tar -xzf otelcol-contrib_0.131.0_linux_amd64.tar.gz
chmod +x otelcol-contrib
```

On macOS:

```bash
# Download for macOS
wget https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.131.0/otelcol-contrib_0.131.0_darwin_amd64.tar.gz
tar -xzf otelcol-contrib_0.131.0_darwin_amd64.tar.gz
chmod +x otelcol-contrib
```

### Step 2: Prepare credentials

Ensure you have a Google Cloud service account and JSON key as described above. Set the environment variable so the Collector can authenticate:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/gcp-credentials.json
```

### Step 3: Create the Collector configuration

Create `config.yaml` with the following content:
Make sure to replace `<<YOUR-GCP-PROJECT-ID>>` with your Google Cloud Platform Project ID.

```yaml
receivers:
  googlecloudmonitoring/project_1:
    collection_interval: 2m
    project_id: "<<YOUR-GCP-PROJECT-ID>>"
    metrics_list:
      - metric_descriptor_filter: "metric.type = starts_with(\"compute.googleapis.com\")"
  googlecloudmonitoring/project_2:
    collection_interval: 2m
    project_id: "<<YOUR-GCP-PROJECT-ID>>"
    metrics_list:
      - metric_name: "connectors.googleapis.com/flex/instance/cpu/usage_time"
processors:
  batch: {}

exporters:
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring/project_1, googlecloudmonitoring/project_2]
      processors: [batch]
      exporters: [prometheusremotewrite]
```

{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

Optional metric filters under `metrics_list`:

```yaml
- metric_descriptor_filter: "metric.type = starts_with(\"cloudsql.googleapis.com\")"
- metric_descriptor_filter: "metric.type = starts_with(\"bigquery.googleapis.com\")"
- metric_descriptor_filter: "metric.type = starts_with(\"storage.googleapis.com\")"
- metric_descriptor_filter: "metric.type = \"compute.googleapis.com/instance/cpu/utilization\""
- metric_name: "connectors.googleapis.com/flex/instance/cpu/usage_time"
```

### Step 4: Run the Collector

```bash
./otelcol-contrib --config ./config.yaml | cat
```

Make sure the process inherits `GOOGLE_APPLICATION_CREDENTIALS`.

### Verify

- Look for exporter logs without errors
- Confirm metrics appear under your Logz.io account after a few minutes

### Troubleshooting

- Credentials path not set or incorrect in `GOOGLE_APPLICATION_CREDENTIALS`
- Missing `roles/monitoring.viewer` on the service account
- Incorrect `project_id` or overly restrictive `metrics_list`
- Network egress blocked to Logz.io metrics endpoint

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

  </TabItem>
  <TabItem value="kubernetes" label="Kubernetes (Helm)" default>

### Prerequisites

- Kubernetes cluster with Helm installed
- kubectl configured to access your cluster
- Google Cloud project with Monitoring enabled
- Logz.io account with a metrics shipping token

### Step 1: Create Google Cloud Service Account

Grant the service account the Monitoring Viewer role (`roles/monitoring.viewer`) and create a JSON key.

Using Google Cloud Console:

- Go to Google Cloud Console > IAM & Admin > Service Accounts > Create Service Account
- Give it a name/description and click Create and Continue
- Grant role: Monitoring Viewer (`roles/monitoring.viewer`)
- Go to the Keys tab > Add key > Create new key > JSON, then download the key file.

Alternative using gcloud CLI:

```bash
export PROJECT_ID="your-project-id"

gcloud iam service-accounts create otel-gcp-metrics-logzio-sa \
  --display-name="OpenTelemetry GCP Metrics Service Account" \
  --description="Service account for collecting GCP metrics via OpenTelemetry" \
  --project=$PROJECT_ID

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:otel-gcp-metrics-logzio-sa@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/monitoring.viewer"

gcloud iam service-accounts keys create gcp-credentials.json \
  --iam-account=otel-gcp-metrics-logzio-sa@$PROJECT_ID.iam.gserviceaccount.com \
  --project=$PROJECT_ID
```

### Step 2: Create Kubernetes Secret

```bash
kubectl create namespace monitoring --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic google-cloud-credentials \
  --from-file=your-credentials.json=/path/to/your/gcp-credentials.json \
  -n monitoring

kubectl get secret google-cloud-credentials -n monitoring | cat
```

### Step 3: Configure Helm values

Create or update your `values.yaml` for the `logzio-monitoring` umbrella chart (nest under `logzio-k8s-telemetry`):
Make sure to replace `<<YOUR-GCP-PROJECT-ID>>` with your Google Cloud Platform Project ID.

```yaml
logzio-k8s-telemetry:
  global:
    logzioMetricsToken: "your-logzio-metrics-token"
    env_id: "your-environment-name"
    customMetricsEndpoint: "https://listener.logz.io:8053"  # Optional override

  metrics:
    enabled: true

  collector:
    mode: standalone  # or daemonset

  extraEnvs:
    - name: GOOGLE_APPLICATION_CREDENTIALS
      value: /var/secrets/google/your-credentials.json  # must match filename in the secret

  secretMounts:
    - name: google-cloud-credentials
      secretName: google-cloud-credentials
      mountPath: /var/secrets/google
      readOnly: true


  metricsConfig: # or daemonsetConfig
    receivers:
      googlecloudmonitoring/project_1:
        collection_interval: 2m
        project_id: "<<YOUR-GCP-PROJECT-ID>>"
        metrics_list:
          - metric_descriptor_filter: "metric.type = starts_with(\"compute.googleapis.com\")"
      googlecloudmonitoring/project_2:
        collection_interval: 2m
        project_id: "<<YOUR-GCP-PROJECT-ID>>"
        metrics_list:
          - metric_name: "connectors.googleapis.com/flex/instance/cpu/usage_time"            
    service:
      pipelines:
        metrics/googlecloudmonitoring:
        # existing receivers in your pipeline.
          receivers:
            - googlecloudmonitoring/project_1
            - googlecloudmonitoring/project_2
          processors:
            - attributes/env_id
            - batch
          exporters:
            - prometheusremotewrite/infrastructure
```

Metric filter examples you can add under `metrics_list`:

```yaml
- metric_descriptor_filter: "metric.type = starts_with(\"cloudsql.googleapis.com\")"
- metric_descriptor_filter: "metric.type = starts_with(\"bigquery.googleapis.com\")"
- metric_descriptor_filter: "metric.type = starts_with(\"storage.googleapis.com\")"
- metric_descriptor_filter: "metric.type = \"compute.googleapis.com/instance/cpu/utilization\""
- metric_name: "connectors.googleapis.com/flex/instance/cpu/usage_time"
```

### Step 4: Deploy the chart

```bash
helm repo add logzio-helm https://logzio.github.io/logzio-helm && helm repo update
helm upgrade --install logzio-monitoring logzio-helm/logzio-monitoring \
  -n monitoring \
  --create-namespace \
  -f your-values.yaml
```

### Verify

```bash
kubectl get pods -n monitoring | cat
kubectl logs -n monitoring -l app.kubernetes.io/name=otel-collector --tail=50 | cat

POD_NAME=$(kubectl get pods -n monitoring -l component=logzio-telemetry-collector-standalone -o jsonpath='{.items[0].metadata.name}')
kubectl exec -n monitoring $POD_NAME -- ls -la /var/secrets/google/ | cat
kubectl exec -n monitoring $POD_NAME -- env | grep GOOGLE_APPLICATION_CREDENTIALS | cat
```

### Troubleshooting

- Credentials filename/path mismatch in secret vs `GOOGLE_APPLICATION_CREDENTIALS`
- Missing `roles/monitoring.viewer` on the service account
- Wrong `project_id` or metric filters return no data
- Collector crash loops due to invalid misconfigured `metricsConfig` / `daemonsetConfig`

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

  </TabItem>
</Tabs>

  </TabItem>
</Tabs>
