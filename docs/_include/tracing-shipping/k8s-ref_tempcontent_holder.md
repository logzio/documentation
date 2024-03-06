###### Kubernetes Reference

If you are deploying your application on Kubernetes, first [deploy Jaeger/OpenTelemetry collector and agents](https://docs.logz.io/docs/user-guide/distributed-tracing/set-up-tracing/k8s-deployment/).
Then add the following environment variables to your application containers:

 ```yaml
 env:
 - name: JAEGER_AGENT_HOST
   valueFrom:
     fieldRef:
       fieldPath: status.hostIP
 - name: JAEGER_AGENT_PORT
   value: "6831"
```