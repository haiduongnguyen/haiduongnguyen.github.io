---
title: Thesis Scope and First Milestone
title_vi: Scope luận văn và milestone đầu tiên
title_en: Thesis scope and first milestone
description: Research scope, pipeline, baselines, and acceptance criteria for a multidimensional anomaly-detection thesis.
description_vi: Scope, pipeline, baseline và acceptance criteria cho luận văn anomaly detection đa chiều.
description_en: Research scope, pipeline, baselines, and acceptance criteria for a multidimensional anomaly-detection thesis.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly-detection/thesis/first-assignment/
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}
## Anomaly detection

**My master thesis is "Method of applied different algorithms on multidimension data"**

🔙 [Back to Home](/)

## Chat GPT ask me:

### Step 1 – Define the Project Scope (Mandatory)

Write down clear answers to the following three questions:

1. What is your primary data type?  

Choose one main type first:  

Multivariate tabular data  

Multivariate time-series data  

Recommendation: start with tabular data, then extend to time series later if time allows.  

2. How many anomaly detection models will you implement?  

Do not be over-ambitious.

Recommended for a Master’s thesis:

Isolation Forest

Autoencoder

(+ LOF or One-Class SVM only if time permits)

2 models = solid
3 models = very good
More than 3 = unnecessary risk

3. What is the basis of your Root Cause Analysis (RCA)?

You must be able to express this in one clear sentence.

Examples:

“RCA is based on feature contribution analysis.”

“RCA is based on reconstruction error from Autoencoders.”

❌ Avoid vague answers such as “general RCA” or “multiple methods”.

## My answer  

1. What is your primary data type?  
- For MVP1, I will choose multivariate tabular data  

2. How many anomaly detection models will you implement?
I think 3:
- Isolation forest  
- LOF  
- Autoencoder  

3. What is the basis of your Root Cause Analysis (RCA)?  
Cannot answer right now, I need to read more documents.  


### Task 2 – Pipeline Definition (Required)
The pipeline of this project (as now):
- Data input
- Data preprocessing
- Anomaly detection algorithms
- Root cause analysis
- Evaluation
- Visualization

### Task 3 – First Coding Milestone (Required)

Implement a minimal end-to-end pipeline with:

One dataset loader

One preprocessing step (scaling only)

One anomaly detector (only one model)

One script that runs everything once

