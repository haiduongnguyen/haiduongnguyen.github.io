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

A global distance threshold can miss anomalies when one part of a dataset is naturally dense and another is sparse. Local Outlier Factor (LOF) instead asks whether a point has substantially lower density than its own neighbors. The key modeling choice is therefore not only the score threshold, but what counts as a neighbor.

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

In the synthetic APM data, latency reaches a much larger numeric range than CPU or memory. Feeding the raw columns into Euclidean distance would allow latency to dominate the neighborhood geometry. Scaling should be fitted on the training reference data and then reused; fitting it separately on evaluation data changes the space in which “local” is defined.

The value of `k` should be treated as a sensitivity analysis rather than selected from one attractive output. Compare several plausible neighborhoods and inspect whether the same traces remain unusual. If the anomaly list changes completely with a small change in `k`, the local-density conclusion is fragile.

## LOF has practical limits

- Nearest-neighbor calculations become expensive as the dataset grows.
- Distance becomes less informative in high-dimensional spaces.
- Scores from different fitted datasets are not automatically comparable because each score depends on its reference neighborhood.
- Standard outlier detection scores the training observations; scoring genuinely new observations requires a novelty-detection setup.

Applications include fraud detection, network intrusion, medical anomaly detection, and manufacturing quality control. In each case, the useful interpretation is local: the observation differs from nearby peers, not necessarily from the entire population.

## Outlier detection and novelty detection are different deployments

Standard LOF compares observations inside the dataset used to fit the neighborhoods. In a monitoring system, new spans arrive after the reference data have been fitted. That requires novelty-detection mode and a stable preprocessing pipeline; refitting on every new batch changes both the neighborhoods and the meaning of the scores.

The evaluation split should also respect `trace_id` because the synthetic dataset contains five spans per trace with a shared label. Otherwise, close relatives from one generated request can appear in both the reference and evaluation sets.

## LOF and Isolation Forest fail in different ways

| Question | LOF | Isolation Forest |
| --- | --- | --- |
| Evidence of anomaly | Lower density than nearby observations | Short average isolation path |
| Most sensitive design choice | Distance, scaling, and `k` | Subsample, feature set, and score threshold |
| Strength | Detects local deviations across regions with different density | Scales without explicit nearest-neighbor search |
| Main risk | Distance degrades in high dimensions | An easy-to-isolate point is not automatically a root cause |

The comparison should use the same trace-level split and alert budget. Otherwise, a difference in preprocessing or evaluation population can be mistaken for a difference between algorithms.

LOF answers a narrow question: is this observation sparse relative to its chosen neighborhood? Selecting the neighborhood, preserving it for new data, and deciding whether the resulting alert is operationally useful remain separate parts of the system.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Local Outlier Factor: so sánh một point với các point lân cận

Global distance threshold có thể bỏ sót anomaly khi một vùng của dataset tự nhiên rất dày còn vùng khác lại thưa. Local Outlier Factor (LOF) thay vào đó kiểm tra một point có mật độ thấp hơn đáng kể so với chính các neighbor của nó hay không. Vì vậy, modeling choice quan trọng không chỉ là score threshold mà còn là thế nào được coi là một neighbor.

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

Trong synthetic APM data, latency có numeric range lớn hơn nhiều CPU hoặc memory. Đưa raw column trực tiếp vào Euclidean distance sẽ khiến latency chi phối neighborhood geometry. Scaling phải được fit trên training reference data rồi tái sử dụng; fit riêng trên evaluation data sẽ thay đổi không gian định nghĩa “local”.

Giá trị `k` cần được xem như sensitivity analysis thay vì chọn từ một output đẹp. Nên so sánh nhiều neighborhood hợp lý và kiểm tra cùng trace có tiếp tục bị coi là bất thường hay không. Nếu anomaly list thay đổi hoàn toàn chỉ với một thay đổi nhỏ của `k`, kết luận local-density đang rất mong manh.

## LOF có các giới hạn thực tế

- Nearest-neighbor calculation trở nên tốn kém khi dataset lớn.
- Distance ít mang thông tin hơn trong không gian nhiều chiều.
- Score từ các fitted dataset khác nhau không tự động so sánh được vì mỗi score phụ thuộc vào reference neighborhood.
- Standard outlier detection chấm điểm training observation; chấm điểm observation hoàn toàn mới cần novelty-detection setup.

Ứng dụng gồm fraud detection, network intrusion, medical anomaly detection và quality control trong sản xuất. Trong mỗi trường hợp, cách diễn giải hữu ích là cục bộ: observation khác với các peer gần nó, không nhất thiết khác toàn bộ population.

## Outlier detection và novelty detection là hai cách triển khai khác nhau

Standard LOF so sánh các observation bên trong dataset dùng để fit neighborhood. Trong monitoring system, span mới đến sau khi reference data đã được fit. Trường hợp đó cần novelty-detection mode và preprocessing pipeline ổn định; refit trên từng batch mới sẽ thay đổi cả neighborhood lẫn ý nghĩa của score.

Evaluation split cũng phải tôn trọng `trace_id` vì synthetic dataset có năm span mỗi trace và dùng chung label. Nếu không, các observation gần nhau từ cùng một generated request có thể xuất hiện trong cả reference set và evaluation set.

## LOF và Isolation Forest thất bại theo những cách khác nhau

| Câu hỏi | LOF | Isolation Forest |
| --- | --- | --- |
| Anomaly evidence | Mật độ thấp hơn các observation lân cận | Average isolation path ngắn |
| Design choice nhạy nhất | Distance, scaling và `k` | Subsample, feature set và score threshold |
| Điểm mạnh | Phát hiện local deviation giữa các vùng có mật độ khác nhau | Scale tốt hơn mà không cần nearest-neighbor search rõ ràng |
| Rủi ro chính | Distance mất ý nghĩa trong high-dimensional data | Point dễ cô lập không tự động là root cause |

Phép so sánh phải dùng cùng trace-level split và alert budget. Nếu không, khác biệt về preprocessing hoặc evaluation population có thể bị hiểu nhầm thành khác biệt giữa hai thuật toán.

LOF trả lời một câu hỏi hẹp: observation này có thưa hơn so với neighborhood đã chọn không? Việc chọn neighborhood, giữ nguyên nó cho dữ liệu mới và quyết định alert có giá trị vận hành hay không vẫn là những phần riêng của hệ thống.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
