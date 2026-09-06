---
title: "Mann–Whitney U: Compare Ranks, Not Means"
title_vi: "Mann–Whitney U: so sánh thứ hạng, không phải trung bình"
title_en: "Mann–Whitney U: Compare Ranks, Not Means"
description: What the Mann–Whitney U test measures, when it replaces an independent t-test, and when a median interpretation is valid.
description_vi: Mann–Whitney U đo gì, khi nào thay independent t-test và khi nào có thể diễn giải bằng median.
description_en: What the Mann–Whitney U test measures, when it replaces an independent t-test, and when a median interpretation is valid.
date: 2026-04-08
writing_topic: statistics
---

{% capture article_en %}
🔙 [Back to Home](/)

# Mann–Whitney U: Compare Ranks, Not Means

An independent [t-test](/data_post/t-test/) compares the means of two groups. Mann–Whitney U asks a different question: whether observations from one independent group tend to rank above or below observations from the other. It is not simply a t-test with the normality assumption removed.

## The test uses relative ordering

Combine the observations from both groups, rank them, and calculate the rank sum for each group. If values from the two groups occupy similar positions in the combined ranking, their rank sums should also be similar.

For group sizes `n1` and `n2`, with rank sums `R1` and `R2`:

- `U1 = n1 × n2 + n1 × (n1 + 1) / 2 - R1`
- `U2 = n1 × n2 + n2 × (n2 + 1) / 2 - R2`

The smaller of `U1` and `U2` is commonly used as the test statistic. Statistical software then obtains a p-value from its exact or asymptotic distribution, depending on sample size and ties.

For a small example, let Group A contain `[1, 3, 5]` and Group B contain `[2, 4, 6]`. Their combined ranks alternate between the groups. The rank sums are `R1 = 9` and `R2 = 12`, producing U statistics of `6` and `3`; the smaller value is `3`. The calculation uses ordering, so replacing the values with any monotonically transformed scale leaves the ranks unchanged.

When values are tied, they receive average ranks. Ties also affect the variance used by the asymptotic p-value, which is why hand calculations and software output can differ if tie correction or the exact/asymptotic method is not stated.

## The hypotheses concern the distributions

- **Null hypothesis:** observations from the two populations have the same distribution, expressed by the test as neither group tending to produce larger values than the other.
- **Alternative hypothesis:** observations from one population tend to be larger or smaller than observations from the other.

If the two distributions have the same shape and spread, a location shift can be interpreted as a difference in medians. Without that condition, a significant result does not by itself prove that the medians differ; it may reflect another distributional difference.

This distinction is visible when one group is much more variable than the other. Their medians can be equal while observations from one distribution still occupy systematically different ranks. Plotting both distributions is therefore part of interpreting the test, not decoration after the p-value.

## Use it for two independent groups

Mann–Whitney U is appropriate for two independent groups with an ordinal or continuous outcome when ranking is meaningful. It is not the non-parametric test for paired observations; paired data require a paired method such as the Wilcoxon signed-rank test.

Non-normality alone does not automatically require Mann–Whitney U. Welch's t-test can still be useful for a mean comparison, especially with adequate sample sizes, while Mann–Whitney answers a rank-based distributional question. The test should follow the estimand: use the method that matches what the analysis is trying to compare.

## Report magnitude, not only the p-value

Alongside the U statistic and p-value, report the group sizes, medians, interquartile ranges, and an effect size such as rank-biserial correlation or probability of superiority. State the direction convention used by the software, because implementations may attach U to different groups.

The final interpretation should remain narrow: one group tends to produce larger observations than the other under the sampling design. Causality still depends on how the groups were created, and a small p-value does not tell us whether the difference matters operationally.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Mann–Whitney U: so sánh thứ hạng, không phải trung bình

Independent [t-test](/data_post/t-test/) so sánh mean của hai group. Mann–Whitney U trả lời một câu hỏi khác: observation từ một group độc lập có xu hướng xếp hạng cao hơn hay thấp hơn group còn lại. Đây không đơn thuần là t-test sau khi bỏ normality assumption.

## Test sử dụng thứ tự tương đối

Gộp observation của hai group, xếp hạng chúng và tính rank sum của mỗi group. Nếu value từ hai group chiếm vị trí tương tự nhau trong ranking chung, rank sum của chúng cũng phải tương tự.

Với group size `n1`, `n2` và rank sum `R1`, `R2`:

- `U1 = n1 × n2 + n1 × (n1 + 1) / 2 - R1`
- `U2 = n1 × n2 + n2 × (n2 + 1) / 2 - R2`

Giá trị nhỏ hơn giữa `U1` và `U2` thường được dùng làm test statistic. Statistical software sau đó lấy p-value từ exact hoặc asymptotic distribution, tùy sample size và các giá trị bị tie.

Trong một ví dụ nhỏ, Group A gồm `[1, 3, 5]` và Group B gồm `[2, 4, 6]`. Rank sau khi gộp xen kẽ giữa hai group. Rank sum là `R1 = 9` và `R2 = 12`, tạo hai U statistic là `6` và `3`; giá trị nhỏ hơn là `3`. Phép tính chỉ dùng thứ tự nên nếu thay value bằng bất kỳ monotonic transformation nào thì rank vẫn không đổi.

Khi value bị tie, chúng nhận average rank. Tie cũng ảnh hưởng variance dùng để tính asymptotic p-value; vì vậy hand calculation và software output có thể khác nếu không nêu rõ tie correction hoặc exact/asymptotic method.

## Hypothesis liên quan đến distribution

- **Null hypothesis:** observation từ hai population có cùng distribution; test biểu diễn điều này bằng việc không group nào có xu hướng tạo value lớn hơn group còn lại.
- **Alternative hypothesis:** observation từ một population có xu hướng lớn hơn hoặc nhỏ hơn population kia.

Nếu hai distribution có cùng shape và spread, location shift có thể được diễn giải thành chênh lệch median. Nếu không có điều kiện này, significant result không tự nó chứng minh median khác nhau; kết quả có thể đến từ một khác biệt distribution khác.

Khác biệt này thấy rõ khi một group có variance lớn hơn nhiều group còn lại. Median có thể bằng nhau nhưng observation từ một distribution vẫn chiếm các rank khác một cách có hệ thống. Vì vậy, plot cả hai distribution là một phần của việc diễn giải test, không phải phần trang trí sau p-value.

## Dùng cho hai group độc lập

Mann–Whitney U phù hợp với hai group độc lập có ordinal hoặc continuous outcome khi ranking có ý nghĩa. Đây không phải non-parametric test cho paired observation; paired data cần phương pháp theo cặp như Wilcoxon signed-rank test.

Non-normality không tự động buộc phải dùng Mann–Whitney U. Welch's t-test vẫn có thể phù hợp cho câu hỏi về mean, nhất là khi sample size đủ lớn; Mann–Whitney trả lời câu hỏi distribution dựa trên rank. Test cần đi theo estimand: chọn phương pháp phù hợp với đại lượng phân tích thực sự muốn so sánh.

## Báo cáo độ lớn, không chỉ p-value

Cùng với U statistic và p-value, cần báo cáo group size, median, interquartile range và effect size như rank-biserial correlation hoặc probability of superiority. Cần nêu convention về hướng mà software sử dụng vì các implementation có thể gắn U cho group khác nhau.

Diễn giải cuối cùng phải giữ đúng phạm vi: observation từ một group có xu hướng lớn hơn group kia trong sampling design đã dùng. Causality vẫn phụ thuộc vào cách hai group được tạo ra, và p-value nhỏ không cho biết chênh lệch có quan trọng về vận hành hay không.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
