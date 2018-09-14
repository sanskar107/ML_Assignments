# 16EE10041
# Sanskar Agrawal
# Assignment Number 4
# Compilation : python <program_name>

import numpy as np
import math

data = np.genfromtxt('data4.csv', delimiter = ',', dtype = np.float32)

X = np.array(data[:, 0 : data.shape[1] - 1])
Y = np.array(data[:, data.shape[1] - 1])

def calc_dist(data):
	distance = []
	for i, row in enumerate(X):
		dist = 0.0
		for j in range(0, len(row)):
			dist += pow(row[j] - data[j], 2)
		dist = math.sqrt(dist)
		distance.append([dist, Y[i]])
	return distance

def KNN(distance):
	distance.sort()
	count_0 = 0
	for i in range(0, 5):
		if(distance[i][1] == 0):
			count_0 += 1

	if(count_0 > 2):
		return '0 '
	else:
		return '1 '

if __name__ == '__main__':
	test_data = np.genfromtxt('test4.csv', delimiter = ',', dtype = np.float32)
	ans = ''
	for data in test_data:
		distance = calc_dist(data)
		ans = ans + KNN(distance)
	print ans
	file = open('16EE10041_4.out', 'w')
	file.write(ans)
	file.close()