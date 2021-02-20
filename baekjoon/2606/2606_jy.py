computers = int(input())
pairs = int(input())
t_networks = [list(map(int, input().split())) for _ in range(pairs)]

networks = dict()
for i, j in t_networks:
    if i not in networks.keys():
        networks[i] = [j]
    else:
        networks[i].append(j)
    if j not in networks.keys():
        networks[j] = [i]
    else:
        networks[j].append(i)

def DFS(networks):
    visited = []
    stack = [1]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack = list(set(stack + networks[node]))
    return len(visited) - 1
print(DFS(networks))