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
	cluster_centers =z

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
	while(np.array_equal(old_cluster_centers,new_cluster_centers)):

		old_cluster_centers = new_cluster_centers
		new_cluster_centers = update_cluster_centers(X, old_cluster_centers)


	return np.sort(new_cluster_centers)




<<<<<<< Updated upstream
X = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])
=======
def main():

	#test K_Means and K_Means better


	test_set_1 = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])
	test_set_2 = np.array([[1, 0], [7, 4], [9, 6], [2, 1], [4, 8], [0, 3], [13, 5], [6, 8], [7, 3], [3, 6], [2, 1], [8, 3], [10, 2], [3, 5], [5, 1], [1, 9], [10, 3], [4, 1], [6, 6], [2, 2]])

	centers_1_2 = K_Means(test_set_1, 2)
	centers_1_3 = K_Means(test_set_1, 3)

	centers_2_2 = K_Means(test_set_2, 2)
	# centers_2_3 = K_Means(test_set_2, 3)

	# better_centers_1_2 = K_Means_better(test_set_1, 2)
	# better_centers_1_3 = K_Means_better(test_set_1, 3)
	#
	# better_centers_2_2 = K_Means_better(test_set_2, 2)
	# better_centers_2_3 = K_Means_better(test_set_2, 3)
	#
	# print("Classification Using K = 1:", centers_1_2)
	# print("Classification Using K = 2:", centers_1_3)
	# print("Classification Using K = 5:", centers_2_2)
	# print("Classification Using K = 1:", centers_2_3)
	# print("Classification Using K = 2:", better_centers_1_2)
	# print("Classification Using K = 5:", better_centers_1_3)
	# print("Classification Using K = 2:", better_centers_2_2)
	# print("Classification Using K = 5:", better_centers_2_3)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes

print(K_Means(X, 3))



