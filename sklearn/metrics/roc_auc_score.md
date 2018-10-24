# sklearn.metrics.roc_auc_score

```python
sklearn.metrics.roc_auc_score(y_true, y_score, average=’macro’, sample_weight=None, max_fpr=None)
```

**Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores.**

*Note: this implementation is restricted to the binary classification task or multilabel classification task in label indicator format.*



# Parameters

- **y_true** : array, shape = [n_samples] or [n_samples, n_classes] ; True binary labels or binary label indicators.
- **y_score** : array, shape = [n_samples] or [n_samples, n_classes] ; Target scores, can either be probability estimates of the positive class, confidence values, or non-thresholded measure of decisions (as returned by “decision_function” on some classifiers). For binary y_true, y_score is supposed to be the score of the class with greater label.
- **average** : string, [None, ‘micro’, ‘macro’ (default), ‘samples’, ‘weighted’] ;
  1. **micro**: Calculate metrics globally by considering each element of the label indicator matrix as a label.
  2. **macro**:Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
  3. **weighted**: Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).
  4. **samples**: Calculate metrics for each instance, and find their average.
- **sample_weight** : array-like of shape = [n_samples], optional



# Examples

```python
>>> import numpy as np
>>> from sklearn.metrics import roc_auc_score
>>> y_true = np.array([0, 0, 1, 1])
>>> y_scores = np.array([0.1, 0.4, 0.35, 0.8])
>>> roc_auc_score(y_true, y_scores)
0.75
```

