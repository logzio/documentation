:::note
When running the OTEL collector in a Docker container, your application should run in separate containers on the same host network. **Ensure all containers share the same network**. Using Docker Compose ensures that all containers, including the OTEL collector, share the same network configuration automatically.
:::







