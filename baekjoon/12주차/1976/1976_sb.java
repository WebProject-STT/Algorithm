import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

/** 백준 1976 여행가자
 * 중간에 여행지를 경유할 수 있음 => union find
 * 입력 : 도시 수 N, 여행 계획에 속한 도시 수 M, N개의 도시 연결 정보, 여행 경로
 * 출력 : 계획한 경로대로 여행이 가능하면 YES 아니면 NO
 * */

class B1976 {
    public static int find(int[] parent, int x) { // 부모에 대해 찾는 함수
        if(parent[x] == x) return x;
        return parent[x] = find(parent, parent[x]);
    }

    public static void union(int[] parent, int a, int b) { // a, b의 부모 합치기
        a = find(parent, a);
        b = find(parent, b);
        if(a != b) parent[b] = a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); // 도시 수
        int M = Integer.parseInt(br.readLine()); // 여행 계획에 속한 도시 수
        String answer = "YES";

        int[] parent = IntStream.rangeClosed(0, N).toArray(); // 각 도시의 부모 정보, 0부터 N까지 생성
        int info; // 도시 연결 정보

        for (int i = 1; i < N + 1; i++) { // 도시 연결 정보를 입력 받음
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < N + 1; j++) {
                info = Integer.parseInt(st.nextToken());
                if (info == 1) // 연결된 경우 부모에 대한 정보 합치기
                   union(parent, i, j);
            }
        }

        st = new StringTokenizer(br.readLine());
        int start = find(parent, Integer.parseInt(st.nextToken())); // 첫번째 여행지 부모 정보 확인
        for (int i = 1; i < M; i++) { // 여행 경로를 입력 받음
            int now = find(parent, Integer.parseInt(st.nextToken())); // 현재 여행지 부모 정보 확인
            if (start != now) {
                answer = "NO";
                break;
            }
        }

        System.out.println(answer);
    }
}