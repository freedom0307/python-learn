# -*- coding = utf-8 -*-
# @Time:2023/6/4 22:26
# @Author:youran
# @File:demo2.py

import pandas as pd
df=pd.read_csv("WorldCupMatches.csv")
df=df.head()

#行列操作

#1、选择列
print(df['City'])
print(type(df['City']))

#2、增加列
dfv=df.values
zf=[sum(dfv[i,6:8]) for i in range(dfv.shape[0])]
df['总分']=pd.Series(zf)
print(df)

#3、删除一列
del df['总分']
print(df)

#4、选择行函数
print(df.iloc[2])#输出第3行数据
print(df.iloc[2]["Home Team Name"])

#5、行切片
print(df[0:])

#6、添加行
# adf=pd.DataFrame([["网名","87"]],columns=["姓名","C"])
# df2=df.append(adf)

#7、删除行
df3=df.drop(0)
print(df3)
