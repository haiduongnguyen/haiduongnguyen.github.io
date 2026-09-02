---
title: Logistic Regression
title_vi: Logistic Regression — xác suất, threshold và calibration
title_en: Logistic regression — probability, thresholds, and calibration
description: Logistic regression maps log-odds to probabilities; regularization, calibration, and operating costs determine how predictions are used.
description_vi: Logistic regression ánh xạ log-odds thành xác suất; regularization, calibration và chi phí vận hành quyết định cách dùng dự báo.
description_en: Logistic regression maps log-odds to probabilities; regularization, calibration, and operating costs determine how predictions are used.
date: 2026-04-08
writing_topic: foundations
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>Logistic Regression</h1><p>Một classifier tuyến tính cho xác suất: dễ tạo baseline, dễ giải thích và thường mạnh với dữ liệu tabular.</p></header>
  <h2>Từ score đến xác suất</h2><pre><code>z = β₀ + β₁x₁ + ... + βₚxₚ
p(y=1|x) = 1 / (1 + exp(-z))
log(p / (1-p)) = z</code></pre><p>Mỗi hệ số mô tả thay đổi của log-odds khi feature tăng một đơn vị. <code>exp(βⱼ)</code> là odds ratio có điều kiện, không phải mức tăng trực tiếp của probability.</p>
  <h2>Loss và regularization</h2><p>Model thường tối ưu log loss (binary cross-entropy). L2 regularization làm hệ số co lại và ổn định hơn khi feature tương quan; L1 có thể tạo hệ số bằng 0.</p>
  <h2>Threshold là quyết định kinh doanh</h2><p><code>0.5</code> chỉ là mặc định, không phải quy luật. Với fraud, churn hoặc campaign, threshold nên dựa trên chi phí false positive/false negative, capacity xử lý và precision–recall trade-off.</p>
  <h2>Workflow</h2><ol class="process"><li>Split tránh leakage theo thời gian hoặc customer.</li><li>Fit preprocessing chỉ trên train.</li><li>Đánh giá ROC-AUC và PR-AUC nhưng không dừng ở ranking.</li><li>Kiểm tra calibration bằng reliability curve/Brier score.</li><li>Chọn threshold trên validation set theo mục tiêu vận hành.</li><li>Report confusion matrix và metric tại threshold đã chọn.</li></ol>
  <h2>Python</h2><pre><code>from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(class_weight="balanced", max_iter=1000)
)
model.fit(X_train, y_train)
 probability = model.predict_proba(X_test)[:, 1]</code></pre>
  <h2>Calibration, numerical stability và threshold vận hành</h2>
  <h3>Đầu ra sigmoid không tự động là một xác suất đáng tin cậy</h3><p>Logistic regression ước lượng xác suất có điều kiện theo specification đã fit. Regularization, class weighting, cách lấy mẫu, drift và interaction bị thiếu đều có thể ảnh hưởng calibration. Cần đánh giá ranking và calibration riêng: ROC-AUC hoặc PR-AUC mô tả khả năng xếp hạng, còn Brier score và reliability curve kiểm tra xem các dự báo 0,7 có thực sự xảy ra khoảng 70% hay không.</p>
  <h3>Tính log loss mà không lấy log(0)</h3><pre><code class="language-python">import numpy as np

def sigmoid(score):
    score = np.clip(score, -500, 500)
    return 1.0 / (1.0 + np.exp(-score))

def binary_log_loss(actual, probability, epsilon=1e-15):
    probability = np.clip(probability, epsilon, 1.0 - epsilon)
    return -np.mean(
        actual * np.log(probability)
        + (1 - actual) * np.log(1 - probability)
    )

def confusion_at_threshold(actual, probability, threshold):
    predicted = probability >= threshold
    return {
        "tp": int(np.sum((actual == 1) & predicted)),
        "fp": int(np.sum((actual == 0) & predicted)),
        "tn": int(np.sum((actual == 0) & ~predicted)),
        "fn": int(np.sum((actual == 1) & ~predicted)),
    }</code></pre>
  <h3>Chọn threshold vận hành trước khi mở test set</h3><p>Fit trên train, chọn threshold bằng validation, rồi chỉ báo cáo một kết quả cuối trên test. Nếu đội fraud chỉ xử lý được 500 hồ sơ mỗi ngày, threshold có thể là mức score vừa lấp đầy capacity vừa tối đa hóa giá trị thu hồi kỳ vọng. Cách này có cơ sở hơn dùng mặc định 0,5 hoặc tune trực tiếp trên test label.</p>
  <h3>Class weighting thay đổi objective được tối ưu</h3><p><code>class_weight="balanced"</code> hữu ích khi lỗi ở minority class cần trọng số lớn hơn, nhưng không phải lời giải mặc định cho imbalance. Nó có thể làm dịch xác suất dự báo, vì vậy phải kiểm tra calibration trên dữ liệu có prevalence giống môi trường thật. Nên giữ một baseline không weighting và ghi rõ giả định chi phí mà weight đại diện.</p>
  <h3>Diễn giải coefficient theo đúng scale model đã dùng</h3><p>Odds ratio tương ứng với một đơn vị thay đổi của feature sau preprocessing. Nếu feature đã standardize, một đơn vị chính là một standard deviation của tập train. Feature tương quan có thể làm từng coefficient thiếu ổn định dù prediction vẫn hữu ích; hãy so sánh dấu và độ lớn qua nhiều resample trước khi kể một câu chuyện nghiệp vụ từ một hệ số.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression">Scikit-learn: Logistic Regression</a></li><li><a href="https://scikit-learn.org/stable/modules/calibration.html">Scikit-learn: Probability calibration</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><h1>Logistic regression</h1><p>A linear probabilistic classifier that is easy to baseline, explain, and often competitive on tabular data.</p></header>
  <h2>From score to probability</h2><pre><code>z = β₀ + β₁x₁ + ... + βₚxₚ
