from sklearn.model_selection import GridSearchCV
pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('randomforestclassifier', RandomForestClassifier())
])
