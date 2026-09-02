---
title: Decision Tree
title_vi: Decision Tree — trực giác và cách chọn split
title_en: Decision trees — intuition and split selection
description: A concise, technically reviewed guide to decision-tree splits, weighted impurity, and regularization.
description_vi: Giải thích ngắn gọn và chính xác về cách decision tree chọn split, weighted impurity và regularization.
description_en: A concise, technically reviewed guide to decision-tree splits, weighted impurity, and regularization.
date: 2026-02-01
writing_topic: foundations
---

<section class="reading-page original-source" data-original-source="true" data-lang="vi">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

---
title: Decision Tree
---

🔙 [Back to Home](/)

## Decision tree: 

Reference link: https://machinelearningcoban.com/tabml_book/ch_model/decision_tree.html 


## Definition

![image.png](images/1.png)

Tại mỗi bước:

- Duyệt qua từng feature
- Duyệt qua từng ngưỡng của feature
- Tính gini của từng ngưỡng
- Lấy gini bé nhất để chia cây thành 2 cây nhỏ left và right

Tại sao lại lấy gini bé? 

Ví dụ khi cắt 1 ngưỡng mà cả 2 cây Left và Right bị lẫn 2 tập vào nhau (tức là k tốt) 

→ cây left có: gini = 1 - 0.5^2 - 0.5^2 = 0.5

→ cây right có: gini = 1 - 0.5^2 - 0.5^2 = 0.5

Còn ví dụ khi cắt 1 ngưỡng tốt, tức là có khả năng phân biệt, thì cây Left có tỉ lệ 0.3 0.7; còn cây Right có tỉ lệ 0.8 0.2 

→ cây left có: gini = 1 - 0.3^2 - 0.7^2 = 0.42

→ cây right có: gini =. 1 - 0.2^2 - 0.8^2 = 0.32

Tổng gini = 0.42 + 0.32

Như vậy gini càng bé chứng tỏ càng có khả năng phân tách tốt

Note: Ngoài gini còn có thể dùng entropy, logloss để chia cây

![image.png](images/2.png)

Câu hỏi: Có cần thiết phải duyệt qua hết tất cả feature lại không? Và với mỗi feature có cần duyệt hết các ngưỡng để cắt không?

trả lời từ chatgpt:

- **Thuật toán cơ bản**:
    
    Có, với feature dạng số (continuous), thuật toán sẽ xét tất cả các giá trị có thể làm ngưỡng chia. Thường là các giá trị trung điểm giữa hai quan sát liên tiếp sau khi sắp xếp.
    
- **Chi tiết**:
    - Nếu có n giá trị khác nhau cho feature đó, sẽ có tối đa n−1 ngưỡng cần xét.
        
        n → n-1
        
    - Với feature dạng phân loại (categorical), thuật toán sẽ xét các cách nhóm các category (nhưng thường dùng heuristic vì số tổ hợp rất lớn).
- **Tối ưu hóa**:
    - **Approximation**: Chỉ xét một số ngưỡng được chọn ngẫu nhiên hoặc dựa trên histogram.
    - **Pre-sorting**: Sắp xếp trước để giảm chi phí tính toán.

Câu hỏi: thực tế trong thuật toán decision tree từ sklearn thì họ dùng những kĩ thuật nào 

### **1. Không duyệt tất cả ngưỡng một cách brute-force**

- Với feature dạng số, scikit-learn **sắp xếp trước** các giá trị của feature và chỉ xét các điểm chia ở **giữa hai giá trị liên tiếp** (midpoints).

### **2. Pre-sorting và sử dụng mảng chỉ số**

- Thay vì sắp xếp lại dữ liệu ở mỗi node, scikit-learn **giữ một mảng chỉ số đã sắp xếp cho từng feature**.
→ Giúp việc tính toán nhanh hơn khi đi xuống các node con.

### **3. Giới hạn số lượng feature và ngưỡng**

- Bạn có thể điều chỉnh:
    - `max_features`: Chỉ xét một tập con ngẫu nhiên của feature tại mỗi node (giống Random Forest).
    - `max_depth`, `min_samples_split`, `min_samples_leaf`: Giới hạn độ sâu và số lượng mẫu để tránh duyệt quá nhiều.

### **4. Sử dụng Cython để tăng tốc**

- Phần lõi của thuật toán được viết bằng **Cython**, giúp tính toán impurity và tìm split nhanh hơn nhiều so với Python thuần.

### **5. Không xét tất cả tổ hợp cho feature phân loại**

- Với feature dạng categorical (nếu được mã hóa thành số), scikit-learn **chỉ xét chia theo giá trị đơn lẻ**, không xét tất cả nhóm category (vì số tổ hợp quá lớn).

