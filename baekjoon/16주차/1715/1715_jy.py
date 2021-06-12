# 카드 정렬하기
import heapq
if __name__ == "__main__":
    N = int(input())

    nums = [int(input()) for _ in range(N)]

    if N == 1:
        print(0)
    else:
        heapq.heapify(nums)

        total = 0

        while len(nums) >= 2:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            total += (n1+n2)
            heapq.heappush(nums, n1+n2)
        print(total)
