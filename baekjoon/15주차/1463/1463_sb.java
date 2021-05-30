import java.util.Scanner;

/** 백준 1463 1로 만들기
 * 입력 : 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N
 * 출력 : 연산 횟수의 최솟값
 * */

class B1463 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N+1];

        if (N < 2)
            System.out.println(0);
        else {
            for (int i = 2; i <= N; i++) {

                // 3. 1을 뺌
                // => 이 조건을 먼저 수행하는 이유? 3가지의 조건 중 가능한 경우에 대해 비교를 하는 과정이 필요하며,
                //    1을 빼는 경우는 3이나 2로 나누어 떨어지든 아니든 무조건 수행되기 때문에
                dp[i] = dp[i-1] + 1;

                if (i%3 == 0) { // 1. 3으로 나누어떨어지면 3으로 나눔
                    dp[i] = Math.min(dp[i], dp[i/3] + 1);
                }

                if (i%2 == 0) { // 2. 2로 나누어떨어지면 2로 나눔
                    dp[i] = Math.min(dp[i], dp[i/2] + 1);
                }
            }

            System.out.println(dp[N]);
        }

    }
}