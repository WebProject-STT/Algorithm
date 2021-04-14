# 미친 아두이노
import sys

def solution(R, C, crazy, r, c, command, d):
    for i in range(len(command)):
        # 1. 종수의 아두이노 위치 이동
        r, c = r + d[command[i]][0], c + d[command[i]][1]
        # 2. 종수의 아두이노 위치가 미친 아두이노의 위치인 경우
        if (r, c) in crazy :
            print(f"kraj {i + 1}")
            exit(0)
        # 3. 미친 아두이노 이동
        for n in range(len(crazy)) :
            cur_r, cur_c = crazy[n][0], crazy[n][1] # 미친 아두이노의 현재 위치
            min_d, min_r, min_c = sys.maxsize, 0, 0 # 최소 거리, 최소 위치에 대한 정보 저장
            for m in range(1, 10) : # 8방향에 대한 확인
                if m == 5 : continue # 5은 현재 위치
                nr, nc = cur_r + d[m][0], cur_c + d[m][1] # 미친 아두이노의 예상 이동 위치
                if 0 <= nr < R and 0 <= nc < C :
                    distance = abs(r - nr) + abs(c - nc) # 종수의 아두이노와 미친 아두이노의 차
                    if min_d > distance : # 가장 작은 거리를 가지면 정보 업데이트
                        min_d, min_r, min_c = distance, nr, nc
            # 4. 미친 아두이노 위치가 종수의 아두이노의 위치인 경우
            if min_r == r and min_c == c :
                print(f"kraj {i + 1}")
                exit(0)
            # 8방향 중 최소 위치 정보 업데이트
            crazy[n][0], crazy[n][1] = min_r, min_c
        # 5. 같은 위치에 존재하는 미친 아두이노 제거
        crazy.sort()
        not_boom = [crazy[0]]
        for k in range(1, len(crazy)) :
            if crazy[k] == crazy[k-1] :
                if len(not_boom) > 0 and crazy[k] == not_boom[-1] :
                    not_boom.pop()
            else :
                not_boom.append(crazy[k])
        crazy = not_boom # 미친 아두이노의 좌표 업데이트
    else : # for문 정상 종료
        board = [['.']*C for _ in range(R)]
        board[r][c] = 'I' # 종수의 아두이노 위치 표시
        for i, j in crazy :
            board[i][j] = 'R' # 미친 아두이노 위치 표시
        for b in board :
            print(''.join(b))
                


if __name__=="__main__" :
    input = sys.stdin.readline

    R, C = map(int, input().split())
    r, c = 0, 0 # 종수의 아두이노 현재 위치
    crazy = [] # 미친 아두이노의 위치 리스트
    for i in range(R) :
        state = input()
        for j in range(C) :
            if state[j] == 'I' :
                r, c = i, j
            elif state[j] == "R" :
                crazy.append([i, j])
    command = list(map(int, input().strip()))
    d = [(), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)] # 8방향에 대한 dict

    solution(R, C, crazy, r, c, command, d)
        

'''
1. 종수의 아두이노를 8방향으로 이동시키거나 현재 위치에 그대로 둠 => 9가지 경우
2. 종수의 아두이노가 미친 아두이노가 있는 칸으로 이동한 경우 게임 종료
3. 미친 아두이노는 8방향 중 종수의 아두이노와 가장 가까워지는 방향으로 1칸 이동 (거리 계산으로 이동함)
4. 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우 게임 종료
5. 2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우 큰 폭발과 함께 그 칸의 아두이노는 모두 파괴됨
--- 입력
R줄 C개 문자
빈칸은 . , 미친 아두이노는 R , 종수는 I
5가 현재 위치이며, 나머지는 8방향에 대한 위치 번호
7  8  9
4  5  6
1  2  3
--- 출력
중간에 게임이 끝나는 경우
kraj X 출력. 여기서 X는 종수의 이동 횟수
게임이 정상 종료된 경우 보드 상태 출력
--- 풀이
종수의 아두이노는 주어진 위치로 이동 => 정상종료되면 보드 출력 (for else)
미친 아두이노는 종수의 아두이노와의 거리 계산을 통해 이동 (8가지 방향 중 가장 가까운 방향으로 이동하는 형태)
만약 위치가 같은 아두이노가 존재하면 그 아두이노들은 제거
'''