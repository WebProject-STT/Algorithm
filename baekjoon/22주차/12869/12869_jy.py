# 뮤탈리스크
"""
12 10 4

[1] -3, -9, -1 => 9, 1, 3 => [13]
    -9, -1, -3 => 3, 9, 1 => [13]
    -1, -9, -3 => 11, 1, 1 => [13]
    -1, -3, -9 => 11, 7, -5 => [18]

[2] -9, -1, -3 => 0, 0, 0 => []

=> 최솟 값 2번

54 18 6

[1] -9, -3, -1 => 6 
"""

from collections import deque
if __name__ == "__main__":
    N = int(input())

    life = list(map(int, input().split()))

    if N==1: 
        result = life[0]//9 + 1 if life[0]%9 else life[0]//9
        print(result)
    else:
        # N==3이면 조합 6개. N==2이면 조합 2개
        combis = [(9, 3, 1), (9, 1, 3), (3, 9, 1),\
             (3, 1, 9), (1, 9, 3), (1, 3, 9)] if N==3 \
                 else [(9, 3), (3, 9)]
        
        mins = deque()
        mins.append([life, 0])
        min_value = 181

        check = True

        visited = [life]

        while True:
            current, count = mins.popleft()

            # combi 모두 확인
            for combi in combis:
                temp = []
                temp_count = 0
                for l, c in zip(current, combi):
                    if l-c >= 0: 
                        temp.append(l-c)
                        temp_count += 1
                    else: temp.append(0)
                
                temp_sum = sum(temp)
                if temp_sum <= 0:
                    print(count+1)
                    check = False
                    break

                if temp in visited: continue
                else: visited.append(temp)
                
                if (N==3 and temp_count==3) or (N==2 and temp_count==2):
                    mins.appendleft([temp, count+1])
                    min_value = temp_sum
                else:
                    mins.append([temp, count+1])
            
            if not check: break
        


        



        
"""
수빈 - 뮤탈리스크 1개
강화 - SCV N개

SCV = 남아 있는 체력, 뮤탈리스크 공격 X
즉, 이 게임에서는 수빈이가 이김

뮤탈리스크가 공격할 때, 
    한 번에 세 개의 SCV를 공격 가능
    [1] 첫 번째로 SCV는 -9
    [2] 두 번째로 SCV는 -3
    [3] 세 번째로 SCV는 -1

SCV 체력이 0 or 그 이하면 SCV 파괴

=> 남아 있는 SCV 체력이 주어졌을 때, 모든 SCV를 파괴
하기 위해 공격해야 되는 횟수의 최솟값 출력
"""