---
title: T-tests
title_vi: T-test — chọn đúng kiểm định và báo cáo đúng
title_en: T-tests — choosing and reporting the right test
description: One-sample, Welch's independent, and paired t-tests with assumptions, confidence intervals, and Python examples.
description_vi: One-sample, Welch independent và paired t-test với assumptions, confidence interval và ví dụ Python.
description_en: One-sample, Welch's independent, and paired t-tests with assumptions, confidence intervals, and Python examples.
date: 2026-04-08
writing_topic: statistics
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>T-test</h1><p>Nhóm kiểm định dùng chênh lệch mean, mức biến thiên và sample size để đánh giá một khác biệt có tương thích với giả thuyết không hay không.</p></header>
  <h2>Chọn loại nào?</h2><div class="table-wrap"><table><thead><tr><th>Thiết kế</th><th>Kiểm định</th><th>Ví dụ</th></tr></thead><tbody><tr><td>Một mẫu so với mốc</td><td>One-sample t-test</td><td>Mean transaction amount có khác 1 triệu?</td></tr><tr><td>Hai nhóm độc lập</td><td>Welch’s t-test</td><td>Mean của segment A và B</td></tr><tr><td>Cùng đối tượng trước/sau</td><td>Paired t-test</td><td>Chi tiêu trước và sau campaign</td></tr></tbody></table></div>
  <p>Với hai nhóm độc lập, Welch’s t-test thường là lựa chọn an toàn hơn vì không giả định equal variance.</p>
  <h2>Assumptions</h2><ul><li>Quan sát độc lập theo đúng thiết kế.</li><li>Outcome là dữ liệu số và mean có ý nghĩa.</li><li>Dữ liệu hoặc paired differences không có outlier quá mạnh.</li><li>Normality quan trọng hơn khi mẫu nhỏ; với mẫu lớn, cần chú ý practical significance vì p-value rất nhạy.</li></ul>
  <h2>Python</h2><pre><code>from scipy import stats

one_sample = stats.ttest_1samp(sample, popmean=100)
independent = stats.ttest_ind(group_a, group_b, equal_var=False)
paired = stats.ttest_rel(before, after)</code></pre>
  <h2>Đừng chỉ báo p-value</h2><p>Nên báo mean của mỗi nhóm, mean difference, confidence interval, effect size, sample size và assumptions. P-value nhỏ không nói khác biệt có lớn hoặc hữu ích trong kinh doanh hay không.</p>
  <h2>P-value, normality, uncertainty và multiple testing</h2>
  <h3>P-value là xác suất có điều kiện theo H₀</h3><p>P-value không phải xác suất “kết quả xảy ra do ngẫu nhiên”, cũng không phải xác suất H₀ đúng. Nó là xác suất thu được test statistic ít nhất cực đoan như statistic đã quan sát, với điều kiện H₀ và các assumptions của model đúng. Cách diễn đạt này dài hơn nhưng tránh một trong những hiểu nhầm phổ biến nhất của thống kê.</p>
  <h3>Normality áp dụng cho đại lượng được kiểm định</h3><p>Với paired t-test, điều cần gần normal là phân phối của paired differences, không phải từng cột before và after riêng lẻ. Với two-sample test, independence và sampling design thường quan trọng hơn một normality test máy móc. Shapiro–Wilk có thể quá nhạy khi n lớn và thiếu power khi n nhỏ; nên xem Q–Q plot, outlier và ý nghĩa của mean.</p>
  <h3>Welch thường là mặc định tốt cho hai nhóm độc lập</h3><p>Student’s pooled t-test cần giả định equal variance. Welch’s test không cần giả định đó và thường mất rất ít power khi variance thực sự bằng nhau. Equal variance phải đến từ thiết kế hoặc bằng chứng vững, không nên chỉ dựa vào một preliminary test rồi mới quyết định test chính.</p>
  <h3>Thêm uncertainty bằng bootstrap interval</h3><pre><code class="language-python">import numpy as np

