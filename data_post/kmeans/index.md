---
title: K-means Clustering
title_vi: K-means — thuật toán và cách chọn K
title_en: K-means — algorithm and choosing K
description: A practical bilingual guide to Lloyd's algorithm, initialization, scaling, and cluster evaluation.
description_vi: Hướng dẫn thực tế về Lloyd’s algorithm, initialization, scaling và đánh giá cluster.
description_en: A practical guide to Lloyd's algorithm, initialization, scaling, and cluster evaluation.
date: 2026-02-01
writing_topic: foundations
---

<section class="reading-page original-source" data-original-source="true" data-lang="vi">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

🔙 [Back to Home](/)

## Kmeans


## Definition
Kmeans là 1 thuật toán phân cụm, với tập N điểm cho trước, có thể phân về k cụm dựa trên khoảng cách với các tâm cụm.  

Kmeans là thuật toán Unsupervised learning, tức là bài toán k có nhãn, vì vậy khó (k clear) để đánh giá kết quả thuật toán, cũng như không tìm được nghiệm tốt nhât.  

## Ứng dụng Kmeans

Trên thực tế trong bank, có một vài bài toán áp dụng Kmeans. Ví dụ 1 tập KH mua bảo hiểm, liệu tập này có thể chia về các tập mà có chân dung (feature) giống nhau không. Output trả ra có dạng kiểu Tập 1: KH trên 35 tuổi, có AUM tốt,có nhiều giao dịch mua thuốc/ khám bệnh, ...  

Tuy nhiên trải nghiệm thực tế áp dụng Kmeans trong các bài toán này, Kmeans mang tính am hiểu khách hàng, am hiểu kinh doanh nhiều hơn là việc giải quyết 1 bài toán cụ thể (classification)

## Các bước trong thuật toán

B1: Chọn k là số cụm muốn phân vào

B2: Khởi tạo ngẫu nhiên = chọn k điểm - gọi đây là k centroid

khi có 1 điểm mới → phân vào cụm gần nhất → update lại centroid của cụm đó

B3: lặp lại cho đến khi hết các điểm → kết thúc sẽ được k cluster 


## Các điểm cần chú ý 

Làm thế nào để chọn được K phù hơp:

Dựa vào 2 thứ: Elbow curve và Silhouette score

Elbow curve = tổng (distance từ các điểm đến centroid) 

![image.png](images/1.png)


Silhouette = avg (s(i)) trong đó s(i) = ( b(i) - a(i) ) / max( b(i), a(i) ) 

- a(i): trung bình kc từ điểm i tới các điểm khác trong cụm
- b(i): trung bình kc từ điểm i tới cụm gần nhất

![image.png](images/2.svg)


Khi tăng K lên 

- Elbow giảm → tốt lên
- Siouse giảm → xấu đi

Cần chọn K để cân bằng cho cả 2.
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Clustering</p><h1>K-means</h1><p>K-means chia dữ liệu thành K nhóm bằng cách tối thiểu hóa tổng bình phương khoảng cách từ mỗi điểm đến centroid của nhóm.</p></header>
  <h2>Lloyd’s algorithm</h2>
  <ol class="process"><li>Chọn K centroid ban đầu, thường bằng k-means++.</li><li>Gán <strong>toàn bộ</strong> điểm vào centroid gần nhất.</li><li>Tính lại mỗi centroid bằng trung bình của các điểm trong cluster.</li><li>Lặp bước gán và cập nhật đến khi hội tụ hoặc đạt giới hạn vòng lặp.</li></ol>
  <p>Đây là batch update. Cập nhật centroid ngay sau từng điểm là một biến thể online, không phải mô tả chuẩn của Lloyd’s algorithm.</p>
  <h2>Chọn K</h2>
  <ul><li><strong>Inertia / elbow:</strong> luôn không tăng khi K tăng, vì thêm cluster không thể làm nghiệm tối ưu tệ hơn.</li><li><strong>Silhouette:</strong> đo mức gần với cluster của mình so với cluster lân cận. Score không bắt buộc giảm khi K tăng; nên so sánh các candidate K và kết hợp hiểu biết nghiệp vụ.</li></ul>
  <h2>Các giả định dễ quên</h2><ul><li>Scale feature trước khi dùng khoảng cách Euclidean.</li><li>K-means phù hợp hơn với cluster gần dạng cầu và kích thước tương đối cân bằng.</li><li>Outlier có thể kéo centroid mạnh.</li><li>Chạy nhiều initialization vì nghiệm phụ thuộc điểm bắt đầu.</li></ul>
  <h2>Trong bài toán khách hàng</h2><p>Cluster chỉ có giá trị khi mô tả được một nhóm ổn định và dẫn đến hành động khác nhau. Sau khi fit, tôi sẽ kiểm tra stability qua nhiều seed/time window, profile từng cluster và xem cluster có tạo ra chiến lược khác biệt hay không.</p>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2>
  <h3>Objective của K-means là within-cluster sum of squares</h3><p>Mỗi vòng Lloyd’s algorithm gồm một bước gán toàn bộ điểm và một bước cập nhật toàn bộ centroid. Hai bước này không làm objective tăng, nhưng chỉ đảm bảo hội tụ đến local optimum. Vì vậy initialization và số lần chạy lại vẫn quan trọng.</p>
  <pre><code class="language-python">import numpy as np

