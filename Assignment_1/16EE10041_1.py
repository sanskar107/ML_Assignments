# 16EE10041
# Sanskar Agrawal
# Assignment Number 1
# Compilation : python <program_name> <filename>

import numpy as np
import sys

if(len(sys.argv) != 2):
	print("Please pass filename as a command line argument\nExiting!!!\n")
	exit()
data = np.genfromtxt(sys.argv[1], delimiter = ',', dtype = np.int32())

X = data[:, 0:data.shape[1] - 1]
Y = data[:, data.shape[1] - 1]

hyp = np.zeros(X.shape[1], dtype = np.int32)

pos_exm = []

for i in range(0, X.shape[0]):
	if(Y[i]):
		pos_exm.append(X[i])

pos_exm = np.array(pos_exm)

for i in range(0, pos_exm.shape[0]):
	# print hyp
	for j in range(0, hyp.shape[0]):
		if(hyp[j] == 0):
			if(pos_exm[i][j] == 1):
				hyp[j] = 1
			else:
				hyp[j] = -1
			continue
		if((hyp[j] == 1 and pos_exm[i][j] == 0) or (hyp[j] == -1 and pos_exm[i][j] == 1)):
			hyp[j] = 2
			continue

n = 0
ret = []
for i in range(0, hyp.shape[0]):
	if(hyp[i] == 2):
		continue
	n = n + 1

ret.append(n)
for i in range(0, hyp.shape[0]):
	if(hyp[i] == 2):
		continue
	ret.append(hyp[i]*(i + 1))

print ret