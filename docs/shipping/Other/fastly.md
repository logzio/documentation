---
id: fastly-data
title: Fastly
overview: Forward Fastly logs to Logz.io using a configurable AWS Lambda HTTPS endpoint
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/fastly-red.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Fastly is a real-time content delivery network (CDN) and edge cloud platform that accelerates and secures web and application traffic. Forward Fastly logs to Logz.io for centralized analysis, monitoring, and alerting alongside the rest of your observability data.

This AWS Lambda function serves as an HTTPS logging endpoint for Fastly and forwards received logs to Logz.io. It handles both Fastly's health check mechanism and log forwarding functionality, with configuration managed via URL query parameters.

## Prerequisites

Before creating your Fastly endpoint, review the URL Parameters Reference to understand the required and optional parameters you'll need to include in your endpoint URL:

**URL Parameters Reference**

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `service_id` | Yes | Your Fastly Service ID | `service_id=YOUR_SERVICE_ID` |
| `token` | Yes | Your Logz.io logs shipping token | `token=LOGZIO_SHIPPING_TOKEN` |
| `host` | Yes | The Logz.io listener host address (may vary by region) | `host=listener.logz.io` or `host=listener-eu.logz.io` |
| `type` | No | Custom log type to be assigned in Logz.io (default: `fastly-logs`) | `type=my-custom-logs` |
| `debug` | No | Set to `true` to enable debug logging (default: `false`) | `debug=true` |


## 1. Create a Logz.io HTTPS Endpoint in Fastly

1. Log into your Fastly account and select your service
2. Go to **Logging** → **Create a new endpoint** → **HTTPS**
3. Configure the following settings:

| Setting | Value |
|---------|-------|
| Name | `Logz.io Logs` (or any name you prefer) |
| URL | `https://fastly.listener-logz.io/?service_id=YOUR_SERVICE_ID&token=<<LOGZIO_SHIPPING_TOKEN>>&host=<<LOGZIO_LISTENER_ADDRESS>>` |
| Method | `POST` |
| Format Version | `2` |
| Response Condition | Leave blank |
| Content Type | `application/json` |
| Maximum Batch Size | `0` (no limit) or your preferred size |
| JSON log entry format | Use newline-delimited JSON |
| Request Compression | Gzip (optional but recommended) |

## 2. Configure Your Log Format

The Lambda function is format-agnostic. Below is an example of a comprehensive log format that includes common fields, but you can customize it based on your needs:

```json
{"@timestamp":"%{begin:%Y-%m-%dT%H:%M:%SZ}t","time_elapsed_msec":"%{time.elapsed.msec}V","is_tls":"%{if(req.is_ssl, \"true\", \"false\")}V","client_ip":"%h","message":"%m %U returned %>s for %h on %v in %{time.elapsed.msec}Vms (UA: %{User-Agent}i, Cache: %{fastly_info.state}V)" ,"client_geo_city":"%{client.geo.city}V","client_geo_country_code":"%{client.geo.country_code}V","client_geo_continent_code":"%{client.geo.continent_code}V","client_geo_region":"%{client.geo.region}V","http_host":"%v","http_method":"%m","http_url":"%U","http_protocol":"%H","http_status_code":"%>s","http_referer":"%{Referer}i","http_user_agent":"%{User-Agent}i","bytes_received_from_client":"%I","bytes_sent_to_client":"%O","resp_content_type":"%{Content-Type}o","fastly_service_id":"%{req.service_id}V","fastly_service_version":"%{req.vcl.version}V","fastly_pop":"%{server.identity}V","fastly_region":"%{server.region}V","fastly_cache_status":"%{fastly_info.state}V","fastly_is_h2":"%{if(fastly_info.is_h2, \"true\", \"false\")}V","fastly_is_h3":"%{if(fastly_info.is_h3, \"true\", \"false\")}V","tls_client_protocol":"%{tls.client.protocol}V","tls_client_cipher":"%{tls.client.cipher}V","tls_client_ciphers_sha":"%{tls.client.ciphers_sha}V","tls_client_iana_chosen_cipher_id":"%{tls.client.iana_chosen_cipher_id}V","fastly_error_details":"%{fastly.error}V"}
```

### Customizing Your Log Format

You can customize the log format to include only the fields you need. The Lambda function will forward whatever JSON structure you define. Here are some tips for customization:

* **Required Fields for Logz.io**:
   - `@timestamp` - Required for proper log indexing, must be in ISO 8601 format (e.g., `%{begin:%Y-%m-%dT%H:%M:%SZ}t`)
   - `message` - A human-readable log message (recommended for better log readability)

* **Important Note About Service ID**:
   - While you provide the `service_id` as a URL parameter, this is only used by the Lambda for processing
   - The service ID is NOT automatically added to the logs sent to Logz.io
   - If you want to see or filter by service ID in Logz.io, you must include it in your Fastly log format (e.g., `%{req.service_id}V`)

* **Optional Fastly Fields to Consider**:
   - `fastly_service_id` - For service identification in Logz.io (`%{req.service_id}V`)
   - `fastly_service_version` - For version tracking (`%{req.vcl.version}V`)
   - `fastly_pop` - Point of Presence information (`%{server.identity}V`)
   - `fastly_region` - Geographic region information (`%{server.region}V`)
   - `fastly_cache_status` - Cache hit/miss status (`%{fastly_info.state}V`)

