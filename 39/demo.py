# -*- coding: utf-8 -*-
# 使用 RandomForest 对 IRIS 数据集进行分类
# 利用 GridSearchCV 寻找最优参数
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
rf = RandomForestClassifier()
parameters = {"n_estimators": range(1,11)}
iris = load_iris()
# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)
# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)
print(" 最优分数： %.4lf" %clf.best_score_)
print(" 最优参数：", clf.best_params_)

'''output
 最优分数： 0.9600
 最优参数： {'n_estimators': 7}
'''
