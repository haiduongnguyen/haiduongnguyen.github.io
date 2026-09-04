---
title: "Local Outlier Factor: Compare a Point With Its Neighbors"
title_vi: "Local Outlier Factor: so sánh một điểm với các điểm lân cận"
title_en: "Local Outlier Factor: Compare a Point With Its Neighbors"
description: LOF detects a point whose local density is lower than the density around its nearest neighbors.
description_vi: LOF phát hiện điểm có mật độ cục bộ thấp hơn mật độ quanh các điểm lân cận gần nhất.
description_en: LOF detects a point whose local density is lower than the density around its nearest neighbors.
date: 2026-02-01
writing_topic: anomaly
---

{% capture article_en %}
🔙 [Back to Home](/)

# Local Outlier Factor: Compare a Point With Its Neighbors

A global distance threshold can miss anomalies when one part of a dataset is naturally dense and another is sparse. Local Outlier Factor (LOF) instead asks whether a point has substantially lower density than its own neighbors.

LOF was introduced by Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng, and Jörg Sander in 2000.

## Three quantities lead to the LOF score

For a chosen neighborhood size `k`:

1. **k-distance:** the distance from a point to its k-th nearest neighbor.
2. **Reachability distance:** for points `a` and `b`, the larger of the actual distance between them and the k-distance of `b`.
3. **Local reachability density (LRD):** the inverse of the average reachability distance from a point to its neighbors.

Reachability distance prevents extremely close pairs from dominating the density calculation. LRD then represents how tightly a point is connected to its local neighborhood.

## LOF compares local densities as a ratio

The LOF score compares a point's LRD with the average LRD of its neighbors:

- `LOF ≈ 1`: the point has density similar to its neighbors.
- `LOF > 1`: the point is less dense than its neighbors and may be an outlier.
- A larger score indicates stronger local isolation.

This is why LOF can find a point that looks normal under a global distance rule but unusual inside its own region.

## The neighborhood size changes the question

A small `k` makes the score sensitive to very local structure and noise. A large `k` compares each point with a broader region and can smooth away small anomalous pockets. There is no universally correct value; `k` defines the scale at which “local” is measured.

Feature scaling and the distance metric matter for the same reason. A feature with a much larger numeric range can dominate Euclidean distance and therefore change every neighborhood.

## LOF has practical limits

- Nearest-neighbor calculations become expensive as the dataset grows.
- Distance becomes less informative in high-dimensional spaces.
- Scores from different fitted datasets are not automatically comparable because each score depends on its reference neighborhood.
- Standard outlier detection scores the training observations; scoring genuinely new observations requires a novelty-detection setup.

Applications include fraud detection, network intrusion, medical anomaly detection, and manufacturing quality control. In each case, the useful interpretation is local: the observation differs from nearby peers, not necessarily from the entire population.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Local Outlier Factor: so sánh một point với các point lân cận

Global distance threshold có thể bỏ sót anomaly khi một vùng của dataset tự nhiên rất dày còn vùng khác lại thưa. Local Outlier Factor (LOF) thay vào đó kiểm tra một point có mật độ thấp hơn đáng kể so với chính các neighbor của nó hay không.

LOF được Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng và Jörg Sander giới thiệu năm 2000.

## Ba đại lượng dẫn đến LOF score

Với neighborhood size `k` đã chọn:

1. **k-distance:** khoảng cách từ một point đến neighbor gần thứ k.
2. **Reachability distance:** với hai point `a` và `b`, lấy giá trị lớn hơn giữa khoảng cách thực tế của chúng và k-distance của `b`.
3. **Local reachability density (LRD):** nghịch đảo của average reachability distance từ một point đến các neighbor.

Reachability distance ngăn các cặp point cực gần chi phối density calculation. LRD sau đó biểu diễn một point liên kết chặt đến mức nào với local neighborhood.

## LOF so sánh local density dưới dạng tỉ lệ

LOF score so sánh LRD của một point với average LRD của các neighbor:

- `LOF ≈ 1`: point có density tương tự neighbor.
- `LOF > 1`: point thưa hơn neighbor và có thể là outlier.
- Score lớn hơn cho biết local isolation mạnh hơn.

Đây là lý do LOF có thể tìm được một point trông bình thường dưới global distance rule nhưng bất thường trong chính vùng của nó.

## Neighborhood size làm thay đổi câu hỏi

`k` nhỏ khiến score nhạy với cấu trúc rất cục bộ và noise. `k` lớn so sánh từng point với vùng rộng hơn và có thể làm mất các anomalous pocket nhỏ. Không có một giá trị đúng cho mọi bài toán; `k` xác định scale của khái niệm “local”.

Feature scaling và distance metric quan trọng vì cùng lý do. Feature có numeric range lớn hơn nhiều có thể chi phối Euclidean distance và làm thay đổi toàn bộ neighborhood.

## LOF có các giới hạn thực tế

- Nearest-neighbor calculation trở nên tốn kém khi dataset lớn.
- Distance ít mang thông tin hơn trong không gian nhiều chiều.
- Score từ các fitted dataset khác nhau không tự động so sánh được vì mỗi score phụ thuộc vào reference neighborhood.
- Standard outlier detection chấm điểm training observation; chấm điểm observation hoàn toàn mới cần novelty-detection setup.

Ứng dụng gồm fraud detection, network intrusion, medical anomaly detection và quality control trong sản xuất. Trong mỗi trường hợp, cách diễn giải hữu ích là cục bộ: observation khác với các peer gần nó, không nhất thiết khác toàn bộ population.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
