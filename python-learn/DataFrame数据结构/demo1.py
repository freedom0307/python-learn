# -*- coding = utf-8 -*-
# @Time:2023/6/4 21:59
# @Author:youran
# @File:demo1.py

import pandas as pd

#1、读取文件
df=pd.read_csv("WorldCupMatches.csv")
# print(df)

#2、转置
tdf=df.T
# print(tdf)

#3、求索引
index=df.index
print(index)
for itm in index:
    print(itm)

#4、axes 轴属性，返回行与列
dfi=df.axes
print(dfi)
for elt in dfi[1]:
    print(elt)

#5、属性列名表
print(df.columns)
print(df.columns[0:3])

#6、属性，返回行列元组
print(df.shape)

#7、value属性，去掉标签，只要数据
print(df.values)

#8、head返回前n行，tail返回后n行
print(df.head(2))
print(df.tail(2))


