# 후위 표기식

text = input()
answer = ''
stack = [] # 연산자 관리용

for t in text :
    if t.isalpha() : # 피연산자
        answer += t
    else : # 연산자
        if t == '(' :
            stack.append(t)
        elif t == '*' or t == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                answer += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.append(t)
        elif t == ')' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.pop() # '('를 빼는 작업

while stack :
    answer += stack.pop()

print(answer)

'''
중위 표기식으로 주어진 값을 후위 표기식으로 변경하는 문제이다.
즉, A+B를 AB+와 같이 피연산자 다음에 연산자를 쓰는 형태이다.
피연산자는 알파벳으로 주어진다.
--- 풀이
결과값이 문자로 출력되므로 문자열로 관리한다.
피연산자의 경우 문자열에 그냥 더해준다.
연산자의 경우 우선순위를 정하고 우선 순위에 맞춰서 stack에 추가하거나 빼는 형태로 진행한다.
우선순위 : (, */, +-, )
( => stack에 추가
*/ => * 나 / 인 경우에만 pop 진행
+- => ( 를 만날 때까지 pop
) => ( 를 민날 때까지 pop해준 뒤, ( 제거를 위해 pop를 한 번 더 수행
--- 예
입력 : A+B*C-D/E
출력 : ABC*+DE/-
'''