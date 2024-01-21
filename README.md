#  《极客时间数据分析实战45讲-详细笔记》

> 亲爱的朋友们，现在 AI 时代已经到来，我的项目维护虽然在继续，但是无法同步和大家分享知识，最近我已经注册了微信订阅号，希望看到的朋友互相通知一下： 微信公众号：编程悟道


[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)

## 博客 BLog

nodejs7.com

## 版本 2.3.1

![](img/DataAnalysisInAction-snap.png)

[在线文档](https://xiaomiwujiecao.github.io/DataAnalysisInAction)

## 代码克隆出错

```bash
// Skip smudge - We'll download binary files later in a faster batch
git lfs install --skip-smudge

// Do git clone here
git clone ...

// Fetch all the binary files in the new clone
git lfs pull

// Reinstate smudge
git lfs install --force
```

## 前言

### 工欲善其事必先利其器

Windows平台开发如何能够更快捷，更舒适，请 Windows 的看官务必读一下这篇：

[windows 流畅开发准备工作](https://ai.nodejs7.com/2020/01/14/118.html)

### 环境及配置问题

-  常见问题在本项目的 `Issues` 中，其他按住不表，如果存在疑问，请在Issues中添加新的 `Issue`

-  配置清华大学 `pipenv` 源的方法请 [点我](https://github.com/xiaomiwujiecao/DataAnalysisInAction/issues/9)

-  所有代码 依赖包 请结合 `pipenv` 和  `pyenv`  运行 ， 如果包含以上环境 请直接运行 `pipenv install`  安装所有依赖 ，依赖包已包含在 `Pipfile`

> 注意： 本项目仅限于学习

### 问题讨论：

1. [问题讨论区](https://github.com/xiaomiwujiecao/DataAnalysisInAction/issues/14)
2. [疑难杂症](https://ai.nodejs7.com/category/default/)


## 致谢

感谢阁下的star，感谢关注此项目！

## 数据集合收集

数据集合收集正在进行中，参见：[python 数据集收集与整理](https://github.com/xiaomiwujiecao/pythonDataSetCollection)

## 目录

### (🆕更新至第 `46` 讲)  *已完结*

1. 配置镜像源为 `清华大学` 镜像源
2. 项目 `pyenv` 依赖为 `Python 3.6.7`
3. 如果需要重新安装依赖 请删除项目根路径下的 `.venv` 目录 和 `Pipfile.lock`文件

## 知识体系

![知识体系.png](https://static.nodejs7.com/2020/01/798357214.png)

### 目录

-  **基础与算法**
    - [01丨 数据分析全景图及修炼指南（笔记）](./01/README.md)
    - [02丨 学习数据挖掘的最佳路径是什么?（笔记）](./02/README.md)
    - [03丨 PYTHON基础语法?（习题）](./03/README.md)
    - [04丨 Numpy（笔记）](./04/README.md)
    - [05丨 Pandas（代码）](./05/README.md)
    - [11丨 数据清洗（部分代码）](./11/README.md)
    - [14丨 数据可视化）](./14/README.md)
    - [15丨 一次学会Python数据可视化的10种技能](./15/README.md)
    - [16-17丨 决策树](./16-17/README.md)
    - [18丨 分类回归树](./18/README.md)
    - [19丨 泰坦尼克号生存预测](./19/README.md)
    - [20丨 -朴素贝叶斯(上)](./20/README.md)
    - [21丨 -朴素贝叶斯(下)](./21/README.md)
    - [22丨 -SVM(上)](./22/README.md)
    - [23丨 -SVM(下) 如何进行乳腺癌检测](./23/README.md)
    - [24丨 -KNN(上)](./24/README.md)
    - [25丨 -KNN(下) 如何识别手写数字](./25/README.md)
    - [26丨 K-Means(上) 如何给20支亚洲球队做聚类？](./26/README.md)
    - [27丨 K-Means(下) 如何使用K-Means对图像进行分割？](./27/README.md)
    - [28丨 EM (上) 如何将一份菜等分给两个人？](./28/README.md)
    - [29丨 EM (下) 用EM算法对王者荣耀英雄进行划分](./29/README.md)
    - [30丨 关联挖掘 (上) 如何用Apriori发现用户购物规则？](./30/README.md)
    - [31丨 关联挖掘 (下) 导演如何选择演员？](./31/README.md)
    - [32丨 PageRank (上) 搞懂Google的PageRank算法](./32/README.md)
    - [33丨 PageRank (下) 分析希拉里邮件中的人物关系](./33/README.md)
    - [34丨 AdaBoost (上) 如何使用AdaBoost提升分类器性能？](./34/README.md)
    - [35丨 AdaBoost (下) 如何使用AdaBoost对房价进行预测？](./35/README.md)
- **场景实战**
    - [37丨 数据采集实战：如何自动化运营微博？](./37/README.md)
    - [38丨数据可视化实战：如何给毛不易的歌曲做词云展示？](./38/README.md)
    - [39丨数据挖掘实战（1）：信用卡违约率分析](./39/README.md)
    - [40丨数据挖掘实战（2）：信用卡诈骗分析](./40/README.md)
    - [41丨数据挖掘实战（3）：如何对比特币走势进行预测？](./41/README.md)
    - [42丨当我们谈深度学习的时候，我们都在谈什么？](./42/README.md)
    - [43丨深度学习（下）：如何用Keras搭建深度学习网络做手写数字识别？](./43/README.md)
    - [44丨如何培养你的数据分析思维？](./44/README.md)
    - [45丨求职简历中没有相关项目经验，怎么办？](./45/README.md)
    - [46丨课程推荐](./46/README.md)
## TODO

### 算法
- [x] 1.朴素贝叶斯分类
- [x] 2.SVM
- [x] 3.KNN
- [x] 4.K-Means
- [x] 5.EM 聚类
- [x] 6.关联规则挖掘
- [x] 7.PageRank
- [x] 8.AdaBoost
### 场景实战
- [x] 9.自动化运营微博
- [x] 10.毛不易歌词云
- [x] 11.信用卡违约率分析
- [x] 12.信用卡诈骗分析
- [x] 13.信用卡诈骗分析
- [x] 14.如何对比特币走势进行预测？
- [x] 15.我们谈深度学习的时候，我们都在谈什么？
- [x] 16.如何用Keras搭建深度学习网络做手写数字识别？
- [x] 17.最终章【送君千里终须一别】
- [x] 18.课程推荐




## 新项目通告

`github` 地址：[架构师的功夫](https://github.com/xiaomiwujiecao/KongFuOfArchitect)


## PS

2. 获取数据请自学Scrapy
3. 多多动手实践  

## python 环境

1. `pipenv`
2. `pyenv`

> 请读者自行百度并安装

## 引用内容版权声明
极客时间版权所有: https://time.geekbang.org/column/

Copyright (c) 2019 Copyright Holder All Rights Reserved.



