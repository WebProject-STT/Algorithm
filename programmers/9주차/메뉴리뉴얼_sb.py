from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course :
        temp = []
        for order in orders :
            combi = combinations(sorted(order), c)
            temp += combi
        odict = Counter(temp) 
        
        if odict : 
            max_ = max(list(odict.values()))
            if max_ >= 2:
                for key, value in odict.items() :
                    if odict[key] == max_ :
                        answer.append(''.join(key))
    
    return sorted(answer)