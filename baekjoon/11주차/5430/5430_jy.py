# AC

import sys
from collections import deque

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        pp = sys.stdin.readline()
        n = int(input())
        arr = deque()
        for a in sys.stdin.readline()[1:-2].split(','):
            if a == '': arr = []
            else: arr.append(a)
        # 사실상 뒤집기는 D를 만나기 전까지 안뒤집어도 됨
        r = False # False는 뒤집x,True면 뒤집o
        for p in pp:
            if p == 'R' and r:
                r = False
            elif p == 'R' and not r:
                r = True
            elif p == 'D':
                if arr:
                    if r: # 뒤집을 수 있다면 -> 뒤집고 delete -> 즉 뒤에꺼 빼주면 됨
                        arr.pop() # 맨뒤에꺼 빼주기
                    else:
                        arr.popleft() # 맨 앞에꺼 빼주기ㅣ
                else:
                    print('error')
                    break
        else:
            len_arr = len(arr)
            if r:
                arr.reverse()
                print("[", end="")
                for i in range(len_arr):
                    print(arr[i], end="")
                    if i != len_arr-1:
                        print(",", end="")
                print("]")
            else:
                print("[", end="")
                for i in range(len_arr):
                    print(arr[i], end="")
                    if i != len_arr-1:
                        print(",", end="")
                print("]")

"""
3시 10분 ~ 
새로운 언어 AC
함수 2가지
[1] R (뒤집기)
    배열에 있는 숫자의 순서 뒤집
[2] D (버리기)
    첫번째 숫자 버림(배열 있을때만)
함수는 조합해서 사용가능
최종 결과를 구하는 프로그램 작성
"""

"""
import sys
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        pp = sys.stdin.readline()
        len_pp = len(pp)
        n = int(sys.stdin.readline())
        arr = sys.stdin.readline()[1:-2].split(',')
        if arr[0] == '': arr = []
        if 'D' not in pp:
            if len_pp%2 == 0: print(arr)
            else: print(arr[::-1])
        elif 'R' not in pp:
            if len_pp > len(arr): print('error')
            else: print(arr[len_pp:])
        else:
            print("check : ", arr, pp)
            re_check = False
            for p in pp:
                if p == 'R' and re_check: 
                    re_check = False
                elif p == 'R' and not re_check:
                    re_check = True
                elif p == 'D':
                    if arr:
                        if re_check:
                            arr = arr[:-1]
                        else:
                            arr = arr[1:]
                    else:
                        print('error')
                        break
            else:
                if re_check:
                    print(arr[::-1])
                else:
                    print(arr)
"""