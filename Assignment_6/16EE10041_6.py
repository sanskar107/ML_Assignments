# 16EE10041
# Sanskar Agrawal
# Assignment Number 6
# Compilation : python <program_name>


import numpy as np

def sigmoid(arr):
	return (1/(1 + np.exp(-1*arr)))

def loss(y, y_train):
	y = y - y_train
	arr = abs(y)
	return arr.sum()/(arr.shape[0]*1.0)

data = np.genfromtxt('data6.csv', delimiter = ',')
X_train = data[:, 0 : 8]
Y_train = data[:, 8]
Y_train = Y_train.reshape(X_train.shape[0])

bias = np.array([[1] for i in range(0, X_train.shape[0])])
X_train = np.concatenate((bias, X_train), axis = 1)

data = np.genfromtxt('test6.csv', delimiter = ',')
X_test = data
bias = np.array([[1] for i in range(0, X_test.shape[0])])
X_test = np.concatenate((bias, X_test), axis = 1)

W = 0.01*np.random.randn(X_train.shape[1])
alpla = 0.2
# W = np.array(shape = (X_train.shape[0], 1), dtype = np.float64)

num_iter = 10
for epoch in range(0, num_iter):
	for i, X_row in enumerate(X_train):
		Y_row = Y_train[i]
		# print W
		h = np.matmul(X_row, W)
		y = sigmoid(h)
		g = alpla*(Y_row - y)*np.exp(-1*h)/(pow(1 + np.exp(-1*h), 2))
		delw = X_row*g
		W = W + delw
	y = sigmoid(np.matmul(X_train, W))
	# print("Epoch : ", epoch, " loss : ", loss(y, Y_train))



y_out = sigmoid(np.matmul(X_test, W))
y_out[y_out >= 0.5] = 1
y_out[y_out < 0.5] = 0
ans = ''
for i in range(0, y_out.shape[0]):
	ans = ans + str(int(y_out[i]))
	ans = ans + ' '
print ans

file = open('16EE10041_6.out', 'w')
file.write(ans)
file.close()