def bootstrap_mean_difference(group_a, group_b, repeats=10_000, seed=42):
    rng = np.random.default_rng(seed)
    differences = np.empty(repeats)
    for index in range(repeats):
        sample_a = rng.choice(group_a, size=len(group_a), replace=True)
        sample_b = rng.choice(group_b, size=len(group_b), replace=True)
        differences[index] = sample_a.mean() - sample_b.mean()
    estimate = np.mean(group_a) - np.mean(group_b)
    lower, upper = np.quantile(differences, [0.025, 0.975])
    return estimate, (lower, upper)</code></pre>
  <p>Bootstrap không sửa được dữ liệu phụ thuộc hoặc sample bias. Resampling unit phải khớp thiết kế: nếu dữ liệu được cluster theo khách hàng, cần resample theo khách hàng thay vì từng transaction.</p>
  <h3>Đặt kế hoạch cho multiple testing</h3><p>Nếu thử 100 feature với α = 0,05, false positive sẽ xuất hiện ngay cả khi không có effect thật. Xác định primary metric trước, hoặc dùng điều chỉnh như Holm/Benjamini–Hochberg tùy mục tiêu kiểm soát family-wise error hay false discovery rate.</p>
  <h2>Nguồn</h2><ul><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html">SciPy: ttest_1samp</a></li><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html">SciPy: ttest_ind</a></li><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html">SciPy: ttest_rel</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><h1>T-tests</h1><p>A family of tests that uses a mean difference, variability, and sample size to evaluate compatibility with a null hypothesis.</p></header>
  <h2>Which test?</h2><div class="table-wrap"><table><thead><tr><th>Design</th><th>Test</th><th>Example</th></tr></thead><tbody><tr><td>One sample versus a reference</td><td>One-sample t-test</td><td>Does mean transaction amount differ from one million?</td></tr><tr><td>Two independent groups</td><td>Welch’s t-test</td><td>Mean difference between segments A and B</td></tr><tr><td>Same units before/after</td><td>Paired t-test</td><td>Spending before and after a campaign</td></tr></tbody></table></div>
  <p>For two independent groups, Welch’s t-test is often the safer default because it does not assume equal variances.</p>
  <h2>Assumptions</h2><ul><li>Observations follow the independence or pairing in the design.</li><li>The outcome is numerical and a mean is meaningful.</li><li>The data or paired differences are not dominated by extreme outliers.</li><li>Normality matters more with small samples; with large samples, focus on practical significance because p-values become sensitive.</li></ul>
  <h2>Python</h2><pre><code>from scipy import stats

one_sample = stats.ttest_1samp(sample, popmean=100)
independent = stats.ttest_ind(group_a, group_b, equal_var=False)
paired = stats.ttest_rel(before, after)</code></pre>
  <h2>Report more than a p-value</h2><p>Include group means, the mean difference, a confidence interval, effect size, sample sizes, and assumptions. A small p-value does not say whether the effect is large or useful.</p>
  <h2>P-values, normality, uncertainty, and multiple testing</h2>
  <h3>A p-value is conditional on the null hypothesis</h3><p>A p-value is not the probability that the result “occurred by chance,” nor the probability that the null is true. It is the probability of a test statistic at least as extreme as the observed statistic, assuming the null hypothesis and model assumptions hold. The longer wording prevents one of the most common statistical misinterpretations.</p>
  <h3>Normality applies to the quantity being tested</h3><p>For a paired t-test, the paired differences—not the two before/after columns separately—should be approximately normal. For independent groups, independence and sampling design are often more important than a mechanical normality test. Shapiro–Wilk can be overly sensitive at large n and underpowered at small n; inspect Q–Q plots, outliers, and whether a mean is meaningful.</p>
  <h3>Welch is a sensible default for independent groups</h3><p>Student’s pooled t-test assumes equal variances. Welch’s test does not and usually gives up little power when variances really are equal. Equal variance should follow from the design or strong evidence, not from using one preliminary test to decide which primary test to run.</p>
  <h3>Add uncertainty with a bootstrap interval</h3><pre><code class="language-python">import numpy as np

def bootstrap_mean_difference(group_a, group_b, repeats=10_000, seed=42):
    rng = np.random.default_rng(seed)
    differences = np.empty(repeats)
    for index in range(repeats):
        sample_a = rng.choice(group_a, size=len(group_a), replace=True)
        sample_b = rng.choice(group_b, size=len(group_b), replace=True)
        differences[index] = sample_a.mean() - sample_b.mean()
    estimate = np.mean(group_a) - np.mean(group_b)
    lower, upper = np.quantile(differences, [0.025, 0.975])
    return estimate, (lower, upper)</code></pre>
  <p>Bootstrap resampling does not repair dependent data or sampling bias. Match the resampling unit to the design: customer-clustered observations should be resampled by customer, not by transaction.</p>
  <h3>Plan for multiple testing</h3><p>Testing 100 features at α = 0.05 produces false positives even when no real effects exist. Pre-specify a primary metric, or use a procedure such as Holm or Benjamini–Hochberg depending on whether the goal is family-wise error or false-discovery-rate control.</p>
  <h2>Sources</h2><ul><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html">SciPy: ttest_1samp</a></li><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html">SciPy: ttest_ind</a></li><li><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html">SciPy: ttest_rel</a></li></ul>
</article>
