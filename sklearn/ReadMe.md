# [klearn.cluster](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster): Clustering

The [`sklearn.cluster`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster) module gathers popular unsupervised clustering algorithms.

### Functions

| 方法                                                         | 介绍                          |
| ------------------------------------------------------------ | ----------------------------- |
| [`cluster.k_means`](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means)(X, n_clusters[, …]) | K-means clustering algorithm. |



# [`sklearn.datasets`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets): Datasets

The [`sklearn.datasets`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets) module includes utilities to load datasets, including methods to load and fetch popular reference datasets. It also features some artificial data generators.

### Loaders

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`datasets.load_diabetes`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes)([return_X_y]) | Load and return the diabetes dataset (regression).           |
| [`datasets.load_digits`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits)([n_class, return_X_y]) | Load and return the digits dataset (classification).         |
| [`datasets.load_boston`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)([return_X_y]) | Load and return the boston house-prices dataset (regression). |
| [`datasets.load_iris`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris)([return_X_y]) | Load and return the iris dataset (classification).           |



# [`sklearn.decomposition`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.decomposition): Matrix Decomposition

| 方法                                                         | 介绍                               |
| ------------------------------------------------------------ | ---------------------------------- |
| [`decomposition.PCA`](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA)([n_components, copy, …]) | Principal component analysis (PCA) |



# [`sklearn.ensemble`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble): Ensemble Methods

The [`sklearn.ensemble`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble) module includes ensemble-based methods for classification, regression and anomaly detection.

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`ensemble.AdaBoostClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier)([…]) | An AdaBoost classifier.                                      |
| [`ensemble.AdaBoostRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor)([base_estimator, …]) | An AdaBoost regressor.                                       |
| [`ensemble.BaggingClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier)([base_estimator, …]) | A Bagging classifier.                                        |
| [`ensemble.BaggingRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor)([base_estimator, …]) | A Bagging regressor.                                         |
| [`ensemble.ExtraTreesClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier)([…]) | An extra-trees classifier.                                   |
| [`ensemble.ExtraTreesRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor)([n_estimators, …]) | An extra-trees regressor.                                    |
| [`ensemble.GradientBoostingClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier)([loss, …]) | Gradient Boosting for classification.                        |
| [`ensemble.GradientBoostingRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor)([loss, …]) | Gradient Boosting for regression.                            |
| [`ensemble.IsolationForest`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest)([n_estimators, …]) | Isolation Forest Algorithm                                   |
| [`ensemble.RandomForestClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)([…]) | A random forest classifier.                                  |
| [`ensemble.RandomForestRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor)([…]) | A random forest regressor.                                   |
| [`ensemble.RandomTreesEmbedding`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding)([…]) | An ensemble of totally random trees.                         |
| [`ensemble.VotingClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier)(estimators[, …]) | Soft Voting/Majority Rule classifier for unfitted estimators. |



# [`sklearn.linear_model`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model): Generalized Linear Models

The [`sklearn.linear_model`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model) module implements generalized linear models. It includes Ridge regression, Bayesian Regression, Lasso and Elastic Net estimators computed with Least Angle Regression and coordinate descent. It also implements Stochastic Gradient Descent related algorithms.

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`linear_model.Ridge`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge)([alpha, fit_intercept, …]) | Linear least squares with l2 regularization.                 |
| [`linear_model.RidgeClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier)([alpha, …]) | Classifier using Ridge regression.                           |
| [`linear_model.RidgeClassifierCV`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV)([alphas, …]) | Ridge classifier with built-in cross-validation.             |
| [`linear_model.RidgeCV`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV)([alphas, …]) | Ridge regression with built-in cross-validation.             |
| [`linear_model.LinearRegression`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression)([…]) | Ordinary least squares Linear Regression.                    |
| [`linear_model.LogisticRegression`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression)([penalty, …]) | Logistic Regression (aka logit, MaxEnt) classifier.          |
| [`linear_model.LogisticRegressionCV`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV)([Cs, …]) | Logistic Regression CV (aka logit, MaxEnt) classifier.       |
| [`linear_model.Lasso`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso)([alpha, fit_intercept, …]) | Linear Model trained with L1 prior as regularizer (aka the Lasso) |
| [`linear_model.LassoCV`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV)([eps, n_alphas, …]) | Lasso linear model with iterative fitting along a regularization path |
| [`linear_model.ARDRegression`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression)([n_iter, tol, …]) | Bayesian ARD regression.                                     |
| [`linear_model.BayesianRidge`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge)([n_iter, tol, …]) | Bayesian ridge regression                                    |
| [`linear_model.SGDClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier)([loss, penalty, …]) | Linear classifiers (SVM, logistic regression, a.o.) with SGD training |
| [`linear_model.SGDRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor)([loss, penalty, …]) | Linear model fitted by minimizing a regularized empirical loss with SGD |



# [`sklearn.metrics`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics): Metrics

### Classification metrics

---

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`metrics.confusion_matrix`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix)(y_true, y_pred[, …]) | Compute confusion matrix to evaluate the accuracy of a classification |
| [`metrics.f1_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score)(y_true, y_pred[, labels, …]) | Compute the F1 score, also known as balanced F-score or F-measure |
| [`metrics.accuracy_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score)(y_true, y_pred[, …]) | Accuracy classification score.                               |
| [`metrics.auc`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc)(x, y[, reorder]) | Compute Area Under the Curve (AUC) using the trapezoidal rule |
| [`metrics.roc_curve`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve)(y_true, y_score[, …]) | Compute Receiver operating characteristic (ROC)              |
| [`metrics.roc_auc_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score)(y_true, y_score[, …]) | Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores. |
| [`metrics.recall_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score)(y_true, y_pred[, …]) | Compute the recall                                           |
| [`metrics.precision_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score)(y_true, y_pred[, …]) | Compute the precision                                        |
| [`metrics.precision_recall_curve`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve)(y_true, …) | Compute precision-recall pairs for different probability thresholds |
| [`metrics.average_precision_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score)(y_true, y_score) | Compute average precision (AP) from prediction scores        |



