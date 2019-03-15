wc = WordCloud(
  background_color='white',  # 设置背景颜色
  mask=backgroud_Image,  # 设置背景图片
  font_path='./SimHei.ttf',  # 设置字体，针对中文的情况需要设置中文字体，否则显示乱码
  max_words=100,  # 设置最大的字数
  stopwords=STOPWORDS,  # 设置停用词
  max_font_size=150,  # 设置字体最大值
  width=2000,  # 设置画布的宽度
  height=1200,  # 设置画布的高度
  random_state=30  # 设置多少种随机状态，即多少种颜色
)
