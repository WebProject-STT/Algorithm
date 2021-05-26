# 리모컨
# 1초에 반복 횟수가 10^8 (1억)을 초과할 경우 시간 초과가 발생한다고 보기 때문에 충분히 여유있다.
# => max = 500000 - 6자리 / broke가 없으면 0 ~ 9 모두 입력 가능 -> 10^6
if __name__ == "__main__":
    N = int(input())
    M = int(input())

    broke = input().split()
    count = abs(100-N)

    for i in range(1000001):
        num = list(str(i))
        for n in num:
            if n in broke:
                break
        else:
            count = min(count, len(str(i))+abs(N-i)) # 번호 다 누르기 + 차이 만큼 + 또는 -
        
    print(count)
    


"""
5457
3
6 7 8

500000
8
0 2 3 4 6 7 8 9
"""