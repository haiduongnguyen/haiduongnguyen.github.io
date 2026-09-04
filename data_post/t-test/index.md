---
title: "Choose the T-Test From the Data Structure"
title_vi: "Chọn T-test từ cấu trúc dữ liệu"
title_en: "Choose the T-Test From the Data Structure"
description: Decide between one-sample, independent, and paired t-tests before calculating a p-value.
description_vi: Chọn giữa one-sample, independent và paired t-test trước khi tính p-value.
description_en: Decide between one-sample, independent, and paired t-tests before calculating a p-value.
date: 2026-04-08
writing_topic: statistics
---

{% capture article_en %}
🔙 [Back to Home](/)

# Choose the T-Test From the Data Structure

A t-test evaluates a difference in means relative to the uncertainty in that difference. The first decision is not the significance level or the Python function; it is whether the data represent one sample, two independent groups, or paired observations.

## Read the t-statistic and p-value separately

- **Null hypothesis (`H₀`):** the population mean or mean difference equals the value being tested, commonly zero.
- **Alternative hypothesis (`H₁`):** the population mean or mean difference is different from that value.
- **t-statistic:** the observed difference measured in standard-error units. A larger absolute value is less compatible with the null hypothesis.
- **p-value:** assuming the null hypothesis and model assumptions are true, the probability of obtaining a result at least as extreme as the observed one.

If `p < α`, where `α` is chosen before looking at the result, reject `H₀`. This decision does not tell us whether the difference is large enough to matter in practice.

## Check the assumptions for the test you selected

The assumptions apply to the observations or differences being modeled:

1. **Numeric outcome:** the measured variable should be quantitative.
2. **Independent observations:** required between subjects; paired measurements are handled as within-subject differences.
3. **Approximate normality:** the sample values for a one-sample test, each group for a small independent test, or the pairwise differences for a paired test should be approximately normal. A Q–Q plot or Shapiro–Wilk test can help check this.
4. **Equal variances:** required by the pooled independent t-test, but not by Welch's t-test. When equal variance is not defensible, use Welch's version.

## The three tests answer different questions

There are three main types of T-tests depending on the structure of your data and what you want to compare:

### One-sample t-test: compare one sample with a reference mean

- **Formula:** `t = (x̄ - μ) / (s / √n)`
  (`x̄` = sample mean, `μ` = reference mean, `s` = sample standard deviation, `n` = sample size)

- **Example:** A teacher has a class of 30 students and wants to test whether their average height differs from `170 cm`.

### Independent t-test: compare two unrelated groups

- **Formula under equal variances:** `t = (x̄₁ - x̄₂) / (sₚ × √(1/n₁ + 1/n₂))`
  (`sₚ` is the pooled standard deviation.)

- **Example:** A teacher wants to test if there is a significant height difference between Class A and Class B.

### Paired t-test: test the within-pair differences

- **Formula:** `t = d̄ / (s_d / √n)`
  (`d̄` = mean paired difference, `s_d` = standard deviation of the differences.)

- **Example:** Measuring the weight of 20 patients *before* and *after* an 8-week diet plan.

---

## Run all three tests with SciPy

The examples use reproducible synthetic data and match each data structure to its corresponding SciPy function.

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

## Choose from the relationship between observations

- Use a **one-sample t-test** for one group against a reference value.
- Use an **independent t-test**, preferably Welch's when equal variance is uncertain, for two unrelated groups.
- Use a **paired t-test** when the same subjects are measured twice or observations are explicitly matched.

The pairing or independence comes from how the data were collected. It cannot be inferred from the two columns after the fact.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Chọn T-test từ cấu trúc dữ liệu

T-test đánh giá chênh lệch trung bình so với mức uncertainty của chênh lệch đó. Quyết định đầu tiên không phải significance level hay hàm Python; cần xác định dữ liệu là một sample, hai group độc lập hay các observation theo cặp.

## Đọc t-statistic và p-value riêng biệt

- **Null hypothesis (`H₀`):** population mean hoặc mean difference bằng giá trị đang được kiểm định, thường là 0.
- **Alternative hypothesis (`H₁`):** population mean hoặc mean difference khác giá trị đó.
- **t-statistic:** chênh lệch quan sát được tính theo đơn vị standard error. Absolute value lớn hơn ít tương thích với null hypothesis hơn.
- **p-value:** nếu null hypothesis và các assumption của model đúng, đây là xác suất thu được kết quả ít nhất cực đoan như kết quả đã quan sát.

Nếu `p < α`, với `α` được chọn trước khi xem kết quả, bác bỏ `H₀`. Quyết định này không cho biết chênh lệch có đủ lớn để mang ý nghĩa thực tế hay không.

## Kiểm tra assumption cho test đã chọn

Assumption áp dụng cho observation hoặc difference đang được model:

1. **Numeric outcome:** biến được đo phải là quantitative.
2. **Observation độc lập:** cần thiết giữa các subject; paired measurement được xử lý dưới dạng within-subject difference.
3. **Gần phân phối chuẩn:** sample value của one-sample test, từng group trong independent test có sample nhỏ, hoặc pairwise difference trong paired test nên gần phân phối chuẩn. Có thể kiểm tra bằng Q–Q plot hoặc Shapiro–Wilk test.
4. **Equal variance:** pooled independent t-test cần assumption này, nhưng Welch's t-test thì không. Khi không thể bảo vệ giả định equal variance, dùng Welch's version.

## Ba test trả lời ba câu hỏi khác nhau

### One-sample t-test: so sánh một sample với reference mean

- **Công thức:** `t = (x̄ - μ) / (s / √n)`
  (`x̄` = sample mean, `μ` = reference mean, `s` = sample standard deviation, `n` = sample size)

- **Ví dụ:** một giáo viên có lớp gồm 30 học sinh và muốn kiểm tra average height của lớp có khác `170 cm` hay không.

### Independent t-test: so sánh hai group không liên quan

- **Công thức khi equal variance:** `t = (x̄₁ - x̄₂) / (sₚ × √(1/n₁ + 1/n₂))`
  (`sₚ` là pooled standard deviation.)

- **Ví dụ:** giáo viên muốn kiểm tra chiều cao trung bình của Lớp A và Lớp B có khác nhau hay không.

### Paired t-test: kiểm định within-pair difference

- **Công thức:** `t = d̄ / (s_d / √n)`
  (`d̄` = mean paired difference, `s_d` = standard deviation của các difference.)

- **Ví dụ:** đo cân nặng của cùng 20 bệnh nhân trước và sau chương trình ăn kiêng kéo dài tám tuần.

## Chạy cả ba test bằng SciPy

Ví dụ sử dụng synthetic data có random seed và ghép từng data structure với hàm SciPy tương ứng.

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

## Chọn từ mối quan hệ giữa các observation

- Dùng **one-sample t-test** cho một group so với reference value.
- Dùng **independent t-test**, ưu tiên Welch's khi equal variance không chắc chắn, cho hai group không liên quan.
- Dùng **paired t-test** khi cùng subject được đo hai lần hoặc các observation được match rõ ràng.

Pairing hay independence đến từ cách dữ liệu được thu thập. Không thể suy ra điều đó từ hai column sau khi dữ liệu đã được tạo.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
