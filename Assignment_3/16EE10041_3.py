# 16EE10041
# Sanskar Agrawal
# Assignment Number 3
# Compilation : python <program_name>

import numpy as np

data = np.genfromtxt('data3.csv', delimiter = ',', dtype = np.int32)

X = np.array(data[:, 0 : 8])
Y = np.array(data[:, 8])

Prob = np.ones([X.shape[1], 2, 2], dtype = np.float32)
Y_0 = 0
Y_1 = 0
for i in range(0, Y.shape[0]):
	if(Y[i] == 0):
		Y_0 += 1
	else:
		Y_1 += 1

for i in range(0, X.shape[1]):
	for j in range(0, X.shape[0]):
		if(X[j][i] == 0):
			if(Y[j] == 0):
				Prob[i][0][0] += 1
			else:
				Prob[i][0][1] += 1
		else:
			if(Y[j] == 0):
				Prob[i][1][0] += 1
			else:
				Prob[i][1][1] += 1
	# print Prob
	Prob[i][0][0] /= (Y_0 + 2)
	Prob[i][0][1] /= (Y_1 + 2)
	Prob[i][1][0] /= (Y_0 + 2)
	Prob[i][1][1] /= (Y_1 + 2)

# print Prob

test = np.genfromtxt('test3.csv', delimiter = ',', dtype = np.int32)
test = np.array(test)
ans = ''
# print test.shape
for i in range(0, test.shape[0]):
	P_0 = Y_0
	P_1 = Y_1
	for j in range(0, test.shape[1]):
		# print test[i][j]
		m0 = Prob[j][test[i][j]][0]
		m1 = Prob[j][test[i][j]][1]
		P_0 = P_0*m0
		P_1 = P_1*m1
	# print P_0, P_1
	ans = ans + '0 ' if P_0 > P_1 else ans + '1 '
print ans

file = open('16EE10041_3.out', 'w')
file.write(ans)
file.close()