### **6. Heuristic cho dữ liệu lớn**

- Với `criterion="gini"` hoặc `"entropy"`, scikit-learn tính toán impurity theo công thức tối ưu hóa để giảm số phép tính.
- Có thể dùng `splitter="random"` để chọn ngưỡng ngẫu nhiên thay vì duyệt hết (giúp tăng tốc).
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Learning note · Classification</p><h1>Decision Tree</h1><p>Một cây quyết định liên tục chia dữ liệu thành các vùng sao cho target trong mỗi vùng ngày càng thuần nhất.</p></header>
  <h2>Cây chọn split như thế nào?</h2>
  <p>Với mỗi feature số, thuật toán xét các candidate threshold giữa những giá trị liên tiếp đã sắp xếp. Mỗi split tạo ra node trái và phải. Chất lượng split được đo bằng <strong>weighted impurity</strong>:</p>
  <pre><code>impurity(split) = (n_left / n) × I(left)
                + (n_right / n) × I(right)</code></pre>
  <p>Với classification, <code>I</code> thường là Gini hoặc entropy. Không nên cộng impurity của hai node mà bỏ qua kích thước của chúng: một node 990 mẫu phải có trọng số khác node 10 mẫu.</p>
  <h2>Gini trực quan</h2>
  <pre><code>Gini = 1 - Σ p(k)²</code></pre>
  <p>Gini bằng 0 khi node chỉ có một class. Cây chọn split làm giảm impurity nhiều nhất, rồi lặp lại ở các node con.</p>
  <h2>Tránh overfitting</h2>
  <ul><li><code>max_depth</code>: giới hạn độ sâu.</li><li><code>min_samples_leaf</code>: tránh các leaf quá nhỏ.</li><li><code>min_samples_split</code>: yêu cầu đủ mẫu trước khi chia.</li><li><code>ccp_alpha</code>: post-pruning bằng minimal cost-complexity.</li></ul>
  <div class="callout"><p><strong>Lưu ý về categorical feature:</strong> DecisionTreeClassifier của scikit-learn không xử lý category một cách native. Nếu mã hóa category thành số nguyên, cây sẽ coi chúng là dữ liệu số có thứ tự. Hãy dùng encoding phù hợp hoặc estimator hỗ trợ categorical feature.</p></div>
  <h2>Khi nào phù hợp?</h2><p>Decision tree dễ diễn giải, mô hình hóa nonlinear interaction và ít cần scaling. Đổi lại, một cây đơn thường không ổn định; bagging hoặc boosting thường cho khả năng tổng quát hóa tốt hơn.</p>
  <h2>Hiệu chỉnh và mở rộng từ ghi chép gốc</h2>
  <h3>Đánh giá split bằng impurity reduction, không cộng thô impurity của hai node</h3><p>Đại lượng cần quan tâm là impurity của parent trừ đi impurity của các child sau khi đã tính trọng số theo số mẫu. Một child rất nhỏ nhưng thuần không được lấn át một child lớn còn trộn lẫn. Với feature số, candidate threshold nằm giữa các giá trị kề nhau và khác nhau sau khi sort; threshold tạo child rỗng là không hợp lệ.</p>
  <pre><code class="language-python">import numpy as np

def gini(labels):
    _, counts = np.unique(labels, return_counts=True)
    probability = counts / counts.sum()
    return 1.0 - np.sum(probability ** 2)

