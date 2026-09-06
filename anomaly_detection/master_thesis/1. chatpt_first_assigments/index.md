---
title: "Before Coding My Thesis, I Had to Cut the Scope"
title_vi: "Trước khi code luận văn, tôi phải thu hẹp scope"
title_en: "Before Coding My Thesis, I Had to Cut the Scope"
description: The first thesis milestone fixes the data type, model list, unresolved RCA question, and minimum end-to-end pipeline.
description_vi: Milestone đầu tiên chốt loại dữ liệu, danh sách model, câu hỏi RCA chưa giải quyết và pipeline end-to-end tối thiểu.
description_en: The first thesis milestone fixes the data type, model list, unresolved RCA question, and minimum end-to-end pipeline.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly-detection/thesis/first-assignment/
---

{% capture article_en %}
🔙 [Back to Home](/)

# Before Coding My Thesis, I Had to Cut the Scope

My master's thesis is **“Method of applied different algorithms on multidimension data.”** The first assignment from ChatGPT was not to implement a model. It was to make the project small and explicit enough to finish and defend.

The result was a decision register, not a model. It separates choices already made from questions that still require evidence:

| Decision | Current status | Consequence |
| --- | --- | --- |
| Primary data structure | Multivariate tabular data | Time-series modeling stays outside MVP1 |
| Initial detectors | Isolation Forest, LOF, and Autoencoder | No fourth model enters the first comparison |
| RCA definition | Unresolved | Literature review must precede implementation |
| First milestone | One end-to-end run | Tuning and ensembles wait until the pipeline works |

## Choose one primary data structure

The initial choice was between:

- Multivariate tabular data.
- Multivariate time-series data.

The recommendation was to start with tabular data and extend to time series only if time allowed. My decision for MVP1 was therefore **multivariate tabular data**.

## Limit the number of anomaly detectors

The suggested scope was:

- Isolation Forest.
- Autoencoder.
- LOF or One-Class SVM only if time permitted.

Two well-evaluated models would provide a defensible comparison. A third can add a genuinely different mechanism; more than three would increase implementation and evaluation work without automatically strengthening the research question.

I initially selected three:

1. Isolation Forest.
2. Local Outlier Factor.
3. Autoencoder.

This is already wider than the safest recommendation, so additional models should not enter MVP1.

The three models were not selected as interchangeable names. Isolation Forest uses random partitioning, LOF compares local density, and an Autoencoder can use reconstruction error. Their different anomaly evidence makes the comparison more informative than adding several small variations of the same mechanism.

## Do not use “general RCA” as a definition

Root-cause analysis must have an explicit basis, for example feature-contribution analysis or reconstruction error from an autoencoder. I could not answer this question at the time of the assignment and recorded it as unresolved rather than choosing a vague definition.

That unresolved decision affects both model selection and evaluation, so it needs literature review before the RCA stage is implemented.

A useful RCA output must identify its unit and evidence. For example, a trace-level anomaly might be explained by feature deviations aggregated across its spans, while an Autoencoder may expose features with large reconstruction error. Neither output is automatically a causal root cause; the thesis must define the narrower claim it can evaluate.

## Define the whole pipeline before optimizing a model

The planned project pipeline is:

1. Data input.
2. Data preprocessing.
3. Anomaly-detection algorithms.
4. Root-cause analysis.
5. Evaluation.
6. Visualization.

## The first coding milestone contains one of everything

The minimum end-to-end version contains:

- One dataset loader.
- One preprocessing step: scaling only.
- One anomaly detector.
- One script that runs the pipeline once.

No ensemble, advanced RCA, or tuning belongs in this milestone. Its purpose is to prove that data can travel through the entire pipeline before additional models increase the scope.

## The evaluation contract must be defined before tuning

The synthetic dataset contains five spans per trace with one shared anomaly label. This means the train/test boundary must be created by `trace_id`, not by individual rows. Otherwise, sibling spans from one generated request can appear in both sets.

The first comparison should keep the data split, preprocessing, and alert budget fixed across models. Useful outputs include precision and recall for the minority anomaly class, a precision–recall curve, performance at a fixed number of alerts, and fit/scoring time. A model should not win merely because it was evaluated at a more favorable threshold.

## MVP1 has a clear stopping condition

MVP1 is complete when one command can load the data, create a trace-safe split, fit preprocessing on the reference portion, train one detector, score the evaluation portion, and save reproducible metrics. It is not complete when a notebook happens to display an anomaly score once.

After that contract works for one detector, the next model can enter without changing the evaluation underneath it. Scope control here is not about making the thesis smaller for its own sake; it keeps each comparison attributable to the algorithm rather than to a moving pipeline.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Trước khi code luận văn, tôi phải thu hẹp scope

Luận văn thạc sĩ của tôi là **“Method of applied different algorithms on multidimension data.”** Assignment đầu tiên từ ChatGPT không phải triển khai model mà là làm cho project đủ nhỏ và rõ ràng để có thể hoàn thành và bảo vệ.

