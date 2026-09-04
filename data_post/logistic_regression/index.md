---
title: "Logistic Regression: From Linear Scores to Probabilities"
title_vi: "Logistic Regression: từ linear score đến xác suất"
title_en: "Logistic Regression: From Linear Scores to Probabilities"
description: Why a sigmoid replaces the unbounded output of linear regression, and how cross-entropy and gradient descent fit the model.
description_vi: Vì sao sigmoid thay thế đầu ra không giới hạn của linear regression, và cách cross-entropy cùng gradient descent fit mô hình.
description_en: Why a sigmoid replaces the unbounded output of linear regression, and how cross-entropy and gradient descent fit the model.
date: 2026-04-08
writing_topic: foundations
---

{% capture article_en %}
🔙 [Back to Home](/)

# Logistic Regression: From Linear Scores to Probabilities

Binary classification needs a probability between 0 and 1. Linear regression cannot guarantee that range: its output is unbounded, and a fitted line can be pulled by extreme observations in ways that move the classification boundary.

## A linear model alone does not produce probabilities

![image.png](images/1.png)

This is why logistic regression keeps a linear score but passes it through a sigmoid before making a binary prediction.

![image.png](images/2.png)

## The sigmoid maps any linear score into (0, 1)

First calculate the linear score:

`z = w · x + b`

Then transform it with the sigmoid:

`p = g(z) = 1 / (1 + e⁻ᶻ)`

The input `z` can take any real value, while the output satisfies `0 < p < 1`.

![image.png](images/3.png)

## Logistic regression is linear in the log-odds

Rearranging the sigmoid gives:

`w · x + b = log(p / (1 - p))`

The ratio `p / (1 - p)` is the **odds**, and its logarithm is the **logit** or **log-odds**. Logistic regression therefore models a linear relationship between the input features and log-odds, not between the features and probability itself.

Cross-entropy measures the error between the predicted probability and the binary target. Its gradients provide the updates for `w` and `b`.

## Fit one-feature logistic regression from scratch

```python
import math
import numpy as np

def predict(x, alpha, beta):
    # Clip z to prevent overflow when calculating exp, keeping output continuous
    z = alpha * x + beta
    z = max(min(z, 10), -10)  # clip between -10 and 10 for stability
    return 1.0 / (1.0 + math.exp(-z))

def logistic_regression_scratch(x, y, alpha_init=0, beta_init=0, learning_rate=0.01, epochs=101):
    alpha = alpha_init
    beta = beta_init

    n = len(y)

    for run in range(epochs):
        loss = 0
        update_alpha = 0
        update_beta = 0

        for i in range(n):
            z = alpha * x[i] + beta
            z = max(min(z, 10), -10) # clip to avoid overflow
            y_pred = 1 / (1 + np.exp(-z))  # sigmoid

            # cross-entropy loss
            loss += (-1/n) * (y[i] * np.log(y_pred + 1e-9) + (1 - y[i]) * np.log(1 - y_pred + 1e-9))

            # gradients
            update_alpha += (y_pred - y[i]) * x[i]
            update_beta += (y_pred - y[i])

        # Update weights
        alpha -= learning_rate * (update_alpha / n)
        beta  -= learning_rate * (update_beta / n)

        if run % 100 == 0:
            print(f"Epoch {run}: Loss = {loss:.4f}, alpha = {alpha:.4f}, beta = {beta:.4f}")

    return alpha, beta

def predict_scratch(x, alpha, beta, threshold=0.5):
    # Calculate probability and apply threshold for final class prediction
    prob = [1 / (1 + math.exp(-(ele * alpha + beta))) for ele in x]
    return [int(ele >= threshold) for ele in prob]

# Example usage (assuming x, y are defined)
# y_pred_all = [predict(xi, alpha, beta) for xi in x]
# print(y_pred_all)
```

The final `predict_scratch` function keeps probability and class prediction separate: the sigmoid produces a probability, while the threshold converts that probability into a class. Changing the threshold changes the predicted classes without refitting the logistic-regression coefficients.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Logistic Regression: từ linear score đến xác suất

Binary classification cần một xác suất nằm trong khoảng 0 đến 1. Linear regression không đảm bảo được khoảng này: output của nó không bị chặn, và các quan sát cực trị có thể kéo fitted line làm thay đổi classification boundary.

## Chỉ linear model thì chưa tạo ra xác suất

![Linear regression cho classification](images/1.png)

Vì vậy, logistic regression vẫn sử dụng linear score nhưng đưa score qua sigmoid trước khi tạo binary prediction.

![Logistic regression](images/2.png)

## Sigmoid đưa mọi linear score về khoảng (0, 1)

Đầu tiên tính linear score:

`z = w · x + b`

Sau đó biến đổi qua sigmoid:

`p = g(z) = 1 / (1 + e⁻ᶻ)`

Input `z` có thể nhận mọi giá trị thực, trong khi output thỏa mãn `0 < p < 1`.

![Sigmoid function](images/3.png)

## Logistic regression tuyến tính theo log-odds

Biến đổi lại công thức sigmoid:

`w · x + b = log(p / (1 - p))`

Tỉ lệ `p / (1 - p)` là **odds**, logarithm của nó là **logit** hoặc **log-odds**. Vì vậy, logistic regression mô hình hóa quan hệ tuyến tính giữa input feature và log-odds, không phải giữa feature và probability.

Cross-entropy đo sai số giữa predicted probability và binary target. Gradient của loss cung cấp lượng cập nhật cho `w` và `b`.

## Fit logistic regression một feature từ đầu

```python
import math
import numpy as np

def predict(x, alpha, beta):
    # Clip z to prevent overflow when calculating exp, keeping output continuous
    z = alpha * x + beta
    z = max(min(z, 10), -10)  # clip between -10 and 10 for stability
    return 1.0 / (1.0 + math.exp(-z))

def logistic_regression_scratch(x, y, alpha_init=0, beta_init=0, learning_rate=0.01, epochs=101):
    alpha = alpha_init
    beta = beta_init

    n = len(y)

    for run in range(epochs):
        loss = 0
        update_alpha = 0
        update_beta = 0

        for i in range(n):
            z = alpha * x[i] + beta
            z = max(min(z, 10), -10) # clip to avoid overflow
            y_pred = 1 / (1 + np.exp(-z))  # sigmoid

            # cross-entropy loss
            loss += (-1/n) * (y[i] * np.log(y_pred + 1e-9) + (1 - y[i]) * np.log(1 - y_pred + 1e-9))

            # gradients
            update_alpha += (y_pred - y[i]) * x[i]
            update_beta += (y_pred - y[i])

        # Update weights
        alpha -= learning_rate * (update_alpha / n)
        beta  -= learning_rate * (update_beta / n)

        if run % 100 == 0:
            print(f"Epoch {run}: Loss = {loss:.4f}, alpha = {alpha:.4f}, beta = {beta:.4f}")

    return alpha, beta

def predict_scratch(x, alpha, beta, threshold=0.5):
    # Calculate probability and apply threshold for final class prediction
    prob = [1 / (1 + math.exp(-(ele * alpha + beta))) for ele in x]
    return [int(ele >= threshold) for ele in prob]

# Example usage (assuming x, y are defined)
# y_pred_all = [predict(xi, alpha, beta) for xi in x]
# print(y_pred_all)
```

Hàm `predict_scratch` cuối cùng tách probability khỏi class prediction: sigmoid tạo xác suất, còn threshold chuyển xác suất thành class. Thay đổi threshold làm thay đổi predicted class mà không cần fit lại coefficient của logistic regression.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
