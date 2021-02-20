# 바이러스

computer = int(input()) # 컴퓨터 수
line = int(input()) # 네트워크 상에 연결되어 있는 컴퓨터 쌍의 수
computerPair = [[0] * (computer+1) for i in range(computer+1)] # 컴퓨터 번호 쌍
for i in range(line):
    n, m = map(int, input().split())

    # 연결됨을 Matrix에 표시
    computerPair[n][m] = 1
    computerPair[m][n] = 1

check = [0] * (computer + 1) # 인덱스를 활용하여 사용여부 확인
virus = [] # 1번과 연결되어 바이러스에 걸린 컴퓨터

def DFS(n):
    virus.append(n) # 바이러스에 걸린 컴퓨터 추가
    check[n] = 1 # 바이러스에 걸림 표시
    for i in range(1, computer + 1):
        if check[i] == 0 and computerPair[n][i] == 1: # 바이러스에 걸리지 않았고, 연결된 상태일 때
            DFS(i)

    

DFS(1)
print(len(virus) - 1) # 1번 컴퓨터 제외
