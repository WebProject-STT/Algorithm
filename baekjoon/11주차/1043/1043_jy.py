# 거짓말
import sys
if __name__ == "__main__":
    N, M = map(int, input().split())
    T = set(input().split()[1:])# 진실을 아는 번호
    party, check = [], []
    for i in range(M):
        party.append(set(input().split()[1:]))
        check.append(1)
    len_p = len(party)

    for _ in range(M): # 거짓말 하는 모든 사람 번호 수집 해야함
        for idx in range(len_p):
            if party[idx] & T: # 교집합이 있으면 거짓말 x
                T = T | party[idx]
                check[idx] = 0
    print(sum(check))


"""
이야기 = 그대로 진실 or 엄청나게 과장
되도록 과장 but 진실을 아는 사람들이 있으면 진실을 이야기 해야함
=> 지민이가 거짓말쟁이로 알려지지 않으면서 과장된 이야기 할 수 있는 파티 수
"""