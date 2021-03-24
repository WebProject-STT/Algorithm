# 주식
# 뒤에서부터 생각하기!
import sys
input = sys.stdin.readline

t = int(input()) # testcase
answers = []

for _ in range(t) :
    n = int(input())
    stock_price = list(map(int, input().split()))

    profit = 0
    max_sp = stock_price[-1]

    for i in range(n-2, -1, -1) :
        if max_sp > stock_price[i] :
            profit += max_sp - stock_price[i]
        elif max_sp < stock_price[i] :
            max_sp = stock_price[i]
    answers.append(profit)

for answer in answers :
    print(answer)

''' 속도가 너무 오래 걸림
for _ in range(t) :
    n = int(input())
    stock_price = list(map(int, input().split()))
    max_sp = max(stock_price)
    if max_sp == stock_price[0] :
        answers.append(0)
    else :
        profit = 0
        for i in range(n) :
            if max_sp == stock_price[i] :
                if i < n - 1 :
                    max_sp = max(stock_price[i+1:])
            else :
                profit += max_sp - stock_price[i]
        answers.append(profit)

for answer in answers :
    print(answer)
'''

