import java.io.*;
import java.util.StringTokenizer;

/** 백준 12865 평범한 배낭
 *
 * 입력 : 물품 수 N, 준서가 버틸 수 있는 무게 K, (N개) 각 물건의 무게 W, 물건의 가치 V
 * 출력 : 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
 *
 *   K     0  1  2  3  4  5  6  7
 * item1 6 0  0  0  0  0  0  13 13
 * item2 4 0  0  0  0  8  8  13 13 (이전에 넣은 물건의 가치와 현재 물건의 가치 비교)
 * item3 3 0  0  0  6  8  8  13 14 (이전에 넣은 물건의 가치와 합이 K가 될 때의 가치 비교)
 * item4 5 0  0  0  6  8  12 13 14
 * => 물건 K에 대한 가치합의 최댓값은 14
 * => 이전에 넣은 물건의 K 무게일 때의 가치와 현재 무게와 더해서 합이 K 무게일 때의 가치 비교
 *
 * */

class B12865 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] WV = new int[N+1][2]; // dp 규칙을 편하게 적용하기 위해 1칸을 더 생성

        for (int i = 1; i <= N; i++) { // dp 규칙을 적용하기 위해 1부터 시작
            st = new StringTokenizer(br.readLine());
            WV[i][0] = Integer.parseInt(st.nextToken());
            WV[i][1] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N+1][K+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                if (j - WV[i][0] >= 0) { // 현재 무게에 특정 무게를 더해 j를 만들 수 있는 경우
                    dp[i][j] = Math.max(dp[i-1][j], WV[i][1] + dp[i-1][j-WV[i][0]]); // 이전 아이템의 현재 무게에 대한 가치와
                                                                                     // 현재 무게 더하기 합 j를 만들 수 있는 위치의 이전 아이템의 가치 합 비교
                } else { // j보다 큰 경우
                    dp[i][j] = dp[i-1][j]; // 이전 아이템의 현재 무게에 대한 가치를 그대로 기록
                }
            }
        }

        System.out.println(dp[N][K]);

        br.close();
    }

}