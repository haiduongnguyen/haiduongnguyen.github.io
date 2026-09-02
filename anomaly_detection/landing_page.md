---
title: Anomaly Detection
title_vi: Phát hiện bất thường
title_en: Anomaly detection
description: Notes and project work on detecting anomalies in multidimensional logs and metrics.
description_vi: Ghi chép và dự án về phát hiện bất thường trong dữ liệu logs và metrics đa chiều.
description_en: Notes and project work on detecting anomalies in multidimensional logs and metrics.
writing_topic: projects
project_order: 2
permalink: /anomaly_detection/landing_page.html
---

<details class="original-archive" data-original-source="true" data-lang="en">
<summary>Original page notes (preserved in full)</summary>
{% capture original_page_content %}
## Anomaly detection

**My master thesis is "Method of applied different algorithms on multidimension data"**

🔙 [Back to Home](/)

## Pages

- [Isolation forest](/anomaly_detection/isolation_forest/)
- [Local Outlier Factor](/anomaly_detection/local_base_outlier_identify)

## My journey of doing this:
- 10/2025 I join a competitive, and I choose this topic to do. Here is the blog about this: [vpbank_hackathon](/anomaly_detection/vpbank_hackathon/overall_info/)
- 1/2026 I am going to take Master course at Phenikaa University. I choose this project as my master thesis. So please read about my journey doing this here: [my master](/anomaly_detection/master_thesis/)
{% endcapture %}
<div>{{ original_page_content | markdownify }}</div>
</details>
<section class="page-intro" data-lang="vi"><p class="eyebrow">Research journey</p><h1>Phát hiện bất thường</h1><p>Chủ đề tôi đang đào sâu cho luận văn thạc sĩ: từ định nghĩa anomaly và tạo dữ liệu kiểm thử đến lựa chọn baseline, đánh giá và vận hành.</p></section>
<section class="page-intro" data-lang="en"><p class="eyebrow">Research journey</p><h1>Anomaly detection</h1><p>The topic I am exploring for my master’s thesis: from anomaly definitions and test-data generation to baselines, evaluation, and operations.</p></section>

<div class="card-grid card-grid--two">
  <article class="card"><h2>Isolation Forest</h2><p data-lang="vi">Cô lập điểm bất thường bằng random partition và path length.</p><p data-lang="en">Isolating anomalies with random partitions and path length.</p><a class="card__link" href="/anomaly_detection/isolation_forest/">Read →</a></article>
  <article class="card"><h2>Local Outlier Factor</h2><p data-lang="vi">So sánh mật độ cục bộ của một điểm với các điểm lân cận.</p><p data-lang="en">Comparing a point’s local density with that of its neighbors.</p><a class="card__link" href="/anomaly_detection/local_base_outlier_identify/">Read →</a></article>
  <article class="card"><h2 data-lang="vi">Dữ liệu logs và metrics giả lập</h2><h2 data-lang="en">Synthetic logs and metrics</h2><p data-lang="vi">Bộ sinh dữ liệu và mô tả hai nguồn signal cho bài toán observability.</p><p data-lang="en">Data generators and an overview of two observability signal sources.</p><a class="card__link" href="/anomaly_detection/vpbank_hackathon/overall_info/"><span data-lang="vi">Xem dữ liệu →</span><span data-lang="en">Explore the data →</span></a></article>
  <article class="card"><h2 data-lang="vi">Nhật ký luận văn</h2><h2 data-lang="en">Thesis journal</h2><p data-lang="vi">Scope, câu hỏi nghiên cứu và các mốc kiểm chứng trước khi viết model.</p><p data-lang="en">Scope, research questions, and validation milestones before modeling.</p><a class="card__link" href="/anomaly_detection/master_thesis/"><span data-lang="vi">Theo dõi hành trình →</span><span data-lang="en">Follow the journey →</span></a></article>
</div>
