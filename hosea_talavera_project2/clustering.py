import numpy as np
import random


#Finds the distance between X and cluster_center, returns an integer
def find_distance(X, cluster_center):

	#subracts the two arrays and squares them
	distance = np.power(X - cluster_center,2)

	#returns the sum of all of the values
	return sum(distance)


'''

'''
def update_cluster_centers(X, cluster_centers):

	print("Old Cluster Center: ", cluster_centers)
	closest_center_index = np.array([])


	for sample in X:

		#Sets the distance of the best distance to the distance between the sample and the first cluster center
		best_cluster_distance = find_distance(sample,cluster_centers[0])
		best_cluster_index = 0

		for index in range(len(cluster_centers)):
		
			new_cluster_distance = find_distance(sample,cluster_centers[index])


			if new_cluster_distance < best_cluster_distance:

				best_cluster_distance = new_cluster_distance
				best_cluster_index = index


		closest_center_index = np.append(closest_center_index,best_cluster_index)




	new_cluster_centers = np.array([])

	for index in range(len(cluster_centers)):

		new_cluster_centers = np.append(new_cluster_centers, np.mean(X[closest_center_index == index], axis = 0))


	return new_cluster_centers



'''
Finds K cluster centers for X
Parameters:
	X -> np.array of training data
	K -> integer number of cluster centers
Returns:

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


	return np.sort(new_cluster_centers)




X = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])

print(K_Means(X, 3))