### Regression metrics

---

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`metrics.explained_variance_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score)(y_true, y_pred) | Explained variance regression score function                 |
| [`metrics.mean_absolute_error`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error)(y_true, y_pred) | Mean absolute error regression loss                          |
| [`metrics.mean_squared_error`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error)(y_true, y_pred[, …]) | Mean squared error regression loss                           |
| [`metrics.mean_squared_log_error`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error)(y_true, y_pred) | Mean squared logarithmic error regression loss               |
| [`metrics.median_absolute_error`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error)(y_true, y_pred) | Median absolute error regression loss                        |
| [`metrics.r2_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score)(y_true, y_pred[, …]) | R^2 (coefficient of determination) regression score function. |



# [`sklearn.model_selection`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection): Model Selection

### Splitter Functions

---

| 方法                                                         | 介绍                                                        |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| [`model_selection.check_cv`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv)([cv, y, classifier]) | Input checker utility for building a cross-validator        |
| [`model_selection.train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split)(*arrays, …) | Split arrays or matrices into random train and test subsets |



### Hyper-parameter optimizers

---

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`model_selection.GridSearchCV`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV)(estimator, …) | Exhaustive search over specified parameter values for an estimator. |



### Model validation

---

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`model_selection.cross_val_predict`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict)(estimator, X) | Generate cross-validated estimates for each input data point |
| [`model_selection.cross_val_score`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score)(estimator, X) | Evaluate a score by cross-validation                         |
| [`model_selection.cross_validate`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate)(estimator, X) | Evaluate metric(s) by cross-validation and also record fit/score times. |
| [`model_selection.learning_curve`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve)(estimator, X, y) | Learning curve.                                              |



# [`sklearn.multiclass`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.multiclass): Multiclass and multilabel classification

### Multiclass and multilabel classification strategies

---

| 方法                                                         | 介绍                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| [`multiclass.OneVsRestClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier)(estimator[, …]) | One-vs-the-rest (OvR) multiclass/multilabel strategy |
| [`multiclass.OneVsOneClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier)(estimator[, …]) | One-vs-one multiclass strategy                       |



# [`sklearn.neighbors`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors): Nearest Neighbors

**The [`sklearn.neighbors`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors) module implements the k-nearest neighbors algorithm.**

| 方法                                                         | 介绍                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [`neighbors.KNeighborsClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)([…]) | Classifier implementing the k-nearest neighbors vote. |
| [`neighbors.KNeighborsRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor)([n_neighbors, …]) | Regression based on k-nearest neighbors.              |



#　[`sklearn.pipeline`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.pipeline): Pipeline

**The [`sklearn.pipeline`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.pipeline) module implements utilities to build a composite estimator, as a chain of transforms and estimators.**

| 方法                                                         | 介绍                                            |
| ------------------------------------------------------------ | ----------------------------------------------- |
| [`pipeline.Pipeline`](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline)(steps[, memory]) | Pipeline of transforms with a final estimator.  |
| [`pipeline.make_pipeline`](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline)(*steps, **kwargs) | Construct a Pipeline from the given estimators. |



# [`sklearn.preprocessing`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing): Preprocessing and Normalization

**The [`sklearn.preprocessing`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing) module includes scaling, centering, normalization, binarization and imputation methods.**

| 方法                                                         | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`preprocessing.MinMaxScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler)([feature_range, copy]) | Transforms features by scaling each feature to a given range. |
| [`preprocessing.StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler)([copy, …]) | Standardize features by removing the mean and scaling to unit variance |
| [`preprocessing.scale`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale)(X[, axis, with_mean, …]) | Standardize a dataset along any axis                         |



# [`sklearn.svm`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm): Support Vector Machines

**The [`sklearn.svm`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm) module includes Support Vector Machine algorithms.**

| 方法                                                         | 介绍                                  |
| ------------------------------------------------------------ | ------------------------------------- |
| [`svm.LinearSVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC)([penalty, loss, dual, tol, C, …]) | Linear Support Vector Classification. |
| [`svm.LinearSVR`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR)([epsilon, tol, C, loss, …]) | Linear Support Vector Regression.     |
| [`svm.SVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC)([C, kernel, degree, gamma, coef0, …]) | C-Support Vector Classification.      |
| [`svm.SVR`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR)([kernel, degree, gamma, coef0, tol, …]) | Epsilon-Support Vector Regression.    |



# [`sklearn.tree`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree): Decision Trees

**The [`sklearn.tree`](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree) module includes decision tree-based models for classification and regression.**

| 方法                                                         | 介绍                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| [`tree.DecisionTreeClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)([criterion, …]) | A decision tree classifier.              |
| [`tree.DecisionTreeRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor)([criterion, …]) | A decision tree regressor.               |
| [`tree.ExtraTreeClassifier`](http://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier)([criterion, …]) | An extremely randomized tree classifier. |
| [`tree.ExtraTreeRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor)([criterion, …]) | An extremely randomized tree regressor.  |