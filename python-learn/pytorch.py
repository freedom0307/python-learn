# -*- coding = utf-8 -*-
# @Time:2023/1/28 21:50
# @Author:youran
# @File:pytorch.py

import pandas as pd
from torch.utils.tensorboard import SummaryWriter

file_path=r'F:\智能路由部\件量预测\order_analysis_detail.xlsx'
df=pd.read_excel(file_path)

#获取行数
rows=len(df)
print(len(df))

order_score=df['order_score'].values
print(order_score)

accuray=df['准确率'].values
print(accuray)

writer=SummaryWriter("logs")

for i in range(200):
    writer.add_scalar("order_score",order_score[i],i)
    writer.add_scalar("accuray",accuray[i],i)
writer.close()
