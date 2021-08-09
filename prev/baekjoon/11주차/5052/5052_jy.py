# 전화번호 목록
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        check = False
        nums = [input() for _ in range(N)]
        nums.sort()
        for i in range(N-1):
            if nums[i] == nums[i+1][:len(nums[i])]:
                print("NO")
                break
        else:
            print("YES")



"""
전화번호 목록
[일관성 유지] - 한 번호가 다른 번호의 접두어 X
[이런 경우 일관성 X]
긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26

# sort -> 사전 순으로 sort되기 때문에 
1 1 2
1 1 3
1 1 3 4 5
1 2 4 5 6
1 3 3 4 7 이런식으로 sort됨 
그러므로 전꺼 길이만큼 현재꺼 확인하면 댐
"""