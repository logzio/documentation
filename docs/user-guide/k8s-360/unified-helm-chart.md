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



