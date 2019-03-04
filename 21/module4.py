# 多项式贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)