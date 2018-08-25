# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import math

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.parent = None
		self.data = data

	def PrintTree(self):
		print(self.data)

def entropy(m, n):
		if(m == 0 and n == 0):
			return 0
		elif(m == 0):
			return -(n/(m + n))*math.log((n/(m + n)), 2)
		elif(n == 0):
			return -(m/(m + n))*math.log((m/(m + n)), 2)
		else:
			return -(m/(m + n))*math.log((m/(m + n)), 2) -(n/(m + n))*math.log((n/(m + n)), 2)


data = np.genfromtxt('data2.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1]
n_features = X.shape[1]
mark = np.zeros([1, n_features], dtype = np.int32)
# print data
# print X

def function(X, Y, root):
	temp = root
	marked = []
	while(temp != None):
		marked.append(temp.data)
		temp = temp.parent
	E_class = 0.0
	p = n = 0.0
	for i in range(0, X.shape[0]):
		if(Y[i] == 1):
			p += 1
		else:
			n += 1
	E_class = entropy(p, n)
	print("Class Entropy : ", E_class)
	max_gain = -1
	max_gain_attr = -1
	for i in range(0, X.shape[1]):
		if(i in marked):
			continue
		p1 = n1 = p2 = n2 = pos = neg = 0.0
		for j in range(0, X.shape[0]):
			if(X[j][i] == 0):
				neg += 1
				if(Y[j] == 1):
					p1 += 1
				else:
					n1 += 1
			else:
				pos += 1
				if(Y[j] == 1):
					p2 += 1
				else:
					n2 += 1

		neg_entropy = entropy(p1, n1)
		pos_entropy = entropy(p2, n2)
		I_G = (pos/(pos + neg))*pos_entropy + (neg/(pos + neg))*neg_entropy
		gain = E_class - I_G
		if(max_gain < gain):
			max_gain = gain
			max_gain_attr = i
		print gain
		if(root == None):
			root = Node(max_gain_attr)
		else:
			


function(X, Y, None)
