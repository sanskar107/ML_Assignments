# 16EE10041
# Sanskar Agrawal
# Assignment Number 2
# Compilation : python <program_name>

import numpy as np
import math

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def PrintTree(self):
		if(self.left):
			self.left.PrintTree()
		print self.data
		if(self.right):
			self.right.PrintTree()

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

def function(X, Y, marked):
	if(X.shape[1] == len(marked)):
		# print "All_Marked"
		return None
	flag_0 = flag_1 = 1
	for i in range(0, Y.shape[0]):
		if(Y[i] == 1):
			flag_0 = 0
		else:
			flag_1 = 0

	if(flag_0):
		# print "Pure negative"
		return Node(-1)
	if(flag_1):
		# print "Pure Positive"
		return Node(-2)
	E_class = 0.0
	p = n = 0.0
	for i in range(0, X.shape[0]):
		if(Y[i] == 1):
			p += 1
		else:
			n += 1
	E_class = entropy(p, n)
	# print("Class Entropy : ", E_class)
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
		# print gain
	# print "Max gain = ", max_gain
	# print "Max gain_attr = ", max_gain_attr
	marked.append(max_gain_attr)
	root = Node(max_gain_attr)
	X_pos = []
	X_neg = []
	Y_pos = []
	Y_neg = []
	for i in range(0, X.shape[0]):
		if(X[i][max_gain_attr] == 0):
			X_neg.append(X[i])
			Y_neg.append(Y[i])
		else:
			X_pos.append(X[i])
			Y_pos.append(Y[i])
	X_neg = np.reshape(np.array(X_neg), (-1, X.shape[1]))
	X_pos = np.reshape(np.array(X_pos), (-1, X.shape[1]))
	Y_neg = np.array(Y_neg)
	Y_pos = np.array(Y_pos)
	root.left = function(X_neg, Y_neg, marked)
	root.right = function(X_pos, Y_pos, marked)

	return root

# print Y.shape
# print X.shape
root = function(X, Y, [])
test = np.genfromtxt('test2.csv', delimiter = ',')
ans = []
for i in range(0, test.shape[0]):
	temp = root
	while(temp):
		if(temp.data == -1):
			ans.append(0)
			break
		if(temp.data == -2):
			ans.append(1)
			break
		temp = temp.left if test[i][temp.data] == 0 else temp.right
file = open('16EE10041_2.out', 'w')
for i in ans:
	file.write(str(i) + ' ')
file.close()
file = open('16EE10041_2.out', 'r')
data = file.read()
print data