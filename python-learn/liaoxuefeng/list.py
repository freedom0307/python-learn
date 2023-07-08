# -*- coding = utf-8 -*-
# @Time:2023/4/16 21:36
# @Author:youran
# @File:list.py

from icecream import ic

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

ic(L)
#第一个元素
ic(L[0])
#最后一个元素
ic(L[-1])
#取前3个数据
ic(L[0:3])
#取后3个数
ic(L[-3:])
#隔一个取数,从左到右的参数分别是：开始的下标，结束的下标，步长
ic(L[0:4:2])

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

from collections.abc import Iterable

res= isinstance('abc',Iterable)
ic(res)

list1=list(range(1,11))
ic(list1)