# Simple general rule engine example.
# In this case, the reflex agent
# rule engine (agent program)
# squares its input.
#
# Author: Fabrício G. M. C - Ph.D
##


{'ovo':1, 'aveia':2}


rule_db = [
            {'percept': '1',
             'relation': '==',
             'action': 'Brahma'},
            {'percept': '2',
             'relation': '==',
             'action': 4},
             {'percept': '3',
             'relation': '==',
             'action': 9},
            {'percept': '38',
             'relation': '>=',
             'action': 'Febre'}
            ]

def eval_rule(rule, percept):
    #Verificar se a comparação é de número
    if eval(percept + rule['relation'] \
            + rule['percept']):
        return rule['action']
    else:
        return None


def rule_engine(rule_db, percept):
    actions = []
    for rule in rule_db:
        actions.append(eval_rule(rule,percept))
    return actions

def convert_to_number(string):
    if string == 'pilsen':
        return '1'
    

percept = input('Informe a bebida: ')
percept2 = convert_to_number(percept)

print(rule_engine(rule_db, percept2))
        
