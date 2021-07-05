# 데스노트

def dfs(cur_idx, cur_score): # 현재 줄에서, 지금 까지 쓴 이름 길이 + 띄어쓰기
    if cur_idx >= n: # 이름 다 돌았음
        return 0
    
    # 내가 갈 수 있는 경로 : 
    
    # (1) 포함 안시킴 -> 다음 줄로 넘어감
        # 다음 줄에 길이 names[cur_idx] + 1(1은띄어쓰기)
    min_ = (m-cur_score+1)**2 + dfs(cur_idx+1, names[cur_idx] + 1) 

    # (2) 현재 단어를 현재 줄에 포함
    if cur_score + names[cur_idx] <= m:
        min_ = min(min_, dfs(cur_idx+1, cur_score + names[cur_idx] + 1))

    return min_

if __name__ == "__main__":
    n, m = map(int, input().split())
    names = []
    for _ in range(n):
        names.append(int(input()))

    print(dfs(0, 0))