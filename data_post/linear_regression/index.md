---
title: Linear Regression
title_vi: Linear Regression — từ baseline đến chẩn đoán
title_en: Linear regression — from baseline to diagnostics
description: OLS estimation, time-aware validation, residual diagnostics, VIF, and coefficient stability for linear regression.
description_vi: OLS estimation, time-aware validation, residual diagnostics, VIF và coefficient stability cho linear regression.
description_en: OLS estimation, time-aware validation, residual diagnostics, VIF, and coefficient stability for linear regression.
date: 2026-04-08
writing_topic: foundations
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>Linear Regression</h1><p>Một baseline đơn giản nhưng mạnh: mô hình hóa kỳ vọng của target như tổ hợp tuyến tính của các feature.</p></header>
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
  <h2>Gradient, numerical stability và validation quyết định độ tin cậy</h2>
  <h3>Gradient của MSE phải khớp với định nghĩa loss</h3>
  <p>Với mean squared error thông thường, đạo hàm chứa hệ số hai. Hệ số này có thể được hấp thụ vào learning rate, nhưng giữ nhất quán giữa loss và derivative giúp debug và gradient checking dễ hơn.</p>
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
  <header class="page-intro"><h1>Linear regression</h1><p>A simple but strong baseline that models the expected target as a linear combination of features.</p></header>
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
  <h2>Gradients, numerical stability, and validation determine reliability</h2>
  <h3>The MSE gradient needs to match the loss definition</h3>
  <p>For plain mean squared error, the derivative contains a factor of two. That factor can be absorbed into the learning rate, but keeping the loss and derivative consistent makes debugging and gradient checking easier.</p>
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
