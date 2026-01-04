# Isolation Forest

### Overview

Isolation Forest is an anomaly detection algorithm that isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. This recursive partitioning can be represented by a tree structure, and anomalies are isolated in fewer steps as they are typically "few and different."

### Key Concepts

- **Isolation**: The process of separating an instance from the rest of the data
- **Path Length**: Number of edges traversed from root to terminating node
- **Anomaly Score**: Calculated based on path length (shorter path = more likely to be an anomaly)
- **Sub-sampling**: Helps improve robustness and reduce computational complexity

### Algorithm Steps

1. Build isolation trees (iTree) from random sub-samples of data
2. For each instance, calculate its path length across all trees
3. Calculate anomaly score using average path length
4. Classify instances as anomalies based on score threshold

### Anomaly Score Formula

```
s(x, n) = 2^(-E(h(x))/c(n))
```

Where:

- s(x, n) is the anomaly score
- E(h(x)) is the average path length of instance x
- c(n) is the average path length of unsuccessful searches in a BST
- n is the number of external nodes

### Advantages

- Linear time complexity: O(t × n log n) where t = number of trees, n = data size
- Memory efficient compared to distance-based methods
- Works well with high-dimensional data
- No distance calculation needed
- No assumptions about data distribution
- Handles mixed attribute types well

### Implementation Pseudo-code

**Building an iTree:**

```python
def build_iTree(X, height_limit, current_height=0):
    if current_height >= height_limit or len(X) <= 1:
        return ExNode(size=len(X))
    
    # Randomly select attribute
    q = randomly select feature
    
    # Randomly select split point
    p = randomly select value between min and max of X[:, q]
    
    X_left = X[X[:, q] < p]
    X_right = X[X[:, q] >= p]
    
    return InNode(
        left=build_iTree(X_left, height_limit, current_height + 1),
        right=build_iTree(X_right, height_limit, current_height + 1),
        split_attribute=q,
        split_value=p
    )
```

**Path Length Calculation:**

```python
def path_length(x, tree, current_height=0):
    if isinstance(tree, ExNode):
        return current_height
    
    if x[tree.split_attribute] < tree.split_value:
        return path_length(x, tree.left, current_height + 1)
    else:
        return path_length(x, tree.right, current_height + 1)
```

### Practical Considerations

- **Number of trees**: 100-500 typically sufficient
- **Subsample size**: 256 recommended in the original paper
- **Height limit**: log2(subsample_size) default
- **Anomaly threshold**: Usually 0.5-0.6 (scores > threshold = anomalies)

### Visualizations

- Path length distributions: Normal points vs. anomalies
- Decision boundaries in 2D feature space
- Anomaly score heatmaps