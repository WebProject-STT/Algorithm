import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B2156 {
    public static void main(String[] args) throws Exception{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        int[] grapes = new int[n];
        int[] dp = new int[n];

        // 포도주 양 입력 받기
        for (int i = 0; i < n; i++) {
            grapes[i] = Integer.parseInt(bf.readLine());
        }

        // 포도주 양 계산
        if (n >= 1)
            dp[0] = grapes[0];
        if (n >= 2)
            dp[1] = grapes[0] + grapes[1];
        if (n >= 3) {
            dp[2] = Math.max(dp[1], Math.max(dp[0] + grapes[2], grapes[1] + grapes[2]));
            for (int i = 3; i < n; i++)
                dp[i] = Math.max(dp[i - 1], grapes[i] + Math.max(dp[i - 2], dp[i - 3] + grapes[i - 1]));
        }
            System.out.println(dp[n-1]);
    }
}
/* 포도주 시식 규칙
* 연속으로 3잔을 마실 수 없음!
* 한 잔 => dp[0] = grapes[0]
* 두 잔 => dp[1] = grapes[0] + grapes[1]
* 세 잔 - 현재 와인 제외 (1 + 2), 현재 와인과 이전 와인 (2 + 3), 이전 와인 제외 (1 + 3)
* => dp[i - 1], grapes[i] + grapes[i-1], grapes[i] + dp[i-2]
* 네 잔부터는 다음과 같음
*   1. 현재 와인 제외 - 이전 dp 값
*   2. 현재 와인과 이전 와인 - 현재 와인과 이전 와인의 합 + 현재 와인 - 3 위치의 dp (세 잔 연속이 불가하므로)
*   3. 이전 와인 제외 - 현재 와인과 이전 와인의 전에 대한 dp 값의 합
* */