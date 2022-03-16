# Reading a set of rules that were persisted in MongoDB and analysing it
#
# Author: Fabrício Galende M. de Carvalho, Ph.D

import pymongo
from inference_engine import Rule, Inference

'''
Inference rule in database: This is an example to show a composite "rule anatomy"
{rules: [
            {relation:">=", percept_ref: "37.5", percept_name:"temperature", action:"True"},
            {relation:"==", percept_ref: "loss of taste", percept_name:"taste", action:"True"}
        ],
operators: ["and"],
action: ["covid"]
}
'''

application_client = pymongo.MongoClient("mongodb://localhost:27017/")
application_db = application_client["ia"]
application_collection = application_db["rule_collection"]


### Rule insertion.
''''
composite_rule = {'rules': [
            {'relation':">=", 'percept_ref': "37.5", 'percept_name':"temperature", 'action':"True"},
            {'relation':"==", 'percept_ref': "'loss of taste'", 'percept_name':"taste", 'action':"True"}],
    'operators': ["and"],
    'action': ["covid"]
}

x = application_collection.insert_one(composite_rule)

# single rule
composite_rule = {'rules': [
            {'relation':">=", 'percept_ref': "37.5", 'percept_name':"temperature", 'action':"fever"}],
    'operators': [],
    'action': ["fever"]
}

x = application_collection.insert_one(composite_rule)


''' 

### Rule retrieval:

composite_rules = application_collection.find()
inferences = []
for composite_rule in composite_rules:
    rules = []
    for rule in composite_rule['rules']:
        r = Rule(rule['relation'], rule['percept_ref'], rule['percept_name'], rule['action'])
        rules.append(r)
    inferences.append(Inference(rules, composite_rule['operators'], composite_rule['action']))

print("Inferences: ")
print(inferences)
'''
# How to visualize an individual rule: 
print(inferences[0].rules)
print(inferences[0].operators)
print(inferences[0].action)
'''

# Inference engine usage example
percepts = [ {"taste": "'loss of taste'", "breath":"'shortness of breath'", "temperature":"38.5"},
             {"breath":"'shortness of breath'", "temperature":"38.5", "taste": "'loss of taste'"},
             {"taste": "'loss of taste'" },
             {"temperature":"38.5"}]

count = 1
for inference in inferences:
    print("Analysing inference rule # " + str(count))
    for percept in percepts:
        print(inference.infer(percept))
    count += 1
