# 스타트와 링크

N = int(input()) # 축구하기 위해 모인 사람 수

ability =  [list(map(int, input().split())) for _ in range(N)] # 능력치 Matrix

start = [0] * (N//2) # 스타트팀

min_diff = 2147000000 # 능력치 비교값 (대략적으로 큰 수 넣어둠)

def DFS(L, cur):
    global min_diff
    if L == N//2: # 인원의 절반이 start팀으로 구성됨
        link = [] # link팀
        for i in range(1, N+1): # link 팀 구성
            if i not in start:
                link.append(i)
        startSum, linkSum = 0, 0
        for i in range(L-1) : # 능력치 계산
            for j in range(i+1, L):
                sI, sJ = start[i]-1, start[j]-1
                lI, lJ = link[i]-1, link[j]-1
                startSum += ability[sI][sJ] + ability[sJ][sI]
                linkSum += ability[lI][lJ] + ability[lJ][lI]
        diff = abs(startSum - linkSum) # 두 팀의 능력치 차 비교
        if min_diff > diff: # 능력치 차 최솟값 저장
            min_diff = diff
    else:
        for i in range(cur, N+1): # start 팀 구성
            start[L] = i
            DFS(L + 1, i + 1)

DFS(0, 1)

print(min_diff)
