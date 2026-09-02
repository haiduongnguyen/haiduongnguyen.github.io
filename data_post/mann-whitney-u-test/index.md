---
title: Mann–Whitney U Test
title_vi: Mann–Whitney U test và cách diễn giải
title_en: Mann–Whitney U test and interpretation
description: What the Mann–Whitney U test measures, its assumptions, and how to report it without overclaiming a median difference.
description_vi: Mann–Whitney U đo gì, cần giả định nào và vì sao không nên luôn diễn giải thành khác biệt median.
description_en: What the Mann–Whitney U test measures, its assumptions, and how to report it without overclaiming a median difference.
date: 2026-04-08
writing_topic: statistics
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>Mann–Whitney U test</h1><p>Một kiểm định phi tham số cho hai mẫu độc lập, dựa trên thứ hạng thay vì trực tiếp dùng giá trị gốc.</p></header>
  <h2>Kiểm định trả lời câu hỏi gì?</h2><p>Giả thuyết không tổng quát là hai phân phối giống nhau. Có thể hiểu statistic thông qua xác suất một quan sát ngẫu nhiên từ nhóm X lớn hơn một quan sát từ nhóm Y, có xử lý tie.</p>
  <div class="callout"><p><strong>Không nên mặc định nói đây là “kiểm định median”.</strong> Chỉ khi hai phân phối có hình dạng và độ phân tán tương tự, khác biệt mới có thể được diễn giải chủ yếu như location/median shift.</p></div>
  <h2>Assumptions</h2><ul><li>Hai nhóm độc lập.</li><li>Quan sát trong mỗi nhóm độc lập.</li><li>Biến đo ít nhất ở thang ordinal.</li><li>Nếu muốn diễn giải median shift, hình dạng phân phối cần tương tự.</li></ul>
  <h2>Python</h2><pre><code>from scipy.stats import mannwhitneyu

result = mannwhitneyu(group_a, group_b, alternative="two-sided")
print(result.statistic, result.pvalue)</code></pre>
  <p>Khi báo cáo, nên kèm sample size, U statistic, p-value, effect size và mô tả phân phối. “Không reject H0” không có nghĩa là chứng minh hai nhóm giống nhau.</p>
  <h2>Effect size, exact inference và lựa chọn kiểm định</h2>
  <h3>U đo thứ tự cặp quan sát</h3><p>Sau khi xử lý tie, U liên hệ với xác suất một quan sát ngẫu nhiên của nhóm A lớn hơn một quan sát của nhóm B. Điều này giúp effect size dễ hiểu hơn, nhưng không tự động xác định khác biệt đến từ median, spread hay shape.</p>
  <pre><code class="language-python">import numpy as np

def mann_whitney_u_and_rank_biserial(group_a, group_b):
    values = np.concatenate([group_a, group_b])
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    start = 0
    while start &lt; len(values):
        end = start + 1
        while end &lt; len(values) and values[order[end]] == values[order[start]]:
            end += 1
        ranks[order[start:end]] = (start + 1 + end) / 2.0
        start = end

    n_a, n_b = len(group_a), len(group_b)
    u_a = ranks[:n_a].sum() - n_a * (n_a + 1) / 2.0
    rank_biserial = 2.0 * u_a / (n_a * n_b) - 1.0
    return u_a, rank_biserial</code></pre>
  <h3>Exact và asymptotic p-value không giống nhau</h3><p>Với mẫu nhỏ và không có tie, exact distribution có thể phù hợp. Với mẫu lớn hoặc có tie, software thường dùng asymptotic approximation kèm tie correction. Cần ghi lại method/version thay vì chỉ lưu một p-value không có ngữ cảnh.</p>
  <h3>Không dùng cho dữ liệu paired</h3><p>Nếu mỗi quan sát ở A ghép với cùng đối tượng ở B, independence giữa hai nhóm không còn đúng. Hãy phân tích paired differences và cân nhắc paired t-test hoặc Wilcoxon signed-rank tùy câu hỏi và assumptions.</p>
  <h3>Nhìn distribution trước khi đặt tên effect</h3><p>Vẽ ECDF, box/violin plot và báo quantile. Nếu hai nhóm khác shape hoặc spread, hãy mô tả đó là distributional difference; chỉ dùng ngôn ngữ “median shift” khi assumption hình dạng tương tự có cơ sở.</p>
  <h2>Nguồn</h2><ul><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html">SciPy: mannwhitneyu</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><h1>Mann–Whitney U test</h1><p>A non-parametric test for two independent samples that works with ranks rather than raw values.</p></header>
  <h2>What question does it answer?</h2><p>The general null hypothesis is that the two distributions are the same. The statistic can also be understood through the probability that a random observation from X exceeds one from Y, with ties handled appropriately.</p>
  <div class="callout"><p><strong>Do not automatically call it a “test of medians.”</strong> A location or median-shift interpretation needs similarly shaped distributions with comparable spread.</p></div>
  <h2>Assumptions</h2><ul><li>The two groups are independent.</li><li>Observations within each group are independent.</li><li>The outcome is at least ordinal.</li><li>A median-shift interpretation requires similarly shaped distributions.</li></ul>
  <h2>Python</h2><pre><code>from scipy.stats import mannwhitneyu

result = mannwhitneyu(group_a, group_b, alternative="two-sided")
print(result.statistic, result.pvalue)</code></pre>
  <p>Report sample sizes, the U statistic, p-value, an effect size, and distribution summaries. Failing to reject the null does not prove that the groups are identical.</p>
  <h2>Effect size, exact inference, and test selection</h2>
  <h3>U measures pairwise ordering</h3><p>After accounting for ties, U is related to the probability that a random observation from group A exceeds one from group B. That gives an interpretable effect size, but it does not identify whether a difference comes from the median, spread, or distribution shape.</p>
  <pre><code class="language-python">import numpy as np

def mann_whitney_u_and_rank_biserial(group_a, group_b):
    values = np.concatenate([group_a, group_b])
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    start = 0
    while start &lt; len(values):
        end = start + 1
        while end &lt; len(values) and values[order[end]] == values[order[start]]:
            end += 1
        ranks[order[start:end]] = (start + 1 + end) / 2.0
        start = end

    n_a, n_b = len(group_a), len(group_b)
    u_a = ranks[:n_a].sum() - n_a * (n_a + 1) / 2.0
    rank_biserial = 2.0 * u_a / (n_a * n_b) - 1.0
    return u_a, rank_biserial</code></pre>
  <h3>Exact and asymptotic p-values are different calculations</h3><p>For small samples without ties, an exact null distribution may be appropriate. With larger samples or ties, software commonly uses an asymptotic approximation and tie correction. Record the method and library version instead of storing a context-free p-value.</p>
  <h3>Do not use it for paired data</h3><p>If each A observation is matched to the same unit in B, independence between groups is false. Analyze the paired differences and consider a paired t-test or Wilcoxon signed-rank test, depending on the question and assumptions.</p>
  <h3>Inspect distributions before naming the effect</h3><p>Plot ECDFs, box/violin summaries, and quantiles. If shapes or spreads differ, describe a distributional difference; use “median shift” language only when the similarly-shaped-distribution assumption is defensible.</p>
  <h2>Source</h2><ul><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html">SciPy: mannwhitneyu</a></li></ul>
</article>
