---
title: Linear Regression
title_vi: Linear Regression — từ baseline đến chẩn đoán
title_en: Linear regression — from baseline to diagnostics
description: A practical bilingual guide to OLS, assumptions, validation, and diagnostics for linear regression.
description_vi: Hướng dẫn thực tế về OLS, assumptions, validation và diagnostics cho linear regression.
description_en: A practical guide to OLS, assumptions, validation, and diagnostics for linear regression.
date: 2026-04-08
writing_topic: foundations
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

🔙 [Back to Home](/)

## Linear regression


## Definition

![image.png](images/1.png)

- Linear regression 1 variable

    y = w*x + b

- Linear regression for multiple variable

    y = w1*x1 + w2*x2 + … + wn*xn + b

- Linear regression with polynomial variable (treat polynomial as new variable by feature engineering)

    y = w1*x1 + w2*x1^2 + … + b

## Application

Use linear regression in :

- Predict continuous output: house price, stock, credit score,…
- Understand relationship: for example when increasing interest rate -> total saving of book increases?

## Solving

When we have data of y and x, and need to understand relationship between them (y dependent on x), and use that for predicting future data.  So we have 2 ways to solve linear regression:

- Gradient descent
- Matrix

**Detail solution:**

**- Gradient descent**

**Step 1: Init w & b**

```python
# khoi tao w

w_init = -0.01
w_init

# khoi tao b

b_init = 46
b_init

learning_rate = 0.0000001
loss_history = []
w_history = []
b_history = []
```

**Step 2: write mse calculation**

```
def calculate_mse(y_pred, y):
    mse = 0
    for i in range(len(y)):
        mse += ((y_pred[i] - y[i])**2)/len(y)
    
    return mse
```

**Step 3: write gradient descent calculation**

```python
def grad_y_by_w(w, b, x, y):
    tot_grad = 0
    for ele in range(len(x)):
        tot_grad += (1/len(x))*(w*x[ele] + b - y[ele])*x[ele]
    return tot_grad
        
def grad_y_by_b(w, b, x, y):
    tot_grad = 0
    for ele in range(len(x)):
        tot_grad += (1/len(x))*(w*x[ele] + b - y[ele])
    return tot_grad

```

**Step 4: Loop calculate w and b by gradient descent**

```python
for epoch in range(30):
    print("================================")
    print(f"Run for epoch {epoch}")
    
    if epoch == 0:
        w = w_init
        b = b_init
        y_pred = w*x + b 
        
    if epoch >= 1:
        grad_l_by_w = grad_y_by_w(w, b, x, y)
        grad_l_by_b = grad_y_by_b(w, b, x, y)
        print(grad_l_by_w)
        print(grad_l_by_b)
        
        w = w - learning_rate*grad_l_by_w
        b = b - learning_rate*grad_l_by_b
        
        print("w: ", w)
        print("b: ", b)
        
        y_pred = w*x + b 
    
    
    loss = calculate_mse(y_pred, y)
    # print(loss)
    loss_history.append(loss)
    print("Loss: ", loss)
    w_history.append(w)
    b_history.append(b)
    
```

**Step 5: Compare to SGD function from sklearn**

```python
import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor

# data
X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([1.2, 1.9, 3.2, 3.9, 5.1])

# exact OLS
lr = LinearRegression().fit(X, y)
print("LinearRegression coef:", lr.coef_, "intercept:", lr.intercept_)

# gradient descent version
sgd = SGDRegressor(max_iter=10000, eta0=0.01, learning_rate='constant').fit(X, y)
print("SGDRegressor coef:", sgd.coef_, "intercept:", sgd.intercept_)

```

**- Matrix**

![image.png](images/2.png)

![image.png](images/3.png)

Code:

```python
x_temp = np.concatenate([np.ones((n, 1)), np.reshape(x, (n,1))], axis=1)

x_temp

w_temp = np.linalg.inv((x_temp.T) @ x_temp) @ (x_temp.T) @ y

w_temp

b = w_temp[0]
w = w_temp[1]
```

