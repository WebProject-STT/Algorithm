import java.util.*;

/** 섬 연결하기
* 1. 비용을 기준으로 정렬
* 2. Union Find 알고리즘을 이용해 모든 노드를 연결한다.
*    (이미 연결된 노드는 넘어가면 되며, 부모 노드가 같게 나와야 함)
*/

class P42861 {
    // 부모 찾기
    public static int find(int[] parent, int x) {
        if(parent[x] == x) return x;
        return parent[x] = find(parent, parent[x]);
    }

    public int solution(int n, int[][] costs) {
        int answer = 0;
        int costsLen = costs.length;
        int[] parent = new int[n]; // 부모 노드에 대해 기록
        
        // 비용을 기준으로 오름차순 정렬
        Arrays.sort(costs, (int[] c1, int[] c2) -> c1[2] - c2[2]);
        
        // 초기에 부모는 자기 자신으로 설정
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Union-Find 알고리즘을 응용해 부모 찾기
        for (int i = 0; i < costsLen; i++) {
            int first = find(parent, costs[i][0]);
            int second = find(parent, costs[i][1]);
            if (first != second) { // 두 노드의 부모가 같지 않은 경우 => 연결이 안된 상태
                answer += costs[i][2];
                parent[second] = first; // 서로 다른 부모이므로 합쳐줌
            }
        }
        
        return answer;
    }
}
