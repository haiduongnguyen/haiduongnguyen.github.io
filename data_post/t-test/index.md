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

A t-test evaluates a difference in means relative to the uncertainty in that difference. The first decision is not the significance level or the Python function; it is whether the data represent one sample, two independent groups, or paired observations. That relationship comes from data collection, not from how two columns happen to appear in a table.

## Read the t-statistic and p-value separately

- **Null hypothesis (`H₀`):** the population mean or mean difference equals the value being tested, commonly zero.
- **Alternative hypothesis (`H₁`):** the population mean or mean difference is different from that value.
- **t-statistic:** the observed difference measured in standard-error units. A larger absolute value is less compatible with the null hypothesis.
- **p-value:** assuming the null hypothesis and model assumptions are true, the probability of obtaining a result at least as extreme as the observed one.

If `p < α`, where `α` is chosen before looking at the result, reject `H₀`. This decision does not tell us whether the difference is large enough to matter in practice.

A complete result should therefore report the estimated mean difference and a confidence interval alongside the p-value. The interval shows both direction and plausible magnitude; the p-value alone answers neither.

## Check the assumptions for the test you selected

The assumptions apply to the observations or differences being modeled:

1. **Numeric outcome:** the measured variable should be quantitative.
2. **Independent observations:** required between subjects; paired measurements are handled as within-subject differences.
3. **Approximate normality:** the sample values for a one-sample test, each group for a small independent test, or the pairwise differences for a paired test should be approximately normal. A Q–Q plot can reveal severe skewness and outliers. A Shapiro–Wilk result should not be used as an automatic switch because large samples can detect departures too small to matter.
4. **Equal variances:** required by the pooled independent t-test, but not by Welch's t-test. When equal variance is not defensible, use Welch's version.

## The three tests answer different questions

There are three main types of T-tests depending on the structure of your data and what you want to compare:

### One-sample t-test: compare one sample with a reference mean

- **Formula:** `t = (x̄ - μ) / (s / √n)`
  (`x̄` = sample mean, `μ` = reference mean, `s` = sample standard deviation, `n` = sample size)

- **Example:** Test whether the mean transaction-processing time from a sample differs from a `2`-second reference value.

### Independent t-test: compare two unrelated groups

- **Formula under equal variances:** `t = (x̄₁ - x̄₂) / (sₚ × √(1/n₁ + 1/n₂))`
  (`sₚ` is the pooled standard deviation.)

- **Example:** Compare mean card spending between customers randomly assigned to a campaign and an independent control group. If assignment was not random, the test describes a difference but does not by itself establish that the campaign caused it.

### Paired t-test: test the within-pair differences

- **Formula:** `t = d̄ / (s_d / √n)`
  (`d̄` = mean paired difference, `s_d` = standard deviation of the differences.)

- **Example:** Compare the monthly balance of the same customers before and after a product change. The test operates on each customer's within-pair difference, not on two unrelated columns of balances.

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

## Statistical significance is not business significance

With a large sample, a small and operationally irrelevant difference can produce a small p-value. With a small sample, a meaningful difference may remain uncertain. Report the sample sizes, mean difference, confidence interval, and an effect size such as Cohen's `d` when its assumptions are appropriate.

If many segments, products, or time windows are tested, the chance of at least one false positive increases. Those comparisons should be planned in advance or handled with a multiple-testing procedure rather than selecting only the smallest p-value afterward.

The useful sequence is: define the comparison, identify whether observations are independent or paired, choose the test, inspect the effect and uncertainty, and only then interpret the p-value.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Chọn T-test từ cấu trúc dữ liệu

T-test đánh giá chênh lệch trung bình so với mức uncertainty của chênh lệch đó. Quyết định đầu tiên không phải significance level hay hàm Python; cần xác định dữ liệu là một sample, hai group độc lập hay các observation theo cặp. Quan hệ này đến từ cách thu thập dữ liệu, không phải cách hai column tình cờ xuất hiện trong bảng.

## Đọc t-statistic và p-value riêng biệt

