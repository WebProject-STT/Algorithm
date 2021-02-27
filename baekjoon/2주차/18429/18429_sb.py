# 근손실

n, k = map(int, input().split())
kits = list(map(int, input().split()))

cnt = 0 # 3대 500 이상을 유지할 수 있는 경우의 수

result = [0] * n # 운동 키트 순서를 담을 리스트
check = [0] * n

def DFS(L):
    global cnt
    if k*L > sum(result[:L]): # 리스트를 초기화시키고 사용하는 것이 아니므로 list룰 자른 합과 비교
        return
    if L == n :
        cnt += 1
    else : # 순열을 생성하는 부분 (아래 공식은 중복 순열식)
        for i in range(n):
            if check[i] == 0: # 사용 여부 확인
                check[i] = 1
                result[L] = kits[i]
                DFS(L + 1)
                check[i] = 0
DFS(0)
print(cnt)
