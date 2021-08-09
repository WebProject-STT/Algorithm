# 이진트리
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
nums = []
while 1:
    try:
        nums.append(int(input()))
    except: break

def post_order(start, end):
    # 자식 노드 더이상 없으면 끝
    if start > end: 
        return
    #print(start, end)
    # 왼쪽 노드 , 오른쪽 노드
    temp = end+1 # start와 end 차이가 1 또는 0일 경우 for문 못돌림
    for i in range(start+1, end+1):
        if nums[i] > nums[start]: 
            temp = i
            break
    
    post_order(start+1, temp-1) # 왼쪽 노드 순회
    post_order(temp, end) # 오른쪽 노드 순회
    
    print(nums[start])
    
post_order(0, len(nums)-1)