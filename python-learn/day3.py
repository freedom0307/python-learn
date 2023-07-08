# -*- coding = utf-8 -*-
# @Time:2022/12/19 23:26
# @Author:youran
# @File:day3.py


for i in range(5):
    print(i)

for i in range(0,10,3):
    print(i)

name="chengdu"
for i in name:
    print(i)

a=["aa","bb","cc","dd"]
for i in range(len(a)):
    print(a[i])

i=0
while i<5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i=i+1

count=0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于或等于5")