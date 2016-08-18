# Задача: перемножьте две матрицы!

# На вход программе подаются две матрицы, каждая в следующем формате: на первой строке два целых
# положительных числа nn и mm, разделенных пробелом - размерность матрицы. В следующей строке находится
# n⋅mn⋅m целых чисел, разделенных пробелами - элементы матрицы. Подразумевается, что матрица заполняется
# построчно, то есть первые mm чисел - первый ряд матрицы, числа от m+1m+1 до 2⋅m2⋅m - второй, и т.д.

# Напечатайте произведение матриц XYTXYT, если они имеют подходящую форму, или строку 
# "matrix shapes do not match", если формы матриц не совпадают должным образом.

import sys
sys.stdin = open('01.txt', 'r')

import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)

y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

if x_shape[1] != y_shape[1]:
  print('matrix shapes do not match')
else:
  print(X.dot(Y.T))