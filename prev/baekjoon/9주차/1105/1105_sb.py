# 팔
import sys
input = sys.stdin.readline

L, R = input().split()
Llen, Rlen = len(L), len(R)
cnt = 0
if Llen != Rlen :
    print(cnt)
else :
    for i in range(Llen) :
        if L[i] != R[i] :
            break
        else :
            if L[i] == '8' :
                cnt += 1
    print(cnt)


'''
L부터 R까지의 수 중 8이 가장 적게 들어가는 수의 8 개수 찾기
---
ex1) L = 1, R = 10
1부터 10 중 8이 가장 적게 들어가는 수는 8 제외한 모든 수이며, 해당 숫자의 8 개수는 0개
---
ex2) L = 88, R = 88
L부터 R까지의 숫자는 88 하나이며, 88의 8 개수는 2개
--- 풀이
1. 두 숫자의 길이가 다르면 8이 하나도 포함되지 않는 경우가 발생함
2. 두 숫자의 길이 같을 때
    1) 두 숫자의 값이 다를 때
       L 234, R 333
       이러한 경우 앞부분 시작이 다르므로 8을 하나도 포함하지 않는 경우 발생
    2) 두 숫자의 값 일부가 같을 때
       L 880, R 899
       이러한 경우 앞의 8을 제외하고 나머지 뒷 부분은 8을 포함하지 않는 경우 발생
    3) 두 숫자의 값이 같을 때, 포함하고 있는 8 세기
'''