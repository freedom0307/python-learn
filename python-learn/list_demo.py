# -*- coding = utf-8 -*-
# @Time:2023/1/10 21:15
# @Author:youran
# @File:list_demo.py

from icecream import ic

#1、定义列表
#namelist=[]

print("定义列表")
namelist=["小王","小张"]
ic(namelist)

testlist=[1,"测试"]
ic(testlist)

#保持每个元素自身的类型
ic(type(testlist[0]))
ic(type(testlist[1]))

# 2、遍历列表
print("遍历列表")
for name in namelist:
    print(name)

##增加
print("增加")
#1、在末尾追加一个元素
namelist.append("小李")
print(namelist)

#2、追加列表，b列表将会当作一个元素追加在a的末尾
a=[1,2]
b=[3,4]
print(a.append(b))
#3、扩展，b的每一个元素逐一添加到a列表中
a.extend(b)
print(a)

#4、insert：指定下标位置插入元素
a=[0,1,2]
#1表示下标，3表示对象，把3插入下标为1的地方，其他元素依次往后移
a.insert(1,3)

##删除
print("删除")
movieName=["加勒比海盗","骇客帝国","第一滴血","指环王","速度与激情"]

#1、del 在指定的位置删除
del movieName[2] #制定位置删除一个元素

#2、pop 弹出末尾元素，相当于删除了最后一个元素
movieName.pop()

#3、remove 直接删除制定内容的元素
movieName.remove("指环王")


##修改
print("修改")
#1、直接制定下标修改
namelist[1]="小红"
print(namelist)

##查询，其实就是查询一个元素在不在列表中
print("查询")
#1、in 、not in 某个元素是不是在列表中
if "小红" in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")

#2、index 在制定的下标范围内查找元素，返回找到对应数据的下标
#注意，范围是左闭右开
mylist=["a","b","c","a","b"]
print(mylist.index("a",1,4))

##统计某个元素出现几次
print("统计")
print(mylist.count("c"))


##排序
print("排序")
a=[1,4,2,3]
#将列表所有元素反转
a.reverse()
print(a)

#升序排列
a.sort()
print(a)

#降序排列
a.sort(reverse=True)
print(a)

##二维数组
#有三个元素的空列表，每个元素是一个空列表
schoolNames=[[],[],[]]
#嵌套的列表，每个列表元素可以不一样
schoolNames=[["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山洞大学","中国海洋大学"]]

#访问第一个列表的内容
print(schoolNames[0])
#访问第一个列表的第一个元素
print(schoolNames[0][0])










