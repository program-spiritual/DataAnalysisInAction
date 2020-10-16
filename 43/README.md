---
第一点: 进一步了解 CNN 网络
第二点: 初步了解 LeNet 和 AlexNet
第三点: 对常用的深度学习框架进行对比
第四点: 使用 Keras 这个深度学习框架编写代码
---

43丨深度学习（下）：如何用Keras搭建深度学习网络做手写数字识别？

## 理解卷积的作用
### CNN 网络结构

* 卷积层
* 池化层
* 全连接层

### 什么是卷积？

假设有下面的一张图

![](https://static001.geekbang.org/resource/image/9d/cf/9d1bb65b30517775b632c10c1cb1c0cf.jpg)

1. 翻转矩阵180度

> 至于为什么，客官请看社区的这篇文章: [链接1][]

2. 卷积运算

![](https://static001.geekbang.org/resource/image/90/11/90a3bbabba732a2a7ad97a24f3587411.jpg)

3. 重复第二步骤 得到结果

![](https://static001.geekbang.org/resource/image/b8/6c/b824778383e3a898fe2399fb2eb8846c.jpg)

使用代码进行总结

[点我](demo.py)

```python
# coding=utf-8

import pylab
import numpy as np
from scipy import signal

# 设置原图像
img = np.array([[10, 10, 10, 10, 10],
                [10, 5, 5, 5, 10],
                [10, 5, 5, 5, 10],
                [10, 5, 5, 5, 10],
                [10, 10, 10, 10, 10]])
# 设置卷积核
fil = np.array([[-1, -1, 0],
                [-1, 0, 1],
                [0, 1, 1]])
# 对原图像进行卷积操作
res = signal.convolve2d(img, fil, mode='valid')
# 输出卷积后的结果
print(res)

'''output
[[ 15  10   0]
 [ 10   0 -10]
 [  0 -10 -15]]
'''

```

4. 图像卷积

[代码](demo1.py)

```python
# coding=utf-8
import matplotlib

matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
from scipy import signal

# 读取灰度图像
img = cv2.imread("haibao.jpeg", 0)
# 显示灰度图像
plt.imshow(img, cmap="gray")
pylab.show()
# 设置卷积核
fil = np.array(
  [
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
  ]
)
# 卷积操作
res = signal.convolve2d(img, fil, mode='valid')
print(res)
# 显示卷积后的图片
plt.imshow(res, cmap="gray")
pylab.show()

```

效果：

![](WX20190322-184344@2x.png)

![](WX20190322-194910@2x.png)

实际上每个卷积都是一种滤波器 筛选符合条件的部分 类似特征提取

卷积层可以有多个卷积核 例如第一层含有6个可以提取6个特征 得到6个特征图

## 特征函数的作用

卷积操作的下一步， 回归函数 `Sigmoid` 在机器学习中有广泛的应用

`tanh`、`ReLU` 都是常用的激活函数。

## 池化层的作用

- 位置： 通常位于两个卷积层之间
- 作用： 对神经元的数据做降维处理
- 目的： 降低整体计算量


tanh、ReLU 都是常用的激活函数。

## 全连接层的作用

将前面一层的输出结果与当前层的每个神经元都进行了连接

计算出来的特征 -> 分类器

比如 `Softmax` 分类器。在深度学习中，`Softmax`比较实用

## `LeNet` 和 `AlexNet` 网络

通常我们可以使用多个卷积层和池化层，最后再连接一个或者多个全...
LeNet 提出于 1986 年，是最早用于数字识别的 CN...

AlexNet 在 LeNet 的基础上做了改进，提出了更深...

## 常用的深度学习框架对比

.![](https://static001.geekbang.org/resource/image/ea/67/ea523df67c73d19732df1d172b30fd67.png)

## 用 `Keras` 做 `Mnist` 手写数字识别
使用 `Keras` 之前，我们需要安装相应的工具包

`Keras` 需要用 `tensorflow` 或者 `theano` 作为后端

### 创建蓄贯模型

```python
from keras.models import Sequential
model = Sequential()


```
### 创建二维卷积层

使用 `Conv2D(filters, kernel_size,activation=None)` 进行创建

`filters` 代表卷积核的数量

`kernel_size` 代表卷积核的宽度和长度

`activation` 代表激活函数

是第一个卷积层，我们还需要提供 `input_shape` 参数

### 对 `2D` 信号做最大池化层

MaxPooling2D(pool_size=(2, 2))...
`pool_size` 代表下采样因子
### 创建 Flatten 层

使用 `Flatten()` 创建

### 创建全连接层

使用 Dense(units, activation=Non...

model.compile(loss, optimizer=‘adam’, metrics=[‘accuracy’]) 来完成损失函数和优化器的

### 示例代码

 [点我](demo3.py)
 
 ```python
# coding=utf-8
# 使用 LeNet 模型对 Mnist 手写数字进行识别
import keras
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential

# 数据加载
(train_x, train_y), (test_x, test_y) = mnist.load_data()
# 输入数据为 mnist 数据集
train_x = train_x.reshape(train_x.shape[0], 28, 28, 1)
test_x = test_x.reshape(test_x.shape[0], 28, 28, 1)
train_x = train_x / 255
test_x = test_x / 255
train_y = keras.utils.to_categorical(train_y, 10)
test_y = keras.utils.to_categorical(test_y, 10)
# 创建序贯模型
model = Sequential()
# 第一层卷积层：6 个卷积核，大小为 5∗5, relu 激活函数
model.add(Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
# 第二层池化层：最大池化
model.add(MaxPooling2D(pool_size=(2, 2)))
# 第三层卷积层：16 个卷积核，大小为 5*5，relu 激活函数
model.add(Conv2D(16, kernel_size=(5, 5), activation='relu'))
# 第二层池化层：最大池化
model.add(MaxPooling2D(pool_size=(2, 2)))
# 将参数进行扁平化，在 LeNet5 中称之为卷积层，实际上这一层是一维向量，和全连接层一样
model.add(Flatten())
model.add(Dense(120, activation='relu'))
# 全连接层，输出节点个数为 84 个
model.add(Dense(84, activation='relu'))
# 输出层 用 softmax 激活函数计算分类概率
model.add(Dense(10, activation='softmax'))
# 设置损失函数和优化器配置
model.compile(loss=keras.metrics.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])
# 传入训练数据进行训练
model.fit(train_x, train_y, batch_size=128, epochs=2, verbose=1, validation_data=(test_x, test_y))
# 对结果进行评估
score = model.evaluate(test_x, test_y)
print('误差:%0.4lf' % score[0])
print('准确率:', score[1])


'''output
Using TensorFlow backend.
Downloading data from https://s3.amazonaws.com/img-datasets/mnist.npz
11493376/11490434 [==============================] - 4s 0us/step
WARNING:tensorflow:From /Users/huhongyun/PythonProjects/geekTimeDataAnalysisInAction/.venv/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
WARNING:tensorflow:From /Users/huhongyun/PythonProjects/geekTimeDataAnalysisInAction/.venv/lib/python3.6/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.cast instead.
Train on 60000 samples, validate on 10000 samples
Epoch 1/2
2019-03-22 20:42:43.262460: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
60000/60000 [==============================] - 8s 141us/step - loss: 0.3482 - acc: 0.9021 - val_loss: 0.1100 - val_acc: 0.9673
Epoch 2/2
60000/60000 [==============================] - 8s 141us/step - loss: 0.1022 - acc: 0.9685 - val_loss: 0.0715 - val_acc: 0.9777
10000/10000 [==============================] - 1s 72us/step
误差:0.0715
准确率: 0.9777
'''
```

## 总结

![](https://static001.geekbang.org/resource/image/43/39/431ccdf001d421b3810e03c9c598b539.png)

[链接1]: https://cloud.tencent.com/developer/article/1366358 "什么！卷积要旋转180度？！"
