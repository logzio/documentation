---
sidebar_position: 3
title: Unified Helm Chart
description: Ship Kubernetes telemetry with logzio-monitoring Helm Chart
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, helm, Kybernetes, k8s, helm chart]
slug: /k8s-360/unified-helm-chart/
---

The logzio-monitoring Helm Chart ships your Kubernetes telemetry (logs, metrics, traces and security reports) to your Logz.io account.


{@include: ../../_include/general-shipping/k8s.md}     

## Custom secrets management

To manage secrets separately from the Helm chart deployment, you can create and reference a custom configuration, relying on the default secret creation mechanism.

### Discover required secret keys

Before creating custom secrets, you need to identify what keys each sub-chart expects. Use the helm template command to see the expected resources:

```bash
# Replace 'helm install' with 'helm template' to see what would be deployed
helm template logzio-monitoring logzio-helm/logzio-monitoring \
  --set logzio-k8s-telemetry.secrets.logzioShippingToken="YOUR_TOKEN" \
  --set logzio-k8s-telemetry.secrets.ListenerHost="https://listener.logz.io:8053" \
  --set logzio-k8s-events.secrets.logzioShippingToken="YOUR_EVENTS_TOKEN" \
  --set logzio-k8s-events.secrets.logzioApiToken="YOUR_API_TOKEN" \
  -n monitoring
```

Look for `Secret` resources in the output to understand the required key names.

### Create custom secrets

For logzio-k8s-telemetry, create a custom secret with the required keys:

```yaml
# logzio-telemetry-custom-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: logzio-telemetry-custom
  namespace: monitoring
type: Opaque
data:
  # Base64 encoded values
  logzio-metrics-token: <BASE64_ENCODED_METRICS_TOKEN>
  logzio-traces-token: <BASE64_ENCODED_TRACES_TOKEN>
  p8s_logzio_name: <BASE64_ENCODED_P8S_NAME>
  ListenerHost: <BASE64_ENCODED_LISTENER_HOST>
  # Add other required keys as discovered from helm template
```

For logzio-k8s-events:

```yaml
# logzio-events-custom-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: logzio-events-custom
  namespace: monitoring
type: Opaque
data:
  # Base64 encoded values
  logzio-logs-token: <BASE64_ENCODED_LOGS_TOKEN>
  logzio-api-token: <BASE64_ENCODED_API_TOKEN>
  # Add other required keys as discovered from helm template
```

To encode your tokens:

```bash
echo -n "your-actual-token-here" | base64
echo -n "https://listener.logz.io:8053" | base64
```

### Apply custom secrets

```bash
kubectl apply -f logzio-telemetry-custom-secret.yaml -n monitoring
kubectl apply -f logzio-events-custom-secret.yaml -n monitoring
```

### Configure Helm values

Create a `values.yaml` file to disable default secret creation and reference your custom secrets:

```yaml
# values.yaml
logzio-k8s-telemetry:
  # Disable default secret creation
  secrets:
    create: false
  # Reference your custom secret
  existingSecret:
    name: "logzio-telemetry-custom"
    # Map the keys if they differ from default names
    keys:
      logzioShippingToken: "logzio-traces-token"
      logzioMetricsToken: "logzio-metrics-token"
      p8sLogzioName: "p8s_logzio_name"
      ListenerHost: "ListenerHost"

logzio-k8s-events:
  # Disable default secret creation
  secrets:
    create: false
  # Reference your custom secret
  existingSecret:
    name: "logzio-events-custom"
    keys:
      logzioShippingToken: "logzio-logs-token"
      logzioApiToken: "logzio-api-token"
```

### Deploy with custom configuration

```bash
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring \
  -n monitoring \
  --reuse-values \
  -f values.yaml
```

### Troubleshooting common issues

**Token Mapping Errors**

`error: "not retryable error: Permanent error: error exporting items, request to https://listener-eu.logz.io:8071/?token=map[key:logzio-traces-token name:logzio-secret]"`

This indicates the secret reference is not resolving correctly. Check:

* Secret exists: kubectl get secret logzio-telemetry-custom -n monitoring
* Correct keys: kubectl get secret logzio-telemetry-custom -n monitoring -o yaml
* Values mapping: Ensure your values.yaml maps the correct key names

**Missing Values for SPM**

If SPM is not working, ensure you have all required values:

```bash
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring \
  -n monitoring \
  --reuse-values \
  --set logzio-k8s-telemetry.secrets.ListenerHost='https://listener.logz.io:8053' \
  --set logzio-k8s-telemetry.secrets.p8s_logzio_name='your-p8s-name'
```

**Verification**

Check that your secrets are properly mounted:

```bash
# Check the pod environment or mounted secrets
kubectl describe pod -l app=logzio-k8s-telemetry -n monitoring
kubectl exec -it <pod-name> -n monitoring -- env | grep -i logz
```

Here's a complete working example:

Create the custom secret:

```bash
kubectl create secret generic logzio-telemetry-custom \
  --from-literal=logzio-traces-token="your-traces-token" \
  --from-literal=logzio-metrics-token="your-metrics-token" \
  --from-literal=p8s_logzio_name="your-p8s-name" \
  --from-literal=ListenerHost="https://listener.logz.io:8053" \
  -n monitoring
```

**Deploy with custom secret reference:**

```bash
helm upgrade logzio-monitoring logzio-helm/logzio-monitoring \
  -n monitoring \
  --set logzio-k8s-telemetry.secrets.create=false \
  --set logzio-k8s-telemetry.existingSecret.name="logzio-telemetry-custom"
```

If you continue experiencing issues, run `helm template` to verify expected resources. Next, check pod logs: `kubectl logs -l app=logzio-k8s-telemetry -n monitoring`, and finally, verify secret mounting: `kubectl describe pod <pod-name> -n monitoring`.

### Best practices

* Use CI/CD Secret Management: Integrate with your existing secret management system (AWS Secrets Manager, Azure Key Vault, etc.)
* Regular Rotation: Implement token rotation procedures
* Namespace Isolation: Keep secrets in the same namespace as your deployment
* Least Privilege: Only include necessary keys in each secret
* Documentation: Document your custom key mappings for team reference



