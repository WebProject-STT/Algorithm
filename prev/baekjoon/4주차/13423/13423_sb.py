# Three Dots
# 3%만 되면 시간초과가 뜬다 ㅎr...


import sys
input = sys.stdin.readline

t = int(input()) # testcase
# result = []

def binarySearch(arr, key, left, right) :
    while left <= right :
        midx = (left + right)//2
        mid = arr[midx]
        if mid == key :
            return 1
        elif mid > key :
            right = midx - 1
        else :
            left = midx + 1
    return 0

# 제귀함수가 반복문보다 더 많은 시간이 소요됨  
# def binarySearch(arr, key, left, right) :
    # if left > right :
    #     return 0
    # midx = (left + right)//2
    # mid = arr[midx]
    # if key == mid :
    #     return key
    # elif mid > key :
    #     return binarySearch(arr, key, left, midx-1)
    # else : # mid < key
    #     return binarySearch(arr, key, midx+1, right)

for _ in range(t) :
    n = int(input())
    dots = list(map(int, input().split()))
    dots.sort()
    
    cnt = 0
    
    for a in range(n-2) : # a
        for b in range(a+1, n-1) : # b
            c = 2 * dots[b] - dots[a]
            if dots[b] < c <= dots[n-1] and binarySearch(dots, c, b+1, n-1) :
                cnt += 1
    print(cnt)
#     result.append(cnt)

# for r in result :
#     print(r)