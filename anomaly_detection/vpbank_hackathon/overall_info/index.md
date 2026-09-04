---
title: "Synthetic Logs and Metrics: What the Files Contain"
title_vi: "Logs và metrics giả lập: dữ liệu trong từng file"
title_en: "Synthetic Logs and Metrics: What the Files Contain"
description: Two linked JSONL datasets contain 1,500 application-log and APM-metric records for anomaly-detection experiments.
description_vi: Hai bộ JSONL liên kết chứa 1.500 application log và APM metric để thử nghiệm anomaly detection.
description_en: Two linked JSONL datasets contain 1,500 application-log and APM-metric records for anomaly-detection experiments.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly_detection/vpbank_hackathon/overall_info/
---

{% capture article_en %}
🔙 [Back to Home](/)

# Synthetic Logs and Metrics: What the Files Contain

Logs explain discrete events; metrics describe numeric behavior over time. I generated both so an anomaly-detection experiment can connect an unusual measurement with the application activity around it.

The published artifacts are synthetic. They do not contain customer or internal production data.

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

The trace and span identifiers provide the connection between the log and metric views. The `is_anomaly` field is synthetic ground truth for evaluating a detector; it should not be used as an input feature.

## The generators model anomalies at trace-chain level

The two scripts use a shared trace-chain generator. For each request, they create spans across services and assign the same anomaly state to the generated chain. Normal and anomalous values are sampled from different configured ranges.

- [`generate_logs.py`](./generate_logs.py) writes the application-log records.
- [`generate_metrics.py`](./generate_metrics.py) writes the APM-metric records.

The current scripts reference `trace_chain.py`, `topology.json`, `config_logs.yaml`, and `config_metrics.yaml`, which are not present in this repository. The JSONL artifacts can be downloaded and inspected, but the datasets cannot currently be regenerated from the two published scripts alone.

## Keep the two signals separate before combining them

Logs and metrics answer different questions. A latency spike shows that behavior changed; the related log message, service, path, and trace context can help explain what happened at that time. Keeping both tables linked by trace identifiers preserves that distinction for later anomaly-detection and root-cause-analysis experiments.

Reference: [Splunk — What is log data?](https://www.splunk.com/en_us/blog/learn/log-data.html)
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Logs và metrics giả lập: dữ liệu trong từng file

Log giải thích từng event đã xảy ra; metric mô tả numeric behavior theo thời gian. Tôi tạo cả hai để một anomaly-detection experiment có thể kết nối measurement bất thường với application activity diễn ra quanh nó.

Các artifact được công bố hoàn toàn là synthetic data, không chứa dữ liệu khách hàng hoặc dữ liệu production nội bộ.

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

Trace ID và span ID tạo liên kết giữa góc nhìn log và metric. Field `is_anomaly` là synthetic ground truth để đánh giá detector; không được dùng làm input feature.

## Generator tạo anomaly ở cấp trace chain

Hai script sử dụng chung một trace-chain generator. Với mỗi request, chúng tạo các span đi qua nhiều service và gán cùng anomaly state cho chain được tạo. Normal và anomalous value được sample từ các configured range khác nhau.

- [`generate_logs.py`](./generate_logs.py) ghi application-log record.
- [`generate_metrics.py`](./generate_metrics.py) ghi APM-metric record.

Các script hiện tại tham chiếu đến `trace_chain.py`, `topology.json`, `config_logs.yaml` và `config_metrics.yaml`, nhưng các file này chưa có trong repository. Có thể tải xuống và kiểm tra các JSONL artifact, nhưng hiện chưa thể regenerate dataset chỉ bằng hai script đã công bố.

## Giữ hai signal riêng trước khi kết hợp

Log và metric trả lời hai câu hỏi khác nhau. Latency spike cho biết behavior đã thay đổi; log message, service, path và trace context liên quan giúp giải thích điều gì xảy ra tại thời điểm đó. Giữ hai bảng liên kết bằng trace ID bảo toàn sự khác biệt này cho anomaly-detection và root-cause-analysis experiment sau này.

Tham khảo: [Splunk — What is log data?](https://www.splunk.com/en_us/blog/learn/log-data.html)
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
