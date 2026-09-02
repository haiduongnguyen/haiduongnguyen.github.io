---
title: Isolation Forest
title_vi: Isolation Forest — trực giác và đánh giá
title_en: Isolation Forest — intuition and evaluation
description: How Isolation Forest uses random partitions and path length, plus practical evaluation notes.
description_vi: Isolation Forest dùng random partition và path length như thế nào, kèm lưu ý đánh giá thực tế.
description_en: How Isolation Forest uses random partitions and path length, plus practical evaluation notes.
date: 2026-02-01
writing_topic: anomaly
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}
# Isolation Forest

### Overview

Isolation Forest is an anomaly detection algorithm that isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. This recursive partitioning can be represented by a tree structure, and anomalies are isolated in fewer steps as they are typically "few and different."

### Key Concepts

- **Isolation**: The process of separating an instance from the rest of the data
- **Path Length**: Number of edges traversed from root to terminating node
- **Anomaly Score**: Calculated based on path length (shorter path = more likely to be an anomaly)
- **Sub-sampling**: Helps improve robustness and reduce computational complexity

### Algorithm Steps

1. Build isolation trees (iTree) from random sub-samples of data
2. For each instance, calculate its path length across all trees
3. Calculate anomaly score using average path length
4. Classify instances as anomalies based on score threshold

### Anomaly Score Formula

```
s(x, n) = 2^(-E(h(x))/c(n))
```

Where:

- s(x, n) is the anomaly score
- E(h(x)) is the average path length of instance x
- c(n) is the average path length of unsuccessful searches in a BST
- n is the number of external nodes

### Advantages

- Linear time complexity: O(t × n log n) where t = number of trees, n = data size
- Memory efficient compared to distance-based methods
- Works well with high-dimensional data
- No distance calculation needed
- No assumptions about data distribution
- Handles mixed attribute types well

### Implementation Pseudo-code

**Building an iTree:**

```python
def build_iTree(X, height_limit, current_height=0):
    if current_height >= height_limit or len(X) <= 1:
        return ExNode(size=len(X))
    
    # Randomly select attribute
    q = randomly select feature
    
    # Randomly select split point
    p = randomly select value between min and max of X[:, q]
    
    X_left = X[X[:, q] < p]
    X_right = X[X[:, q] >= p]
    
    return InNode(
        left=build_iTree(X_left, height_limit, current_height + 1),
        right=build_iTree(X_right, height_limit, current_height + 1),
        split_attribute=q,
        split_value=p
    )
```

**Path Length Calculation:**

```python
def path_length(x, tree, current_height=0):
    if isinstance(tree, ExNode):
        return current_height
    
    if x[tree.split_attribute] < tree.split_value:
        return path_length(x, tree.left, current_height + 1)
    else:
        return path_length(x, tree.right, current_height + 1)
```

### Practical Considerations

- **Number of trees**: 100-500 typically sufficient
- **Subsample size**: 256 recommended in the original paper
- **Height limit**: log2(subsample_size) default
- **Anomaly threshold**: Usually 0.5-0.6 (scores > threshold = anomalies)

### Visualizations

