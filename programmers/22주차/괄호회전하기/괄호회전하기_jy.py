def solution(s):
    answer = 0
    
    s = list(s.strip())
    len_s = len(s)
    if len_s == 1: return 0
    if set(s) in ({'['}, {'('}, {'{'}, {']'}, {')'}, {'}'}): return 0
    for i in range(len_s):
        if i > 0:
            s.append(s.pop(0))
        
        stack = []
        for idx in range(len_s):
            if s[idx] in ('[', '(', '{'): stack.append(s[idx])
            elif stack and \
                ((s[idx] == "]" and stack[-1] == "[") or (s[idx] == ")" and stack[-1] == "(") or (s[idx] == "}" and stack[-1] == "{")): stack.pop()
            else: break
        else:
            if not stack: answer += 1

    return answer

print(solution("{{{}"))

"""
(), [], {} => 모두 올바른 괄호
"""