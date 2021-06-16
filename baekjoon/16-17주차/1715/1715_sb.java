import java.util.*;

/** 백준 1715 카드 정렬하기
*
* 정렬된 상태에서 가장 낮은 값부터 더하는 형태가 좋음 => 우선순위 큐 활용
*
* 입력 : 카드 묶음 수 N, N개의 카드 묶음 각각의 카드 수
* 출력 : 최소 비교 횟수
*/
public class B1715 {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        
        int answer = 0;
        int n = sc.nextInt();
        PriorityQueue<Integer> pque = new PriorityQueue<>();
        
        for (int i = 0; i < n; i++)
            pque.add(sc.nextInt());
        
        while (pque.size() > 1) {
            int num1 = pque.poll();
            int num2 = pque.poll();
            answer += num1 + num2;
            pque.add(num1 + num2);
        }
        
        System.out.println(answer);
        
    }
}
