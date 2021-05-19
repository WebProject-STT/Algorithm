import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/** 백준 1309 동물원
 *
 * 사자를 넣지 않은 경우, 사자 넣기를 왼쪽부터 시작, 사자 넣기를 오른쪽부터 시작
 * 이렇게 총 세 가지 경우가 존재함
 *
 * 입력 : 우리의 크기 N
 * 출력 : 사자를 배치하는 경우의 수
 * */

class B1309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int conditionNum = 9901;

        int[][] dp = new int[N][3];

        Arrays.fill(dp[0], 1); // N이 1일 때 모든 경우가 1개씩 존재

        for (int i = 1; i < N; i++) {
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % conditionNum; // 넣지 않음
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % conditionNum; // 오른쪽
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % conditionNum; // 왼쪽
        }

        int answer = 0;
        for (int i = 0; i < 3; i++) {
            answer = (answer + dp[N-1][i]) % conditionNum;
        }

        System.out.println(answer);
    }
}