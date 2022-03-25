# Simple inference engine that handles multiple rules associated
# by AND operator
#
# Author: Fabrício G. M. C - Ph.D
##

class Rule:
    def __init__(self, relation, percept_ref, percept_name, action):
        self.percept_name = percept_name
        self.percept_ref = percept_ref
        self.relation = relation
        self.action = action


class Inference:
    def __init__(self, rules, operators, action):
        self.rules = rules
        self.operators = operators
        self.action = action
        self.rule_percept_names = set()
        # builds the rule's percept names set to compare it
        # to percept inputs.
        for rule in rules:
            self.rule_percept_names.add(rule.percept_name)


    def infer(self, percepts):
        #verify if percepts match rules's percept names
        if self.rule_percept_names.issubset(percepts.keys()):
            rule_actions = []
            for i in range(len(self.rules)):
                if eval(percepts[self.rules[i].percept_name] +" "+ self.rules[i].relation +" "+ self.rules[i].percept_ref):
                    rule_actions.append(self.rules[i].action)
                else:
                    rule_actions.append('False')
            # print(rule_actions) # debug purpuposes only
            if len(rule_actions) == 1:
                return rule_actions[0]
            else:
                current_inference = rule_actions[0]
                k = 1
                while k < len(rule_actions) and current_inference == 'True':
                    current_inference = eval(str(current_inference) + " " +self.operators[k-1] +" "+ rule_actions[k])
                    ++k
                if eval(str(current_inference)):
                    return self.action
                else:
                    return False

        else:
            return False


# Usage example:
'''
rule_1 = Rule(">=", "37.5", "temperature", "True")
rule_2 = Rule("==", "'loss of taste'", "taste", "True")
inference = Inference([rule_1, rule_2],["and"],["Covid"])

percepts = {"temperature":"38.5", "taste": "'loss of taste'", "breath":"'shortness of breath'"}

print(inference.infer(percepts))

'''



