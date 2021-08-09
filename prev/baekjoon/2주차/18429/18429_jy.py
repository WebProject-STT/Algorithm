N, K = map(int, input().split())
kits = list(map(int, input().split()))
total = 0
gravity = 500
def perm(days, cur_num):
    global total
    if cur_num == N:
        temp = gravity
        for j in days:
            temp = (temp + kits[j-1] - K)
            if temp < gravity: break
        else:
            total += 1
        return
    for i in range(cur_num, N):
        days[i], days[cur_num] = days[cur_num], days[i]
        perm(days, cur_num+1)
        days[i], days[cur_num] = days[cur_num], days[i]

perm([i for i in range(1, N+1)], 0)
print(total)