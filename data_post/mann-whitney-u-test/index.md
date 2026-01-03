---
title: Mann-whitney U Test
---

🔙 [Back to Home](/)

## Mann-whitney U Test

## Definition

The t-test ([T-test](/data_post/t-test/)) is commonly used to test whether the means of two groups are equal. It assumes that the data are approximately normally distributed (or that the sample size is large enough for the Central Limit Theorem to apply).

The Mann–Whitney U test does not require the normality assumption. It is a non-parametric test that works by ranking the data values rather than using the raw data. Instead of testing for equality of means, it tests whether the distributions of the two groups differ in location (often interpreted as a difference in medians).  

So the output of Mann-white U test is test: The two distributions have the same shape and spread

1. Use case

### **Hypotheses in the Mann-Whitney U Test**

- [**Null Hypothesis (H₀):**](https://www.geeksforgeeks.org/null-hypothesis/) The two populations are equal; there is no significant difference between them.
- [**Alternative Hypothesis (H₁):**](https://www.geeksforgeeks.org/alternative-hypothesis-definition-types-and-examples/) The two populations are not equal; at least one group has significantly different values.

1. Fomula
- The U statistic is calculated for both groups:
    - `U1 = n1 * n2 + (n1 * (n1 + 1)) / 2 - R1`.
    - `U2 = n1 * n2 + (n2 * (n2 + 1)) / 2 - R2`.
- The smaller of `U1` and `U2` is the test statistic, often denoted as `U`.
- If **U ≤ U₀** ([**critical value**](https://www.geeksforgeeks.org/critical-value/)), reject the null hypothesis.
- Otherwise, do not reject the null hypothesis.