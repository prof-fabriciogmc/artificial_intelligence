# Simple example of model based reflex
# system.
#
# Author: Fabrício G. M. de Carvalho, Ph.D


# The internal state corresponds to
# temperature history.
# The environment model is expressed 
# in the condition-action rules
class ModelBasedReflexAgent:
    def __init__(self, temp):
        # internal state
        self.last_temp = temp 

    def select_action(self, temp):
        if (temp - self.last_temp) > 0 :
            temp_increase = True
        else:
            temp_increase = False
        # internal state update:        
        self.last_temp = temp
        if temp_increase and temp > 37.5 :
            return "Strong medication"
        elif not temp_increase and temp > 37.5:
            return "Mild medication"
        elif temp <= 37.5:
            return "No medication"
        

# This agent has no internal state
# (i.e.: memory) nor environment model.
class ReflexAgent:
    def __init__(self):
        pass    
    def select_action(self, temp):
        if temp > 37.5:
            return "Mild medication"
        else:
            return "No medication"




percept = float(input('Enter temperature: (h=0) '))

ra = ReflexAgent()
mbra = ModelBasedReflexAgent(percept)

print("Reflex agent doctor action: " + \
      str(ra.select_action(percept)))
print("Model based reflex agent doctor action: " + \
      mbra.select_action(percept))

# temperature measurement after some time:
percept= float(input('Enter temperature (h=2): '))
print("Reflex agent doctor action: " + \
      str(ra.select_action(percept)))
print("Model based reflex agent doctor action: " + \
      mbra.select_action(percept))


# temperature measurement after some time:
percept= float(input('Enter temperature (h=3): '))
print("Reflex agent doctor action: " + \
      str(ra.select_action(percept)))
print("Model based reflex agent doctor action: " + \
      mbra.select_action(percept))
	  
pause = input('Press enter to continue')

     
    
