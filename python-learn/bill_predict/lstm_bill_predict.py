import torch
import torch.nn as nn
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from icecream import ic

print(sns.utils.get_data_home())


#通过git实时下载速度太慢，将文件下载下来放在本地
file_path = r'F:\学习\练习项目\AI项目\python-learn\广州-佛山.xlsx'
bill_data = pd.read_excel(file_path)
print(bill_data.size)
print(bill_data.shape)

#绘图参数设置
fig_size=plt.rcParams["figure.figsize"]
fig_size[0]=15
fig_size[1]=5
plt.rcParams["figure.figsize"]=fig_size

plt.title("Day vs Bill Total")
plt.ylabel('Total Bills')
plt.xlabel('Day')
plt.grid(True)
plt.autoscale(axis='x',tight=True)
plt.plot(bill_data['total'])  # 只画一列
plt.show()

print(bill_data.columns)

#将passengers转换为float类型
all_data=bill_data["total"].values.astype(float)
print(all_data)

test_data_size=12

train_data=all_data[:-test_data_size]
test_data=all_data[-test_data_size:]

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler(feature_range=(-1,1))
train_data_normalized=scaler.fit_transform(train_data.reshape(-1,1))

#查看标准化的数据
print(train_data_normalized[:5])
print(train_data_normalized[-5:])

#数据类型转换numpy转换为火炬张量
train_data_normalized=torch.FloatTensor(train_data_normalized).view(-1)


# 每次训练的个数
train_window=30

def create_inout_sequences(input_data,tw):
    inout_seq=[]
    L=len(input_data)
    for i in range(L-tw):
        train_seq=input_data[i:i+tw]
        train_label=input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq,train_label))
    return inout_seq

train_inout_seq=create_inout_sequences(train_data_normalized,train_window)

print(train_inout_seq[:5])

#创建【LSTM】 模型
class LSTM(nn.Module):
    def __init__(self,input_size=1,hidden_layer_size=100,output_size=1):
        super().__init__()
        self.hidden_layer_size=hidden_layer_size
        self.lstm=nn.LSTM(input_size,hidden_layer_size)
        self.linear=nn.Linear(hidden_layer_size,output_size)
        self.hidden_cell=(torch.zeros(1,1,self.hidden_layer_size),
                          torch.zeros(1,1,self.hidden_layer_size))

    def forward(self,input_seq):
        lstm_out,self.hidden_cell=self.lstm(input_seq.view(len(input_seq),1,-1),self.hidden_cell)
        predictionis=self.linear(lstm_out.view(len(input_seq),-1))
        return predictionis[-1]

model=LSTM()

loss_function=nn.MSELoss()
optimizer=torch.optim.Adam(model.parameters(),lr=0.001)
print(model)

#训练模型
epochs=150
for i in range(epochs):
    for seq,labels in train_inout_seq:
        optimizer.zero_grad()
        model.hidden_cell=(torch.zeros(1,1,model.hidden_layer_size),
                           torch.zeros(1,1,model.hidden_layer_size))
        y_pred=model(seq)

        single_loss=loss_function(y_pred,labels)
        single_loss.backward()
        optimizer.step()

    if i%25==1:
        print(f'epoch:{i:3} loss:{single_loss.item():10.8f}')

print(f'epoch:{i:3} loss:{single_loss.item():10.10f}')


fut_pred=30
test_inputs=train_data_normalized[-train_window:].tolist()
print(test_inputs)
#用模型执行预测
model.eval()

for i in range(fut_pred):
    seq=torch.FloatTensor(test_inputs[-train_window:])
    with torch.no_grad():
        model.hidden=(torch.zeros(1,1,model.hidden_layer_size),
                      torch.zeros(1,1,model.hidden_layer_size))
        test_inputs.append(model(seq).item())

print(test_inputs[fut_pred])

#反归一化
actual_predictions=scaler.inverse_transform(np.asarray(test_inputs[train_window:]).reshape(-1,1))
print(actual_predictions)

#绘制预测值和实际值得对比
x=np.arange(211,241,1)
print(x)

plt.title("Day vs Bill")
plt.ylabel('Total Bills')
plt.grid(True)
plt.autoscale(axis='x',tight=True)
plt.plot(bill_data['total'])
plt.plot(x,actual_predictions)
plt.show()

#将要对比的范围放大
plt.title("Day vs bills")
plt.ylabel("Total Bills")
plt.grid(True)
plt.autoscale(axis='x',tight=True)
plt.plot(bill_data['total'][-train_window:])
plt.plot(x,actual_predictions)
plt.show()