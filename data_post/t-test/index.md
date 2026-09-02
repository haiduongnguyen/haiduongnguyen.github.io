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

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

🔙 [Back to Home](/)

## I. What is a T-test?

A **T-test** is a type of inferential statistic used to determine if there is a significant difference between the means of two groups, which may be related in certain features. It is heavily used in hypothesis testing to assess whether a process or treatment actually had an effect on the population of interest.

To put it simply, a T-test helps us answer: *"Are these two groups really different, or is the difference we see just due to random chance?"*

**Key Terms:**
- **Null Hypothesis ($H_0$):** Assumes there is no significant difference between the populations.
- **Alternative Hypothesis ($H_1$):** Assumes there is a significant difference.
- **t-value:** The calculated difference represented in units of standard error. The larger the absolute t-value, the stronger the evidence against the null hypothesis.
- **p-value:** The probability that the results from your sample data occurred by chance. If $p < \alpha$ (usually chosen as $0.05$), we reject the null hypothesis.

---

## II. Assumptions of T-test

Before applying a T-test, your data must satisfy these assumptions. If they fail, you should consider using non-parametric alternative tests.

1. **Continuous Data:** The target variable should be measured on a continuous or ordinal scale.
2. **Random Sample:** Data should be collected from a representative, randomly selected portion of the total population.
3. **Normal Distribution:** The data should approximately follow a normal (Gaussian) distribution. (Can be checked via Shapiro-Wilk test or Q-Q plots).
4. **Homogeneity of Variance:** (Specifically for Independent T-test) The variances of the 2 groups should be approximately equal. If they are not equal, we must use a variant called **Welch's T-test**.

---

## III. Three Main Types of T-test 

There are three main types of T-tests depending on the structure of your data and what you want to compare:

### 1. One-Sample T-test
Used to compare the mean of a single group against a known mean (a theoretical mean, or a population mean).

- **Formula:** 
  $$ t = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$
  *(Where $\bar{x}$ = sample mean, $\mu$ = population mean, $s$ = sample standard deviation, $n$ = sample size)*

- **Example:** A teacher has a class of 30 students. The teacher wants to statistically test if the average height of students in this class is significantly different from $170\text{ cm}$.

### 2. Independent Two-Sample T-test (Unpaired)
Used to compare the means of **two independent groups** to determine whether there is statistical evidence that the associated population means are significantly different.

- **Formula (Assuming Equal Variances):**
  $$ t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} $$
  *(Where $s_p$ is the pooled standard deviation)*

- **Example:** A teacher wants to test if there is a significant height difference between Class A and Class B.

### 3. Paired Sample T-test
Used to compare the means of two **related groups**. Often used for "before and after" studies on the *exact same* subjects.

- **Formula:**
  $$ t = \frac{\bar{d}}{s_d / \sqrt{n}} $$
  *(Where $\bar{d}$ = mean difference between the paired observations, $s_d$ = standard deviation of the differences)*

- **Example:** Measuring the weight of 20 patients *before* and *after* an 8-week diet plan.

---

## IV. Python Implementation (Examples & Code)

In Python, we can easily perform all types of T-tests using the `scipy.stats` library.

```python
import numpy as np
from scipy import stats

# Set random seed to generate reproducible dummy data
np.random.seed(42)

# ==========================================
# 1. One-Sample T-test
# ==========================================
print("--- 1. One-Sample T-test ---")

# Hypothesis: Is the sample mean significantly different from 170?
sample_heights = np.random.normal(loc=172, scale=5, size=30)
theoretical_mean = 170

t_stat, p_value = stats.ttest_1samp(sample_heights, theoretical_mean)

print(f"T-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
if p_value < 0.05:
    print("=> Reject Null Hypothesis: The mean is significantly different from 170.\n")
else:
    print("=> Fail to Reject Null Hypothesis: No significant difference.\n")


# ==========================================
# 2. Independent Two-Sample T-test
# ==========================================
print("--- 2. Independent Two-Sample T-test ---")

# Hypothesis: Are the means of Class A and Class B different?
class_a_heights = np.random.normal(loc=168, scale=5, size=30)
class_b_heights = np.random.normal(loc=175, scale=6, size=35)

# By default, ttest_ind assumes equal population variances.
# Because standard deviations are 5 and 6 (slightly different), we use Welch's t-test by setting equal_var=False
t_stat, p_value = stats.ttest_ind(class_a_heights, class_b_heights, equal_var=False)

print(f"T-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
if p_value < 0.05:
    print("=> Reject Null Hypothesis: There is a significant difference between Class A and Class B.\n")
else:
    print("=> Fail to Reject Null Hypothesis: No significant difference.\n")


# ==========================================
# 3. Paired Sample T-test
# ==========================================
print("--- 3. Paired Sample T-test ---")

# Hypothesis: Is there a significant difference in weight before and after the diet?
weight_before = np.random.normal(loc=85, scale=10, size=20)

# Assume the diet causes an average weight loss of 3kg per person
weight_after = weight_before - np.random.normal(loc=3, scale=2, size=20) 

t_stat, p_value = stats.ttest_rel(weight_before, weight_after)

print(f"T-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
if p_value < 0.05:
    print("=> Reject Null Hypothesis: The weight before and after the diet are significantly different.\n")
else:
    print("=> Fail to Reject Null Hypothesis: No significant difference.\n")
```