```python
ymean = y.mean()

xmean = x.mean()

ymean

yoffset = y - ymean 
xoffset = x - xmean 

yoffset

w = np.linalg.inv(((x_temp.T) @ x_temp))  @ (x_temp.T) @ y_temp

w

b = ymean - xmean*w 
b
```

Benchmark of Gradient descent vs Matrix

```python
import time
import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor

def benchmark(n_samples, n_features):
    X = np.random.randn(n_samples, n_features)
    y = np.random.randn(n_samples)
    
    # LinearRegression
    start = time.time()
    try:
        LinearRegression().fit(X, y)
        lr_time = time.time() - start
    except Exception as e:
        lr_time = str(e)
    
    # SGDRegressor
    start = time.time()
    SGDRegressor(max_iter=1000).fit(X, y)
    sgd_time = time.time() - start
    
    return lr_time, sgd_time

sizes = [(1000, 1000), (2000, 2000), (5000, 5000), (10000, 1000), (1000, 10000)]
for n, d in sizes:
    print(f"n={n}, d={d}:", benchmark(n, d))

```

## Linear regression assumptions

(vì phần này khó nên viết tiếng việt cho dễ hiểu)

**Bảng tổng hợp các giả thuyết**

| Giả thuyết | Cách kiểm định | Công cụ |
| --- | --- | --- |
| Tuyến tính | Vẽ biểu đồ residuals vs fitted values | sns.residplot() |
| Độc lập ( durbin-watson áp dụng với time series) | Kiểm định Durbin-Watson | durbin_watson() |
| Phương sai không đổi | Vẽ residuals vs fitted, kiểm định Breusch-Pagan | statsmodels |
| Phân phối chuẩn | Kiểm định Shapiro-Wilk hoặc vẽ histogram + Q-Q plot | shapiro(), qqplot() |
| Không đa cộng tuyến | Tính VIF (Variance Inflation Factor) | variance_inflation_factor() |


**Phần dư residual (resid) cần tuân theo phân phối chuẩn, có phương sai không đổi**

Để kiểm chứng thường sẽ chạy Shapiro-wilk để tính ra p-value 

Shapiro-wilk: H0: resid tuân theo phân phối chuẩn

p-value < 0.05 → Bác bỏ H0

Tuy nhiên nếu mẫu lớn → Shapiro thường cho ra p-value < 0.05 nên sẽ cần thêm vẽ biểu đồ trực quan ra

**Biểu đồ Q-Q**

```python
import statsmodels.api as sm
import matplotlib.pyplot as plt

sm.qqplot(np.array(resid), line='45', fit=True)
plt.show()

```

Biểu đồ histogram

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(resid, kde=True)
plt.show()

```

**Kiểm định đa cộng tuyến:**

Sử dụng hàm variance_inflation_factor: https://en.wikipedia.org/wiki/Variance_inflation_factor

Bản chất là predict 1 feature Xi dựa vào các X còn lại, đo r square của mô hình 

Nếu VIF > 5 (tính ra thì là R2 > 0.8) thì biến i cần xem xét là bị đa cộng tuyến 

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# Giả sử X là DataFrame chứa các biến độc lập
X = add_constant(x)   # thêm cột hằng số (intercept)

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
```

![image.png](images/4.png)


1. Xử lí khi bị các vấn đề 

Khi đã bị đa cộng tuyến, thì có những cách xử lí sau:

- Loại bớt biến giải thích (predictors) bị trùng lặp thông tin.
- Kết hợp các biến có tương quan cao (ví dụ tạo chỉ số tổng hợp).
- Sử dụng **Regularization methods** (Ridge, Lasso).

Cách 1: Bỏ bớt biến đi 

Cách 2: Kết hợp các biến = phương pháp PCA 

## 1️⃣ Eigenvalue là gì?

Cho 1 ma trận vuông AAA, ta giải phương trình:

Av = λv

A: n x n 

v: n x 1 

λ: 1 số thực (float) 

Av=λv

- vvv = **eigenvector** (vector riêng).
- λ\lambdaλ = **eigenvalue** (trị riêng).

