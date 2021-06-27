import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 백준 11053.가장 긴 증가하는 부분 수열
 * 10 20 10 30 20 50
 *  1  2  1  3  1  4
 * 입력 : 수열 A의 크기, 수열 A에 대한 숫자들
 * 출력 : 수열 A의 가장 긴 증가하는 부분 수열의 길이
 * */

class B11054 {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));

        int arrLen = Integer.parseInt(br.readLine());
        int[] arr = new int[arrLen];
        int[] dp = new int[arrLen]; // dp 구성
        int maxLen = 0;

        // arr 구성
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arrLen; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < arrLen; i++) {
            dp[i] = 1; // 처음 숫자의 길이는 1이므로 1로 초기화
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] && dp[i] < dp[j] + 1) // 이전 값이 현재 값보다 더 작으면서, 부분 수열의 길이가 작은 경우
                    dp[i] = dp[j] + 1;
            }
            maxLen = Math.max(maxLen, dp[i]); // 구하는 과정에서 max 값 계속 확인
        }

        System.out.println(maxLen);
    }
}