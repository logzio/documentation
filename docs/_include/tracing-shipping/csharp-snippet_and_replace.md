Within the snippet:

  + Replace `<<JAEGER_AGENT_HOST>>` with the host address of your Jaeger agent: Use `localhost` if it's on the same machine. 
  + For a Kubernetes deployment, use `Environment.GetEnvironmentVariable(Jaeger.Configuration.  JaegerAgentHost)` and make sure your application deployment contains the environment variables as shown in the Kubernetes reference, below.
 

{@include: ./tracing-shipping/k8s-ref_tempcontent_holder.md}
