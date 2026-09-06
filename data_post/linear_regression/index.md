---
title: "Linear Regression: Two Solvers and the Checks After Fitting"
title_vi: "Linear Regression: hai cách giải và các kiểm tra sau khi fit"
title_en: "Linear Regression: Two Solvers and the Checks After Fitting"
description: Build linear regression with gradient descent and matrix operations, then inspect residuals and multicollinearity.
description_vi: Xây dựng linear regression bằng gradient descent và matrix operations, sau đó kiểm tra residual và multicollinearity.
description_en: Build linear regression with gradient descent and matrix operations, then inspect residuals and multicollinearity.
date: 2026-04-08
writing_topic: foundations
---

{% capture article_en %}
🔙 [Back to Home](/)

# Linear Regression: Two Solvers and the Checks After Fitting

Linear regression is easy to fit and easy to misuse. Its coefficients can describe how an expected outcome changes with the input variables, but only after the observation unit, feature timing, and model assumptions have been made explicit.

## One model, from one feature to polynomial features

![image.png](images/1.png)

- One input variable:

    y = w*x + b

- Multiple input variables:

    y = w1*x1 + w2*x2 + … + wn*xn + b

- Polynomial terms treated as engineered input features:

    y = w1*x1 + w2*x1^2 + … + b

## Use it for prediction or for understanding relationships

- Predict a continuous output such as house price, stock value, or credit score.
- Examine a relationship, such as whether a higher interest rate is associated with a higher total savings-book balance.

These goals are not interchangeable. A model can predict well while individual coefficients remain unstable, and a coefficient that describes an association does not prove that changing the feature will cause the outcome to change. In the savings example, customer characteristics may influence both the offered interest rate and the balance.

Before fitting, define one row and one cutoff date. If one row represents one customer at month-end, every predictor must be available by that month-end and the target must belong to the intended future or contemporaneous window. This prevents information from the target period from leaking into the features.

## Fit the same model in two ways

Given `x` and `y`, the coefficients can be estimated iteratively with gradient descent or directly with matrix operations. Implementing both makes the difference between optimization and a closed-form solution concrete.

- **Gradient descent:** iteratively reduces the loss and exposes the role of learning rate, feature scale, and convergence.
- **Matrix solution:** calculates the least-squares coefficients directly and exposes the role of matrix rank and collinearity.

Both approaches estimate the same linear model. They differ in computation, not in the relationship being assumed between the predictors and outcome.

## Gradient descent updates the slope and intercept iteratively

### Step 1: Initialize `w` and `b`

```python
# initialize w

w_init = -0.01
w_init

# initialize b

b_init = 46
b_init

learning_rate = 0.0000001
loss_history = []
w_history = []
b_history = []
```

### Step 2: Calculate mean squared error

```
def calculate_mse(y_pred, y):
    mse = 0
    for i in range(len(y)):
        mse += ((y_pred[i] - y[i])**2)/len(y)

    return mse
```

### Step 3: Calculate the gradients

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

### Step 4: Update `w` and `b` over multiple epochs

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

### Step 5: Compare with scikit-learn

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

## Matrix operations give a direct solution

![image.png](images/2.png)

![image.png](images/3.png)

The following notebook snippets calculate the intercept and slope from the design matrix and from centered variables.

```python
n = len(x)
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

w = (xoffset.T @ yoffset) / (xoffset.T @ xoffset)

w

b = ymean - xmean*w
b
```

The first form follows the normal equation directly. In production code, `np.linalg.lstsq` is preferable to explicitly calculating a matrix inverse, especially when predictors are close to linearly dependent.

The closed-form expression is useful for understanding the estimator, but explicitly forming an inverse adds numerical risk and unnecessary work. Gradient descent avoids that inverse, although it introduces a learning rate, stopping rule, and sensitivity to feature scale.

## Benchmark iterative and direct solvers

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

The larger cases in this benchmark allocate dense matrices and can require substantial memory; they should be run individually rather than treated as a lightweight example.

A fair comparison records more than elapsed time. It should use the same generated data, compare coefficient or prediction error, and report whether either solver failed because of memory, convergence, or an ill-conditioned design matrix. A faster answer is not useful if it is numerically different from the least-squares solution.