* **Common Fields to Consider**:
   - HTTP method, URL, and status code
   - Client IP and geo information
   - Response time
   - Error details if applicable

* **Format Options**:
   - Use Fastly's VCL variables (prefixed with `%{...}V`)
   - Include request headers (prefixed with `%{...}i`)
   - Add response headers (prefixed with `%{...}o`)
   - Use standard format specifiers (like `%h` for client IP)
   - Use consistent field names across your logging

For more information about available Fastly logging variables, refer to the [Fastly VCL Variables documentation](https://developer.fastly.com/reference/vcl/variables/).

## 3. Build the HTTPS Endpoint URL

Your URL should include the following required parameters:

```
https://fastly.listener-logz.io/?service_id=YOUR_SERVICE_ID&token=<<LOGZIO_SHIPPING_TOKEN>>&host=<<LOGZIO_LISTENER_ADDRESS>>
```

**URL Parameters Reference**

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `service_id` | Yes | Your Fastly Service ID | `service_id=YOUR_SERVICE_ID` |
| `token` | Yes | Your Logz.io logs shipping token | `token=LOGZIO_SHIPPING_TOKEN` |
| `host` | Yes | The Logz.io listener host address (may vary by region) | `host=listener.logz.io` or `host=listener-eu.logz.io` |
| `type` | No | Custom log type to be assigned in Logz.io (default: `fastly-logs`) | `type=my-custom-logs` |
| `debug` | No | Set to `true` to enable debug logging (default: `false`) | `debug=true` |

Replace:
- `YOUR_SERVICE_ID` with your Fastly Service ID
- `LOGZIO_SHIPPING_TOKEN` with your Logz.io shipping token
- `LOGZIO_LISTENER_ADDRESS` with your Logz.io listener host (e.g., `listener.logz.io` or region-specific host)

For region-specific listener hosts, refer to the [Logz.io Regions documentation](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/).

## 4. Viewing Your Logs in Logz.io

After configuring the endpoint:
1. Generate some traffic to your Fastly service
2. Wait a few moments (typically less than 1 minute) for logs to appear
3. Log into your Logz.io account
4. Go to the Logs tab
5. Search for `type:fastly-logs` to see your Fastly logs (or `type:YOUR_CUSTOM_TYPE` if you specified a custom type using the `type` parameter)

## Technical Implementation Details

### Architecture Overview

This implementation follows this flow:

1. **Request Handling**: AWS API Gateway receives requests from Fastly
2. **Lambda Processing**:
   - Validates query parameters
   - Handles health checks (required by Fastly)
   - Processes incoming log data
   - Forwards logs to Logz.io
3. **Response**: Returns appropriate responses to Fastly

### Request Types

The Lambda function handles two types of requests:

1. **Health Check Requests**: Fastly periodically sends requests to `/.well-known/fastly/logging/challenge` to verify the endpoint is working
   - The function calculates a SHA256 hash of the service_id and returns it as plain text
   - This is required by Fastly to validate the endpoint

2. **Log Forwarding Requests**: Fastly sends log data via POST to the configured endpoint
   - The function receives the log data from the request body
   - Handles base64 encoding and gzip compression
   - Forwards the logs to Logz.io using the provided token and host

### Error Handling

- The function implements a retry mechanism for transient failures
- All errors are logged to CloudWatch for monitoring
- The function always returns 200 to Fastly, even on downstream errors, to prevent retry storms

## Release Process

This project uses GitHub Actions to automate the release process. When a new release is published on GitHub, the Lambda function is automatically deployed to AWS.

### Creating a New Release

1. Create a new release on GitHub with a version number tag (e.g., "1.0.1")
2. The release workflow will automatically:
   - Update the version.py file with the release tag version
   - Package the Lambda function
   - Deploy it to AWS Lambda
   - Update the function configuration

### Required GitHub Secrets

The following secrets need to be configured in your GitHub repository:

- `AWS_ACCESS_KEY_ID`: AWS access key with permissions to update Lambda
- `AWS_SECRET_ACCESS_KEY`: AWS secret key

### Required GitHub Variables

The following variables need to be configured in your GitHub repository:

- `AWS_REGION`: AWS region where your Lambda is deployed
- `AWS_LAMBDA_FUNCTION_NAME`: Name of your Lambda function

## Setup and Deployment

### Lambda Setup

1. Create a new Python 3.11+ Lambda function
2. Upload the `lambda_function.py` and `version.py` files
3. No environment variables required as all configuration is via query parameters
4. Set the Lambda timeout to at least 30 seconds
5. Set the memory allocation based on your log volume (128MB is usually sufficient)

### API Gateway Configuration

1. Create a new HTTP API in API Gateway
2. Create the following routes:
   - `GET /.well-known/fastly/logging/challenge` → Lambda integration
   - `POST /logs` → Lambda integration
3. Ensure query string parameters are passed to the Lambda
4. Deploy the API to a stage (e.g., `prod`)

### IAM Role Configuration

The Lambda function requires an IAM role with the following policies:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

## Monitoring and Troubleshooting

- Monitor the Lambda function's CloudWatch Logs for execution details and errors
- Debug Mode: To enable detailed debug logging, add `debug=true` to your query parameters
- Setting `debug=true` changes the logger level to DEBUG, showing more detailed logs
- Logs include the service ID for easy filtering
- Check CloudWatch Metrics for Lambda execution time, memory usage, and error rates