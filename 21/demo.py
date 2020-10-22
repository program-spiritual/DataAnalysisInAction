# coding=utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()

documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)

print('不重复的词:', tfidf_vec.get_feature_names())

print('每个单词的 ID:', tfidf_vec.vocabulary_)


print('每个单词的 tfidf 值:', tfidf_matrix.toarray())
