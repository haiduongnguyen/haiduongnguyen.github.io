---
title: "K-Means in Banking: Useful for Profiles, Not Labels"
title_vi: "K-means trong ngân hàng: hiểu chân dung thay vì tạo nhãn"
title_en: "K-Means in Banking: Useful for Profiles, Not Labels"
description: A practical view of customer segmentation, the K-means iteration, and choosing K with inertia and silhouette score.
description_vi: Góc nhìn thực tế về phân khúc khách hàng, vòng lặp K-means và cách chọn K bằng inertia cùng silhouette score.
description_en: A practical view of customer segmentation, the K-means iteration, and choosing K with inertia and silhouette score.
date: 2026-02-01
writing_topic: foundations
---

{% capture article_en %}
🔙 [Back to Home](/)

# K-Means in Banking: Useful for Profiles, Not Labels

K-means can divide customers into groups with similar features, but it does not tell us that those groups are objectively correct. In my banking work, its main value has been helping people understand customer profiles rather than solving a specific classification problem.

## A banking use case: understanding insurance customers

Suppose we have a set of customers who purchased insurance. K-means can reveal groups such as customers over 35 with high assets under management and frequent medicine or medical-examination transactions.

That output is useful for exploring the portfolio and discussing customer behavior with the business. It is different from classification: there is no known target label, and the cluster number itself does not carry business meaning until we inspect the features of the customers assigned to it.

## K-means alternates assignment and centroid updates

Given `N` data points, K-means assigns them to `K` clusters according to their distance from the cluster centroids:

1. Choose `K`, the number of clusters.
2. Initialize `K` centroids, often from selected data points.
3. Assign every point to its nearest centroid.
4. Recalculate each centroid from the points assigned to that cluster.
5. Repeat assignment and update until the assignments or centroids stop changing enough.

Because the initial centroids affect the final result, different initializations can produce different clusters.

## Inertia always falls as K increases

The elbow curve uses within-cluster distance, commonly called inertia: the sum of squared distances from each point to its assigned centroid.

![Elbow curve](images/1.png)

Increasing `K` gives the algorithm more centroids, so inertia cannot increase. This also means the smallest inertia does not identify the best `K`; choosing one cluster per point would minimize it without producing a useful segmentation. The elbow is the point after which additional clusters reduce inertia only slightly.

## Silhouette checks separation as well as compactness

For point `i`, the silhouette value is:

`s(i) = (b(i) - a(i)) / max(b(i), a(i))`

- `a(i)`: average distance from point `i` to other points in its own cluster.
- `b(i)`: lowest average distance from point `i` to points in another cluster.

The silhouette score is the average of `s(i)` across all points. A higher value means points are closer to their own cluster than to neighboring clusters.

![Silhouette score](images/2.svg)

Unlike inertia, silhouette does not move in one guaranteed direction as `K` increases. I use the elbow and silhouette together, then inspect whether the resulting customer profiles are distinct and understandable to the business.

That final inspection matters: a mathematically separated cluster is not automatically a useful customer segment.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# K-means trong ngân hàng: hữu ích cho chân dung, không phải nhãn

K-means có thể chia khách hàng thành những nhóm có feature tương tự, nhưng không khẳng định các nhóm đó đúng một cách khách quan. Trong công việc ngân hàng của tôi, giá trị chính của K-means là giúp hiểu chân dung khách hàng thay vì giải quyết một bài toán classification cụ thể.

## Một use case ngân hàng: hiểu nhóm khách hàng mua bảo hiểm

Giả sử có một tập khách hàng đã mua bảo hiểm. K-means có thể cho thấy các nhóm như khách hàng trên 35 tuổi, có assets under management cao và thường xuyên phát sinh giao dịch mua thuốc hoặc khám bệnh.

Output này hữu ích khi khám phá portfolio và thảo luận hành vi khách hàng với business. Nó khác classification: không có target label đã biết, và cluster number tự nó không mang business meaning cho đến khi chúng ta kiểm tra feature của khách hàng trong cluster.

## K-means luân phiên assignment và cập nhật centroid

Với `N` data point, K-means gán chúng vào `K` cluster theo khoảng cách tới cluster centroid:

1. Chọn `K`, số cluster.
2. Khởi tạo `K` centroid, thường từ các data point được chọn.
3. Gán mỗi point vào centroid gần nhất.
4. Tính lại từng centroid từ các point thuộc cluster đó.
5. Lặp lại assignment và update cho đến khi assignment hoặc centroid gần như không đổi.

Vì centroid ban đầu ảnh hưởng đến kết quả cuối, các initialization khác nhau có thể tạo ra cluster khác nhau.

## Inertia luôn giảm khi K tăng

Elbow curve sử dụng within-cluster distance, thường gọi là inertia: tổng squared distance từ từng point đến centroid được gán.

![Elbow curve](images/1.png)

Khi tăng `K`, thuật toán có thêm centroid nên inertia không thể tăng. Vì thế, inertia nhỏ nhất không xác định được `K` tốt nhất; nếu mỗi point là một cluster thì inertia sẽ nhỏ nhất nhưng segmentation không có ích. Elbow là điểm mà thêm cluster mới chỉ làm inertia giảm một lượng nhỏ.

## Silhouette kiểm tra cả độ tách biệt và độ chặt

Với point `i`:

`s(i) = (b(i) - a(i)) / max(b(i), a(i))`

- `a(i)`: khoảng cách trung bình từ point `i` đến các point khác trong cùng cluster.
- `b(i)`: khoảng cách trung bình nhỏ nhất từ point `i` đến các point thuộc một cluster khác.

Silhouette score là trung bình của `s(i)` trên toàn bộ point. Giá trị cao hơn nghĩa là point gần cluster của nó hơn các cluster lân cận.

![Silhouette score](images/2.svg)

Khác với inertia, silhouette không có một chiều biến động cố định khi `K` tăng. Tôi dùng elbow và silhouette cùng nhau, sau đó kiểm tra các customer profile thu được có khác biệt và có thể giải thích với business hay không.

Bước kiểm tra cuối cùng rất quan trọng: một cluster tách biệt về mặt toán học chưa chắc là một customer segment hữu ích.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
