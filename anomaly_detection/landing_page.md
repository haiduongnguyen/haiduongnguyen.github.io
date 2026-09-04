---
title: "Anomaly Detection: From a Competition to My Master's Thesis"
title_vi: "Anomaly Detection: từ cuộc thi đến luận văn thạc sĩ"
title_en: "Anomaly Detection: From a Competition to My Master's Thesis"
description: A project that began in a 2025 competition and became my multidimensional anomaly-detection thesis at Phenikaa University.
description_vi: Dự án bắt đầu từ một cuộc thi năm 2025 và trở thành luận văn anomaly detection đa chiều tại Đại học Phenikaa.
description_en: A project that began in a 2025 competition and became my multidimensional anomaly-detection thesis at Phenikaa University.
writing_topic: projects
project_order: 2
permalink: /anomaly_detection/landing_page.html
---

{% capture article_en %}
🔙 [Back to Home](/)

# Anomaly Detection: From a Competition to My Master's Thesis

My project studies how different anomaly-detection algorithms behave on multidimensional data. It began as a competition topic in October 2025 and became the subject of my master's thesis at Phenikaa University in January 2026.

## The project has two stages

- **October 2025 — competition:** I started with application logs and APM metrics, including synthetic data linked through trace and span identifiers.
- **January 2026 — master's thesis:** I kept the topic and began documenting the scope, model choices, root-cause-analysis question, and implementation milestones.

## Read the project in this order

1. [Inspect the synthetic logs and metrics dataset](/anomaly_detection/vpbank_hackathon/overall_info/).
2. [Understand why Isolation Forest isolates anomalies early](/anomaly_detection/isolation_forest/).
3. [Compare local density with Local Outlier Factor](/anomaly_detection/local_base_outlier_identify/).
4. [Read the rule I use when working with ChatGPT on my thesis](/anomaly_detection/master_thesis/).
5. [See how I reduced the first coding milestone](/anomaly-detection/thesis/first-assignment/).

The journal records the decisions in sequence so later results can be compared with the scope defined before implementation.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Anomaly Detection: từ cuộc thi đến luận văn thạc sĩ

Dự án của tôi nghiên cứu cách các thuật toán anomaly detection khác nhau hoạt động trên dữ liệu đa chiều. Dự án bắt đầu từ một đề tài thi vào tháng 10/2025 và trở thành chủ đề luận văn thạc sĩ của tôi tại Đại học Phenikaa vào tháng 1/2026.

## Dự án có hai giai đoạn

- **Tháng 10/2025 — cuộc thi:** tôi bắt đầu với application logs và APM metrics, gồm dữ liệu giả lập được liên kết bằng trace ID và span ID.
- **Tháng 1/2026 — luận văn thạc sĩ:** tôi giữ lại chủ đề này và bắt đầu ghi chép về scope, lựa chọn model, câu hỏi root-cause analysis và các milestone triển khai.

## Đọc dự án theo thứ tự này

1. [Xem bộ dữ liệu logs và metrics giả lập](/anomaly_detection/vpbank_hackathon/overall_info/).
2. [Hiểu vì sao Isolation Forest cô lập anomaly sớm](/anomaly_detection/isolation_forest/).
3. [So sánh mật độ cục bộ bằng Local Outlier Factor](/anomaly_detection/local_base_outlier_identify/).
4. [Đọc nguyên tắc tôi dùng khi làm luận văn với ChatGPT](/anomaly_detection/master_thesis/).
5. [Xem cách tôi thu hẹp milestone code đầu tiên](/anomaly-detection/thesis/first-assignment/).

Nhật ký ghi lại các quyết định theo trình tự để kết quả sau này có thể được so sánh với scope đã xác định trước khi triển khai.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
