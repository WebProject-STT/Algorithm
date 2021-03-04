# 행렬
N, M = map(int, input().split())
A = [[int(i) for i in input()] for _ in range(N)]
B = [[int(i) for i in input()] for _ in range(N)]

count = 0
for row in range(N-2):
    for col in range(M-2):
        if A[row][col] != B[row][col]:
            count += 1
            for i in range(3):
                for j in range(3):
                    A[row+i][col+j] ^= 1

for i in range(N):
    if A[i] != B[i]: 
        print(-1)
        break          
else:   
    print(count)