- **Null hypothesis (`H₀`):** population mean hoặc mean difference bằng giá trị đang được kiểm định, thường là 0.
- **Alternative hypothesis (`H₁`):** population mean hoặc mean difference khác giá trị đó.
- **t-statistic:** chênh lệch quan sát được tính theo đơn vị standard error. Absolute value lớn hơn ít tương thích với null hypothesis hơn.
- **p-value:** nếu null hypothesis và các assumption của model đúng, đây là xác suất thu được kết quả ít nhất cực đoan như kết quả đã quan sát.

Nếu `p < α`, với `α` được chọn trước khi xem kết quả, bác bỏ `H₀`. Quyết định này không cho biết chênh lệch có đủ lớn để mang ý nghĩa thực tế hay không.

Vì vậy, một kết quả đầy đủ cần báo cáo estimated mean difference và confidence interval cùng với p-value. Interval cho biết cả hướng và độ lớn hợp lý; p-value một mình không trả lời được hai điều đó.

## Kiểm tra assumption cho test đã chọn

Assumption áp dụng cho observation hoặc difference đang được model:

1. **Numeric outcome:** biến được đo phải là quantitative.
2. **Observation độc lập:** cần thiết giữa các subject; paired measurement được xử lý dưới dạng within-subject difference.
3. **Gần phân phối chuẩn:** sample value của one-sample test, từng group trong independent test có sample nhỏ, hoặc pairwise difference trong paired test nên gần phân phối chuẩn. Q–Q plot có thể phát hiện skewness mạnh và outlier. Không nên dùng Shapiro–Wilk như công tắc tự động vì sample lớn có thể phát hiện sai lệch quá nhỏ để tạo ý nghĩa thực tế.
4. **Equal variance:** pooled independent t-test cần assumption này, nhưng Welch's t-test thì không. Khi không thể bảo vệ giả định equal variance, dùng Welch's version.

## Ba test trả lời ba câu hỏi khác nhau

### One-sample t-test: so sánh một sample với reference mean

- **Công thức:** `t = (x̄ - μ) / (s / √n)`
  (`x̄` = sample mean, `μ` = reference mean, `s` = sample standard deviation, `n` = sample size)

- **Ví dụ:** kiểm tra mean transaction-processing time của một sample có khác reference value `2` giây hay không.

### Independent t-test: so sánh hai group không liên quan

- **Công thức khi equal variance:** `t = (x̄₁ - x̄₂) / (sₚ × √(1/n₁ + 1/n₂))`
  (`sₚ` là pooled standard deviation.)

- **Ví dụ:** so sánh mean card spending giữa khách hàng được random vào campaign và một control group độc lập. Nếu assignment không ngẫu nhiên, test mô tả chênh lệch nhưng không tự chứng minh campaign đã gây ra chênh lệch đó.

### Paired t-test: kiểm định within-pair difference

- **Công thức:** `t = d̄ / (s_d / √n)`
  (`d̄` = mean paired difference, `s_d` = standard deviation của các difference.)

- **Ví dụ:** so sánh monthly balance của cùng khách hàng trước và sau một thay đổi sản phẩm. Test hoạt động trên within-pair difference của từng khách hàng, không phải hai column balance không liên quan.

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

## Statistical significance không phải business significance

Với sample lớn, một chênh lệch nhỏ và không quan trọng về vận hành vẫn có thể tạo p-value nhỏ. Với sample nhỏ, một chênh lệch có ý nghĩa vẫn có thể chứa nhiều uncertainty. Cần báo cáo sample size, mean difference, confidence interval và effect size như Cohen's `d` khi assumption của nó phù hợp.

Nếu kiểm định nhiều segment, product hoặc time window, xác suất xuất hiện ít nhất một false positive sẽ tăng. Các phép so sánh đó cần được lên kế hoạch trước hoặc xử lý bằng multiple-testing procedure, thay vì chỉ chọn p-value nhỏ nhất sau khi xem kết quả.

Trình tự hữu ích là: xác định phép so sánh, nhận diện observation độc lập hay theo cặp, chọn test, kiểm tra effect và uncertainty, rồi mới diễn giải p-value.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
