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

Two models would make a solid thesis, three would be very good, and more than three would add unnecessary delivery risk.

I initially selected three:

1. Isolation Forest.
2. Local Outlier Factor.
3. Autoencoder.

This is already wider than the safest recommendation, so additional models should not enter MVP1.

## Do not use “general RCA” as a definition

Root-cause analysis must have an explicit basis, for example feature-contribution analysis or reconstruction error from an autoencoder. I could not answer this question at the time of the assignment and recorded it as unresolved rather than choosing a vague definition.

That unresolved decision affects both model selection and evaluation, so it needs literature review before the RCA stage is implemented.

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
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Trước khi code luận văn, tôi phải thu hẹp scope

Luận văn thạc sĩ của tôi là **“Method of applied different algorithms on multidimension data.”** Assignment đầu tiên từ ChatGPT không phải triển khai model mà là làm cho project đủ nhỏ và rõ ràng để có thể hoàn thành và bảo vệ.

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

Hai model đủ tạo thành một luận văn vững; ba model là rất tốt; nhiều hơn ba tạo thêm delivery risk không cần thiết.

Ban đầu tôi chọn ba model:

1. Isolation Forest.
2. Local Outlier Factor.
3. Autoencoder.

Scope này đã rộng hơn khuyến nghị an toàn nhất, vì vậy không thêm model khác vào MVP1.

## Không dùng “general RCA” làm định nghĩa

Root-cause analysis phải có cơ sở rõ ràng, chẳng hạn feature-contribution analysis hoặc reconstruction error từ autoencoder. Tại thời điểm nhận assignment, tôi chưa trả lời được câu hỏi này và ghi nhận nó là vấn đề chưa giải quyết thay vì chọn một định nghĩa mơ hồ.

Quyết định chưa chốt này ảnh hưởng đến cả model selection và evaluation, nên cần literature review trước khi triển khai RCA stage.

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
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
