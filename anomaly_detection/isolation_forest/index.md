---
title: Isolation Forest
title_vi: Isolation Forest — trực giác và đánh giá
title_en: Isolation Forest — intuition and evaluation
description: Isolation Forest converts random-partition path length into anomaly scores that require data-specific thresholds and event-level evaluation.
description_vi: Isolation Forest chuyển path length từ random partition thành anomaly score cần threshold theo dữ liệu và đánh giá theo event.
description_en: Isolation Forest converts random-partition path length into anomaly scores that require data-specific thresholds and event-level evaluation.
date: 2026-02-01
writing_topic: anomaly
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>Isolation Forest</h1><p>Thay vì học “normal” trước, Isolation Forest tìm các điểm dễ bị cô lập bằng random partition.</p></header>
  <h2>Trực giác</h2><p>Mỗi isolation tree chọn ngẫu nhiên một feature và một split value. Điểm hiếm và khác biệt thường cần ít split hơn để đứng một mình, nên có average path length ngắn hơn.</p>
  <h2>Anomaly score</h2><pre><code>s(x, ψ) = 2 ^ (-E[h(x)] / c(ψ))</code></pre><p><code>ψ</code> là subsample size, <code>E[h(x)]</code> là path length trung bình và <code>c(ψ)</code> chuẩn hóa theo expected path length của binary search tree. Score cao hơn biểu thị điểm dễ bị cô lập hơn.</p>
  <h2>Lưu ý thực tế</h2><ul><li>Scale ít quan trọng hơn distance-based model, nhưng feature representation vẫn quyết định kết quả.</li><li><code>contamination</code> ảnh hưởng threshold, không thay thế việc định nghĩa chi phí false positive/negative.</li><li>Với time series, cần tránh random split làm rò rỉ tương lai và phải kiểm tra drift.</li><li>Đánh giá bằng labeled incidents nếu có; nếu không, dùng injection test, review chuyên gia và stability.</li></ul>
  <h2>Implementation, threshold và đánh giá theo event</h2>
  <h3>Pseudo-code cần thêm cấu trúc cây và expected path length</h3><p>Các dòng như <code>q = randomly select feature</code> cần được thay bằng random generator và data structure cho internal/external node trong code thật. Khi path kết thúc ở external node chứa nhiều hơn một mẫu, implementation chuẩn còn cộng expected path length <code>c(size)</code>; chỉ trả về current depth sẽ làm score lệch.</p>
  <h3>Không có threshold 0,5–0,6 dùng chung cho mọi dữ liệu</h3><p>Score phụ thuộc sample, feature representation và implementation. <code>contamination</code> đặt quantile threshold theo tỷ lệ anomaly giả định; nó không chứng minh tỷ lệ đó đúng. Hãy chọn threshold trên validation incident, alert budget hoặc cost function và đóng băng trước khi đánh giá test.</p>
  <h3>Time series cần feature có ngữ cảnh</h3><p>Isolation Forest không tự hiểu thứ tự thời gian hay seasonality. Cần tạo lag, rolling statistic hoặc seasonal residual chỉ từ quá khứ. Một spike 100 giao dịch có thể bình thường vào ngày lương nhưng bất thường vào cuối tuần; timestamp context quyết định ý nghĩa.</p>
  <h3>Đánh giá theo event thay vì từng dòng</h3><p>Một incident kéo dài 20 phút có thể tạo 20 timestamp bất thường nhưng chỉ là một event vận hành. Nên báo event precision/recall, detection delay, số alert mỗi ngày và false-positive run length bên cạnh point-wise metric.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Scikit-learn: IsolationForest</a></li><li><a href="https://doi.org/10.1109/ICDM.2008.17">Liu, Ting &amp; Zhou (2008)</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><h1>Isolation Forest</h1><p>Instead of first modeling “normal,” Isolation Forest searches for observations that are easy to isolate with random partitions.</p></header>
  <h2>Intuition</h2><p>Each isolation tree randomly selects a feature and split value. Rare, different points usually require fewer splits to stand alone, giving them a shorter average path length.</p>
  <h2>Anomaly score</h2><pre><code>s(x, ψ) = 2 ^ (-E[h(x)] / c(ψ))</code></pre><p><code>ψ</code> is the subsample size, <code>E[h(x)]</code> is average path length, and <code>c(ψ)</code> normalizes by the expected path length of a binary search tree. Higher scores indicate easier isolation.</p>
  <h2>Practical notes</h2><ul><li>Scaling matters less than for distance-based models, but feature representation still determines the result.</li><li><code>contamination</code> affects the threshold; it does not replace an explicit false-positive/false-negative cost.</li><li>For time series, avoid future leakage and monitor drift.</li><li>Evaluate with labeled incidents when available; otherwise combine injection tests, expert review, and stability checks.</li></ul>
  <h2>Implementation, thresholds, and event-level evaluation</h2>
  <h3>Pseudo-code needs tree structures and expected path length</h3><p>Lines such as <code>q = randomly select feature</code> need a random generator and concrete internal/external node structures. When traversal ends in an external node containing multiple samples, the standard path-length calculation also adds the expected path length <code>c(size)</code>; returning only the current depth biases the score.</p>
  <h3>There is no universal 0.5–0.6 threshold</h3><p>Scores depend on the sample, feature representation, and implementation. <code>contamination</code> sets a quantile threshold from an assumed anomaly rate; it does not prove that rate. Select the threshold from validation incidents, an alert budget, or a cost function, then freeze it before test evaluation.</p>
  <h3>Time series need contextual features</h3><p>Isolation Forest does not understand order or seasonality by itself. Build lags, rolling statistics, or seasonal residuals from past data only. A spike of 100 transactions may be normal on payday and abnormal on a weekend; timestamp context changes the meaning.</p>
  <h3>Evaluate events, not only rows</h3><p>A twenty-minute incident may produce twenty anomalous timestamps but represents one operational event. Report event precision/recall, detection delay, alerts per day, and false-positive run length alongside point-wise metrics.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Scikit-learn: IsolationForest</a></li><li><a href="https://doi.org/10.1109/ICDM.2008.17">Liu, Ting &amp; Zhou (2008)</a></li></ul>
</article>