p(y=1|x) = 1 / (1 + exp(-z))
log(p / (1-p)) = z</code></pre><p>Each coefficient describes a change in log-odds. <code>exp(βⱼ)</code> is a conditional odds ratio, not a direct change in probability.</p>
  <h2>Loss and regularization</h2><p>The model commonly optimizes log loss (binary cross-entropy). L2 regularization shrinks coefficients and improves stability with correlated features; L1 can set coefficients to zero.</p>
  <h2>The threshold is a business decision</h2><p><code>0.5</code> is only a default. For fraud, churn, or campaigns, select a threshold from false-positive/false-negative costs, operating capacity, and the precision–recall trade-off.</p>
  <h2>Workflow</h2><ol class="process"><li>Split by time or customer to avoid leakage.</li><li>Fit preprocessing on training data only.</li><li>Evaluate ROC-AUC and PR-AUC, but go beyond ranking.</li><li>Check calibration with a reliability curve or Brier score.</li><li>Select the threshold on validation data for the operating objective.</li><li>Report the confusion matrix and metrics at that threshold.</li></ol>
  <h2>Python</h2><pre><code>from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(class_weight="balanced", max_iter=1000)
)
model.fit(X_train, y_train)
 probability = model.predict_proba(X_test)[:, 1]</code></pre>
  <h2>Calibration, numerical stability, and operating thresholds</h2>
  <h3>A sigmoid output is not automatically a trustworthy probability</h3><p>Logistic regression estimates a conditional probability under its fitted specification. Regularization, class weighting, sampling, drift, and missing interactions can all affect calibration. Evaluate ranking and calibration separately: ROC-AUC or PR-AUC describe ordering, while Brier score and reliability curves examine whether predictions such as 0.7 occur about 70% of the time.</p>
  <h3>Compute log loss without taking log(0)</h3><pre><code class="language-python">import numpy as np

def sigmoid(score):
    score = np.clip(score, -500, 500)
    return 1.0 / (1.0 + np.exp(-score))

def binary_log_loss(actual, probability, epsilon=1e-15):
    probability = np.clip(probability, epsilon, 1.0 - epsilon)
    return -np.mean(
        actual * np.log(probability)
        + (1 - actual) * np.log(1 - probability)
    )

def confusion_at_threshold(actual, probability, threshold):
    predicted = probability >= threshold
    return {
        "tp": int(np.sum((actual == 1) & predicted)),
        "fp": int(np.sum((actual == 0) & predicted)),
        "tn": int(np.sum((actual == 0) & ~predicted)),
        "fn": int(np.sum((actual == 1) & ~predicted)),
    }</code></pre>
  <h3>Select the operating threshold before opening the test set</h3><p>Fit on train, choose the threshold on validation data, then report one final result on test. In a fraud queue with capacity for 500 reviews per day, the threshold can be the score that fills that capacity while maximizing expected recovered value. This is more defensible than choosing 0.5 or tuning directly against the test labels.</p>
  <h3>Class weighting changes the fitted objective</h3><p><code>class_weight="balanced"</code> is useful when minority errors deserve more weight, but it is not a universal fix for imbalance. It can shift predicted probabilities, so validate calibration on data with the real deployment prevalence. Keep an unweighted baseline and document the cost assumption represented by the weights.</p>
  <h3>Interpret coefficients on the scale actually used by the model</h3><p>An odds ratio corresponds to a one-unit feature change after preprocessing. If a feature was standardized, that unit is one training-set standard deviation. Correlated features can make individual coefficients unstable even when predictions remain useful; compare signs and magnitudes across resamples before telling a business story about one coefficient.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression">Scikit-learn: Logistic Regression</a></li><li><a href="https://scikit-learn.org/stable/modules/calibration.html">Scikit-learn: Probability calibration</a></li></ul>
</article>
