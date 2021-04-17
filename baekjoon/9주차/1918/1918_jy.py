# 후위 표기식
import sys

if __name__ == "__main__":
    notation = sys.stdin.readline()[:-1]
    stack = []
    result = ""

    check = {
        '*':3, '/':3, '+':2, '-':2, '(':1
    }

    for n in notation:
        if n not in "()+-*/": # 알파벳
            result += n
        elif n == "(": stack.append(n)
        elif n == ")": #pop!
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop() # ( 빼기
        elif n in "+-*/":
            while stack:
                if stack and check[n] <= check[stack[-1]]:
                    result += stack.pop()
                else: break
            stack.append(n)
    
    while stack: 
        result += stack.pop()

    print(result)