def best_numeric_split(values, labels):
    order = np.argsort(values)
    values, labels = values[order], labels[order]
    parent = gini(labels)
    best = None
    for index in range(1, len(values)):
        if values[index - 1] == values[index]:
            continue
        threshold = (values[index - 1] + values[index]) / 2.0
        left, right = labels[:index], labels[index:]
        weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(labels)
        gain = parent - weighted
        if best is None or gain > best["gain"]:
            best = {"threshold": threshold, "gain": gain}
    return best</code></pre>
  <h3>Implementation detail không phải cam kết của thuật toán</h3><p>Các thư viện tối ưu split search bằng Cython/C++ và phần nội bộ này có thể thay đổi. Nên giải thích invariant—duyệt candidate hợp lệ một cách hiệu quả—thay vì khẳng định mọi phiên bản luôn giữ một global sorted-index array cho từng feature. Nếu benchmark hoặc reproducibility phụ thuộc implementation, cần pin phiên bản thư viện.</p>
  <h3>Xác suất ở leaf có thể quá tự tin</h3><p>Một leaf có 9 positive trong 10 dòng train sẽ cho dự báo 0,9 theo cách đơn giản, nhưng leaf nhỏ có variance cao. Hãy tune <code>min_samples_leaf</code>, kiểm tra calibration trên held-out data và không diễn giải một đường đi trong cây thành quan hệ nhân quả.</p>
  <h3>Kiểm tra pruning và stability</h3><p>Chọn depth hoặc <code>ccp_alpha</code> trên validation fold giữ đúng ranh giới thời gian/khách hàng. Fit lại trên bootstrap sample hoặc time window lân cận và so sánh top split. Nếu root liên tục thay đổi, business rule suy ra từ một cây duy nhất chưa đủ ổn định để vận hành trực tiếp.</p>
  <h2>Nguồn</h2><ul><li><a href="https://scikit-learn.org/stable/modules/tree.html">Scikit-learn: Decision Trees user guide</a></li><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">DecisionTreeClassifier API</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Learning note · Classification</p><h1>Decision trees</h1><p>A decision tree repeatedly partitions data into regions whose targets become progressively purer.</p></header>
  <h2>How is a split selected?</h2>
  <p>For each numerical feature, the algorithm evaluates candidate thresholds between sorted adjacent values. A split creates left and right nodes and is scored with <strong>weighted impurity</strong>:</p>
  <pre><code>impurity(split) = (n_left / n) × I(left)
                + (n_right / n) × I(right)</code></pre>
  <p>For classification, <code>I</code> is commonly Gini impurity or entropy. Child impurities must not be added without weighting: a node with 990 samples should count differently from one with 10.</p>
  <h2>Gini intuition</h2><pre><code>Gini = 1 - Σ p(k)²</code></pre><p>Gini is zero when a node contains one class. The tree selects the split with the largest impurity reduction and repeats the process recursively.</p>
  <h2>Controlling overfitting</h2><ul><li><code>max_depth</code> limits tree depth.</li><li><code>min_samples_leaf</code> prevents tiny leaves.</li><li><code>min_samples_split</code> requires enough samples before splitting.</li><li><code>ccp_alpha</code> enables minimal cost-complexity pruning.</li></ul>
  <div class="callout"><p><strong>Categorical features:</strong> scikit-learn’s DecisionTreeClassifier does not handle categories natively. Integer encoding makes the values appear ordered. Use an appropriate encoding strategy or an estimator with categorical support.</p></div>
  <h2>When does it work well?</h2><p>Decision trees are interpretable, model nonlinear interactions, and need little feature scaling. A single tree can be unstable, however, which is why bagging and boosting often generalize better.</p>
  <h2>Corrections and extensions to the original notes</h2>
  <h3>A split is judged by impurity reduction, not raw child impurity</h3><p>The useful quantity is parent impurity minus the sample-weighted child impurity. A tiny pure child should not dominate a large mixed child. Candidate thresholds for a numerical feature lie between adjacent distinct values after sorting; thresholds that leave an empty child are invalid.</p>
  <pre><code class="language-python">import numpy as np

def gini(labels):
    _, counts = np.unique(labels, return_counts=True)
    probability = counts / counts.sum()
    return 1.0 - np.sum(probability ** 2)

def best_numeric_split(values, labels):
    order = np.argsort(values)
    values, labels = values[order], labels[order]
    parent = gini(labels)
    best = None
    for index in range(1, len(values)):
        if values[index - 1] == values[index]:
            continue
        threshold = (values[index - 1] + values[index]) / 2.0
        left, right = labels[:index], labels[index:]
        weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(labels)
        gain = parent - weighted
        if best is None or gain > best["gain"]:
            best = {"threshold": threshold, "gain": gain}
    return best</code></pre>
  <h3>Implementation details are not algorithm guarantees</h3><p>Libraries optimize split search in Cython/C++ and those internals can change. It is safer to explain the invariant—evaluate valid candidates efficiently—than to promise that every version keeps one globally sorted index array per feature. Pin the library version when a benchmark or reproducibility claim depends on its internals.</p>
  <h3>Leaf probabilities can be overconfident</h3><p>A leaf with 9 positives among 10 training rows predicts 0.9 in the simplest implementation, but small leaves have high variance. Tune <code>min_samples_leaf</code>, check calibration on held-out data, and avoid presenting a path through the tree as a causal explanation.</p>
  <h3>Validate pruning and stability</h3><p>Select depth or <code>ccp_alpha</code> on validation folds that preserve time/customer boundaries. Refit across bootstrap samples or adjacent time windows and compare top splits. If the root changes repeatedly, the business rule implied by one fitted tree is not stable enough to operationalize directly.</p>
  <h2>Sources</h2><ul><li><a href="https://scikit-learn.org/stable/modules/tree.html">Scikit-learn: Decision Trees user guide</a></li><li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">DecisionTreeClassifier API</a></li></ul>
</article>
