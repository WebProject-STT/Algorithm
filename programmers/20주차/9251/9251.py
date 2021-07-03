# lcs

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    # DP 배열 생성
    len_s1 = len(s1)+1
    len_s2 = len(s2)+1
    dp = [[0 for _ in range(len_s1)] for _ in range(len_s2)]

    # TABLE 생성
    max_ = 0
    for i in range(1, len_s2):
        for j in range(1, len_s1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_ = max(max_, dp[i][j])
    
    print(max_)