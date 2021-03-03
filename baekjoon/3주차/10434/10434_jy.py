# 행복한 소수
num = int(input())
nums = []
max_ = 0
for _ in range(num):
    a, b = map(int, input().split())
    max_ = max(max_, b)
    nums.append([a, b])

result = [True]*(max_+1)
sqrt = int(len(result)**0.5)
for i in range(2, sqrt+1):
    if result[i]:
        for j in range(i+i, len(result), i):
            result[j] = False

temp, temp2 = [], []
for n in nums:
    if result[n[1]] and n[1] != 1:
        if n[1] in temp:
            print(n[0], n[1], 'YES')
        elif n[1] in temp2:
            print(n[0], n[1], 'NO')
        else:
            temp3, num = [n[1]], n[1]
            while True:
                s = 0
                for i in str(num): s+= (int(i)**2)
                if s in temp3:
                    for i in temp3: temp2.append(i)
                    print(n[0], n[1], 'NO')
                    break
                if s == 1: 
                    for i in temp3: temp.append(i)
                    print(n[0], n[1], 'YES')
                    break
                temp3.append(s)
                num = s
    else:
        print(n[0], n[1], 'NO')