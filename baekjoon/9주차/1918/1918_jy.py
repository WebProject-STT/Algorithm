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
        if n not in "()+-*/": # 피연산자 > 연산자 이므로 알파벳은 바로 출력
            result += n
        elif n == "(": stack.append(n)
        elif n == ")": # ")" 를 만나면 "("만나기 전까지 연산자들을 빼줘야 한다
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop() # ( 빼기
        elif n in "+-*/":
            while stack:
                # 현재 연산자보다 stack에 있는 연산자가 우선순위가 높으면 pop!
                if stack and check[n] <= check[stack[-1]]: 
                    result += stack.pop() # pop한것은 바로 붙여줘야한다
                else: break
            stack.append(n) # 현재 연산자 추가해주기
    
    while stack: #stack에 남아 있으면 출력
        result += stack.pop()

    print(result)

