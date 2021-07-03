# 캐시

def solution(cacheSize, cities):
    total = 0
    if cacheSize == 0:
        return len(cities)*5
    
    stack = []
    for city in cities:
        city = city.lower()

        if city not in stack:
            total += 5
            if len(stack) < cacheSize:
                stack.append(city)
            else:
                stack.pop(0)
                stack.append(city)
            
        else:
            total += 1
            if stack[-1] != city:
                idx = stack.pop(stack.index(city))
                stack.append(city)
    
    return total


print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))