---
title: Anomaly Detection
title_vi: Phát hiện bất thường
title_en: Anomaly detection
description: Rule baselines, Isolation Forest, LOF, synthetic data, and event-level evaluation for multidimensional logs and metrics.
description_vi: Rule baseline, Isolation Forest, LOF, dữ liệu giả lập và đánh giá theo event cho logs cùng metrics đa chiều.
description_en: Rule baselines, Isolation Forest, LOF, synthetic data, and event-level evaluation for multidimensional logs and metrics.
writing_topic: projects
project_order: 2
permalink: /anomaly_detection/landing_page.html
---

<section class="page-intro" data-lang="vi"><h1>Phát hiện bất thường</h1><p>Chủ đề tôi đang đào sâu cho luận văn thạc sĩ: từ định nghĩa anomaly và tạo dữ liệu kiểm thử đến lựa chọn baseline, đánh giá và vận hành.</p></section>
<section class="page-intro" data-lang="en"><h1>Anomaly detection</h1><p>The topic I am exploring for my master’s thesis: from anomaly definitions and test-data generation to baselines, evaluation, and operations.</p></section>

<div class="card-grid card-grid--two">
  <article class="card"><h2>Isolation Forest</h2><p data-lang="vi">Cô lập điểm bất thường bằng random partition và path length.</p><p data-lang="en">Isolating anomalies with random partitions and path length.</p><a class="card__link" href="/anomaly_detection/isolation_forest/">Read →</a></article>
  <article class="card"><h2>Local Outlier Factor</h2><p data-lang="vi">So sánh mật độ cục bộ của một điểm với các điểm lân cận.</p><p data-lang="en">Comparing a point’s local density with that of its neighbors.</p><a class="card__link" href="/anomaly_detection/local_base_outlier_identify/">Read →</a></article>
  <article class="card"><h2 data-lang="vi">Dữ liệu logs và metrics giả lập</h2><h2 data-lang="en">Synthetic logs and metrics</h2><p data-lang="vi">Hai file JSONL, mỗi file 1.500 record, cung cấp logs, APM metrics và nhãn anomaly để kiểm tra pipeline.</p><p data-lang="en">Two JSONL files with 1,500 records each provide logs, APM metrics, and anomaly labels for pipeline tests.</p><a class="card__link" href="/anomaly_detection/vpbank_hackathon/overall_info/"><span data-lang="vi">Mở dữ liệu và validator →</span><span data-lang="en">Open the data and validator →</span></a></article>
  <article class="card"><h2 data-lang="vi">Nhật ký luận văn</h2><h2 data-lang="en">Thesis journal</h2><p data-lang="vi">Scope xác định anomaly score theo timestamp và nhóm signal; evaluation dùng incident label, injected anomaly, alert volume và detection delay.</p><p data-lang="en">The scope defines anomaly scores by timestamp and signal group; evaluation uses incident labels, injected anomalies, alert volume, and detection delay.</p><a class="card__link" href="/anomaly_detection/master_thesis/"><span data-lang="vi">Đọc scope và tiêu chí đánh giá →</span><span data-lang="en">Read the scope and evaluation criteria →</span></a></article>
</div>
