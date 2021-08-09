# 섬연결하기

def solution(n, costs):
    
    costs = sorted(costs, key=lambda x:x[2])
    checks = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]

    costs = costs[1:] # 0 번은으 set에 들어가 있음
    while len(checks) != n:
        for idx, cost in enumerate(costs):
            n1, n2, c = cost
            if n1 in checks and n2 in checks: continue
            # 둘 중 하나 노드만 들어가 있어야 다른 섬이랑 연결할 수 있음을 알기때문
            if n1 in checks or n2 in checks:
                checks.update([n1, n2])
                answer += c
                costs[idx] = [-1, -1, -1] # 들렸던곳 안가려고
                break
    return answer
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))