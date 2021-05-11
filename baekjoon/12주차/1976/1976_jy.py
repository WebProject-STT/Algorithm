# 여행 가자
def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


if __name__ == "__main__":
    N = int(input())
    parents = [i for i in range(N+1)]
    M = int(input())

    for i in range(1, N+1):
        temp = input().split()
        for j in range(1, len(temp)+1):
            if temp[j-1] == '1':
                union(i, j)

    trip = list(map(int, input().split()))
    len_t = len(trip)
    if len_t <= 1: print("YES")
    else:
        pre = parents[trip[0]]
        for i in range(1, len_t):
            if pre != parents[trip[i]]: 
                print("NO")
                break
        else: print("YES")
