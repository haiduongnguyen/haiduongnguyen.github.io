---
title: T-Test
---

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