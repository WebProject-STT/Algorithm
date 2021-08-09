import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        StringBuffer strBuff = new StringBuffer(); // 게임 진행 시 숫자에 대해 저장
        String[] decimal = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}; // 숫자 규칙 적용을 위해 만든 배열
        int gameCnt = t * m; // t * m번 안에 튜브가 t개의 숫자를 말함
        int num = 0; // 게임 숫자는 0부터 시작
        
        while (strBuff.length() < gameCnt) {
            if (num < n)
                strBuff.append(decimal[num]);
            else {
                StringBuffer subStrBuff = new StringBuffer(); // 현재 숫자의 n진법에 대해 임시로 저장할 str
                int temp = num;
                while (temp >= n) {
                    int mod = temp%n;
                    subStrBuff.append(decimal[mod]); // 나머지에 대해 저장
                    temp /= n;
                }
                subStrBuff.append(decimal[temp]); // 남아있는 몫에 대해서도 추가해줌
                strBuff.append(subStrBuff.reverse()); // 현재 저장된 subStrBuff를 뒤집어서 넣어야 올바르게 들어감
            }
            
            num++;
        }
        
        p--; // 숫자가 0부터 시작이므로 순서는 -1 해줘야 함
        for (int i = 0; i < t; i++) {
            answer += strBuff.charAt(p);
            p += m;
        }
        
        return answer;
    }
}
