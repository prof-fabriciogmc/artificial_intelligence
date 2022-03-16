# Simple inference engine that handles multiple rules associated
# by AND operator
#
# Author: Fabrício G. M. C - Ph.D
##

class Rule:
    def __init__(self, relation, percept_ref, action):
        self.percept_ref = percept_ref
        self.relation = relation
        self.action = action


class Inference:
    def __init__(self, rules, operators, action):
        self.rules = rules
        self.operators = operators
        self.action = action

    def infer(self, percepts):
        rule_actions = []
        for i in range(len(percepts)):
              if eval( percepts[i] + self.rules[i].relation + self.rules[i].percept_ref):
                  rule_actions.append(self.rules[i].action)
              else:
                  rule_actions.append('False')
        print(rule_actions)
        if len(rule_actions) == 1:
            return rule_actions[0]
        else:
            current_inference = rule_actions[0]
            i = 1
            while i < len(rule_actions) and current_inference == True:
                current_inference = eval(str(current_inference) + self.operators[i-1] + rule_actions[i])
                ++i
            if eval(current_inference):
                return self.action
            else:
                return False


rule_1 = Rule(">=", "37.5", "True")
rule_2 = Rule("==", "'perda de paladar'", "True")
inference = Inference([rule_1, rule_2],[" and "],["Covid"])
print(inference.infer(["35.5","'perda de paladar'"]))