## Check the assumptions after fitting

The fitted coefficients and predictions are not the end of the analysis. The residuals help show whether the linear model is a reasonable description of the data.

The importance of each assumption depends on the goal. Normal residuals are mainly relevant to small-sample inference; they are not a requirement for calculating least-squares predictions. Linearity, leakage, changing variance, dependent observations, and influential points can damage the model even when a normality test looks acceptable.

| Assumption | How to check it | Tool |
| --- | --- | --- |
| Linearity | Plot residuals against fitted values | `sns.residplot()` |
| Independent errors | Check serial correlation; Durbin–Watson is useful for ordered or time-series data | `durbin_watson()` |
| Constant variance | Inspect residuals versus fitted values or run a Breusch–Pagan test | `statsmodels` |
| Approximately normal residuals | Use a Q–Q plot, histogram, or Shapiro–Wilk test | `shapiro()`, `qqplot()` |
| No severe multicollinearity | Calculate the Variance Inflation Factor | `variance_inflation_factor()` |

Residual plots diagnose patterns left by the fitted model; they do not prove that the data-generating assumptions are true. Independence in particular comes mainly from the sampling and time structure. A Durbin–Watson statistic cannot repair duplicated customers, overlapping time windows, or another dependence introduced during dataset construction.

### Inspect the residual distribution visually

For the Shapiro–Wilk test:

- `H₀`: the residuals follow a normal distribution.
- If `p < 0.05`, reject `H₀`.

With a large sample, even a small departure from normality can produce a very small p-value. A Q–Q plot and histogram show whether that departure is material rather than merely detectable.

Q–Q plot:

```python
import statsmodels.api as sm
import matplotlib.pyplot as plt

sm.qqplot(np.array(resid), line='45', fit=True)
plt.show()
```

Histogram:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(resid, kde=True)
plt.show()
```

## VIF exposes predictors that repeat the same information

To calculate the VIF for feature `Xᵢ`, regress it on the remaining predictors and use the resulting `Rᵢ²`:

`VIF_i = 1 / (1 - R_i²)`

A VIF above 5 corresponds to `Rᵢ² > 0.8` and is a signal to inspect the feature. It is a diagnostic threshold, not an automatic instruction to delete the variable.

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# X is a DataFrame containing the predictors
X = add_constant(x)

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
```

![VIF output](images/4.png)

## Three responses to multicollinearity

When several predictors carry overlapping information, there are three practical options:

1. Remove predictors that duplicate information already represented elsewhere.
2. Combine correlated predictors, for example with Principal Component Analysis.
3. Use regularization such as Ridge or Lasso.

The choice depends on the goal. Removing or combining features changes interpretation; regularization keeps the model predictive while shrinking unstable coefficients.

For explanation, removing a redundant feature may preserve a coefficient that the business can still interpret. For prediction, Ridge often keeps correlated signals without forcing an arbitrary winner. PCA can reduce dimension but replaces named business variables with linear combinations. Lasso performs selection through shrinkage, yet among strongly correlated predictors the selected variable can change across samples.

## PCA keeps directions with the most variance

For a square matrix `A`, an eigenvector `v` and eigenvalue `λ` satisfy:

`Av = λv`

Multiplying `v` by `A` changes its scale by `λ` without changing its direction.

In PCA, `A` is the covariance matrix. Each eigenvalue measures how much variance is retained along its corresponding eigenvector. Sorting eigenvalues from largest to smallest ranks the principal-component directions by the information they retain.

The explained-variance ratio is used to select the first `k` components—for example, enough components to retain 95% of the variance.

![Explained variance ratio](images/5.png)

An `n × n` covariance matrix has `n` eigenvalue–eigenvector pairs:

![Eigenvalue and eigenvector calculation](images/6.png)

Placing the selected eigenvectors into a projection matrix transforms the original `m` features into `k` principal components. This reduces dimension, but the new components are combinations of the original variables and are therefore less direct to interpret.

## Ridge and Lasso keep the predictors but penalize coefficients

Ridge adds an L2 penalty and shrinks correlated coefficients. Lasso adds an L1 penalty and can reduce some coefficients to exactly zero.

