# A simple 1-level association rule apriori
# algorithm implementation
#
# Author: Fabrício G. M. de Carvalho, Ph.D


itemset = ['pão','manteiga','presunto','queijo']
transactions_bd= [{'pão'},
                  {'pão', 'queijo'},
                  {'pão', 'queijo', 'manteiga'},
                  {'pão', 'queijo', 'presunto'},
                  {'queijo', 'manteiga'},
                  {'queijo', 'presunto'}
                  ]

#Support calculation
def support(Ix, Iy, bd):
    sup = 0
    for transaction in bd:
        if (Ix.union(Iy)).issubset(transaction):
            sup+=1
    sup = sup/len(bd)
    return sup

# Confidence calculation
def confidence(Ix, Iy, bd):
    Ix_count = 0
    Ixy_count = 0
    for transaction in bd:
        if Ix.issubset(transaction):
            Ix_count+=1
            if (Ix.union(Iy)).issubset(transaction):
                Ixy_count += 1
    conf = Ixy_count / Ix_count
    return conf
            

# This function eliminates all the items in 
# ass_rules which have sup < min_sup and
# conf < min_conf. It returns a "pruned" list
def prune(ass_rules, min_sup, min_conf):
    pruned_ass_rules = []
    for ar in ass_rules:
        if ar['support'] >= min_sup and ar['confidence'] >= min_conf:
            pruned_ass_rules.append(ar)
    return pruned_ass_rules
    

# Apriori for association between 2 items
def apriori_2(itemset, bd, min_sup, min_conf):
    ass_rules = []
    ass_rules.append([]) #level 1 (large itemsets)
    for item in itemset:
        sup = support({item},{item},bd)
        ass_rules[0].append({'rule': str(item), \
                             'support':sup, \
                             'confidence': 1})        
    ass_rules[0] = prune(ass_rules[0],min_sup, min_conf)
    ass_rules.append([]) #level 2 (2 items association)
    for item_1 in ass_rules[0]:
        for item_2 in ass_rules[0]:
            if item_1['rule'] != item_2['rule']:
                rule = item_1['rule']+'_'+item_2['rule']
                Ix = {item_1['rule']}
                Iy = {item_2['rule']}
                sup = support(Ix,Iy, bd)
                conf = confidence(Ix, Iy, bd)
                ass_rules[1].append({'rule':rule, \
                                     'support': sup, \
                                     'confidence': conf})
    ass_rules[1] = prune(ass_rules[1],min_sup, min_conf)
    return ass_rules

    

print(apriori_2(itemset, transactions_bd, 0.4, 0.6))
cont = input('Press enter to continue...')



    
