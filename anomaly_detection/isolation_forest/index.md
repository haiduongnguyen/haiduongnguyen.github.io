---
title: "Isolation Forest: Anomalies Need Fewer Random Splits"
title_vi: "Isolation Forest: anomaly cần ít random split hơn"
title_en: "Isolation Forest: Anomalies Need Fewer Random Splits"
description: Isolation Forest turns random-tree path length into an anomaly score; the threshold then determines which scores become alerts.
description_vi: Isolation Forest chuyển path length của random tree thành anomaly score; threshold quyết định score nào thành cảnh báo.
description_en: Isolation Forest turns random-tree path length into an anomaly score; the threshold then determines which scores become alerts.
date: 2026-02-01
writing_topic: anomaly
---

{% capture article_en %}
🔙 [Back to Home](/)

# Isolation Forest: Anomalies Need Fewer Random Splits

Isolation Forest does not first learn what a normal cluster looks like. It repeatedly chooses a random feature and a random split value, then measures how many splits are needed to isolate each observation. The useful output is an anomaly ranking; the business threshold comes later.

## Define the anomaly unit before fitting the forest

In the synthetic APM dataset, one row contains CPU, memory, latency, and throughput for one span. Five spans share the same trace and synthetic anomaly label. This creates two possible analysis units:

- **Span level:** score each service span independently.
- **Trace level:** aggregate or combine the five spans and score the request as a unit.

That choice changes both the feature table and the evaluation. If the target is a trace-level incident, a random row split is unsafe because sibling spans from one trace can enter both training and test data. Splitting by `trace_id` keeps an entire request on one side.

## Random partitions create an isolation path

Each isolation tree is built from a random subsample:

1. Select a feature at random.
2. Select a split value between that feature's minimum and maximum values.
3. Send observations to the left or right child.
4. Repeat until an observation is isolated or the tree reaches its height limit.

The **path length** is the number of edges from the root to the terminating node. Short paths indicate observations that were easy to separate from the rest of the sample.

## Average path length becomes an anomaly score

Across multiple trees, the score is:

```text
s(x, n) = 2^(-E[h(x)] / c(n))
```

- `E[h(x)]`: average path length of observation `x` across the forest.
- `c(n)`: expected path length of an unsuccessful search in a binary search tree.
- `n`: subsample size.

A shorter average path produces a score closer to 1. A longer path produces a score closer to 0.

## The tree-building logic is small

This pseudocode keeps the original recursive idea visible:

```python
def build_iTree(X, height_limit, current_height=0):
    if current_height >= height_limit or len(X) <= 1:
        return ExNode(size=len(X))

    q = randomly_select_feature(X)
    p = randomly_select_value(min(X[:, q]), max(X[:, q]))

    X_left = X[X[:, q] < p]
    X_right = X[X[:, q] >= p]

    return InNode(
        left=build_iTree(X_left, height_limit, current_height + 1),
        right=build_iTree(X_right, height_limit, current_height + 1),
        split_attribute=q,
        split_value=p,
    )
```

The same observation is passed through every tree, and its path lengths are averaged before calculating the score.

```python
def path_length(x, tree, current_height=0):
    if isinstance(tree, ExNode):
        return current_height

    if x[tree.split_attribute] < tree.split_value:
        return path_length(x, tree.left, current_height + 1)
    return path_length(x, tree.right, current_height + 1)
```

## Subsampling is part of the method

The original method uses small random subsamples; `256` observations is a common default when the dataset is larger than that. Small samples make trees cheaper to build and reduce the chance that many normal observations hide an anomaly inside a dense region.

The main parameters control different parts of the result:

- Number of trees controls how many random partitions contribute to the average.
- Subsample size controls the population seen by each tree.
- Maximum features controls which dimensions are available to each tree.
- The score threshold controls how many observations are finally labeled anomalous.

The four APM features also have different distributions. CPU and memory are bounded percentages, throughput is a count, and latency has a much wider upper range in the published data. Isolation Forest is less directly scale-sensitive than a Euclidean-distance method such as LOF, but skewed features and extreme ranges still affect where random partitions can isolate points. Feature distributions should be inspected rather than scaled by habit or ignored by habit.

## A score is not yet an alert

Isolation Forest produces a ranking or score before it produces a business decision. A fixed threshold such as `0.5` or `0.6` is not automatically correct for every dataset. The useful threshold depends on the expected anomaly rate and, more importantly, how many false alerts can be reviewed.

This separation matters in practice: the forest generates anomaly evidence; the operating threshold decides what the team must investigate.

## Evaluate the ranking at trace level and at the review budget

The synthetic `is_anomaly` field is evaluation ground truth, not a model feature. Since anomalies are the minority, accuracy can remain high even when the detector misses them. Evaluation should include precision and recall, a precision–recall curve, and performance at the number of alerts the team can actually review.

Span-level metrics answer whether individual service operations were ranked correctly. Trace-level metrics answer whether the request containing the anomaly was surfaced. Reporting both prevents five anomalous spans from being mistaken for five independent incidents.

## Isolation explains separability, not root cause

A short path tells us that a point was easy to separate through random partitions. It does not prove which feature caused a production incident, and standard feature importance from a supervised model does not automatically apply. Root-cause analysis requires a separate explanation layer and evidence from the relevant trace or logs.

For this project, Isolation Forest is therefore one component: it ranks unusual metric observations. Trace reconstruction, threshold selection, and root-cause evidence remain separate decisions.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Isolation Forest: anomaly cần ít random split hơn

Isolation Forest không bắt đầu bằng việc học một normal cluster trông như thế nào. Thuật toán liên tục chọn ngẫu nhiên một feature và một split value, sau đó đo số lần split cần thiết để cô lập từng observation. Output hữu ích trước tiên là anomaly ranking; business threshold được quyết định sau.

