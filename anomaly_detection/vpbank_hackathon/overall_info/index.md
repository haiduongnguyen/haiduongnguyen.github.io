---
title: "Synthetic Logs and Metrics: What the Files Contain"
title_vi: "Logs và metrics giả lập: dữ liệu trong từng file"
title_en: "Synthetic Logs and Metrics: What the Files Contain"
description: Two synthetic JSONL datasets contain application-log and APM-metric records, but their trace IDs reveal that they cannot yet be joined.
description_vi: Hai bộ JSONL giả lập chứa application log và APM metric, nhưng trace ID cho thấy hiện chưa thể join hai file.
description_en: Two synthetic JSONL datasets contain application-log and APM-metric records, but their trace IDs reveal that they cannot yet be joined.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly_detection/vpbank_hackathon/overall_info/
---

{% capture article_en %}
🔙 [Back to Home](/)

# Synthetic Logs and Metrics: What the Files Contain

Logs explain discrete events; metrics describe numeric behavior over time. I generated both for anomaly-detection experiments, but inspecting the published files exposes an important limitation: they are internally trace-structured, yet they cannot currently be joined to each other.

The published artifacts are synthetic. They do not contain customer or internal production data.

## The two files contain 600 traces, not 300 shared traces

The files have the same shape but were generated as separate datasets:

| File | Records | Unique traces | Spans per trace | Anomalous records | Anomalous traces |
| --- | ---: | ---: | ---: | ---: | ---: |
| `application_logs.jsonl` | 1,500 | 300 | 5 | 125 (8.33%) | 25 (8.33%) |
| `apm_metrics.jsonl` | 1,500 | 300 | 5 | 95 (6.33%) | 19 (6.33%) |

Every trace is internally consistent: all five spans in a trace share the same synthetic anomaly label. However, the two files have **zero shared trace IDs and zero shared span IDs**. The identifiers connect records inside each file, but do not connect a log record to a metric record in the other file.

## Application logs describe what happened

A log is a timestamped record emitted by an application, server, or device. Logs can support debugging, performance monitoring, progress tracking, security audits, and pattern analysis because each record carries event context.

The downloadable [`application_logs.jsonl`](./application_logs.jsonl) contains **1,500 records** with:

- `timestamp`
- `trace_id`, `span_id`, and `parent_span_id`
- `service`
- `level`
- `path`
- `message`
- `status`
- `latency_ms`
- `is_anomaly`

The sample contains services such as `payment-service`, log levels such as `WARN`, endpoint paths, HTTP-like status values, and latency measurements.

## APM metrics describe how the system behaved

The downloadable [`apm_metrics.jsonl`](./apm_metrics.jsonl) also contains **1,500 records**. Each record includes:

- `timestamp`
- `trace_id`, `span_id`, and `parent_span_id`
- `service`
- `cpu`
- `memory`
- `latency`
- `throughput`
- `is_anomaly`

The metric values in the published file range from `20.04` to `99.99` for CPU, `30.02` to `99.94` for memory, `20.01` to `899.59` for latency, and `50` to `200` for throughput. These ranges describe this synthetic artifact, not production operating limits.

The `is_anomaly` field is synthetic ground truth for evaluating a detector; it must not be used as an input feature. Because five rows share one trace and one label, train/test splitting should also happen by `trace_id`. A row-level random split could place sibling spans from the same synthetic request on both sides of the evaluation.

## The generators model anomalies at trace-chain level

The two scripts reference the same trace-chain design. For each request, they create spans across services and assign one anomaly state to the generated chain. Normal and anomalous values are sampled from different configured ranges.

- [`generate_logs.py`](./generate_logs.py) writes the application-log records.
- [`generate_metrics.py`](./generate_metrics.py) writes the APM-metric records.

The current scripts reference `trace_chain.py`, `topology.json`, `config_logs.yaml`, and `config_metrics.yaml`, which are not present in this repository. The JSONL artifacts can be downloaded and inspected, but the datasets cannot currently be regenerated from the two published scripts alone. This is a reproducibility gap, not merely a documentation gap.

## The current artifacts support separate experiments

The metric file can support numeric anomaly-detection experiments using CPU, memory, latency, and throughput. The log file can support experiments using level, service, path, message, status, and latency. Within either file, trace-level aggregation can preserve the five-span request structure.

The current files cannot support a valid claim that a metric anomaly was explained by the log messages from the same request. Similar timestamps or service names are not a safe substitute for a shared trace ID.

## Cross-signal RCA requires one shared generation pass

To create a genuinely linked dataset, one generated trace chain should be passed to both writers in the same run. The log and metric records for each span must reuse the same `trace_id`, `span_id`, `parent_span_id`, timestamp, service, and anomaly state; only the signal-specific fields should differ.

That design would make the intended analysis possible: a latency or CPU anomaly could be joined to the exact log events from the same request. Until the missing generator files are published and the identifiers are shared, the honest boundary is two separate synthetic experiments rather than one combined root-cause-analysis dataset.

