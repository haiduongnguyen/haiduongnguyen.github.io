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

Isolation Forest does not first learn what a normal cluster looks like. It repeatedly chooses a random feature and a random split value, then measures how many splits are needed to isolate each observation. Points that are few and different tend to be isolated earlier.

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

## A score is not yet an alert

Isolation Forest produces a ranking or score before it produces a business decision. A fixed threshold such as `0.5` or `0.6` is not automatically correct for every dataset. The useful threshold depends on the expected anomaly rate and, more importantly, how many false alerts can be reviewed.

This separation matters in practice: the forest generates anomaly evidence; the operating threshold decides what the team must investigate.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Isolation Forest: anomaly cần ít random split hơn

Isolation Forest không bắt đầu bằng việc học một normal cluster trông như thế nào. Thuật toán liên tục chọn ngẫu nhiên một feature và một split value, sau đó đo số lần split cần thiết để cô lập từng observation. Những point vừa ít vừa khác biệt thường được cô lập sớm hơn.

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

## Có score chưa có nghĩa là đã có alert

Isolation Forest tạo ranking hoặc score trước khi tạo business decision. Một threshold cố định như `0.5` hoặc `0.6` không tự động đúng với mọi dataset. Threshold hữu ích phụ thuộc vào expected anomaly rate và quan trọng hơn là số false alert mà nhóm vận hành có thể review.

Sự phân tách này quan trọng trong thực tế: forest tạo anomaly evidence; operating threshold quyết định điều gì team phải điều tra.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
