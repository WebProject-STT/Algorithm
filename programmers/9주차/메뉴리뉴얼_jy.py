# 메뉴리뉴얼

from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for combi_num in course:
        total_combi = []
        for order in orders:
            total_combi += combinations(sorted(order), combi_num)
        total_combi = Counter(total_combi)
        if total_combi:
            max_len = max(total_combi.values())
            for key, value in total_combi.items():
                if value > 1 and value==max_len:
                    result.append("".join(key))
    result.sort()
    return result
            

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))