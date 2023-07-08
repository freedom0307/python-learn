# -*- coding = utf-8 -*-
# @Time:2022/12/19 23:51
# @Author:youran
# @File:day4.py

from icecream import ic

word='字符串'
sentence="这是一个句子"
paragraph="""
    这是一个
       段落
"""

print(word)
print(sentence)
print(paragraph)

my_str="I'm a student"

my_str='I\'m a student'

my_str="Json said \"I like you \""

str="chengdu"
ic(str[0])
#[起始位置 :结束的位置:步进值]
#左边的下标包括，右边下标不包括
ic(str[0:5])
ic(str[1:7:2])

#直接到最后一个
ic(str[:5])
ic(str[5:])

#字符串连接，可以使用加好
ic(str+",你好")

#多次显示一个字符
ic(str*3)

#r的作用，让转义功能消失，显示原始字符串
ic("hello\nchengdu")
ic(r"hello\nchengdu")