def kmeans(X, n_clusters, seed=42, max_iter=100, tolerance=1e-6):
    rng = np.random.default_rng(seed)
    centroids = X[rng.choice(len(X), n_clusters, replace=False)].copy()

    for _ in range(max_iter):
        squared_distance = ((X[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        labels = squared_distance.argmin(axis=1)
        updated = centroids.copy()
        for cluster in range(n_clusters):
            members = X[labels == cluster]
            if len(members):
                updated[cluster] = members.mean(axis=0)
            else:
                updated[cluster] = X[rng.integers(len(X))]
        if np.linalg.norm(updated - centroids) &lt;= tolerance:
            centroids = updated
            break
        centroids = updated

    inertia = ((X - centroids[labels]) ** 2).sum()
    return centroids, labels, inertia</code></pre>
  <h3>Scaling defines what “near” means</h3><p>If income ranges in tens of millions while transaction frequency ranges from 0 to 30, Euclidean distance will mostly follow income unless features are transformed or scaled. Scaling must be learned on training/reference data, and feature weights should reflect the segmentation purpose rather than convenience.</p>
  <h3>Elbow and silhouette do not select a business answer automatically</h3><p>Inertia always falls as K increases; silhouette can move in either direction. Use both as diagnostics, then test whether profiles remain similar across seeds, samples and later time windows. Reject a mathematically neat segmentation if it cannot be named consistently or does not change an action.</p>
  <h3>Evaluate assignment drift after deployment</h3><p>Track centroid movement, cluster sizes, feature distributions and the fraction of customers switching clusters. A sudden change can indicate real behavior, upstream data drift or a preprocessing bug; a cluster ID alone cannot distinguish them.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/clustering.html#k-means">Scikit-learn: K-means</a></li><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html">Silhouette score API</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Learning note · Clustering</p><h1>K-means</h1><p>K-means partitions data into K groups by minimizing the sum of squared distances from each point to its assigned centroid.</p></header>
  <h2>Lloyd’s algorithm</h2>
  <ol class="process"><li>Choose K initial centroids, commonly with k-means++.</li><li>Assign <strong>all</strong> points to their nearest centroid.</li><li>Recompute each centroid as the mean of its assigned points.</li><li>Repeat assignment and update until convergence or the iteration limit.</li></ol>
  <p>This is a batch update. Updating the centroid after every point describes an online variant, not standard Lloyd’s algorithm.</p>
  <h2>Choosing K</h2>
  <ul><li><strong>Inertia / elbow:</strong> never increases as K grows because an additional cluster cannot worsen the optimal objective.</li><li><strong>Silhouette:</strong> compares cohesion with separation. It does not have to decrease as K grows; compare candidate values and combine the result with domain knowledge.</li></ul>
  <h2>Assumptions people forget</h2><ul><li>Scale features before using Euclidean distance.</li><li>K-means works best for roughly spherical, similarly sized groups.</li><li>Outliers can pull centroids substantially.</li><li>Use multiple initializations because the solution depends on the starting points.</li></ul>
  <h2>For customer segmentation</h2><p>A cluster is useful only if it describes a stable group and supports a distinct action. After fitting, I would test stability across seeds and time windows, profile each group, and ask whether it changes a real strategy.</p>
  <h2>Corrections and extensions to the original notes</h2>
  <h3>K-means minimizes within-cluster sum of squares</h3><p>Each Lloyd iteration has one assignment step for all points and one centroid update for all clusters. These steps do not increase the objective, but they guarantee convergence only to a local optimum. Initialization and repeated runs therefore still matter.</p>
  <pre><code class="language-python">import numpy as np

def kmeans(X, n_clusters, seed=42, max_iter=100, tolerance=1e-6):
    rng = np.random.default_rng(seed)
    centroids = X[rng.choice(len(X), n_clusters, replace=False)].copy()

    for _ in range(max_iter):
        squared_distance = ((X[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        labels = squared_distance.argmin(axis=1)
        updated = centroids.copy()
        for cluster in range(n_clusters):
            members = X[labels == cluster]
            if len(members):
                updated[cluster] = members.mean(axis=0)
            else:
                updated[cluster] = X[rng.integers(len(X))]
        if np.linalg.norm(updated - centroids) &lt;= tolerance:
            centroids = updated
            break
        centroids = updated

    inertia = ((X - centroids[labels]) ** 2).sum()
    return centroids, labels, inertia</code></pre>
  <h3>Scaling defines what “near” means</h3><p>If income ranges in tens of millions while transaction frequency ranges from 0 to 30, Euclidean distance will mostly follow income unless features are transformed or scaled. Learn scaling parameters from training/reference data and choose feature weights from the segmentation purpose, not convenience.</p>
  <h3>Elbow and silhouette do not choose the business answer</h3><p>Inertia always falls as K grows; silhouette can move in either direction. Use both as diagnostics, then test whether profiles remain similar across seeds, samples, and later time windows. Reject a mathematically neat segmentation if it cannot be named consistently or does not change an action.</p>
  <h3>Evaluate assignment drift after deployment</h3><p>Track centroid movement, cluster sizes, feature distributions, and the fraction of customers switching clusters. A sudden change may represent real behavior, upstream drift, or a preprocessing bug; a cluster ID alone cannot tell you which.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/clustering.html#k-means">Scikit-learn: K-means</a></li><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html">Silhouette score API</a></li></ul>
</article>