Ý nghĩa: khi nhân ma trận A với vector v, ta chỉ thay đổi độ dài (scale) vector đó lên λ\lambdaλ lần, **mà không đổi hướng**.

Ví dụ: tưởng tượng vvv là một mũi tên, sau phép biến đổi tuyến tính AAA, mũi tên vẫn chỉ cùng hướng, chỉ dài ra hoặc ngắn lại.

## 2️⃣ Eigenvalues trong PCA có ý nghĩa gì?

Trong PCA:

- A chính là **ma trận hiệp phương sai** C.
- Eigenvalue của mỗi eigenvector cho biết **lượng phương sai dữ liệu giữ lại** trên trục đó.

➡️ **Eigenvalue càng lớn → trục (eigenvector) đó chứa nhiều thông tin hơn.**

## 3️⃣ Sử dụng eigenvalues để làm gì trong PCA?

- **Xếp hạng các trục PCA:** ta sắp xếp eigenvalues từ lớn đến nhỏ để biết trục nào quan trọng nhất.
- **Chọn số chiều kkk:** thường chọn kkk sao cho tổng eigenvalues chiếm đủ % phương sai (VD: 95%).

Công thức tính **variance explained ratio**:

Explained Variance Ratioi

![image.png](images/5.png)

Khi đó t chọn top k trong m PCA 

→ Giữ lại được % lớn thông tin trong ma trận 

Tìm λ và v kiểu gì: → Khi A là n x n thì sẽ có n cặp (λ, v) 

![image.png](images/6.png)

Sau đó lập ma trận gồm các [v] đây là ma trận mới vẫn giữ đủ thông tin của A 

Chọn top các hàng mà vẫn giữ được nhiều thông tin nhất 

→ Giảm được số chiều dữ liệu từ m → k 

Cách 3: Sử dụng Regularization Lasso và Ridge

![image.png](images/7.png)

![image.png](images/8.png)

Cách giải:

![image.png](images/9.png)

![image.png](images/10.png)

Cách giải: 

![image.png](images/11.png)
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Regression</p><h1>Linear Regression</h1><p>Một baseline đơn giản nhưng mạnh: mô hình hóa kỳ vọng của target như tổ hợp tuyến tính của các feature.</p></header>
  <h2>Mô hình</h2><pre><code>ŷ = β₀ + β₁x₁ + ... + βₚxₚ</code></pre><p>Ordinary Least Squares chọn hệ số làm nhỏ nhất tổng bình phương residual. Hệ số <code>βⱼ</code> mô tả thay đổi kỳ vọng của target khi <code>xⱼ</code> tăng một đơn vị, trong điều kiện các feature khác giữ nguyên.</p>
  <h2>Hai cách tìm hệ số</h2><ul><li><strong>Closed form / numerical linear algebra:</strong> phù hợp với dữ liệu vừa phải; implementation thực tế thường dùng SVD hoặc least-squares solver thay vì tự nghịch đảo ma trận.</li><li><strong>Gradient descent:</strong> hữu ích khi dữ liệu lớn hoặc là một phần của pipeline tối ưu rộng hơn.</li></ul>
  <h2>Assumptions cần kiểm tra</h2><ul><li><strong>Linearity:</strong> quan hệ kỳ vọng giữa feature và target được mô hình hóa hợp lý.</li><li><strong>Independent errors:</strong> đặc biệt quan trọng với dữ liệu theo thời gian hoặc theo nhóm.</li><li><strong>Homoscedasticity:</strong> phương sai residual tương đối ổn định nếu cần standard error cổ điển.</li><li><strong>Low multicollinearity:</strong> feature gần tuyến tính với nhau làm hệ số thiếu ổn định.</li><li><strong>Normal errors:</strong> chủ yếu cần cho inference mẫu nhỏ, không phải điều kiện để OLS tìm được hệ số.</li></ul>
  <h2>Workflow thực tế</h2><ol class="process"><li>Tách train/test đúng theo cấu trúc thời gian hoặc entity.</li><li>So sánh với baseline như mean hoặc last-period value.</li><li>Fit pipeline xử lý missing, encoding và scaling nếu cần.</li><li>Đánh giá MAE/RMSE cùng residual plot.</li><li>Kiểm tra drift, outlier ảnh hưởng mạnh và coefficient stability.</li><li>Chỉ diễn giải hệ số trong phạm vi assumptions và thiết kế dữ liệu.</li></ol>
  <h2>Python</h2><pre><code>from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

