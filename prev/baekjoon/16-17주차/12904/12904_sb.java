import java.io.*;
import java.util.*;

/** 백준 12094 A와 B
*
* 1. 문자열 뒤에 A 추가
* 2. 문자열 뒤집고 뒤에 B 추가
* => T를 S로 만들 수 있는지 확인하는 형태로 코드를 작성하는 것이 좋음 (그게 더 단순함)
* 5430 AC 문제와 유사한 느낌
* 
* 입력 : 문자열 S와 T
* 출력 : S를 T로 바꿀 수 있으면 1, 없으면 0
*/
class B12904 {
    public static String strReverse(ArrayDeque<Character> deque, boolean isReverse) {
        
        String temp = "";
        
        while(!deque.isEmpty()) {
            if (isReverse) { // 뒤집어진 상태
                temp += deque.pollLast();
            } else {
                temp += deque.pollFirst();
            }
        }

        return temp;
        
    }
    
    public static String strRemove(String s, String t) {
        int sLen = s.length();
        int tLen = t.length();
        int count = tLen - sLen; // 규칙을 수행할 횟수
        
        boolean isReverse = false; // 초기에는 뒤집지 않으므로 false 설정
        
        ArrayDeque<Character> deque = new ArrayDeque<>(); // 덱 초기화
        for (int i = 0; i < tLen; i++) {
            deque.add(t.charAt(i));
        }
        
        char c;
        while (count-- > 0) {
            if (isReverse) // 뒤집어진 상태이므로 앞에서 빼야함
                c = deque.pollFirst();
            else // 뒤집어지지 않은 상태이므로 뒤에서 빼야함
                c = deque.pollLast();
            if (c == 'B') // 빼낸 문자열이 B인 경우 뒤집어 줌
                isReverse = !isReverse;
        }
        
        return strReverse(deque, isReverse);
        
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        String t = br.readLine();
        
        t = strRemove(s, t);
        
        if (s.equals(t))
            System.out.println(1);
        else
            System.out.println(0);
    }
}