![Regularization overview](images/7.png)

![Lasso and Ridge comparison](images/8.png)

### Ridge solution

![Ridge objective](images/9.png)

![Ridge solution](images/10.png)

### Lasso solution

![Lasso solution](images/11.png)

## Choose the response to match the failure

| Observed problem | First response to consider |
| --- | --- |
| Curved residual pattern | Add justified nonlinear structure or change the model |
| Variance grows with fitted value | Revisit the target scale or use inference robust to heteroscedasticity |
| Serially correlated errors | Model the time or group dependence explicitly |
| High VIF but prediction remains stable | Prefer regularization if prediction is the goal |
| High VIF and coefficients must be explained | Remove, combine, or redefine overlapping features |
| A few rows control the fitted line | Inspect influential observations and the data-generation process |

The solver answers how to estimate the coefficients. Residual checks, validation data, and the intended use of those coefficients answer whether the fitted model deserves to be used.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Linear Regression: hai cách giải và các kiểm tra sau khi fit

Linear regression dễ fit nhưng cũng dễ dùng sai. Coefficient có thể mô tả expected outcome thay đổi thế nào theo input variable, nhưng chỉ sau khi đơn vị observation, thời điểm tạo feature và assumption của mô hình được xác định rõ.

## Một mô hình, từ một feature đến polynomial features

![Linear regression](images/1.png)

- Một input variable:

    y = w*x + b

- Nhiều input variable:

    y = w1*x1 + w2*x2 + … + wn*xn + b

- Polynomial term được xem như input feature mới tạo bằng feature engineering:

    y = w1*x1 + w2*x1^2 + … + b

## Dùng cho prediction hoặc để hiểu mối quan hệ

- Dự báo output liên tục như giá nhà, giá cổ phiếu hoặc credit score.
- Kiểm tra một mối quan hệ, chẳng hạn lãi suất cao hơn có liên hệ với tổng số dư sổ tiết kiệm cao hơn hay không.

Hai mục tiêu này không giống nhau. Một mô hình có thể dự báo tốt trong khi từng coefficient thiếu ổn định; một coefficient mô tả association cũng không chứng minh rằng thay đổi feature sẽ gây ra thay đổi ở outcome. Trong ví dụ tiền gửi, đặc điểm khách hàng có thể ảnh hưởng đồng thời đến lãi suất được áp dụng và số dư.

Trước khi fit, cần định nghĩa một dòng dữ liệu và cutoff date. Nếu một dòng đại diện cho một khách hàng tại cuối tháng, mọi predictor phải có trước thời điểm đó và target phải thuộc đúng cửa sổ hiện tại hoặc tương lai đã xác định. Quy tắc này ngăn thông tin từ target period rò rỉ vào feature.

## Fit cùng một mô hình theo hai cách

Với `x` và `y`, các coefficient có thể được ước lượng theo cách lặp bằng gradient descent hoặc giải trực tiếp bằng matrix operations. Tự triển khai cả hai giúp nhìn rõ khác biệt giữa optimization và closed-form solution.

- **Gradient descent:** giảm loss theo từng vòng lặp, qua đó thể hiện vai trò của learning rate, feature scale và convergence.
- **Matrix solution:** tính trực tiếp least-squares coefficient, qua đó thể hiện vai trò của matrix rank và collinearity.

Hai cách cùng ước lượng một linear model. Chúng khác nhau về tính toán, không khác nhau về quan hệ được giả định giữa predictor và outcome.

## Gradient descent cập nhật slope và intercept theo từng vòng lặp

### Bước 1: Khởi tạo `w` và `b`

```python
# initialize w

w_init = -0.01
w_init

# initialize b

b_init = 46
b_init

learning_rate = 0.0000001
loss_history = []
w_history = []
b_history = []
```

### Bước 2: Tính mean squared error

```
def calculate_mse(y_pred, y):
    mse = 0
    for i in range(len(y)):
        mse += ((y_pred[i] - y[i])**2)/len(y)

    return mse
```

### Bước 3: Tính gradient

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

### Bước 4: Cập nhật `w` và `b` qua nhiều epoch

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

### Bước 5: So sánh với scikit-learn

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

