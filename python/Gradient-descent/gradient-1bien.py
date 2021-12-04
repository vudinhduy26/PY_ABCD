# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:14:34 2021

@author: duy
"""

from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt

#để tính đạo hàm
def grad(x):
    return 2*x+ 5*np.cos(x)

#để tính giá trị của hàm số. 
#Hàm này không sử dụng trong thuật toán nhưng thường được dùng
#để kiểm tra việc tính đạo hàm của đúng không 
#hoặc để xem giá trị của hàm số có giảm theo mỗi
#vòng lặp hay không.
def cost(x):
    return x**2 + 5*np.sin(x)

#là phần chính thực hiện thuật toán Gradient Desent nêu phía trên. 
#Đầu vào của hàm số này là learning rate và điểm bắt đầu.
#Thuật toán dừng lại khi đạo hàm có độ lớn đủ nhỏ.
def myGD1(eta, x0): #eta : toc do hoc
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = myGD1(0.01, 5)
(x2, it2) = myGD1(0.5, 5)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))
print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], cost(x2[-1]), it2))