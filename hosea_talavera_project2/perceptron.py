import numpy as np


'''
Updates the weights and bias
Parameters:
	weights -> 1D np.array of the current weights
	bias -> int of current bias
	X -> 1D np.array of teh current sample
	Y -> 1D np.array of current sample label
Returns:
	Cluster Centers -> sorted np.array
'''
def updateWB(weights,bias,X,Y):
	
	new_weights = weights + (X*Y)

	new_bias = bias + Y


	return [new_weights, new_bias]

'''
Returns the weights and bias for a perceptron
Parameters:
	X -> np.array of training data
	Y -> np.array of the training data labels
Returns:
	weights and bias -> List of two elements, the first being the weights and the second being the bias
'''
def perceptron_train(X,Y):

	'''
	start weights and bias at 0
	go through one epoch at a time until previous w and b is equal to current w and b
		each iteration through sample, update if y not equal to prediction
	'''
	
	#Initalize weights and bias to 0
	weights = np.zeros(np.size(X,1))
	bias = 0

	#Boolean to keep track of whether the weights and bias have been updated on the most current epoch
	updated = True

	#run while the weights and bias have been updated
	while (updated):

		#Resets updated to False
		updated = False
	
		#Iterate through all of the samples
		for sample_index in range(len(X)):


			#Find the activation for each sample
			activation = np.sum(weights * X[sample_index,:]) + bias

			
			#If the activation is incorrect, update
			if((activation * Y[sample_index,0]) <= 0):

				weights_bias = updateWB(weights, bias,X[sample_index,:],Y[sample_index])
				weights = weights_bias[0]
				bias = weights_bias[1]

				#Changes update to True
				updated = True


	return weights, bias


'''
Returns the weights and bias for a perceptron
Parameters:
	X_test -> np.array of testing data
	Y_test -> np.array of the testing data labels
	w -> 1D np.array of the weights
	b -> integer bias
Returns:
	weights and bias -> List of two elements, the first being the weights and the second being the bias
'''
def perceptron_test(X_test, Y_test, w, b):


	#Initalizes the count_correct to 0
	count_correct = 0

	#Iterates through all of the testing samples
	for sample_index in range(len(X_test)):

		#Calculates the activation for each sample
		activation = np.sum(w * X_test[sample_index,:]) + b


		#If the activation is correct (activation * label is positive) increment count_correct
		if (activation * Y_test[sample_index,0] > 0):

			count_correct += 1

	#Return the count correct divided by the number of samples
	return(count_correct/len(X_test))