- Path length distributions: Normal points vs. anomalies
- Decision boundaries in 2D feature space
- Anomaly score heatmaps
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Anomaly detection</p><h1>Isolation Forest</h1><p>Thay vì học “normal” trước, Isolation Forest tìm các điểm dễ bị cô lập bằng random partition.</p></header>
  <h2>Trực giác</h2><p>Mỗi isolation tree chọn ngẫu nhiên một feature và một split value. Điểm hiếm và khác biệt thường cần ít split hơn để đứng một mình, nên có average path length ngắn hơn.</p>
  <h2>Anomaly score</h2><pre><code>s(x, ψ) = 2 ^ (-E[h(x)] / c(ψ))</code></pre><p><code>ψ</code> là subsample size, <code>E[h(x)]</code> là path length trung bình và <code>c(ψ)</code> chuẩn hóa theo expected path length của binary search tree. Score cao hơn biểu thị điểm dễ bị cô lập hơn.</p>
  <h2>Lưu ý thực tế</h2><ul><li>Scale ít quan trọng hơn distance-based model, nhưng feature representation vẫn quyết định kết quả.</li><li><code>contamination</code> ảnh hưởng threshold, không thay thế việc định nghĩa chi phí false positive/negative.</li><li>Với time series, cần tránh random split làm rò rỉ tương lai và phải kiểm tra drift.</li><li>Đánh giá bằng labeled incidents nếu có; nếu không, dùng injection test, review chuyên gia và stability.</li></ul>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2>
  <h3>Pseudo-code gốc mô tả ý tưởng, không phải implementation chạy trực tiếp</h3><p>Các dòng như <code>q = randomly select feature</code> cần được thay bằng random generator và data structure cho internal/external node trong code thật. Khi path kết thúc ở external node chứa nhiều hơn một mẫu, implementation chuẩn còn cộng expected path length <code>c(size)</code>; chỉ trả về current depth sẽ làm score lệch.</p>
  <h3>Không có threshold 0,5–0,6 dùng chung cho mọi dữ liệu</h3><p>Score phụ thuộc sample, feature representation và implementation. <code>contamination</code> đặt quantile threshold theo tỷ lệ anomaly giả định; nó không chứng minh tỷ lệ đó đúng. Hãy chọn threshold trên validation incident, alert budget hoặc cost function và đóng băng trước khi đánh giá test.</p>
  <h3>Time series cần feature có ngữ cảnh</h3><p>Isolation Forest không tự hiểu thứ tự thời gian hay seasonality. Cần tạo lag, rolling statistic hoặc seasonal residual chỉ từ quá khứ. Một spike 100 giao dịch có thể bình thường vào ngày lương nhưng bất thường vào cuối tuần; timestamp context quyết định ý nghĩa.</p>
  <h3>Đánh giá theo event thay vì từng dòng</h3><p>Một incident kéo dài 20 phút có thể tạo 20 timestamp bất thường nhưng chỉ là một event vận hành. Nên báo event precision/recall, detection delay, số alert mỗi ngày và false-positive run length bên cạnh point-wise metric.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Scikit-learn: IsolationForest</a></li><li><a href="https://doi.org/10.1109/ICDM.2008.17">Liu, Ting &amp; Zhou (2008)</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Learning note · Anomaly detection</p><h1>Isolation Forest</h1><p>Instead of first modeling “normal,” Isolation Forest searches for observations that are easy to isolate with random partitions.</p></header>
  <h2>Intuition</h2><p>Each isolation tree randomly selects a feature and split value. Rare, different points usually require fewer splits to stand alone, giving them a shorter average path length.</p>
  <h2>Anomaly score</h2><pre><code>s(x, ψ) = 2 ^ (-E[h(x)] / c(ψ))</code></pre><p><code>ψ</code> is the subsample size, <code>E[h(x)]</code> is average path length, and <code>c(ψ)</code> normalizes by the expected path length of a binary search tree. Higher scores indicate easier isolation.</p>
  <h2>Practical notes</h2><ul><li>Scaling matters less than for distance-based models, but feature representation still determines the result.</li><li><code>contamination</code> affects the threshold; it does not replace an explicit false-positive/false-negative cost.</li><li>For time series, avoid future leakage and monitor drift.</li><li>Evaluate with labeled incidents when available; otherwise combine injection tests, expert review, and stability checks.</li></ul>
  <h2>Corrections and extensions to the original notes</h2>
  <h3>The original pseudo-code explains the idea but is not executable Python</h3><p>Lines such as <code>q = randomly select feature</code> need a random generator and concrete internal/external node structures. When traversal ends in an external node containing multiple samples, the standard path-length calculation also adds the expected path length <code>c(size)</code>; returning only the current depth biases the score.</p>
  <h3>There is no universal 0.5–0.6 threshold</h3><p>Scores depend on the sample, feature representation, and implementation. <code>contamination</code> sets a quantile threshold from an assumed anomaly rate; it does not prove that rate. Select the threshold from validation incidents, an alert budget, or a cost function, then freeze it before test evaluation.</p>
  <h3>Time series need contextual features</h3><p>Isolation Forest does not understand order or seasonality by itself. Build lags, rolling statistics, or seasonal residuals from past data only. A spike of 100 transactions may be normal on payday and abnormal on a weekend; timestamp context changes the meaning.</p>
  <h3>Evaluate events, not only rows</h3><p>A twenty-minute incident may produce twenty anomalous timestamps but represents one operational event. Report event precision/recall, detection delay, alerts per day, and false-positive run length alongside point-wise metrics.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Scikit-learn: IsolationForest</a></li><li><a href="https://doi.org/10.1109/ICDM.2008.17">Liu, Ting &amp; Zhou (2008)</a></li></ul>
</article>
