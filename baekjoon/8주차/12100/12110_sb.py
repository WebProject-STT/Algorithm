# 2048 (Easy)
import sys

def up(board) : # 위로 이동
    for c in range(N) : # N번 반복을 통해 모든 열에 대해 수행
        stack = []
        check = 0
        for r in range(N) :
            if board[r][c] > 0 :
                if len(stack) > 0 and stack[-1] == board[r][c] and check == 0 :
                    stack.append(stack.pop() + board[r][c])
                    check = 1
                else :
                    stack.append(board[r][c])
                    check = 0
        for r in range(N) :
            if 0 <= r < len(stack) : board[r][c] = stack[r]
            else : board[r][c] = 0
    return board
        

def down(board) : # 아래로 이동
    for c in range(N) : # N번 반복을 통해 모든 열에 대해 수행
        stack = []
        check = 0
        for r in range(N - 1, -1, -1) :
            if board[r][c] > 0 :
                if len(stack) > 0 and stack[-1] == board[r][c] and check == 0 :
                    stack.append(stack.pop() + board[r][c])
                    check = 1
                else :
                    stack.append(board[r][c])
                    check = 0
        for r in range(N) :
            if 0 <= (N - r - 1) < len(stack) : board[r][c] = stack[N - r - 1]
            else : board[r][c] = 0
    return board

def left(board) : # 왼쪽으로 이동
    for r in range(N) : # N번 반복을 통해 모든 열에 대해 수행
        stack = []
        check = 0
        for c in range(N) :
            if board[r][c] > 0 :
                if len(stack) > 0 and stack[-1] == board[r][c] and check == 0 :
                    stack.append(stack.pop() + board[r][c])
                    check = 1
                else :
                    stack.append(board[r][c])
                    check = 0
        for c in range(N) :
            if 0 <= c < len(stack) : board[r][c] = stack[c]
            else : board[r][c] = 0
    return board

def right(board) : # 오른쪽으로 이동
    for r in range(N) : # N번 반복을 통해 모든 열에 대해 수행
        stack = []
        check = 0
        for c in range(N - 1, -1, -1) :
            if board[r][c] > 0 :
                if len(stack) > 0 and stack[-1] == board[r][c] and check == 0 :
                    stack.append(stack.pop() + board[r][c])
                    check = 1
                else :
                    stack.append(board[r][c])
                    check = 0
        for c in range(N) :
            if 0 <= (N - c - 1) < len(stack) : board[r][c] = stack[N - c - 1]
            else : board[r][c] = 0
    return board

def find_max(board) :
    global max_
    for b in board :
        temp = max(b)
        max_ = max(max_, temp)

def dfs(copy_board, L) : # 복사본을 보내야 여러 경우에 대한 확인 가능
    global max_
    if L == 5 :
        find_max(copy_board)
        return
    dfs(up([copy[:] for copy in copy_board]), L + 1)
    dfs(down([copy[:] for copy in copy_board]), L + 1)
    dfs(left([copy[:] for copy in copy_board]), L + 1)
    dfs(right([copy[:] for copy in copy_board]), L + 1)

if __name__=="__main__" :
    input = sys.stdin.readline

    N = int(input()) # 보드 크기
    board = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    dfs(board, 0)
    print(max_)
    # print(up(board))
    # print(down(board))
    # print(left(board))
    # print(right(board))
    

'''
N*N 크기의 보드
2048 게임과 유사 하나 새로운 블록 추가 없이 처음 주어진 블록으로만 진행
최대 5번, 상하좌우로 모두 이동하는 경로에 대해 생각해야함
같은 수의 블록이 나오는 경우 합쳐야 함 => 한 번 합쳐진 블록은 다시 합칠 수 없음
이전 값과 같은 값이 나온 경우 합치는 방식으로 stack에 넣어서 진행 - 합쳐진 블록인지에 대한 체크가 필요함
4 4 8 8 인 경우 4 + 4 = 8, 합쳐짐 =>check
현재 스택에 8이 있고 다음 수가 8이지만 check가 있으므로 합치지 않음 => check 해제
스택에 8 8이 들어있는 상태이고 다음 수가 8, chekc가 해제되어 있으므로 합칩ㅁ => check
--- up
4
4 0 0 0
4 0 0 0
8 0 0 0
8 0 0 0
--- down
4
4 0 0 0
4 0 0 0
2 0 0 0
2 0 0 0
--- down2
5
8 0 0 0 0
4 0 0 0 0
8 0 0 0 0
4 0 0 0 0
2 0 0 0 0
--- left
4
4 4 8 8
0 0 0 0
0 0 0 0
0 0 0 0
--- right
4
4 4 2 2
0 0 0 0
0 0 0 0
0 0 0 0
'''