## 使用工具 

```python
itemsets, rules = apriori(data, min_support,  min_confidence)

```

- data 
  - 数据集
- list 
  - 数组
- min_support
  - 最小支持度
  

## 挖掘频繁集和规则 ` demo ` 上一讲的超市案例

[代码](demo1.py)

## 导演挖掘演员

流程

1. https://movie.douban.com/
2. 输入 名称
3.  [抓取数据代码](demo2.py)

```python
# -*- coding: utf-8 -*-
from efficient_apriori import apriori
from lxml import etree
import time
from selenium import webdriver
import csv

driver = webdriver.Chrome()
# 设置想要下载的导演 数据集
director = u'宁浩'
# 写 CSV 文件
file_name = './' + director + '.csv'
base_url = 'https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start='
out = open(file_name, 'w', newline='', encoding='utf-8-sig')
csv_write = csv.writer(out, dialect='excel')


# 下载指定页面的数据
def download(request_url):
  driver.get(request_url)
  time.sleep(1)
  html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
  html = etree.HTML(html)
  # 设置电影名称，导演演员 的 XPATH
  movie_lists = html.xpath(
    "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
  name_lists = html.xpath(
    "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
  # 获取返回的数据个数
  num = len(movie_lists)
  if num > 15:  # 第一页会有 16 条数据
    # 默认第一个不是，所以需要去掉
    movie_lists = movie_lists[1:]
    name_lists = name_lists[1:]
  for (movie, name_list) in zip(movie_lists, name_lists):
    # 会存在数据为空的情况
    if name_list.text is None:
      continue
    # 显示下演员名称
    print(name_list.text)
    names = name_list.text.split('/')
    # 判断导演是否为指定的 director
    if names[0].strip() == director:
      # 将第一个字段设置为电影名称
      names[0] = movie.text
      csv_write.writerow(names)
  print('OK')  # 代表这页数据下载成功
  if num >= 15:
    # 继续下一页
    return True
  else:
    # 没有下一页
    return False


# 开始的 ID 为 0，每页增加 15
start = 0
while start < 10000:  # 最多抽取 1 万部电影
  request_url = base_url + str(start)
  # 下载数据，并返回是否有下一页
  flag = download(request_url)
  if flag:
    start = start + 15
  else:
    break
out.close()
print('finished')

```
4. [挖掘](demo3.py)

```python
# -*- coding: utf-8 -*-
from efficient_apriori import apriori
import csv
director = u'宁浩'
file_name = './'+director+'.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
# 数据加载
data = []
for names in lists:
     name_new = []
     for name in names:
           # 去掉演员数据中的空格
           name_new.append(name.strip())
     data.append(name_new[1:])
# 挖掘频繁项集和关联规则
itemsets, rules = apriori(data, min_support=0.5,  min_confidence=1)
print(itemsets)
'''itemsets
{1: {('徐峥',): 5, ('黄渤',): 6}, 2: {('徐峥', '黄渤'): 5}}
'''
print('\r')
print(rules)

'''rules
[{徐峥} -> {黄渤}]
'''

```
5. 总结

![总结](data_dig.png)

 