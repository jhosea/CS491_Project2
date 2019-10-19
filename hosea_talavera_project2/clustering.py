import numpy as np
import random
import collections


# Finds the distance between X and cluster_center, returns an integer
def find_distance(X, cluster_center):
	# subracts the two arrays and squares them
	distance = np.power(X - cluster_center, 2)

	# returns the sum of all of the values
	return sum(distance)


'''
Updates the cluster centers
Parameters:
	X -> np.array of training data
	cluster_centers -> np.array of the current cluster centers
Returns:
	new_cluster_centers -> np.array of the udpated cluster centers
'''


def update_cluster_centers(X, cluster_centers):
	# Creates an empty array for the closest cluster centers, element at index 0 of closest_center_index corresponds index of the closest cluster_center for the 0th sample of X
	closest_center_index = np.array([])

	# Iterates through every sample in X
	for sample in X:

		# Sets the distance of the best distance to the distance between the sample and the first cluster center
		best_cluster_distance = find_distance(sample, cluster_centers[0])
		best_cluster_index = 0

		# Iterates through each index in cluster centers
		for index in range(len(cluster_centers)):

			# Finds the new cluster distance
			new_cluster_distance = find_distance(sample, cluster_centers[index])

			if new_cluster_distance < best_cluster_distance:
				# If the distance from the sample to the cluster center is less than the distance to the previous cluster center
				best_cluster_distance = new_cluster_distance
				best_cluster_index = index

		# append the cluster center with  the shortest distance
		closest_center_index = np.append(closest_center_index, best_cluster_index)

	print(closest_center_index)
	# Initialize the new cluster centers array
	new_cluster_centers = np.zeros(cluster_centers.shape)

	# Iterate through all cluster centers
	for index in range(len(cluster_centers)):
		# Recalculate the cluster center
		new_cluster_centers[index] = np.mean(X[closest_center_index == index], axis=0)

	# returns new cluster centers
	return (new_cluster_centers)


'''
Finds K cluster centers for X
Parameters:
	X -> np.array of training data
	K -> integer number of cluster centers
Returns:
	Cluster Centers -> sorted np.array
'''


def K_Means(X, K):
	# Initalize cluster_centers array to array of 0's
	cluster_centers = np.zeros((K, np.size(X, 1)))

	# Initalizes K cluster centers
	for count in range(K):

		# Boolean to track whether the cluster center has already been added
		cluster_exists = True

		# Randomly picks a new point in X to be a cluster center, until it finds a point that has not been used already
		while cluster_exists:

			# Sets the cluster_exists boolean to False
			cluster_exists = False

			# Randomly picks a point in X to be a cluster center
			new_cluster = random.choice(X)

			# Loop through the cluster_centers array
			for index in range(len(cluster_centers)):

				# If the random cluster centers are already in the cluster_centers array, set cluster_exists to True
				if np.array_equal(cluster_centers[index, :], new_cluster):
					cluster_exists = True

		# Adds the unused cluster center to the cluster_centers array
		cluster_centers[count] = new_cluster

	old_cluster_centers = cluster_centers
	new_cluster_centers = update_cluster_centers(X, old_cluster_centers)

	# While new cluster centers are different than the old cluster centers, continue updating the cluster centers
	while (not np.array_equal(old_cluster_centers, new_cluster_centers)):
		old_cluster_centers = new_cluster_centers
		new_cluster_centers = update_cluster_centers(X, old_cluster_centers)

	# returns the new cluster centers
	return (new_cluster_centers)


'''
Finds K cluster centers for X
Parameters:
	X -> np.array of training data
	K -> integer number of cluster centers
Returns:
	Cluster Centers -> sorted np.array
'''


def K_Means_better(X, K):
	# Creates an np.array of zero's with 1000 rows and K columns
	all_cluster_centers = []

	# Creates 1000 cluster centers and puts them in all_cluster_centers
	for row_index in range(1000):
		all_cluster_centers.append(K_Means(X, K))

	# Finds all unique values in all_cluster_centers and their counts
	unique = np.unique(all_cluster_centers, axis=0, return_counts=True)

	# Extracts the counts of the unique values from the tuple unique.
	unique_counts = unique[1]

	# The 0th elements of unique counts corresponds to the 0th row of unique values
	unique_values = unique[0]

	# Finds the cluster center that was returned most often
	best_cluster_center = unique_values[np.argmax(unique_counts), :]

	# returns the cluster center that occures the most in all_cluster_centers
	return (best_cluster_center)


def main():

	#test K_Means and K_Means better

	test = np.array([[1, 0], [7, 4], [9, 6], [2, 1], [4, 8], [0, 3], [13, 5], [6, 8], [7, 3], [3, 6], [2, 1], [8, 3], [10, 2], [3, 5], [5, 1], [1, 9], [10, 3], [4, 1], [6, 6], [2, 2]])

	# center1 = K_Means(test, 2)
	# center2 = K_Means(test, 3)

	better_centers1 = K_Means_better(test, 2)
	# better_centers2 = K_Means_better(test, 3)

	# print("Cluster Center Using K = 2:", center1)
	# print("Cluster Center Using K = 3:", center2)
	print("Better Cluster Center Using K = 2:", better_centers1)
	# print("Better Cluster Center Using K = 3:", better_centers2)

if __name__ == "__main__":

	main()



