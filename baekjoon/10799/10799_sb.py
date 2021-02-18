# 쇠막대기

inputData = input()

stack = []

cnt = 0
prev = ''
for data in inputData:
    if data == '(':
        stack.append(data)
    else:
        if prev == '(': # 레이저
            stack.pop()
            cnt += len(stack)
        else: # 쇠막대기끝부분
            stack.pop()
            cnt += 1
    prev = data
print(cnt)
