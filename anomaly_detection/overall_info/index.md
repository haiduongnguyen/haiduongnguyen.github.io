# Logs and Metrics data 

## Overview

Reference: 

https://www.splunk.com/en_us/blog/learn/log-data.html

Logs data: 

**Log data consists** of time-stamped, automatically generated records from applications, servers, and network devices, providing a detailed, chronological view of system activity and user behavior.

With this data, IT professionals are able to:

- Debug and troubleshoot issues
- Track progress and results
- [Monitor performance](https://www.splunk.com/en_us/blog/learn/it-monitoring.html)
- Gain valuable insights to inform decision-making
- [Audit and analyze security events](https://www.splunk.com/en_us/blog/learn/cybersecurity-analytics.html)
- Detect patterns or trends

Types of logs data: 

![image.png](attachment:7179cb4e-5c2a-450d-a3db-d5da1d96087d:image.png)

**Using tools for log data analysis**

There are many tools available to help you analyze log data, depending on what type of information you need, your organizational goals, your budget and many other factors. Some go-to solutions include:

- [Splunk](https://www.splunk.com/en_us/blog/learn/what-splunk-does.html)
- ELK/Elastic Stack
- Logz.io
- Graylog
- Loggly

Metrics 

![image.png](attachment:2b42376c-ed47-438f-9db1-8f20bb520797:image.png)

Dummy logs and metrics data

Use Chat GPT for generate dummy data

### 1) `sample_logs.csv` (1,000 rows)

**Columns**

- `timestamp` (ISO 8601, UTC, ms precision)
- `level` (`DEBUG|INFO|WARN|ERROR`)
- `service` (e.g., `auth-service`, `orders`, `inventory`)
- `host` (e.g., `ip-10-0-12-15`)
- `region` (`us-east-1`, `us-west-2`, `eu-central-1`, `ap-southeast-1`)
- `trace_id`, `span_id` (hex)
- `user_id` (nullable, `user_###`)
- `client_ip`
- `http_method` (`GET|POST|PUT|PATCH|DELETE`)
- `path` (templatized endpoints expanded, e.g., `/api/v1/orders/1234`)
- `status_code` (common HTTP codes, realistic distribution)
- `latency_ms` (log-normal skew)
- `bytes_sent` (log-normal skew)
- `message` (short description)

### 2) `sample_metrics.csv` (1,000 rows)

**Columns**

- `timestamp` (ISO 8601, UTC, second precision)
- `metric_name` (e.g., `cpu.utilization`, `memory.usage`, `disk.iops`, `http.requests`, `http.errors`, `queue.depth`)
- `value` (bounded/typed per metric)
- `unit` (`%`, `MB`, `ops/s`, `req/s`, `err/s`, `messages`)
- `service`, `host`, `region`
- `labels` (compact JSON string, e.g., `{"env":"prod","az":"b","version":"v3.2.1"}`)
- `aggregation` (`gauge|sum|avg|max|min`)
- `window_s` (1, 5, 10, 30, 60)


Download the sample logs data: [application_logs.jsonl](./application_logs.jsonl)


Download the sample logs data: [apm_metrics.jsonl](./apm_metrics.jsonl)


Code for generate logs: [generate_logs.py](./generate_logs.py)

Code for generate logs: [generate_metrics.py](./generate_metrics.py)
