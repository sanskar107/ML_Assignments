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
print data
print X