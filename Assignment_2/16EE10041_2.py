# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def PrintTree(self):
		print(self.data)


data = np.genfromtxt('data2.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1]
n_features = X.shape[1]
mark = np.zeros([1, n_features], dtype = np.int32)
print data
print X

def function():
	for i in range(0, n_features):
		if(mark[i]):
			continue