model = LinearRegression().fit(X_train, y_train)
prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)</code></pre>
  <div class="callout"><p><strong>Điểm tách khỏi PCA:</strong> PCA có thể giảm chiều hoặc xử lý collinearity, nhưng làm coefficient khó diễn giải hơn. Nó là một bước modeling riêng, không phải một phần mặc định của linear regression.</p></div>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2>
  <h3>Gradient của MSE phải khớp với định nghĩa loss</h3>
  <p>Phần gradient descent ban đầu đã nắm đúng ý tưởng tối ưu, nhưng đạo hàm đang thiếu hệ số hai nếu loss được định nghĩa là mean squared error thông thường. Hệ số này có thể được hấp thụ vào learning rate nên thuật toán vẫn có thể đi đúng hướng, nhưng viết nhất quán giúp việc debug và gradient checking rõ ràng hơn.</p>
  <pre><code class="language-python">import numpy as np

def mse_gradient(X, y, weights, intercept):
    error = X @ weights + intercept - y
    grad_weights = (2.0 / len(y)) * X.T @ error
    grad_intercept = 2.0 * error.mean()
    return grad_weights, grad_intercept</code></pre>
  <h3>Không nghịch đảo ma trận nếu bài toán không thực sự cần ma trận nghịch đảo</h3>
  <p>Normal equation hữu ích để hiểu OLS, nhưng <code>np.linalg.inv(X.T @ X)</code> thiếu ổn định khi các feature cộng tuyến và thực hiện nhiều phép tính hơn cần thiết. Nên dùng <code>np.linalg.lstsq</code>, solver dựa trên QR/SVD hoặc implementation đã được duy trì. Ridge regression là một lựa chọn modeling chứ không chỉ là mẹo số học, vì penalty của Ridge thay đổi chính objective được tối ưu.</p>
  <h3>Một baseline hoàn chỉnh và tôn trọng thứ tự thời gian</h3>
  <p>Ví dụ này nhỏ, tái lập được và không đọc dữ liệu tương lai. Model học trên 75% quan sát đầu, đánh giá trên 25% quan sát sau và được so sánh với baseline dùng trung bình tập train. Với dữ liệu theo khách hàng, cần dùng group-aware split để một khách hàng không xuất hiện ở cả train lẫn test.</p>
  <pre><code class="language-python">import numpy as np

rng = np.random.default_rng(42)
n_rows = 240
month = np.arange(n_rows)
income = rng.normal(30_000, 6_000, n_rows)
interest_rate = 5.0 + 0.4 * np.sin(month / 12)
X = np.column_stack([income, interest_rate, month])
y = 0.18 * income - 420 * interest_rate + 8 * month + rng.normal(0, 900, n_rows)

split = 180
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Mọi thống kê preprocessing chỉ được học từ giai đoạn train.
train_median = np.nanmedian(X_train, axis=0)
X_train = np.where(np.isnan(X_train), train_median, X_train)
X_test = np.where(np.isnan(X_test), train_median, X_test)
train_mean = X_train.mean(axis=0)
train_std = X_train.std(axis=0)
X_train = (X_train - train_mean) / train_std
X_test = (X_test - train_mean) / train_std

X_train_design = np.column_stack([np.ones(len(X_train)), X_train])
X_test_design = np.column_stack([np.ones(len(X_test)), X_test])
coefficients, *_ = np.linalg.lstsq(X_train_design, y_train, rcond=None)
prediction = X_test_design @ coefficients
baseline = np.full_like(y_test, y_train.mean())

