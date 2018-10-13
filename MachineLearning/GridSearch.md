
# Example
```
param_grid = [
    {
        "weights" : ["uniform"], # 键 ： 列表
        "n_neighbors" : [i for i in range(1,11)],
    },
    {
        "weights" : ["distance"],
        "n_neighbors" : [i for i in range(1,11)],
        "p" :[ i for i in range(1,5)]
    }
]

KNN_clf = KNC()

from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(KNN_clf,param_grid);

%%time
grid_search.fit(X_train,y_train);

grid_search.best_estimator_    #得到最佳的分类器的数值
<<<KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=3, p=3,weights='distance')
grid_search.best_score_ 
<<<0.9853862212943633
grid_search.best_params_
<<< {'n_neighbors': 3, 'p': 3, 'weights': 'distance'}
```
