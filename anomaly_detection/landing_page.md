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

My project compares how anomaly-detection algorithms behave on multidimensional data. It began as a competition topic in October 2025 and became the subject of my master's thesis at Phenikaa University in January 2026. This page is the decision log and reading map; it does not claim final model results that have not yet been produced.

## The project has two stages

- **October 2025 — competition:** I started with application logs and APM metrics. Each synthetic file has its own trace structure, but the published files do not share identifiers with each other.
- **January 2026 — master's thesis:** I kept the topic and began documenting the scope, model choices, root-cause-analysis question, and implementation milestones.

## Read the project in this order

1. [Inspect the synthetic logs and metrics dataset](/anomaly_detection/vpbank_hackathon/overall_info/).
2. [Understand why Isolation Forest isolates anomalies early](/anomaly_detection/isolation_forest/).
3. [Compare local density with Local Outlier Factor](/anomaly_detection/local_base_outlier_identify/).
4. [Read the rule I use when working with ChatGPT on my thesis](/anomaly_detection/master_thesis/).
5. [See how I reduced the first coding milestone](/anomaly-detection/thesis/first-assignment/).

The journal records the decisions in sequence so later results can be compared with the scope defined before implementation.

## Each entry answers a different project question

| Entry | Question answered | Current boundary |
| --- | --- | --- |
| Synthetic logs and metrics | What is actually present in the published files? | The two JSONL files have no shared trace IDs and cannot yet support cross-signal RCA |
| Isolation Forest | Why can random partitions rank unusual points? | Detection score is separated from alert threshold and root-cause evidence |
| Local Outlier Factor | When does local density reveal what a global rule misses? | Distance, scaling, neighborhood size, and novelty deployment remain explicit choices |
| Thesis AI rule | What work can ChatGPT assist without owning the research? | Every claim, experiment, and decision must remain reproducible and defensible |
| First assignment | What is the smallest defensible first pipeline? | Tabular data, three candidate detectors, one trace-safe evaluation contract |

The next meaningful update is not another algorithm summary. It is a reproducible MVP that fixes one dataset split and evaluation protocol, then runs the first detector through that pipeline. Later results can then be compared with decisions recorded before the outcome was known.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Anomaly Detection: từ cuộc thi đến luận văn thạc sĩ

Dự án của tôi so sánh cách các thuật toán anomaly detection hoạt động trên dữ liệu đa chiều. Dự án bắt đầu từ một đề tài thi vào tháng 10/2025 và trở thành chủ đề luận văn thạc sĩ của tôi tại Đại học Phenikaa vào tháng 1/2026. Trang này là decision log và reading map; nó không công bố final model result chưa được tạo ra.

## Dự án có hai giai đoạn

- **Tháng 10/2025 — cuộc thi:** tôi bắt đầu với application logs và APM metrics. Mỗi synthetic file có trace structure riêng, nhưng hai file đã công bố không dùng chung identifier.
- **Tháng 1/2026 — luận văn thạc sĩ:** tôi giữ lại chủ đề này và bắt đầu ghi chép về scope, lựa chọn model, câu hỏi root-cause analysis và các milestone triển khai.

## Đọc dự án theo thứ tự này

1. [Xem bộ dữ liệu logs và metrics giả lập](/anomaly_detection/vpbank_hackathon/overall_info/).
2. [Hiểu vì sao Isolation Forest cô lập anomaly sớm](/anomaly_detection/isolation_forest/).
3. [So sánh mật độ cục bộ bằng Local Outlier Factor](/anomaly_detection/local_base_outlier_identify/).
4. [Đọc nguyên tắc tôi dùng khi làm luận văn với ChatGPT](/anomaly_detection/master_thesis/).
5. [Xem cách tôi thu hẹp milestone code đầu tiên](/anomaly-detection/thesis/first-assignment/).

Nhật ký ghi lại các quyết định theo trình tự để kết quả sau này có thể được so sánh với scope đã xác định trước khi triển khai.

## Mỗi entry trả lời một câu hỏi khác nhau của project

| Entry | Câu hỏi được trả lời | Giới hạn hiện tại |
| --- | --- | --- |
| Synthetic logs và metrics | Các file đã công bố thực sự chứa gì? | Hai JSONL file không có shared trace ID nên chưa hỗ trợ cross-signal RCA |
| Isolation Forest | Vì sao random partition có thể xếp hạng unusual point? | Detection score được tách khỏi alert threshold và root-cause evidence |
| Local Outlier Factor | Khi nào local density phát hiện điều global rule bỏ sót? | Distance, scaling, neighborhood size và novelty deployment vẫn là các lựa chọn phải chốt |
| Quy tắc dùng AI trong luận văn | ChatGPT có thể hỗ trợ phần nào mà không sở hữu research? | Mọi claim, experiment và quyết định phải reproduce và bảo vệ được |
| Assignment đầu tiên | Pipeline nhỏ nhất có thể bảo vệ là gì? | Tabular data, ba candidate detector và một trace-safe evaluation contract |

Update có ý nghĩa tiếp theo không phải một algorithm summary khác. Đó phải là một MVP reproducible, cố định một dataset split và evaluation protocol rồi chạy detector đầu tiên qua pipeline. Kết quả sau này khi đó mới có thể so với các quyết định được ghi trước khi biết outcome.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