## Xác định đơn vị anomaly trước khi fit forest

Trong synthetic APM dataset, một dòng chứa CPU, memory, latency và throughput của một span. Năm span chia sẻ cùng trace và synthetic anomaly label. Điều này tạo ra hai đơn vị phân tích có thể chọn:

- **Span level:** score từng service span độc lập.
- **Trace level:** aggregate hoặc kết hợp năm span rồi score request như một đơn vị.

Lựa chọn này thay đổi cả feature table lẫn evaluation. Nếu target là incident ở cấp trace, random split theo dòng không an toàn vì sibling span của cùng một trace có thể đi vào cả train và test. Split theo `trace_id` giữ toàn bộ request ở cùng một phía.

## Random partition tạo isolation path

Mỗi isolation tree được xây dựng từ một random subsample:

1. Chọn ngẫu nhiên một feature.
2. Chọn một split value nằm giữa giá trị nhỏ nhất và lớn nhất của feature đó.
3. Đưa observation vào left hoặc right child.
4. Lặp lại cho đến khi observation được cô lập hoặc cây chạm height limit.

**Path length** là số edge từ root đến terminating node. Path ngắn cho biết observation dễ tách khỏi phần còn lại của sample.

## Average path length trở thành anomaly score

Trên nhiều tree, score được tính bằng:

```text
s(x, n) = 2^(-E[h(x)] / c(n))
```

- `E[h(x)]`: average path length của observation `x` trên toàn forest.
- `c(n)`: expected path length của một unsuccessful search trong binary search tree.
- `n`: subsample size.

Average path ngắn hơn tạo score gần 1; path dài hơn tạo score gần 0.

## Logic xây tree khá ngắn

Pseudocode này giữ lại ý tưởng recursive ban đầu:

```python
def build_iTree(X, height_limit, current_height=0):
    if current_height >= height_limit or len(X) <= 1:
        return ExNode(size=len(X))

    q = randomly_select_feature(X)
    p = randomly_select_value(min(X[:, q]), max(X[:, q]))

    X_left = X[X[:, q] < p]
    X_right = X[X[:, q] >= p]

    return InNode(
        left=build_iTree(X_left, height_limit, current_height + 1),
        right=build_iTree(X_right, height_limit, current_height + 1),
        split_attribute=q,
        split_value=p,
    )
```

Cùng một observation được đi qua từng tree, sau đó path length được lấy trung bình trước khi tính score.

```python
def path_length(x, tree, current_height=0):
    if isinstance(tree, ExNode):
        return current_height

    if x[tree.split_attribute] < tree.split_value:
        return path_length(x, tree.left, current_height + 1)
    return path_length(x, tree.right, current_height + 1)
```

## Subsampling là một phần của phương pháp

Phương pháp ban đầu dùng các random subsample nhỏ; `256` observation là default phổ biến khi dataset lớn hơn con số này. Sample nhỏ làm tree rẻ hơn khi xây dựng và giảm khả năng nhiều normal observation che khuất một anomaly trong vùng dày.

Các parameter chính kiểm soát những phần khác nhau:

- Số tree kiểm soát số random partition đóng góp vào average.
- Subsample size kiểm soát population mà từng tree nhìn thấy.
- Maximum features kiểm soát các dimension tree có thể sử dụng.
- Score threshold kiểm soát số observation cuối cùng được gắn nhãn anomalous.

Bốn APM feature cũng có distribution khác nhau. CPU và memory là phần trăm có giới hạn, throughput là count, còn latency có upper range rộng hơn nhiều trong dữ liệu đã công bố. Isolation Forest ít phụ thuộc trực tiếp vào scale hơn phương pháp Euclidean-distance như LOF, nhưng skewed feature và extreme range vẫn ảnh hưởng vị trí random partition có thể cô lập point. Cần kiểm tra feature distribution thay vì scaling theo thói quen hoặc bỏ qua theo thói quen.

## Có score chưa có nghĩa là đã có alert

Isolation Forest tạo ranking hoặc score trước khi tạo business decision. Một threshold cố định như `0.5` hoặc `0.6` không tự động đúng với mọi dataset. Threshold hữu ích phụ thuộc vào expected anomaly rate và quan trọng hơn là số false alert mà nhóm vận hành có thể review.

Sự phân tách này quan trọng trong thực tế: forest tạo anomaly evidence; operating threshold quyết định điều gì team phải điều tra.

## Đánh giá ranking ở cả trace level và review budget

Synthetic field `is_anomaly` là evaluation ground truth, không phải model feature. Vì anomaly thuộc nhóm thiểu số, accuracy vẫn có thể cao dù detector bỏ sót chúng. Evaluation cần gồm precision, recall, precision–recall curve và performance tại số alert mà team thực sự có thể review.

Span-level metric trả lời từng service operation có được xếp hạng đúng không. Trace-level metric trả lời request chứa anomaly có được phát hiện không. Báo cáo cả hai ngăn việc coi năm anomalous span là năm incident độc lập.

## Isolation giải thích khả năng phân tách, không phải root cause

Path ngắn cho biết một point dễ bị tách bằng random partition. Nó không chứng minh feature nào gây ra production incident, và standard feature importance của supervised model không tự động áp dụng ở đây. Root-cause analysis cần một explanation layer riêng cùng evidence từ trace hoặc log liên quan.

Trong project này, Isolation Forest vì thế chỉ là một component: nó xếp hạng metric observation bất thường. Trace reconstruction, threshold selection và root-cause evidence vẫn là những quyết định riêng.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
