import numpy as np
import random
import collections


#Finds the distance between X and cluster_center, returns an integer
def find_distance(X, cluster_center):

	#subracts the two arrays and squares them
	distance = np.power(X - cluster_center,2)

	#returns the sum of all of the values
	return sum(distance)


'''

'''
def update_cluster_centers(X, cluster_centers):

	#print("Old Cluster Center: ", cluster_centers)
	closest_center_index = np.array([])


	#Iterates through every sample in X
	for sample in X:

		#Sets the distance of the best distance to the distance between the sample and the first cluster center
		best_cluster_distance = find_distance(sample,cluster_centers[0])
		best_cluster_index = 0


		#Iterates through each index in cluster centers
		for index in range(len(cluster_centers)):
		
			#Finds the new cluster distance
			new_cluster_distance = find_distance(sample,cluster_centers[index])


			if new_cluster_distance < best_cluster_distance:

				#If the distance from the sample to the cluster center is less than the distance to the previous cluster center 
				best_cluster_distance = new_cluster_distance
				best_cluster_index = index

		#append the cluster center with  the shortest distance
		closest_center_index = np.append(closest_center_index,best_cluster_index)



	#Initialize the new cluster centers array
	new_cluster_centers = np.array([])

	#Iterate through all cluster centers
	for index in range(len(cluster_centers)):

		#Recalculate the cluster center
		new_cluster_centers = np.append(new_cluster_centers, np.mean(X[closest_center_index == index], axis = 0))


	#returns new cluster centers
	return new_cluster_centers



'''
Finds K cluster centers for X
Parameters:
	X -> np.array of training data
	K -> integer number of cluster centers
Returns:
	Cluster Centers -> sorted np.array
'''
def K_Means(X,K):

	#Initalize cluster_centers array
	cluster_centers = np.array([])

	#Initalizes K cluster centers
	for count in range(K):

		#Randomly picks a point in X to be a cluster center
		new_cluster = random.choice(X)

		#Randomly picks a new point in X to be a cluster center, until it finds a point that has not been used already
		while new_cluster in cluster_centers:

			new_cluster = random.choice(X)

		#Appends the unused cluster center to the cluster_centers array
		cluster_centers = np.append(cluster_centers,[new_cluster])


	old_cluster_centers = cluster_centers
	new_cluster_centers = update_cluster_centers(X, old_cluster_centers)


	#While new cluster centers are different than the old cluster centers, continue updating the cluster centers
	while((old_cluster_centers != new_cluster_centers).all()):

		old_cluster_centers = new_cluster_centers
		new_cluster_centers = update_cluster_centers(X, old_cluster_centers)

	#returns the new cluster centers, sorted
	return np.sort(new_cluster_centers)


'''
Finds K cluster centers for X
Parameters:
	X -> np.array of training data
	K -> integer number of cluster centers
Returns:
	Cluster Centers -> sorted np.array
'''
def K_Means_better(X,K):

	#Creates an np.array of zero's with 1000 rows and K columns
	all_cluster_centers = np.zeros((1000, K))

	#Creates 1000 cluster centers and puts them in all_cluster_centers
	for row_index in range(len(all_cluster_centers)):

		all_cluster_centers[row_index,:] = K_Means(X,K)


	#Finds all unique values in all_cluster_centers and their counts
	unique = np.unique(all_cluster_centers, axis = 0, return_counts = True)

	#Extracts the counts of the unique values from the tuple unique.
	unique_counts = unique[1]

	#The 0th elements of unique counts corresponds to the 0th row of unique values
	unique_values = unique[0]


	#Finds the cluster center that was returned most often
	best_cluster_center = unique_values[np.argmax(unique_counts),:]


	#returns the cluster center that occures the most in all_cluster_centers
	return np.sort(best_cluster_center)





