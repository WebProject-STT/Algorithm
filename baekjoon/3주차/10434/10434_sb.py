# 행복한 소수

p = int(input()) # testcase

case = [list(map(int, input().split())) for _ in range(p)]

max_num = max(case)[1] # 가장 큰 숫자를 뽑아냄

check = [1] * (max_num + 1) # 가장 큰 수를 기준으로 소수인지 확인하기 위한 리스트 생성

check[0], check[1] = 0, 0

# 에라토스테네스 체를 활용하여 소수 확인
for i in range(2, max_num + 1):
    if check[i] :
        for j in range(2*i, max_num+1, i):
            check[j] = 0

# 행복한 소수 찾기
for i in range(p):
    num = case[i][1]
    if check[num]: # 소수인 경우
        tempList = []
        while (True) :
            if num == 1:
                print(case[i][0], case[i][1], "YES")
                break
            if num < 10:
                num = num**2
            else:
                temp = 0
                while (num >= 10) :
                    temp += (num%10)**2
                    num = num//10
                temp += num**2
                num = temp
                if num in tempList:
                    print(case[i][0], case[i][1], "NO")
                    break
                tempList.append(num)
    else: # 소수가 아닌 경우
        print(case[i][0], case[i][1], "NO")
