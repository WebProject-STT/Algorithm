import java.io.*;
import java.util.*;
import java.lang.*;

/** 백준 14501 퇴사
*
* 
*
* 입력 : 퇴사까지 남은 기간 N (N+1일에 퇴사), 상담 기간 T, 받을 수 있는 금액 P
* 출력 : 얻을 수 있는 최대 이익
*/

public class B14501 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine()); // 퇴사까지 남은 기간 
        
        int[] T = new int[N];
        int[] P = new int[N];
        int[] dp = new int[N+1];
        
        // 상담 기간 및 금액에 대한 정보
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }
        
        // 날짜별 최대 이익 계산
        for (int i = 0; i < N; i++) {
            if(i + T[i] <= N) // 날짜 범위가 넘어가지 않는 경우 기간에 대한 계산을 해줌
                dp[i + T[i]] = Math.max(dp[i + T[i]], dp[i] + P[i]);
            dp[i+1] = Math.max(dp[i], dp[i+1]); // 현재 날짜는 i + 1이고, 이전까지의 최대 수당과 현재 수당을 비교하여 최댓값을 넣어줌
        }
        
        System.out.println(dp[N]);
        
    }
}
