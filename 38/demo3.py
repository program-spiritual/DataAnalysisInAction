# 去掉停用词
def remove_stop_words(f):
     stop_words = ['学会', '就是', '什么']
     for stop_word in stop_words:
           f = f.replace(stop_word, '')
     return f
