# -*- coding = utf-8 -*-
# @Time:2023/2/28 20:42
# @Author:youran
# @File:predict_model.py

import matplotlib.pyplot as plt
import numpy as np

data=np.array(
    [[80,200],
     [95,230],
     [104,245],
     [112,247],
     [125,259],
     [135,262]]
)

X=data[:,0]
Y=data[:,1]
plt.scatter(X,Y,c="red")
plt.show()

import itertools
com_lists=list(itertools.combinations(data,2))
print(com_lists)

ms=[]
bs=[]
for comlist in com_lists:
    x1,y1=comlist[0]
    x2,y2=comlist[1]
    m=(y2-y1)/(x2-x1)
    b=y1-m*x1
    ms.append(m)
    bs.append(b)
print(ms)
print(bs)

m,b=np.mean(ms),np.mean(bs)

x=140
predict_fx=m*x+b
print(f'当x=140时,f(x)={predict_fx}')

