import java.util.Scanner;

/** 백준 9251.LCS
 * 입력 : 문자열 2개
 * 출력 : 두 문자열의 부분 수열 중 가장 긴 수열 찾기
 * if (s1[i] == s2[j])
 *     dp[i][j] = dp[i-1][j-1] + 1;
 * else
 *     dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
 *   0 A C A Y K P
 * 0 0 0 0 0 0 0 0
 * C 0 0 1 1 1 1 1
 * A 0 1 1 2 2 2 2
 * P 0 1 1 2 2 2 3
 * C 0 1 2 2 2 2 3
 * A 0 1 2 3 3 3 3
 * K 0 1 2 3 3 4 4
 * */

class B9251  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] s1 = sc.nextLine().toCharArray();
        char[] s2 = sc.nextLine().toCharArray();
        int s1Len = s1.length;
        int s2Len = s2.length;
        int[][] dp = new int[s1Len + 1][s2Len + 1];

        for (int i = 0; i <= s1Len; i++) {
            for (int j = 0; j <= s2Len; j++) {
                if (i == 0 || j == 0)
                    dp[i][j] = 0; // 0으로 채워줘야하는 영역
                else if (s1[i-1] == s2[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        System.out.println(dp[s1Len][s2Len]);
    }
}