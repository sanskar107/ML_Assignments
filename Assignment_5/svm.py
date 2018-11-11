import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

np.set_printoptions(threshold = 100000)


# data = np.genfromtxt('spambase/spambase.data', delimiter = ',', dtype = np.float64)
# X = data[:, 0 : 57]
# Y = data[:, 57]
# X = (X - np.mean(X, 0))/np.std(X, 0)

# arr = np.arange(X.shape[0])
# np.random.shuffle(arr)
# X = X[arr]
# Y = Y[arr]
# train_test_breakup = int(0.7*X.shape[0])

# X_train = X[0 : train_test_breakup]
# Y_train = Y[0 : train_test_breakup]

# X_test = X[train_test_breakup + 1 : X.shape[0]]
# Y_test = Y[train_test_breakup + 1 : X.shape[0]]

# np.save("X_train", X_train)
# np.save("Y_train", Y_train)
# np.save("X_test", X_test)
# np.save("Y_test", Y_test)

X_train = np.load("X_train.npy")
Y_train = np.load("Y_train.npy")
X_test = np.load("X_test.npy")
Y_test = np.load("Y_test.npy")

print X_train.shape, X_test.shape

test_accuracy = []
max_acc = 0.0
prec_recall = []
c_max = 0
C = [5*i for i in range(1, 20)]

for c in C:
	clf = SVC(gamma = 'auto', C = c, kernel = 'poly', degree = 2)
	clf.fit(X_train, Y_train)

	tp = tn = fp = fn = 0
	Y_pred = clf.predict(X_train)
	for i in range(0, Y_train.shape[0]):
		if(Y_train[i] == 1):
			if(Y_pred[i] == 1):
				tp += 1
			else:
				fn += 1
		else:
			if(Y_pred[i] == 0):
				tn += 1
			else:
				fp += 1

	# print("True Positive : ", tp)
	# print("True Negative : ", tn)
	# print("False Positive : ", fp)
	# print("False Negative : ", fn)
	print("C value = ", c)
	# print("Train Accuracy = ", ((tp + tn)*100.0)/(tp + tn + fp + fn))

	tp = tn = fp = fn = 0
	Y_pred = clf.predict(X_test)
	for i in range(0, Y_test.shape[0]):
		if(Y_test[i] == 1):
			if(Y_pred[i] == 1):
				tp += 1
			else:
				fn += 1
		else:
			if(Y_pred[i] == 0):
				tn += 1
			else:
				fp += 1

	if(((tp + tn)*100.0)/(tp + tn + fp + fn) > max_acc):
		max_acc = ((tp + tn)*100.0)/(tp + tn + fp + fn)
		c_max = c
		prec_recall = [tp, tn, fp, fn, ((tp)*100.0)/(tp + fp), ((tp)*100.0)/(tp + fn)]
	test_accuracy.append(((tp + tn)*100.0)/(tp + tn + fp + fn))


	# print("True Positive : ", tp)
	# print("True Negative : ", tn)
	# print("False Positive : ", fp)
	# print("False Negative : ", fn)

	# print("Test Accuracy = ", ((tp + tn)*100.0)/(tp + tn + fp + fn))
	# print("Test Precision = ", ((tp)*100.0)/(tp + fp))
	# print("Test Recall = ", ((tp)*100.0)/(tp + fn))

plt.plot(C, test_accuracy)
plt.xlabel("Value of C")
plt.ylabel("Test Accuracy")
print "Max Accuracy = ", max_acc
print "Max C = ", c_max
print prec_recall
plt.show()