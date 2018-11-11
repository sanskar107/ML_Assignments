# 16EE10041
# Sanskar Agrawal
# Assignment Number 7
# Compilation : python <program_name>

import numpy as np
import random

def assign_parents(data, c_1, c_2):
	parent = []
	for i, row in enumerate(data):
		if(i == c_1):
			parent.append(c_1)
			continue
		if(i == c_2):
			parent.append(c_2)
			continue
		dist1 = np.linalg.norm(data[i] - data[c_1])
		dist2 = np.linalg.norm(data[i] - data[c_2])
		if(dist1 <= dist2):
			parent.append(c_1)
		else:
			parent.append(c_2)
	return parent


def find_centres(data, parents, c_1, c_2):
	data1 = []
	data2 = []
	for i, row in enumerate(data):
		if(parents[i] == c_1):
			data1.append(row)
		else:
			data2.append(row)
	data1 = np.array(data1)
	data2 = np.array(data2)
	avg1 = np.sum(data1, axis = 0, dtype = np.float64)/data1.shape[0]
	avg2 = np.sum(data2, axis = 0, dtype = np.float64)/data2.shape[0]
	# print avg1, avg2
	min_dist1 = 100000.0
	min_dist2 = 100000.0
	min_index1 = 0
	min_index2 = 0
	for i, row in enumerate(data):
		if(parents[i] == c_1):
			dist = np.linalg.norm(data[i] - avg1)
			if(dist < min_dist1):
				min_dist1 = dist
				min_index1 = i
		else:
			dist = np.linalg.norm(data[i] - avg2)
			if(dist < min_dist2):
				min_dist2 = dist
				min_index2 = i

	return min_index1, min_index2

data = np.genfromtxt('data7.csv', delimiter = ',')

c_1 = random.randint(0, data.shape[0] - 1)
c_2 = c_1
while(c_2 == c_1):
	c_2 = random.randint(0, data.shape[0] - 1)

# print data
parents = assign_parents(data, c_1, c_2)
# print "Initial : ", parents, c_1, c_2

num_iter = 10

for i in range(0, num_iter):
	c_1, c_2 = find_centres(data, parents, c_1, c_2)
	parents = assign_parents(data, c_1, c_2)
	# print parents, c_1, c_2

temp = parents[0]
ans = ''
for i in parents:
	if(i == temp):
		ans = ans + ' 1'
	else:
		ans = ans + ' 2'

print ans

file = open('16EE10041_7.out', 'w')
file.write(ans)
file.close()