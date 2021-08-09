# three dots
import sys
case= int(sys.stdin.readline())

def binary_search(target, li, end):
    left, right = 0, end-1
    while left <= right:
        m = (left+right)//2
        if li[m] < target: left = m + 1
        elif li[m] > target: right = m - 1
        else: return 1
    return 0

for _ in range(case):
    num = int(sys.stdin.readline())
    cases = list(map(int,sys.stdin.readline().split()))
    cases.sort()
    total = 0
    for i in range(1, num-1): # 중간 값
        for j in range(i): # 초기 값
            d1 = cases[i] - cases[j] # 중간 값 - 초기 값
            if binary_search(cases[i] + d1, cases, num): total += 1
    print(total)

"""
# three dots
import sys
case= int(sys.stdin.readline())
cases = [(int(input()), list(map(int,sys.stdin.readline().split()))) for _ in range(case)]

total = []
for num, li in cases:
    temp_total = 0 
    li.sort()
    temp = 0
    for i in range(1, num-1): 
        root, left, right = i, i-1, i+1 
        while True:
            if left < 0 : break
            if right >= num: break
            d1 = li[root] - li[left]
            d2 = li[right] - li[root]
            if d1==d2: 
                temp += 1
                left -= 1
                right += 1
            elif d1<d2: left -= 1
            else: right += 1
    print(temp)
"""