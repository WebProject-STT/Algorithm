import java.util.*;

/** 백준 1904 타일
* 입력 : 자연수 N
* 출력 : 만들 수 있는 길이가 N인 모든 2진 수열 개수를 15746으로 나눈 나머지
*/
class B1904 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int condition = 15746;
        
        if (N < 3)
            System.out.println(N);
        else {
            int[] dp = new int[N+1];
            dp[1] = 1;
            dp[2] = 2;
            for (int i = 3; i <= N; i++) {
                dp[i] = (dp[i-1] + dp[i-2]) % condition;
            }
            System.out.println(dp[N]);
        }
        
    }
}
