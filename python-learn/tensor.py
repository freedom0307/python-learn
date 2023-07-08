# -*- coding = utf-8 -*-
# @Time:2023/4/23 22:39
# @Author:youran
# @File:tensor.py
import torch

# torch.tensor([1.2, 3]).device
# torch.set_default_device('cuda')  # current device is 0
# torch.tensor([1.2, 3]).device
# torch.set_default_device('cuda:1')
# torch.tensor([1.2, 3]).device



# tensor1=torch.tensor([1.2, 3])
# print(tensor1.device)
# torch.cuda.set_device(0)
#
# tensor2=torch.tensor([1.2,3],device=torch.device('cuda'))
# print(tensor2.device)
#
# tensor3=torch.tensor([1.2,3],device=torch.device('cuda'))
# print(tensor3.device)

# device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# torch.backends.cudnn.benchmark=True
#
# #输出当前默认设备
# print(torch.tensor([1.2,3]).device)
# #将默认设备设置为cuda
# torch.cuda.set_device(1)
# #输出当前默认设备
# print(torch.tensor([1.2,3]).device)


# # Limit the precision of elements
# torch.set_printoptions(precision=2)
# torch.tensor([1.12345])
# # Limit the number of elements shown
# torch.set_printoptions(threshold=5)
# torch.arange(10)
# # Restore defaults
# torch.set_printoptions(profile='default')
# torch.tensor([1.12345])
# torch.arange(10)
#
#
# class A(object):
#     pass
#
# a=A()
# a.name='gaogao'
# print(a.name)

# class A(object):
#     def __init__(self,name):
#         self.name=name
#
# a=A('gaogao')
# print(a.name)


class A(object):

    def __init__(self, name):
        self.__name = name

    def print_score(self):
        print('%s: %s' % (self.__name))

a=A('gaogao')
a.print_score()