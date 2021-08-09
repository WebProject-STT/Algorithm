# 봄버맨

if __name__ == "__main__":
    R, C, N = map(int, input().split())

    grids = []
    for i in range(R):
        temp = input()
        temp2 = []
        for j in range(C):
            temp2.append([temp[j], 0]) # ['.', 초]
        grids.append(temp2)

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북

    while N >= 0:
        # 1. 1초 동안은 아무것도 안함 (대신 시간 +1 됨) + 폭발할 폭탄은 폭발
        for i in range(R):
            for j in range(C):
                if grids[i][j][0] == 'O':
                    if grids[i][j][1] == 2: # 폭발해야 함
                        grids[i][j][0], grids[i][j][1] = '.', 0  # 자기 자신은 폭발
                        # 4방향 탐색
                        for r, c in dirs:
                            next_r, next_c = i+r, j+c
                            #print("next : ", (next_r, next_c))
                            if 0 <= next_r < R and 0 <= next_c < C \
                                and grids[next_r][next_c][0] != '.' \
                                and grids[next_r][next_c][1] != 2: # 2초인 애들은 지금 터져야 되니까 pass
                                grids[next_r][next_c][0], grids[next_r][next_c][1]  = '.', 0 # 폭발
                    else: # 3초보다 작으면 시간 흘러가기
                        grids[i][j][1] += 1

        if N-1 == 0: break # 1초 흐른 뒤가 끝나면

        # 2. 봄버맨은 폭탄을 설치한다 
        for i in range(R):
            for j in range(C):
                if grids[i][j][0] == '.':
                    grids[i][j][0], grids[i][j][1] = 'O', 0
                else:
                    grids[i][j][1] += 1

        N -= 2
    
    for i in range(R):
        for j in range(C):
            print(grids[i][j][0], end="")
        print()