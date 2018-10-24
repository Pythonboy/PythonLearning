# sklearn.metrics.average_precision_score

```python
sklearn.metrics.average_precision_score(y_true, y_score, average=’macro’, pos_label=1, sample_weight=None)
```

**Compute average precision (AP) from prediction scores**

*Note: this implementation is restricted to the binary classification task or multilabel classification task.*

AP summarizes a precision-recall curve as the weighted mean of precisions achieved at each threshold, with the increase in recall from the previous threshold used as the weight:

$$AP = \sum (R_n - R_{n-1})P_n$$

where $P_n$ and $R_n$ are the precision and recall at the nth threshold. This implementation is not interpolated and is different from computing the area under the precision-recall curve with the trapezoidal rule, which uses linear interpolation and can be too optimistic.



# Parameters

- **y_true** : array, shape = [n_samples] or [n_samples, n_classes] ; True binary labels or binary label indicators.
- **y_score** : array, shape = [n_samples] or [n_samples, n_classes] ;Target scores, can either be probability estimates of the positive class, confidence values, or non-thresholded measure of decisions (as returned by “decision_function” on some classifiers).
- **average** : string, [None, ‘micro’, ‘macro’ (default), ‘samples’, ‘weighted’]
  1. **micro** : Calculate metrics globally by considering each element of the label indicator matrix as a label.
  2. **macro** : Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
  3. **weighted** : Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).
  4. **samples** : Calculate metrics for each instance, and find their average.
- **pos_label** : int or str (default=1) ; The label of the positive class. Only applied to binary `y_true`. For multilabel-indicator `y_true`, `pos_label` is fixed to 1.
- **sample_weight** : array-like of shape = [n_samples], optional ; Sample weights.



# Examples

```python
>>> import numpy as np
>>> from sklearn.metrics import average_precision_score
>>> y_true = np.array([0, 0, 1, 1])
>>> y_scores = np.array([0.1, 0.4, 0.35, 0.8])
>>> average_precision_score(y_true, y_scores)  
0.83...
```

