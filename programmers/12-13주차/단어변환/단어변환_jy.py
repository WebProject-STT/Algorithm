# 단어변환

from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    len_b, len_w = len(begin), len(words)
    queue = deque()
    queue.append((begin, 0))
    visited = [0]*len_w

    while queue:
        word, count = queue.popleft()
        if word == target:
            return count

        for idx, w in enumerate(words):
            if not visited[idx]:
                for i in range(len_b): # 해당 위치 글자만 다를 경우
                    if w[i] != word[i]:
                        if (i != len_b and w[:i]==word[:i] and w[i+1:] == word[i+1:]) or (i == len_b and w[:i]==word[:i]):
                            visited[idx] = 1
                            queue.append((w, count + 1))


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

"""
두 개의 단어 begin, target과 단어 집합 words가 있습니다.
begib -> target으로 변환하는 가장 짧은 변환 과정
1. 한 번에 한 개의 알파벳만 바꿀 수 있음
2. words에 있는 단어로만 변환할 수 있음
 hit => hot => dot => dog => cog [4단계]

최소 -> BFS

"""