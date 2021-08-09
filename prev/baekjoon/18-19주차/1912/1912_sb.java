import java.io.*;
import java.util.*;

/** 백준 1912 연속합
*
* 숫자 : 10 -4  3  1  5  6 -35 12 21 -1
* 연속 : 10  6  9 10 15 21 -14 12 33 32
* 최대 : 10 10 10 10 15 21  21 21 33 33
*
* 입력 : 정수의 수 n, n개의 정수
* 출력 : 연속된 숫자의 합 중 가장 큰 합
*/
class B1912 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        int[] dp = new int[n]; // 구간합에 대한 기록 저장
        int answer; // 최대합에 대한 정보 저장
        
        // 숫자에 대해 입력받아 옴
        for (int i = 0; i < n; i++)
            nums[i] = Integer.parseInt(st.nextToken());
        
        answer = dp[0] = nums[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
            answer = Math.max(answer, dp[i]);
        }
        
        System.out.println(answer);
    }
}
