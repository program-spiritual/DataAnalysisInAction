## 如何给毛不易的歌曲做词云展示

### 目标

1. 掌握词云分析工具
2. 掌握Python爬虫
3. 掌握Xpath工具

## 词云

词云 == 文字云

目的： 统计文本中高频出现的词 去掉重复常用词 将重要关键词进行可视化，方便文本分析者更快更好的了解文本的重点，同时具有美观度

## 工具

名称: `WordCloud`

安装： `pip install wordcloud`

[构造函数代码](./constructor.py) 

生成词云的方式

```python

# text 代表要分析的文本

wordcloud=generate(text)

```

保存图片的方式

```python

wordcloud.tofile('a.jpg')

```

可视化方式

[可视化代码](./demo1.py)


完整案例 

专栏前 15 节的标题进行词云可视化

[完整实例](demo2.py)

去掉停用词

[实例代码](demo3.py)


## 给毛不易的歌词制作词云

1 具体步骤

![](https://static001.geekbang.org/resource/image/7c/97/7cff33b392cec653ca2e68fbecd4ef97.jpg)

2. [实例代码](demo4.py)

## 总结

![](https://static001.geekbang.org/resource/image/0c/6d/0cbc5f3e4ecd41af9a872fd9b4aed06d.png)



