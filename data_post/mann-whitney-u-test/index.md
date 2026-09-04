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

An independent [t-test](/data_post/t-test/) compares the means of two groups under assumptions about the sampling process and distributions. The Mann–Whitney U test provides a rank-based comparison when a normal model for the outcome is not appropriate.

## The test uses relative ordering

Combine the observations from both groups, rank them, and calculate the rank sum for each group. If values from the two groups occupy similar positions in the combined ranking, their rank sums should also be similar.

For group sizes `n1` and `n2`, with rank sums `R1` and `R2`:

- `U1 = n1 × n2 + n1 × (n1 + 1) / 2 - R1`
- `U2 = n1 × n2 + n2 × (n2 + 1) / 2 - R2`

The smaller of `U1` and `U2` is commonly used as the test statistic. Statistical software then obtains a p-value from its exact or asymptotic distribution, depending on sample size and ties.

## The hypotheses concern the distributions

- **Null hypothesis:** observations from the two populations have the same distribution, expressed by the test as neither group tending to produce larger values than the other.
- **Alternative hypothesis:** observations from one population tend to be larger or smaller than observations from the other.

If the two distributions have the same shape and spread, a location shift can be interpreted as a difference in medians. Without that condition, a significant result does not by itself prove that the medians differ; it may reflect another distributional difference.

## Use it for two independent groups

Mann–Whitney U is appropriate for two independent groups with an ordinal or continuous outcome when ranking is meaningful. It is not the non-parametric test for paired observations; paired data require a paired method such as the Wilcoxon signed-rank test.

The important distinction is simple: the t-test works with means and standard errors, while Mann–Whitney U works with the ordering of observations.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Mann–Whitney U: so sánh thứ hạng, không phải trung bình

Independent [t-test](/data_post/t-test/) so sánh mean của hai group dựa trên assumption về sampling process và distribution. Mann–Whitney U cung cấp một phép so sánh dựa trên rank khi normal model không phù hợp với outcome.

## Test sử dụng thứ tự tương đối

Gộp observation của hai group, xếp hạng chúng và tính rank sum của mỗi group. Nếu value từ hai group chiếm vị trí tương tự nhau trong ranking chung, rank sum của chúng cũng phải tương tự.

Với group size `n1`, `n2` và rank sum `R1`, `R2`:

- `U1 = n1 × n2 + n1 × (n1 + 1) / 2 - R1`
- `U2 = n1 × n2 + n2 × (n2 + 1) / 2 - R2`

Giá trị nhỏ hơn giữa `U1` và `U2` thường được dùng làm test statistic. Statistical software sau đó lấy p-value từ exact hoặc asymptotic distribution, tùy sample size và các giá trị bị tie.

## Hypothesis liên quan đến distribution

- **Null hypothesis:** observation từ hai population có cùng distribution; test biểu diễn điều này bằng việc không group nào có xu hướng tạo value lớn hơn group còn lại.
- **Alternative hypothesis:** observation từ một population có xu hướng lớn hơn hoặc nhỏ hơn population kia.

Nếu hai distribution có cùng shape và spread, location shift có thể được diễn giải thành chênh lệch median. Nếu không có điều kiện này, significant result không tự nó chứng minh median khác nhau; kết quả có thể đến từ một khác biệt distribution khác.

## Dùng cho hai group độc lập

Mann–Whitney U phù hợp với hai group độc lập có ordinal hoặc continuous outcome khi ranking có ý nghĩa. Đây không phải non-parametric test cho paired observation; paired data cần phương pháp theo cặp như Wilcoxon signed-rank test.

Khác biệt quan trọng rất đơn giản: t-test làm việc với mean và standard error, còn Mann–Whitney U làm việc với thứ tự của các observation.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
