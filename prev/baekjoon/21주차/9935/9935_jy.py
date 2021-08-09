# 문자열 폭발
if __name__ == "__main__":
    string = input()
    boom = list(map(str, input().strip()))

    stack = []
    
    check_len = -len(boom)
    last = boom[-1]
    for s in string:
        stack.append(s)
        if s == last and stack[check_len:] == boom:
            del stack[check_len:]          

    if not stack: print("FRULA")
    else: print(''.join(stack))


"""
문자열 시간 초과 => stack 이용해 보기
if __name__ == "__main__":
    string = input()
    boom = input()

    stack = ""
    
    check_len = -len(boom)
    last = boom[-1]

    for s in string:
        stack += s
        if s == last and stack[check_len:] == boom:
            stack = stack[:check_len]           

    if stack == "": print("FRULA")
    else: print(stack)
"""