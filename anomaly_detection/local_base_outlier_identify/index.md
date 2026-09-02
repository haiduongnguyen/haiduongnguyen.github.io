---
title: Local Outlier Factor
title_vi: Local Outlier Factor — bất thường theo mật độ cục bộ
title_en: Local Outlier Factor — local density anomalies
description: A bilingual guide to LOF, reachability density, neighborhood size, and practical limitations.
description_vi: Hướng dẫn song ngữ về LOF, reachability density, neighborhood size và giới hạn thực tế.
description_en: A bilingual guide to LOF, reachability density, neighborhood size, and practical limitations.
date: 2026-02-01
writing_topic: anomaly
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}
# Local Outlier Factor (LOF) Summary

## Overview

Local Outlier Factor (LOF) is an algorithm for identifying density-based local outliers, introduced by Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng, and Jörg Sander in their 2000 paper. Unlike global outlier detection methods, LOF measures the local deviation of density of a point compared to its neighbors.

## Key Concepts

### Local Density

- **k-distance**: The distance to the k-th nearest neighbor of a point
- **Reachability distance**: Max of the k-distance of point b and the actual distance between points a and b
- **Local reachability density (LRD)**: Inverse of the average reachability distance of a point to its k-nearest neighbors

### Local Outlier Factor

- **LOF score**: Ratio of the average LRD of a point's neighbors to its own LRD
- LOF ≈ 1: Point has similar density to neighbors (normal point)
- LOF > 1: Point has lower density than neighbors (potential outlier)
- The higher the LOF value, the more likely the point is an outlier

## Advantages

- Identifies outliers in varying density regions
- More effective than global methods in complex datasets
- Provides a score rather than binary classification
- Can detect outliers that distance-based methods miss

## Limitations

- Requires parameter selection (k value)
- Computational complexity increases with dataset size
- Less effective in high-dimensional spaces (curse of dimensionality)

## Applications

- Fraud detection
- Network intrusion detection
- Medical anomaly detection
- Quality control in manufacturing

## Implementation Considerations

- Choosing appropriate k value
- Distance metric selection (Euclidean, Manhattan, etc.)
- Normalization of features
- Interpretation of LOF scores
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Anomaly detection</p><h1>Local Outlier Factor</h1><p>LOF phát hiện một điểm có mật độ thấp bất thường so với chính các hàng xóm của nó.</p></header>
  <h2>Các thành phần</h2><ul><li><strong>k-distance:</strong> khoảng cách đến hàng xóm thứ k.</li><li><strong>Reachability distance:</strong> làm mượt các khoảng cách quá nhỏ trong cùng neighborhood.</li><li><strong>Local reachability density:</strong> nghịch đảo của reachability distance trung bình.</li><li><strong>LOF score:</strong> mật độ trung bình của hàng xóm chia cho mật độ của điểm đang xét.</li></ul><p>LOF gần 1 thường nghĩa là mật độ tương tự hàng xóm; lớn hơn 1 cho thấy điểm thưa hơn vùng xung quanh. Đây là score tương đối, không phải xác suất.</p>
  <h2>Parameter và giới hạn</h2><ul><li><code>n_neighbors</code> quyết định “local” ở scale nào; nên kiểm tra nhiều giá trị.</li><li>Scale feature và distance metric ảnh hưởng trực tiếp đến neighborhood.</li><li>Trong high dimension, khoảng cách kém phân biệt hơn.</li><li>Trong scikit-learn, phát hiện novelty trên dữ liệu mới cần <code>novelty=True</code> và không dùng training score như prediction score.</li></ul>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2><h3>“Local” được định nghĩa bởi neighborhood</h3><p>K nhỏ làm model nhạy với cấu trúc rất cục bộ và noise; K lớn làm score tiến gần góc nhìn toàn cục. Không nên tune K để tối đa một metric trên cùng test set. Hãy xác định scale có ý nghĩa nghiệp vụ, thử một dải K trên validation và kiểm tra top anomaly có ổn định hay không.</p><h3>LOF score không so sánh tuyệt đối giữa mọi lần fit</h3><p>Score phụ thuộc reference population, preprocessing và neighborhood. Một ngưỡng lấy từ tháng trước có thể mất ý nghĩa khi mix khách hàng thay đổi. Cần lưu distribution của score, tỷ lệ alert và drift của feature/reference set.</p><h3>Outlier detection và novelty detection là hai workflow</h3><p>Trong scikit-learn, mặc định LOF dùng để tìm outlier ngay trên training sample. Với <code>novelty=True</code>, model được fit trên reference data được coi là normal rồi mới score dữ liệu chưa thấy; không dùng <code>fit_predict</code> trên chính training data để mô phỏng production scoring.</p><h3>Khoảng cách trong high dimension cần được kiểm chứng</h3><p>Sau scaling, hãy kiểm tra nearest-neighbor distance có còn phân biệt, feature nào đang chi phối và kết quả có ổn định khi bỏ feature nhiễu. Dimensionality reduction có thể giúp nhưng cũng có thể xóa anomaly signal; phải đánh giá cùng incident/injection test.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor">Scikit-learn: Local Outlier Factor</a></li><li><a href="https://doi.org/10.1145/335191.335388">Breunig et al. (2000)</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Learning note · Anomaly detection</p><h1>Local Outlier Factor</h1><p>LOF detects points whose density is unusually low compared with their own neighbors.</p></header>
  <h2>Core components</h2><ul><li><strong>k-distance:</strong> distance to the k-th nearest neighbor.</li><li><strong>Reachability distance:</strong> smooths very small distances within a neighborhood.</li><li><strong>Local reachability density:</strong> inverse average reachability distance.</li><li><strong>LOF score:</strong> average neighbor density divided by the point’s own density.</li></ul><p>A value near 1 usually means density similar to the neighborhood; a value above 1 means the point is sparser. It is a relative score, not a probability.</p>
  <h2>Parameters and limitations</h2><ul><li><code>n_neighbors</code> defines the scale of “local”; test several values.</li><li>Feature scaling and the distance metric directly affect neighborhoods.</li><li>Distances become less discriminative in high dimensions.</li><li>In scikit-learn, scoring unseen data requires <code>novelty=True</code>; training and novelty workflows differ.</li></ul>
  <h2>Corrections and extensions to the original notes</h2><h3>The neighborhood defines “local”</h3><p>A small K makes the model sensitive to fine structure and noise; a large K moves the score toward a global view. Do not tune K to maximize one metric on the test set. Choose a domain-relevant scale, evaluate a range on validation data, and inspect whether the top anomalies remain stable.</p><h3>LOF scores are not absolute across fits</h3><p>The score depends on the reference population, preprocessing, and neighborhood. A threshold from last month may stop meaning the same thing when the customer mix changes. Store the score distribution, alert rate, and drift of features/reference data.</p><h3>Outlier and novelty detection are different workflows</h3><p>Scikit-learn’s default LOF workflow finds outliers in the training sample. With <code>novelty=True</code>, fit on reference data assumed to be normal and score unseen observations afterward; do not use training <code>fit_predict</code> behavior as a proxy for production scoring.</p><h3>Validate distance in high dimensions</h3><p>After scaling, inspect whether nearest-neighbor distances remain discriminative, which features dominate, and whether results survive removal of noisy features. Dimensionality reduction may help but may also erase the anomaly signal, so validate it against incidents or injection tests.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor">Scikit-learn: Local Outlier Factor</a></li><li><a href="https://doi.org/10.1145/335191.335388">Breunig et al. (2000)</a></li></ul>
</article>
