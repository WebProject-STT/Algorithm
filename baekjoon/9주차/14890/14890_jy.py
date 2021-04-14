# 경사로
# https://www.acmicpc.net/problem/14890
import sys

def ramps(lines, N, L):
    ramp = [False]*N # 경사로 세웠는지 check 용

    for i in range(1, N):
        if lines[i-1] == lines[i]: continue # 같은 숫자면 pass
        else:
            if lines[i] - lines[i-1] == 1: # 2 3일 경우
                temp = lines[i-1] # 일단 2-3-3 처럼 증가 경우는 i-1을 저장해두고 L만큼 있는지 확인
                if i-L >= 0:
                    for j in range(i-1, i-1-L, -1):
                        if lines[j] != temp or ramp[j]: return False
                        ramp[j] = True
                else: return False
                continue
            if lines[i] - lines[i-1] == -1: # 3 2일 경우
                temp = lines[i] # 일단 3-3-2 처럼 감소하는 경우는 i을 저장해두고 L만큼 있는지 확인
                if i-1+L < N:
                    for j in range(i, i+L):
                        if temp != lines[j] or ramp[j]: return False
                        ramp[j] = True
                else: return False # 범위 벗어나면 실패
                continue
            return False
    return True
                    
    
if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    total = 0
    for row in grids:
        if ramps(row, N, L): total += 1
    #print("row total : ", total)
    
    for j in range(N):
        if ramps([grids[i][j] for i in range(N)], N, L): total +=1
    #print("col total : ", total)
    print(total)