## V. Summary

- Always check your **p-value threshold** (commonly $\alpha = 0.05$).
- Always verify data **assumptions** (Normality, Homogeneity) are met before running the test.
- Use **One-sample** when you have 1 group and a known theoretical value.
- Use **Two-sample (Independent)** when you have 2 different groups.
- Use **Paired** when you measure the same group twice (e.g., before/after).
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Statistics</p><h1>T-test</h1><p>Nhóm kiểm định dùng chênh lệch mean, mức biến thiên và sample size để đánh giá một khác biệt có tương thích với giả thuyết không hay không.</p></header>
  <h2>Chọn loại nào?</h2><div class="table-wrap"><table><thead><tr><th>Thiết kế</th><th>Kiểm định</th><th>Ví dụ</th></tr></thead><tbody><tr><td>Một mẫu so với mốc</td><td>One-sample t-test</td><td>Mean transaction amount có khác 1 triệu?</td></tr><tr><td>Hai nhóm độc lập</td><td>Welch’s t-test</td><td>Mean của segment A và B</td></tr><tr><td>Cùng đối tượng trước/sau</td><td>Paired t-test</td><td>Chi tiêu trước và sau campaign</td></tr></tbody></table></div>
  <p>Với hai nhóm độc lập, Welch’s t-test thường là lựa chọn an toàn hơn vì không giả định equal variance.</p>
  <h2>Assumptions</h2><ul><li>Quan sát độc lập theo đúng thiết kế.</li><li>Outcome là dữ liệu số và mean có ý nghĩa.</li><li>Dữ liệu hoặc paired differences không có outlier quá mạnh.</li><li>Normality quan trọng hơn khi mẫu nhỏ; với mẫu lớn, cần chú ý practical significance vì p-value rất nhạy.</li></ul>
  <h2>Python</h2><pre><code>from scipy import stats

one_sample = stats.ttest_1samp(sample, popmean=100)
independent = stats.ttest_ind(group_a, group_b, equal_var=False)
paired = stats.ttest_rel(before, after)</code></pre>
  <h2>Đừng chỉ báo p-value</h2><p>Nên báo mean của mỗi nhóm, mean difference, confidence interval, effect size, sample size và assumptions. P-value nhỏ không nói khác biệt có lớn hoặc hữu ích trong kinh doanh hay không.</p>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2>
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
  <header class="page-intro"><p class="eyebrow">Learning note · Statistics</p><h1>T-tests</h1><p>A family of tests that uses a mean difference, variability, and sample size to evaluate compatibility with a null hypothesis.</p></header>
  <h2>Which test?</h2><div class="table-wrap"><table><thead><tr><th>Design</th><th>Test</th><th>Example</th></tr></thead><tbody><tr><td>One sample versus a reference</td><td>One-sample t-test</td><td>Does mean transaction amount differ from one million?</td></tr><tr><td>Two independent groups</td><td>Welch’s t-test</td><td>Mean difference between segments A and B</td></tr><tr><td>Same units before/after</td><td>Paired t-test</td><td>Spending before and after a campaign</td></tr></tbody></table></div>
  <p>For two independent groups, Welch’s t-test is often the safer default because it does not assume equal variances.</p>
  <h2>Assumptions</h2><ul><li>Observations follow the independence or pairing in the design.</li><li>The outcome is numerical and a mean is meaningful.</li><li>The data or paired differences are not dominated by extreme outliers.</li><li>Normality matters more with small samples; with large samples, focus on practical significance because p-values become sensitive.</li></ul>
  <h2>Python</h2><pre><code>from scipy import stats

one_sample = stats.ttest_1samp(sample, popmean=100)
independent = stats.ttest_ind(group_a, group_b, equal_var=False)
paired = stats.ttest_rel(before, after)</code></pre>
  <h2>Report more than a p-value</h2><p>Include group means, the mean difference, a confidence interval, effect size, sample sizes, and assumptions. A small p-value does not say whether the effect is large or useful.</p>
  <h2>Corrections and extensions to the original notes</h2>
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
