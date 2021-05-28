import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 백준 14430 자원캐기
 *
 * WOOK는 오른쪽 또는 아래쪽으로 한 칸 이동할 수 있으며, 그 외 방향으로의 이동은 불가능
 * WOOK는 자신이 위치한 위치에 자원이 있는 경우에만 해당 자원 채취 가능
 * => 오른쪽과 아래쪽의 경우에 대해 더 많은 광석을 캘 수 있는 경우를 기록하면 됨
 *
 *
 * 입력 : 세로 길이 n, 가로 길이 m, n행 m열에 걸친 탐사영역 정보
 * 출력 : WOOK이 수집할 수 있는 최대 광석의 개수
 * */

class B14430 {

    static int search(int N, int M, int[][] matrix) {
        int[][] dp = new int[N+1][M+1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                dp[i][j] = Math.max(dp[i-1][j] , dp[i][j-1]) + matrix[i][j];
            }
        }

        return dp[N][M];

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] matrix = new int[N+1][M+1];

        // 탐사 영역 생성
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(search(N, M, matrix));

    }
}