## Matrix operations cho nghiệm trực tiếp

![Normal equation](images/2.png)

![Matrix calculation](images/3.png)

Các notebook snippet dưới đây tính intercept và slope từ design matrix và từ các biến đã centered.

```python
n = len(x)
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

w = (xoffset.T @ yoffset) / (xoffset.T @ xoffset)

w

b = ymean - xmean*w
b
```

Cách đầu tiên đi trực tiếp theo normal equation. Trong production code, `np.linalg.lstsq` phù hợp hơn việc tính matrix inverse, đặc biệt khi các predictor gần linearly dependent.

Closed-form expression hữu ích để hiểu estimator, nhưng tính inverse trực tiếp làm tăng rủi ro số học và khối lượng tính toán không cần thiết. Gradient descent tránh phép inverse đó, đổi lại cần learning rate, stopping rule và phụ thuộc vào feature scale.

## Benchmark iterative solver và direct solver

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

Các trường hợp lớn trong benchmark tạo dense matrix và có thể cần nhiều memory; nên chạy riêng từng trường hợp thay vì xem đây là một ví dụ nhẹ.

Một benchmark công bằng cần ghi nhận nhiều hơn elapsed time. Hai solver phải dùng cùng dữ liệu sinh ra, đồng thời so sánh coefficient hoặc prediction error và ghi nhận trường hợp thất bại do memory, convergence hay design matrix bị ill-conditioned. Kết quả nhanh hơn không có ích nếu khác biệt về mặt số học so với least-squares solution.

## Kiểm tra assumption sau khi fit

Coefficient và prediction chưa phải điểm kết thúc. Residual giúp kiểm tra linear model có mô tả dữ liệu hợp lý hay không.

Mức độ quan trọng của từng assumption phụ thuộc vào mục tiêu. Normal residual chủ yếu liên quan đến inference trên sample nhỏ; đây không phải điều kiện để tính least-squares prediction. Linearity, leakage, phương sai thay đổi, observation phụ thuộc và influential point vẫn có thể làm mô hình sai dù normality test trông hợp lệ.

| Assumption | Cách kiểm tra | Tool |
| --- | --- | --- |
| Linearity | Vẽ residual theo fitted value | `sns.residplot()` |
| Error độc lập | Kiểm tra serial correlation; Durbin–Watson hữu ích cho dữ liệu có thứ tự hoặc time series | `durbin_watson()` |
| Phương sai không đổi | Xem residual theo fitted value hoặc chạy Breusch–Pagan test | `statsmodels` |
| Residual gần phân phối chuẩn | Dùng Q–Q plot, histogram hoặc Shapiro–Wilk test | `shapiro()`, `qqplot()` |
| Không có multicollinearity nghiêm trọng | Tính Variance Inflation Factor | `variance_inflation_factor()` |

Residual plot chẩn đoán pattern còn lại sau khi fit; nó không chứng minh các assumption sinh dữ liệu là đúng. Independence đặc biệt phụ thuộc vào cách lấy mẫu và cấu trúc thời gian. Durbin–Watson không thể sửa việc lặp khách hàng, chồng lấn time window hoặc một dạng phụ thuộc khác được tạo ra khi dựng dataset.

### Kiểm tra trực quan phân phối residual

Với Shapiro–Wilk test:

- `H₀`: residual tuân theo phân phối chuẩn.
- Nếu `p < 0.05`, bác bỏ `H₀`.

Khi sample lớn, chỉ một sai lệch nhỏ khỏi phân phối chuẩn cũng có thể tạo p-value rất nhỏ. Q–Q plot và histogram giúp phân biệt sai lệch thực sự đáng kể với sai lệch chỉ có thể phát hiện về mặt thống kê.

Q–Q plot:

```python
import statsmodels.api as sm
import matplotlib.pyplot as plt

sm.qqplot(np.array(resid), line='45', fit=True)
plt.show()
```

