##
# A simple kmeans algorithm implementation.
# K centers are initialized with the first
# K feature vectors.
#
# Author: Fabricio G. M. de Carvalho, Ph.D
##


import copy 

def distance(v1, v2):
	square_sum = 0
	for i in range(len(v1)):
		square_sum += (v1[i] - v2[i])**2
	distance = square_sum**0.5
	return distance

# Returns the index of the minimum	
def min_index(v):
	m_index = 0
	for i in range(len(v)):
		if v[i] < v[m_index]:
			m_index = i
	return m_index
 
class KMeans:
	def __init__(self, n_centers):
		self.n_centers = n_centers;
		self.centers = [ [] for x in range(n_centers)]
		self.classified_vectors = None
		self.center_length = None
		self.n_vectors = None
		
	def init_centers(self, vectors):
		"""" Initializes center coordinates with the corresponding
		n first feature vectors. Moreover, copies each feature vector
		to classified_vectors but without classifying it.
        """
		for n in range(self.n_centers):
			self.centers[n]= copy.deepcopy(vectors[n])
		self.center_length = len(self.centers[0])
		self.classified_vectors = copy.deepcopy(vectors)
		self.n_vectors = len(vectors)
		for n in range(self.n_vectors):
			self.classified_vectors[n].append([]) #vector has no class

	def calc_centers(self):
		''' Computes center coordinates for each one of k centers '''
		
		for i in range(self.n_centers):
			self.centers[i] = [ 0 for x in range(self.center_length)]
			count = 0	# number of points assigned to center
			for vector in self.classified_vectors:
				if (vector[self.center_length] == i):
					count += 1
					for x in range(self.center_length):
						self.centers[i][x] += vector[x]
			if count != 0:
				for x in range(self.center_length):
					self.centers[i][x] /= count
					
	def classify_vectors(self):	
		""" Classify each feature vector based on euclidean distance
		to center coordinates.
		"""
		for v_i in range(self.n_vectors):
			d_to_center = []
			for c_i in range(self.n_centers):
				d_to_center.append(distance(self.centers[c_i], \
											self.classified_vectors[v_i]))
			center = min_index(d_to_center)
			self.classified_vectors[v_i][self.center_length] = center
		

				

	
	
