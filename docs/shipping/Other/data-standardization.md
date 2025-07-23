---
id: data-standardization
title: Data Standardization
overview: Data standardization
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kafka2.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

To improve the usability, performance, and consistency of logs across the platform, Logz.io is implementing data standardization across all log sources. Standardized fields improve data analysis, reduce processing complexity, and enable features like Root Cause Analysis (RCA), efficient filtering, and consistent dashboards.

## Why it matters

Inconsistent log structures across services make it difficult to correlate and query data effectively. By aligning all logs to a common set of fields, users can rely on uniform behavior across all integrations, whether using OpenTelemetry, AWS, Kubernetes, or custom pipelines.

## Standard fields and naming convention

Logz.io expects incoming logs to include the following standardized fields:

| Field name | Description | 
| -- | -- |
| `level` |	Log level (e.g., `INFO`, `ERROR`, `DEBUG`) using OTEL's logging SDK |
| `service_name` | Service or component name, from OTEL resource attributes |
| `env_id` | Environment identifier (e.g., `prod`, `staging`) |
| `host_name` | Hostname or IP, injected by OTEL's default resource attributes |
| `trace_id` | Trace ID for distributed tracing, if available |
| `span_id` | Span ID for distributed tracing, if available |
| `message` | The log body or message, ideally structured as key-value pairs |

If you're using a custom integration, you need to map your fields to these expected names. For example:

* Map `severity` - `level`
* Map `component` - `service_name`
* Inject `trace_id` and `span_id` using OTEL SDK or HTTP headers if available
* Override `@timestamp` if a custom timestamp is included (with timezone info)

## Integrations with standardization implemented

These integrations already support data standardization:

* **OpenTelemetry SDKs** – Supports all fields using semantic conventions. Supported languages include: [.NET](https://docs.logz.io/docs/shipping/Code/dotnet/), [Python](https://docs.logz.io/docs/shipping/Code/Python/), [Java](https://docs.logz.io/docs/shipping/Code/Java/), [Go](https://docs.logz.io/docs/shipping/Code/GO/), [Node.js](https://docs.logz.io/docs/shipping/Code/Node-js/), [PHP](https://docs.logz.io/docs/shipping/Code/php/), and [Rust](https://docs.logz.io/docs/shipping/Code/Rust/).

* **Kubernetes** – Uses annotations and labels; trace context via OTEL sidecar or agent. Supported languages include: [Kubernetes](http://docs.logz.io/docs/shipping/Containers/Kubernetes/), [FluentD logs](http://docs.logz.io/docs/shipping/other/fluentd-data/), and [Trivy security event logs](http://docs.logz.io/docs/shipping/security/trivy/).


* **AWS (CloudWatch, Lambda)** – Injects trace context with AWS X-Ray; environment metadata via environment variables. Supported languages include: [CloudFront](https://docs.logz.io/docs/shipping/aws/aws-cloudfront/), [API Gateway](https://docs.logz.io/docs/shipping/AWS/AWS-API-Gateway/), [Node.js traces on AWS Lambda via OpenTelemetry](https://docs.logz.io/docs/shipping/code/node-js/#traces), [Classic ELB](https://docs.logz.io/docs/shipping/AWS/Amazon-Classic-ELB/), [App ELB](https://docs.logz.io/docs/shipping/AWS/AWS-App-ELB/), [Network ELB](https://docs.logz.io/docs/shipping/AWS/AWS-Network-ELB/), [AppRunner](https://docs.logz.io/docs/shipping/AWS/AWS-AppRunner/), [Athena](https://docs.logz.io/docs/shipping/AWS/AWS-Athena/), [Control Tower](https://docs.logz.io/docs/shipping/AWS/AWS-Control-Tower/), [Cost and Usage Reports](https://docs.logz.io/docs/shipping/aws/aws-cost-and-usage-reports/), [EC2](https://docs.logz.io/docs/shipping/AWS/AWS-EC2/), [EC2 Fargate](https://docs.logz.io/docs/shipping/AWS/AWS-ECS-Fargate/), [ECS](https://docs.logz.io/docs/shipping/AWS/AWS-ECS/), [EKS](https://docs.logz.io/docs/shipping/AWS/aws-eks/), [DynamoDB](https://docs.logz.io/docs/shipping/AWS/AWS-DynamoDB/), [Cross Account](https://docs.logz.io/docs/shipping/AWS/AWS-cross-account/), [SQS](https://docs.logz.io/docs/shipping/AWS/aws-SQS/), [Lambda Extensions](https://docs.logz.io/docs/shipping/AWS/Lambda-extensions/), [Go traces on AWS Lambda via OpenTelemetry](https://docs.logz.io/docs/shipping/Code/GO/#traces), [FSx](https://docs.logz.io/docs/shipping/AWS/AWS-FSx/), [GuardDuty](https://docs.logz.io/docs/shipping/AWS/GuardDuty/), [S3 Access](https://docs.logz.io/docs/shipping/AWS/AWS-S3-Access/), [S3 Bucket](https://docs.logz.io/docs/shipping/AWS/AWS-S3-Bucket/), [Route 53](https://docs.logz.io/docs/shipping/AWS/AWS-Route-53/), [RDS](https://docs.logz.io/docs/shipping/AWS/AWS-RDS/), [Lambda](https://docs.logz.io/docs/shipping/AWS/AWS-Lambda/), and [MSK](https://docs.logz.io/docs/shipping/AWS/AWS-MSK/).

* **HTTPS/OTLP APIs** – Header-based trace injection; field mapping required.

## Support and migration

You can follow the docs or use Logz.io Collector to migrate your data to use standardized fields. If you need additional help, reach out to your account manager or contact [Logz.io's support team](mailto:help@logz.io).