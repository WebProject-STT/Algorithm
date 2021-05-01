import java.util.*;

class Solution_0501 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int start = 0, end = people.length - 1;

        Arrays.sort(people);

        while (start <= end) {
            if ((people[start] + people[end]) <= limit) // 합이 작은 경우, 몸무게 작은 사람 큰 사람 함께 태움
                start++;
            end--; // 합이 큰 경우, 몸무게가 큰 사람만 태움 => 무조건 몸무게가 큰 사람은 타는 구조
            answer++; // 매 수행마다 구명보트에 타는 사람 존재
        }

        return answer;
    }
}