# -*- coding = utf-8 -*-
# @Time:2023/5/30 21:29
# @Author:youran
# @File:WorldCupMatches.py


import csv

#打开文件
with open("WorldCupMatches.csv",'r',encoding='UTF-8') as f:
    reader=csv.DictReader(f)
    home_team_goals=[]
    away_team_goals=[]
    for row in reader:
        home_team_goals.append(int(float(row['Home Team Goals'])))
        away_team_goals.append(int(float(row['Away Team Goals'])))

def quartile_value(list1,num):
    #先个序列排序
    list1.sort()
    location=num* (1+len(list1))/4
    location_int = int(location)
    w = location-location_int
    quartile = list1[location_int - 1] * (1 - w) + list1[location_int] * w
    return quartile

Q1=quartile_value(home_team_goals,1)
Q2=quartile_value(home_team_goals,2)
Q3=quartile_value(home_team_goals,3)

mean=sum(home_team_goals)/len(home_team_goals)
print("均值:{}".format(mean))

IQR=Q3-Q1

#内限
inner_outlier_low=Q1-1.5*IQR
inner_outlier_high=Q3+1.5*IQR

#外限
out_outlier_low=Q1-3*IQR
out_outlier_high=Q3+3*IQR

for score in home_team_goals:
    if out_outlier_low<score<inner_outlier_low or inner_outlier_high<score<out_outlier_high:
        print(score)

print("Q1:{}".format(Q1))
print("Q2:{}".format(Q2))
print("Q3:{}".format(Q3))

print("内限:{}和{}".format(inner_outlier_low,inner_outlier_high))
print("外限:{}和{}".format(out_outlier_low,out_outlier_high))

#绘制箱线图
from matplotlib import  pyplot as plt
plt.boxplot((home_team_goals,away_team_goals),labels=['Home Teams','Away Teams'])
plt.title('Goals for Home Teams and Away Teams in all FIFA World Cups')
plt.show()