mae = lambda actual, forecast: np.mean(np.abs(actual - forecast))
rmse = lambda actual, forecast: np.sqrt(np.mean((actual - forecast) ** 2))
print("model MAE:", mae(y_test, prediction))
print("baseline MAE:", mae(y_test, baseline))
print("model RMSE:", rmse(y_test, prediction))</code></pre>
  <h3>Prediction và inference là hai công việc khác nhau</h3>
  <p>Nếu mục tiêu là dự báo, hãy ưu tiên out-of-sample error, ngăn leakage, theo dõi drift và so với baseline hữu ích. Nếu mục tiêu là suy luận, sampling design, sai số có cấu trúc theo nhóm/thời gian, confidence interval và model specification trở nên quan trọng. Test RMSE thấp không biến một coefficient thành quan hệ nhân quả.</p>
  <h3>Dùng VIF như tín hiệu chẩn đoán, không phải phán quyết</h3>
  <p>Các ngưỡng VIF &gt; 5 hay VIF &gt; 10 chỉ là heuristic. VIF cao cảnh báo coefficient riêng lẻ có thể thiếu ổn định; nó không tự động có nghĩa model dự báo kém hoặc feature bắt buộc phải bị loại. Hãy kiểm tra độ ổn định của coefficient qua nhiều fold và xác định rõ mục tiêu là diễn giải hay dự báo.</p>
  <h3>Những gì nên được log trong một thử nghiệm ngân hàng</h3>
  <ul><li>Mốc train/test hoặc cách chia nhóm khách hàng chính xác.</li><li>Metric của naive baseline và model trên cùng tập quan sát.</li><li>Cách xử lý missing và danh sách feature thực sự có tại thời điểm ra quyết định.</li><li>Residual error theo phân khúc khách hàng và giai đoạn lịch.</li><li>Độ ổn định của coefficient thay vì chỉ lưu một bảng hệ số duy nhất.</li></ul>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares">Scikit-learn: Ordinary Least Squares</a></li><li><a href="https://www.statsmodels.org/stable/regression.html">Statsmodels: Regression and Linear Models</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Learning note · Regression</p><h1>Linear regression</h1><p>A simple but strong baseline that models the expected target as a linear combination of features.</p></header>
  <h2>The model</h2><pre><code>ŷ = β₀ + β₁x₁ + ... + βₚxₚ</code></pre><p>Ordinary Least Squares chooses coefficients that minimize the sum of squared residuals. A coefficient <code>βⱼ</code> represents the expected target change for a one-unit increase in <code>xⱼ</code>, holding the other features fixed.</p>
  <h2>Two ways to estimate coefficients</h2><ul><li><strong>Closed form / numerical linear algebra:</strong> suitable for moderate data; production implementations generally use SVD or least-squares solvers rather than explicitly inverting a matrix.</li><li><strong>Gradient descent:</strong> useful for large data or when regression sits inside a broader optimization pipeline.</li></ul>
  <h2>Assumptions to examine</h2><ul><li><strong>Linearity:</strong> the conditional mean is represented adequately.</li><li><strong>Independent errors:</strong> especially important for time- or group-structured data.</li><li><strong>Homoscedasticity:</strong> stable residual variance when using classical standard errors.</li><li><strong>Low multicollinearity:</strong> near-linear feature relationships make coefficients unstable.</li><li><strong>Normal errors:</strong> mainly relevant to small-sample inference, not to computing OLS coefficients.</li></ul>
  <h2>Practical workflow</h2><ol class="process"><li>Split data according to time or entity structure.</li><li>Compare against a mean or last-period baseline.</li><li>Fit a pipeline for missing values, encoding, and scaling where needed.</li><li>Evaluate MAE/RMSE and residual plots together.</li><li>Check drift, influential outliers, and coefficient stability.</li><li>Interpret coefficients only within the data design and assumptions.</li></ol>
  <h2>Python</h2><pre><code>from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

model = LinearRegression().fit(X_train, y_train)
prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)</code></pre>
  <div class="callout"><p><strong>Keep PCA separate:</strong> PCA can reduce dimensionality or address collinearity, but it makes coefficients harder to interpret. It is a separate modeling choice, not part of linear regression by default.</p></div>
  <h2>Corrections and extensions to the original notes</h2>
  <h3>The MSE gradient needs to match the loss definition</h3>
  <p>The original gradient-descent section captures the optimization idea correctly, but its derivative omits a factor of two if the loss is defined as plain mean squared error. That factor can be absorbed into the learning rate, so the algorithm can still move in the right direction, but writing the derivative consistently makes debugging and gradient checking much easier.</p>
  <pre><code class="language-python">import numpy as np

