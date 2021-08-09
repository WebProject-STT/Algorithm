# 택배

if __name__ == "__main__":
    N, C = map(int, input().split())
    M = int(input())
    box_info = [list(map(int, input().split())) for _ in range(M)]

    # 1. sort => 보내는 마을번호, 받는 마을 번호 순
    box_info = sorted(box_info, key=lambda x: x[1])

    boxs = [C]*N

    total_box = 0

    for s, r, b in box_info:
        temp_C = C
        for i in range(s, r):
            temp_C = min(temp_C, boxs[i])
        temp = min(temp_C, b)
        for i in range(s, r):
            boxs[i] -= temp
        total_box += temp
    
    print(total_box)
    