Reference: [Splunk — What is log data?](https://www.splunk.com/en_us/blog/learn/log-data.html)
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Logs và metrics giả lập: dữ liệu trong từng file

Log giải thích từng event đã xảy ra; metric mô tả numeric behavior theo thời gian. Tôi tạo cả hai cho anomaly-detection experiment, nhưng khi kiểm tra các file đã công bố, một giới hạn quan trọng xuất hiện: mỗi file có cấu trúc trace nội bộ nhưng hiện chưa thể join với file còn lại.

Các artifact được công bố hoàn toàn là synthetic data, không chứa dữ liệu khách hàng hoặc dữ liệu production nội bộ.

## Hai file chứa 600 trace riêng biệt, không phải 300 trace dùng chung

Hai file có cùng hình dạng nhưng được tạo thành hai dataset riêng:

| File | Số record | Unique trace | Span mỗi trace | Anomalous record | Anomalous trace |
| --- | ---: | ---: | ---: | ---: | ---: |
| `application_logs.jsonl` | 1.500 | 300 | 5 | 125 (8,33%) | 25 (8,33%) |
| `apm_metrics.jsonl` | 1.500 | 300 | 5 | 95 (6,33%) | 19 (6,33%) |

Bên trong mỗi trace, dữ liệu nhất quán: cả năm span cùng mang một synthetic anomaly label. Tuy nhiên, hai file có **0 trace ID trùng nhau và 0 span ID trùng nhau**. Các identifier kết nối record bên trong từng file, nhưng không kết nối log record với metric record ở file còn lại.

## Application log mô tả điều gì đã xảy ra

Log là record có timestamp được tạo bởi application, server hoặc device. Log hỗ trợ debugging, performance monitoring, progress tracking, security audit và pattern analysis vì mỗi record mang theo event context.

File [`application_logs.jsonl`](./application_logs.jsonl) chứa **1.500 record** với:

- `timestamp`
- `trace_id`, `span_id` và `parent_span_id`
- `service`
- `level`
- `path`
- `message`
- `status`
- `latency_ms`
- `is_anomaly`

Sample có các service như `payment-service`, log level như `WARN`, endpoint path, giá trị tương tự HTTP status và latency measurement.

## APM metric mô tả hệ thống đã hoạt động thế nào

File [`apm_metrics.jsonl`](./apm_metrics.jsonl) cũng chứa **1.500 record**. Mỗi record gồm:

- `timestamp`
- `trace_id`, `span_id` và `parent_span_id`
- `service`
- `cpu`
- `memory`
- `latency`
- `throughput`
- `is_anomaly`

Trong metric file đã công bố, CPU nằm trong khoảng `20.04`–`99.99`, memory `30.02`–`99.94`, latency `20.01`–`899.59` và throughput `50`–`200`. Đây là range của synthetic artifact này, không phải production operating limit.

Field `is_anomaly` là synthetic ground truth dùng để đánh giá detector; tuyệt đối không được dùng làm input feature. Vì năm dòng cùng chia sẻ một trace và một label, train/test split cũng phải thực hiện theo `trace_id`. Random split theo từng dòng có thể đưa các sibling span của cùng một synthetic request vào cả train và test.

## Generator tạo anomaly ở cấp trace chain

Hai script tham chiếu cùng một thiết kế trace chain. Với mỗi request, chúng tạo các span đi qua nhiều service và gán một anomaly state cho chain được tạo. Normal và anomalous value được sample từ các configured range khác nhau.

- [`generate_logs.py`](./generate_logs.py) ghi application-log record.
- [`generate_metrics.py`](./generate_metrics.py) ghi APM-metric record.

Các script hiện tại tham chiếu đến `trace_chain.py`, `topology.json`, `config_logs.yaml` và `config_metrics.yaml`, nhưng các file này chưa có trong repository. Có thể tải xuống và kiểm tra các JSONL artifact, nhưng hiện chưa thể regenerate dataset chỉ bằng hai script đã công bố. Đây là reproducibility gap, không chỉ là thiếu documentation.

## Artifact hiện tại hỗ trợ hai experiment riêng

Metric file hỗ trợ numeric anomaly-detection experiment với CPU, memory, latency và throughput. Log file hỗ trợ experiment với level, service, path, message, status và latency. Trong từng file, trace-level aggregation có thể giữ lại cấu trúc request gồm năm span.

Các file hiện tại không hỗ trợ một claim hợp lệ rằng metric anomaly được giải thích bằng log message của cùng request. Timestamp hoặc service name tương tự không phải lựa chọn an toàn thay cho shared trace ID.

## Cross-signal RCA cần một shared generation pass

Để tạo dataset thực sự liên kết, cùng một trace chain phải được đưa cho cả hai writer trong cùng một lần chạy. Log record và metric record của từng span phải dùng chung `trace_id`, `span_id`, `parent_span_id`, timestamp, service và anomaly state; chỉ các field riêng của từng signal được phép khác nhau.

Thiết kế đó mới cho phép phân tích đúng mục tiêu: một latency hoặc CPU anomaly có thể được join với chính xác log event từ cùng request. Cho đến khi các generator file còn thiếu được công bố và identifier được dùng chung, giới hạn trung thực là hai synthetic experiment riêng thay vì một cross-signal root-cause-analysis dataset.

Tham khảo: [Splunk — What is log data?](https://www.splunk.com/en_us/blog/learn/log-data.html)
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
