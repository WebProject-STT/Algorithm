import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 백준 18427 함께 블록 쌓기
 * 입력 : 학생 수 N, 최대 블록 수 M, 만들려는 탑 높이 H, N명 학생의 블록 높이 정보
 * 출력 : 높이가 H인 탑을 만드는 경우의 수를 10,007로 나눈 나머지
 * */

class B18427 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 학생 수
        int M = Integer.parseInt(st.nextToken()); // 최대 블록 수
        int H = Integer.parseInt(st.nextToken()); // 만들려는 탑의 높이
        int conditionNum = 10007; // 조건 : 10007로 나눈 나머지를 저장해야 함

        int[][] dp = new int[N+1][H+1]; // 각 학생이 만들 수 있는 높이 정보
        for (int i = 1; i <= N; i++) { // 각 학생별로
            st = new StringTokenizer(br.readLine());
            int blockNum = st.countTokens(); // 블록의 총 개수
            for (int j = 0; j < blockNum; j++) { // 가지고 있는 블록 별로
                int block = Integer.parseInt(st.nextToken()); // 현재 블록
                dp[i][block] += 1;
                for (int k = block + 1; k <= H; k++) {
                    dp[i][k] = (dp[i][k] + dp[i-1][k-block]) % conditionNum;
                }
            }
            // 현재 사람에 대한 경우의 수를 모두 구했으므로 이전 사람의 경우의 수를 더해줌
            for (int j = 1; j <= H; j++) {
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % conditionNum;
            }
        }

        System.out.println(dp[N][H]);
        br.close();
    }
}