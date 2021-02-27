# 쇠막대기
# stack 이용

bars = input()
pre_s, cur_s = bars[0], ''
stack, result = [bars[0]], 0

for bar in bars[1:]:
    cur_s = bar
    if pre_s == "(" and cur_s == ")":
        stack.pop()
        result += len(stack)
    elif pre_s == ")" and cur_s == ")":
        stack.pop()
        result += 1
    else:
        stack.append(bar)
    pre_s = cur_s
print(result)