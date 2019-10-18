import numpy as np

#HI MATT :)

#Finds the distance between X_train and X_test, returns an integer
def find_distance(X_train, X_test):

	#subracts the two arrays and squares them
	distance = np.power(X_train - X_test,2)

	#returns the sum of all of the values
	return sum(distance)

'''
Returns the prediction for X_test
Parameters:
	X_train -> np.array of the training data features
	Y_train -> np.array of the training data labels
	X_test -> np.array of the test data features
	K -> integer of the number of nearest neighbors
Returns:
	Prediction -> integer, either -1 or 1
'''
def KNN_prediction(X_train,Y_train,X_test,K):

	#creates empty distance array
	distance = []

	#Iterates through each training data sample
	for train in X_train:

		#finds the distance between the training data sample and the test sample and appends it to the distance list
		distance.append(find_distance(train, X_test))



	#sorts the distance array, from least to greatest, and returns/stores the indices as sorted_index
	sorted_index = np.argsort(distance)


	
	#creates an empty training_labels array
	training_labels = []


	for index in range(K):

		#Uses index to select the top K nearest neighbors and appends the corresponding labels to training_labels
		training_labels.append(Y_train[sorted_index[index],0])


	#Adds all of the labels
	prediction = sum(training_labels)

	#If the sums of the labels is negative, return -1
	if prediction < 0:

		return -1

	#else return 1
	else:

		return 1


'''
Returns the accuracy for the test data
Parameters:
	X_train -> np.array of the training data features
	Y_train -> np.array of the training data labels
	X_test -> np.array of the test data features
	Y_test -> np.array of the test data labels
	K -> integer of the number of nearest neighbors
Returns:
	Accuracy -> Float of the accuracy of the test data for K nearest neighbors
'''
def KNN_test(X_train,Y_train,X_test,Y_test,K):

	#creates Y_prediction list
	Y_prediction = []

	#Iterate through all of the test samples
	for test_sample in X_test:

		#append the prediction for test_sample to Y_prediction
		Y_prediction.append(KNN_prediction(X_train, Y_train, test_sample, K))


	#Initialize the count of corerct predictions to 0
	count_correct = 0	

	#Iterate through the indices of all the predictions
	for index in range(len(Y_prediction)):


		if Y_prediction[index] == Y_test[index]:

			#If the prediction is correct add 1 to count_correct
			count_correct += 1

	return count_correct/len(Y_prediction)


'''
Finds the K with the best accuracy
Parameters:
	X_train -> np.array of the training data features
	Y_train -> np.array of the training data labels
	X_val -> np.array of the validation data features
	Y_val -> np.array of the validation data labels
Returns:
	Best K Value -> Integer of the K-value with the highest accuracy
'''
def choose_K(X_train,Y_train,X_val,Y_val):

	#Initalized the best_K_value and best_accuracy as 0
	best_K_value = 0
	best_accuracy = 0

	#Interate through the range of the training data samples
	for K_value in range(len(X_train)):

		#If the K_value is not even, find the accuracy for the K_value
		if not (K_value % 2) == 0:
			
			#Find the accuracy for the new K_value 
			new_accuracy = KNN_test(X_train,Y_train,X_val,Y_val,K_value)

			#If the accuracy of the new K_value is better than the old one then update
			if new_accuracy > best_accuracy:

				#Update the bets K_value and accuracy
				best_K_value = K_value
				best_accuracy = new_accuracy

	#Returns the best K_value
	return best_K_value

def main():

	#test KNN_test and choose_K
	test_set_x = np.array([[1, 1], [2, 1], [0, 10], [10, 10], [5, 5], [3, 10], [9, 4], [6, 2], [2, 2], [8, 7]])
	test_set_y = np.array([[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]])

	training_set_x = np.array([[1, 5], [2, 6], [2, 7], [3, 7], [3, 8], [4, 8], [5, 1], [5, 9], [6, 2], [7, 2], [7, 3], [8, 3], [8, 4], [9, 5]])
	training_set_y = np.array([[-1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [1]])

	acc1 = KNN_test(training_set_x, training_set_y, test_set_x, test_set_y, 1)
	acc3 = KNN_test(training_set_x, training_set_y, test_set_x, test_set_y, 3)
	acc5 = KNN_test(training_set_x, training_set_y, test_set_x, test_set_y, 5)

	k = choose_K(training_set_x, training_set_y, test_set_x, test_set_y)

	print("Classification Using K = 1:", acc1)
	print("Classification Using K = 2:", acc3)
	print("Classification Using K = 5:", acc5)
	print("Best K Value: ", k)

if __name__ == "__main__":
    main()