def mse_gradient(X, y, weights, intercept):
    error = X @ weights + intercept - y
    grad_weights = (2.0 / len(y)) * X.T @ error
    grad_intercept = 2.0 * error.mean()
    return grad_weights, grad_intercept</code></pre>
  <h3>Do not compute a matrix inverse unless you need the inverse itself</h3>
  <p>The normal equation is useful for understanding OLS, but <code>np.linalg.inv(X.T @ X)</code> is fragile when features are collinear and does more work than necessary. Use <code>np.linalg.lstsq</code>, a QR/SVD-based solver, or a maintained library implementation. Ridge regression is a modeling decision—not merely a numerical trick—because its penalty changes the fitted objective.</p>
  <h3>A complete baseline that respects time order</h3>
  <p>This example is deliberately small and reproducible. It trains on the first 75% of observations, evaluates on the later 25%, and compares the model with a train-mean baseline. For customer-level data, use a group-aware split instead so the same customer cannot appear in both train and test sets.</p>
  <pre><code class="language-python">import numpy as np

rng = np.random.default_rng(42)
n_rows = 240
month = np.arange(n_rows)
income = rng.normal(30_000, 6_000, n_rows)
interest_rate = 5.0 + 0.4 * np.sin(month / 12)
X = np.column_stack([income, interest_rate, month])
y = 0.18 * income - 420 * interest_rate + 8 * month + rng.normal(0, 900, n_rows)

split = 180
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Learn every preprocessing statistic from the training period only.
train_median = np.nanmedian(X_train, axis=0)
X_train = np.where(np.isnan(X_train), train_median, X_train)
X_test = np.where(np.isnan(X_test), train_median, X_test)
train_mean = X_train.mean(axis=0)
train_std = X_train.std(axis=0)
X_train = (X_train - train_mean) / train_std
X_test = (X_test - train_mean) / train_std

X_train_design = np.column_stack([np.ones(len(X_train)), X_train])
X_test_design = np.column_stack([np.ones(len(X_test)), X_test])
coefficients, *_ = np.linalg.lstsq(X_train_design, y_train, rcond=None)
prediction = X_test_design @ coefficients
baseline = np.full_like(y_test, y_train.mean())

mae = lambda actual, forecast: np.mean(np.abs(actual - forecast))
rmse = lambda actual, forecast: np.sqrt(np.mean((actual - forecast) ** 2))
print("model MAE:", mae(y_test, prediction))
print("baseline MAE:", mae(y_test, baseline))
print("model RMSE:", rmse(y_test, prediction))</code></pre>
  <h3>Prediction and inference are different jobs</h3>
  <p>If the goal is prediction, prioritize out-of-sample error, leakage prevention, drift, and a useful baseline. If the goal is inference, the sampling design, clustered or time-dependent errors, confidence intervals, and model specification matter. A low test RMSE does not turn a coefficient into a causal effect.</p>
  <h3>Use VIF as a diagnostic, not a verdict</h3>
  <p>Thresholds such as VIF &gt; 5 or VIF &gt; 10 are heuristics. A high VIF warns that individual coefficients may be unstable; it does not automatically mean the model predicts poorly or that a feature must be removed. Check coefficient stability across folds and decide whether interpretation or prediction is the actual goal.</p>
  <h3>What I would log in a real banking experiment</h3>
  <ul><li>The exact train/test cutoff or customer-group split.</li><li>The naive baseline and model metrics on the same rows.</li><li>Missing-value policy and features unavailable at decision time.</li><li>Residual error by customer segment and calendar period.</li><li>Coefficient stability, not only one fitted coefficient table.</li></ul>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares">Scikit-learn: Ordinary Least Squares</a></li><li><a href="https://www.statsmodels.org/stable/regression.html">Statsmodels: Regression and Linear Models</a></li></ul>
</article>
