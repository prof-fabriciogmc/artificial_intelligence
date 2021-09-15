# Simple utility based agent
# Goal: Reach B from A through 
# the shortest path (minimizing the 
# total traveling distance).
# Utility: Achieve the goal with the lowest
# possible accident probability 
#
# Author: Fabrício G. M. de Carvalho, Ph.D
##


possible_paths_sequence = [ {'ab1': (10, 0.05), 'ab2': (15, 0.05)}]
				   

def utility(kd, d, ka, pa):
        return kd*(1/d) + ka*(1/pa) 
	
class UtilityBasedAgent:
	def __init__(self):
		self.distance_traveled = 0
		self.utility = 0
		self.route = []
		
	# possible paths correspond to percepts
	def select_path(self, possible_paths, uf):
		candidate_path = list(possible_paths.keys())[0]
		for path in possible_paths:
				selected_utility = uf(1,  possible_paths[candidate_path][0], 0.1,possible_paths[candidate_path][1])
				alternative_utility =  uf(1,  possible_paths[path][0], 0.1,possible_paths[path][1])
				if selected_utility < alternative_utility:
					candidate_path = path				
		return candidate_path
		
	def reach_destination(self, paths_sequence, uf):
		for possible_paths in paths_sequence:
			path = self.select_path(possible_paths, uf)
			self.distance_traveled += possible_paths[path][0]
			self.utility += uf(1,  possible_paths[path][0], \
                                    0.1,possible_paths[path][1])
			self.route.append(path)
		return {'distance_traveled (goal)':self.distance_traveled, \
                        'utility' : self.utility, 'route': self.route}
				
uba = UtilityBasedAgent()
print( uba.reach_destination(possible_paths_sequence, utility))

press_enter = input("Press enter to continue..")
			
		
