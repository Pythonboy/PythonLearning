# sklearn.metrics.precision_recall_curve

```python
sklearn.metrics.precision_recall_curve(y_true, probas_pred, pos_label=None, sample_weight=None)
```

**Compute precision-recall pairs for different probability thresholds**

*Note: this implementation is restricted to the binary classification task.*



# Parameters & Returns

- Parameters
  1. **y_true** : array, shape = [n_samples] ; True targets of binary classification in range {-1, 1} or {0, 1}.
  2. **probas_pred** : array, shape = [n_samples] ; Estimated probabilities or decision function.
  3. **pos_label** : int or str, default=None ; The label of the positive class
  4. **sample_weight** : array-like of shape = [n_samples], optional ; Sample weights.
- Returns
  1. **precision** : array, shape = [n_thresholds + 1] ; Precision values such that element i is the precision of predictions with score >= thresholds[i] and the last element is 1.
  2. **recall** : array, shape = [n_thresholds + 1] ; Decreasing recall values such that element i is the recall of predictions with score >= thresholds[i] and the last element is 0.
  3. **thresholds** : array, shape = [n_thresholds <= len(np.unique(probas_pred))] ; Increasing thresholds on the decision function used to compute precision and recall.



# Examples

```python
>>> import numpy as np
>>> from sklearn.metrics import precision_recall_curve
>>> y_true = np.array([0, 0, 1, 1])
>>> y_scores = np.array([0.1, 0.4, 0.35, 0.8])
>>> precision, recall, thresholds = precision_recall_curve(
...     y_true, y_scores)
>>> precision  
array([0.66666667, 0.5       , 1.        , 1.        ])
>>> recall
array([1. , 0.5, 0.5, 0. ])
>>> thresholds
array([0.35, 0.4 , 0.8 ])
```