Histogram:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(resid, kde=True)
plt.show()
```

## VIF phát hiện các predictor lặp lại cùng một thông tin

Để tính VIF cho feature `Xᵢ`, regress nó theo các predictor còn lại và dùng `Rᵢ²` thu được:

`VIF_i = 1 / (1 - R_i²)`

VIF lớn hơn 5 tương ứng với `Rᵢ² > 0.8` và là tín hiệu cần kiểm tra feature. Đây là diagnostic threshold, không phải yêu cầu tự động xóa biến.

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# X is a DataFrame containing the predictors
X = add_constant(x)

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
```

![Kết quả VIF](images/4.png)

## Ba cách xử lý multicollinearity

Khi nhiều predictor chứa thông tin trùng nhau, có ba lựa chọn thực tế:

1. Bỏ predictor trùng với thông tin đã có ở biến khác.
2. Kết hợp các predictor tương quan, chẳng hạn bằng Principal Component Analysis.
3. Dùng regularization như Ridge hoặc Lasso.

Lựa chọn phụ thuộc vào mục tiêu. Bỏ hoặc kết hợp feature làm thay đổi khả năng diễn giải; regularization giữ mô hình phục vụ prediction nhưng thu nhỏ các coefficient thiếu ổn định.

Nếu mục tiêu là giải thích, bỏ một feature dư thừa có thể giữ lại coefficient mà business vẫn diễn giải được. Nếu mục tiêu là prediction, Ridge thường giữ các tín hiệu tương quan mà không buộc một biến thắng tùy ý. PCA giảm số chiều nhưng thay các business variable có tên bằng linear combination. Lasso thực hiện selection thông qua shrinkage, nhưng giữa các predictor tương quan mạnh, biến được chọn có thể thay đổi theo sample.

## PCA giữ các hướng có nhiều variance nhất

Với square matrix `A`, eigenvector `v` và eigenvalue `λ` thỏa mãn:

`Av = λv`

Nhân `v` với `A` làm thay đổi độ lớn theo `λ` nhưng không đổi hướng.

Trong PCA, `A` là covariance matrix. Mỗi eigenvalue đo lượng variance được giữ trên eigenvector tương ứng. Sắp xếp eigenvalue từ lớn đến nhỏ giúp xếp hạng các principal-component direction theo lượng thông tin chúng giữ lại.

Explained-variance ratio được dùng để chọn `k` component đầu tiên—ví dụ, số component đủ để giữ 95% variance.

![Explained variance ratio](images/5.png)

Một covariance matrix `n × n` có `n` cặp eigenvalue–eigenvector:

![Cách tính eigenvalue và eigenvector](images/6.png)

Đưa các eigenvector được chọn vào projection matrix sẽ biến đổi `m` feature ban đầu thành `k` principal component. Cách này giảm số chiều, nhưng component mới là tổ hợp của các biến ban đầu nên khó diễn giải trực tiếp hơn.

## Ridge và Lasso giữ predictor nhưng phạt coefficient

Ridge thêm L2 penalty và thu nhỏ các coefficient tương quan. Lasso thêm L1 penalty và có thể đưa một số coefficient về đúng 0.

![Tổng quan regularization](images/7.png)

![So sánh Lasso và Ridge](images/8.png)

### Nghiệm Ridge

![Ridge objective](images/9.png)

![Ridge solution](images/10.png)

### Nghiệm Lasso

![Lasso solution](images/11.png)

## Chọn cách xử lý đúng với failure quan sát được

| Vấn đề quan sát được | Cách xử lý nên cân nhắc đầu tiên |
| --- | --- |
| Residual có pattern cong | Thêm nonlinear structure có căn cứ hoặc đổi mô hình |
| Variance tăng theo fitted value | Xem lại target scale hoặc dùng inference chịu được heteroscedasticity |
| Error có serial correlation | Mô hình hóa rõ dependence theo thời gian hoặc theo group |
| VIF cao nhưng prediction ổn định | Ưu tiên regularization nếu mục tiêu là prediction |
| VIF cao và coefficient cần diễn giải | Loại, kết hợp hoặc định nghĩa lại các feature chồng lấn |
| Một số ít dòng chi phối fitted line | Kiểm tra influential observation và quá trình sinh dữ liệu |

Solver trả lời cách ước lượng coefficient. Residual check, validation data và mục đích sử dụng coefficient mới trả lời liệu mô hình đã fit có đáng được sử dụng hay không.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
