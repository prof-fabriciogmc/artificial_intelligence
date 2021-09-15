# Simple goal based agent
# Goal: Reach B from A through 
# the shortest path (minimizing the 
# total traveling distance)
#
# Author: Fabrício G. M. de Carvalho, Ph.D
##


possible_paths_sequence = [ {'ac1': 10, 'ac2': 1, 'ac3':0.5},
				   {'cd1': 10, 'cd2': 1},
				   {'db1': 10, 'db2': 100}]
	
	
class GoalBasedAgent:
	def __init__(self,  distance_traveled):
		self.distance_traveled = distance_traveled
		self.route = []
		
	# possible paths correspond to percepts
	def select_path(self, possible_paths):
		candidate_path = list(possible_paths.keys())[0]
		for path in possible_paths:
				selected_goal = 1/(1+possible_paths[candidate_path])
				alternative_goal = 1/(1+possible_paths[path]) 
				if selected_goal < alternative_goal:
					candidate_path = path				
		return candidate_path
		
	def reach_destination(self, paths_sequence):
		for possible_paths in paths_sequence:
			path = self.select_path(possible_paths)
			self.distance_traveled += possible_paths[path]
			self.route.append(path)
		return {'distance_traveled (goal)':self.distance_traveled, \
		        'route': self.route}
				
gba = GoalBasedAgent(0)
print( gba.reach_destination(possible_paths_sequence))

press_enter = input("Press enter to continue..")
			
		