No ensembles. No advanced RCA. No tuning.
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Thesis milestone 01</p><h1>Scope trước khi code</h1><p>Mục tiêu của milestone là biến một chủ đề rộng thành câu hỏi có dữ liệu, baseline và cách kiểm chứng cụ thể.</p></header>
  <h2>Định nghĩa bài toán</h2><ul><li><strong>Input:</strong> chuỗi metrics theo thời gian và event logs đã được tổng hợp/giả lập.</li><li><strong>Output:</strong> anomaly score theo timestamp và nhóm signal, kèm ngữ cảnh để review.</li><li><strong>Ngoài scope:</strong> root-cause automation và real-time production deployment trong giai đoạn đầu.</li></ul>
  <h2>Pipeline tối thiểu</h2><ol class="process"><li>Kiểm tra schema, missingness và sampling interval.</li><li>Tạo rule baseline theo robust z-score/seasonal residual.</li><li>Tạo window feature không dùng dữ liệu tương lai.</li><li>Fit Isolation Forest và LOF làm baseline ML.</li><li>Đánh giá trên incident label và injected anomaly.</li><li>Review false positives theo từng loại signal.</li></ol>
  <h2>Acceptance criteria</h2><ul><li>Pipeline tái lập được từ raw synthetic data.</li><li>Mọi model được so với ít nhất một rule baseline.</li><li>Không có temporal leakage trong feature hoặc split.</li><li>Report precision/recall theo event window, alert volume và detection delay.</li><li>Ghi lại failure mode, không chỉ best score.</li></ul>
  <h2>Phần bổ sung: đóng scope thành các phase kiểm chứng được</h2><h3>Phase 1 và phase 2 cần dùng hai dataset contract khác nhau</h3><p>Original answer chọn multivariate tabular cho MVP1, trong khi hướng hiện tại nói về logs/metrics theo thời gian. Có thể giữ cả hai bằng cách tuyên bố rõ: Phase 1 dùng một row/window làm tabular observation để kiểm tra pipeline; Phase 2 thêm temporal split, seasonality và event-level evaluation. Không được dùng kết quả random split của Phase 1 như bằng chứng cho time-series deployment.</p><h3>Ba model là upper bound, không phải minimum</h3><p>Rule baseline + Isolation Forest đủ cho milestone đầu. LOF chỉ thêm khi local-density hypothesis có lý do; Autoencoder chỉ thêm khi dataset và validation đủ để biện minh độ phức tạp. Một model được đánh giá tốt có giá trị hơn ba model chỉ có một bảng score.</p><h3>“Chưa trả lời được RCA” trở thành một deliverable</h3><p>Trước khi code RCA, lập taxonomy ground truth: incident nào có component/feature gây lỗi đã biết, ai xác nhận và mức uncertainty. So sánh explanation output với known affected signals; nếu không có nhãn này, chỉ gọi kết quả là diagnostic context, không gọi root cause.</p><h3>Definition of done cho MVP1</h3><ul><li>Một command tái tạo data → feature → score → report.</li><li>Temporal boundary được kiểm tra bằng automated test.</li><li>Threshold chỉ được chọn trên validation segment.</li><li>Report gồm alert volume, delay và ít nhất 20 false-positive review.</li><li>Experiment manifest lưu data hash, seed và config.</li></ul>
  <h2>Milestone code đầu tiên</h2><p>Build một notebook hoặc script tạo feature và baseline trên một metric, kèm test nhỏ xác nhận feature ở thời điểm t không đọc dữ liệu sau t.</p>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Thesis milestone 01</p><h1>Scope before code</h1><p>This milestone turns a broad topic into a question with explicit data, baselines, and validation.</p></header>
  <h2>Problem definition</h2><ul><li><strong>Input:</strong> metric time series and aggregated or synthetic event logs.</li><li><strong>Output:</strong> an anomaly score by timestamp and signal group, with review context.</li><li><strong>Out of scope:</strong> automated root-cause analysis and real-time production deployment in the first phase.</li></ul>
  <h2>Minimum pipeline</h2><ol class="process"><li>Inspect schema, missingness, and sampling intervals.</li><li>Build a robust z-score or seasonal-residual rule baseline.</li><li>Create window features without future information.</li><li>Fit Isolation Forest and LOF as ML baselines.</li><li>Evaluate on incident labels and injected anomalies.</li><li>Review false positives by signal type.</li></ol>
  <h2>Acceptance criteria</h2><ul><li>The pipeline is reproducible from raw synthetic data.</li><li>Every model is compared with at least one rule baseline.</li><li>No temporal leakage exists in features or splits.</li><li>Report event-window precision/recall, alert volume, and detection delay.</li><li>Document failure modes, not only the best score.</li></ul>
  <h2>Extension: close the scope with testable phases</h2><h3>Phase 1 and Phase 2 need different dataset contracts</h3><p>The original answer chooses multivariate tabular data for MVP1, while the current direction discusses temporal logs and metrics. Keep both by stating the phases explicitly: Phase 1 treats one row/window as a tabular observation to verify the pipeline; Phase 2 adds temporal splits, seasonality, and event-level evaluation. A random-split Phase 1 result is not evidence for time-series deployment.</p><h3>Three models are an upper bound, not a minimum</h3><p>A rule baseline plus Isolation Forest is enough for the first milestone. Add LOF only when a local-density hypothesis is justified, and add an autoencoder only when data volume and validation justify the complexity. One well-evaluated model is worth more than three names in a score table.</p><h3>“I cannot answer RCA yet” becomes a deliverable</h3><p>Before coding RCA, define a ground-truth taxonomy: which incidents have a known affected component/feature, who confirmed it, and with what uncertainty. Compare explanation output with known affected signals; without this label, call the output diagnostic context rather than root cause.</p><h3>Definition of done for MVP1</h3><ul><li>One command reproduces data → features → scores → report.</li><li>An automated test verifies temporal boundaries.</li><li>The threshold is selected only on a validation segment.</li><li>The report includes alert volume, delay, and at least 20 false-positive reviews.</li><li>An experiment manifest stores the data hash, seed, and configuration.</li></ul>
  <h2>First coding milestone</h2><p>Build one notebook or script that creates features and a baseline for one metric, including a small test proving that a feature at time t never reads data after t.</p>
</article>