Kết quả là một decision register, không phải model. Nó tách những lựa chọn đã chốt khỏi các câu hỏi còn cần evidence:

| Quyết định | Trạng thái hiện tại | Hệ quả |
| --- | --- | --- |
| Primary data structure | Multivariate tabular data | Time-series modeling nằm ngoài MVP1 |
| Initial detector | Isolation Forest, LOF và Autoencoder | Không đưa model thứ tư vào lần so sánh đầu tiên |
| Định nghĩa RCA | Chưa giải quyết | Literature review phải có trước implementation |
| Milestone đầu tiên | Một end-to-end run | Tuning và ensemble chờ đến khi pipeline hoạt động |

## Chọn một primary data structure

Lựa chọn ban đầu gồm:

- Multivariate tabular data.
- Multivariate time-series data.

Khuyến nghị là bắt đầu bằng tabular data và chỉ mở rộng sang time series nếu còn thời gian. Vì vậy, quyết định của tôi cho MVP1 là **multivariate tabular data**.

## Giới hạn số anomaly detector

Scope được đề xuất:

- Isolation Forest.
- Autoencoder.
- LOF hoặc One-Class SVM chỉ khi thời gian cho phép.

Hai model được đánh giá kỹ đã đủ tạo một phép so sánh có thể bảo vệ. Model thứ ba có thể bổ sung một mechanism thực sự khác; nhiều hơn ba sẽ tăng implementation và evaluation work mà không tự động làm research question mạnh hơn.

Ban đầu tôi chọn ba model:

1. Isolation Forest.
2. Local Outlier Factor.
3. Autoencoder.

Scope này đã rộng hơn khuyến nghị an toàn nhất, vì vậy không thêm model khác vào MVP1.

Ba model không được chọn như những cái tên có thể thay thế nhau. Isolation Forest dùng random partition, LOF so sánh local density, còn Autoencoder có thể dùng reconstruction error. Anomaly evidence khác nhau khiến phép so sánh có ích hơn việc thêm nhiều biến thể nhỏ của cùng một mechanism.

## Không dùng “general RCA” làm định nghĩa

Root-cause analysis phải có cơ sở rõ ràng, chẳng hạn feature-contribution analysis hoặc reconstruction error từ autoencoder. Tại thời điểm nhận assignment, tôi chưa trả lời được câu hỏi này và ghi nhận nó là vấn đề chưa giải quyết thay vì chọn một định nghĩa mơ hồ.

Quyết định chưa chốt này ảnh hưởng đến cả model selection và evaluation, nên cần literature review trước khi triển khai RCA stage.

RCA output hữu ích phải xác định rõ đơn vị và evidence. Ví dụ, trace-level anomaly có thể được giải thích bằng feature deviation được aggregate qua các span; Autoencoder có thể chỉ ra feature có reconstruction error lớn. Không output nào tự động là causal root cause; luận văn phải xác định claim hẹp hơn mà nó có thể đánh giá.

## Xác định toàn bộ pipeline trước khi optimize model

Project pipeline dự kiến:

1. Data input.
2. Data preprocessing.
3. Anomaly-detection algorithms.
4. Root-cause analysis.
5. Evaluation.
6. Visualization.

## Coding milestone đầu tiên chỉ gồm một thành phần mỗi loại

Phiên bản end-to-end tối thiểu gồm:

- Một dataset loader.
- Một preprocessing step: chỉ scaling.
- Một anomaly detector.
- Một script chạy toàn bộ pipeline một lần.

Ensemble, advanced RCA và tuning không thuộc milestone này. Mục tiêu của nó là chứng minh dữ liệu có thể đi qua toàn bộ pipeline trước khi thêm model làm scope lớn hơn.

## Evaluation contract phải được xác định trước tuning

Synthetic dataset có năm span mỗi trace và dùng chung anomaly label. Vì vậy, train/test boundary phải được tạo theo `trace_id`, không phải từng dòng. Nếu không, sibling span của cùng một generated request có thể xuất hiện trong cả hai tập.

Phép so sánh đầu tiên phải giữ cố định data split, preprocessing và alert budget giữa các model. Output hữu ích gồm precision và recall cho minority anomaly class, precision–recall curve, performance tại một số alert cố định và fit/scoring time. Model không được thắng chỉ vì được đánh giá ở threshold thuận lợi hơn.

## MVP1 có stopping condition rõ ràng

MVP1 hoàn thành khi một command có thể load data, tạo trace-safe split, fit preprocessing trên reference portion, train một detector, score evaluation portion và lưu reproducible metric. Một notebook tình cờ hiển thị anomaly score một lần chưa đủ để coi là hoàn thành.

Sau khi contract này hoạt động với một detector, model tiếp theo có thể được thêm mà không thay đổi evaluation bên dưới. Kiểm soát scope không nhằm làm luận văn nhỏ đi; nó giúp khác biệt trong kết quả được quy về algorithm thay vì một pipeline liên tục thay đổi.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
