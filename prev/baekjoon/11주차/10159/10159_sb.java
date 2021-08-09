import java.io.*;
import java.util.StringTokenizer;

/** 백준 10159 저울
 *
 * 플로이드-와샬 알고리즘을 적용하여 풀어야 함
 * 플로이드-와샬 : 모든 정점에서모든 정점으로의 최단 거리를 구하는 알고리즘으로, 거쳐가는 정점을기준으로 알고리즘 수행
 * 제일 바깥쪽 반복문은 거쳐가는 꼭짓점, 두 번째 반복문은 출발하는 꼭짓점, 세 번째 반복문은 도착하는 꼭짓점 (반복문 3개 중첩)
 * 여기서는 거쳐가는 정점을 이용하여 연결되어 있는지 확인
 *
 * 입력 : 물건 수 N, 물건 쌍의 수 M, M개의 물건쌍 (물건1 > 물건2 순서)
 * 출력 : i번째 줄에 물건 i와 비교 결과를 알 수 없는 물건 개수 출력
 * */

class B10159 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine()); // 물건 수
        int M = Integer.parseInt(br.readLine()); // 물건 쌍의 수

        StringTokenizer st;
        int[][] relation= new int[N+1][N+1];

        int num1, num2;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            num1 = Integer.parseInt(st.nextToken());
            num2 = Integer.parseInt(st.nextToken());
            relation[num1][num2] = 1; // num1 > num2
            relation[num2][num1] = -1; // num1 < num2
        }

        floydWarshall(N, relation);

        int cnt;
        for (int i = 1; i <= N; i++){
            cnt = N-1; // 자신을 제외한 전체 물건 수
            for (int j = 1; j <= N; j++) {
                if (relation[i][j] != 0) // 물건의 관계에 대해 아는 경우
                    cnt--; // 아는 만큼 줄여줌
            }
            bw.write(String.valueOf(cnt) + '\n');
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static int[][] floydWarshall(int N, int[][] relation) {

        for (int k = 1; k <= N; k++) { // 거처가는 꼭짓점
            for (int s = 1; s <=N; s++) { // 출발하는 꼭짓점
                for (int e = 1; e <= N; e++) { // 도착하는 꼭짓점
                    if (relation[s][k] != 0 && relation[s][k] == relation[k][e]) {
                        // 0이 아닐 때 => s가 k보다 무거운 또는 가벼운 물건일 때
                        // s-k와 k-e가 같으면 s-e도 같으므로 s-e에 s-k값 대입하여 서로 알 수 있도록 해줌
                        relation[s][e] = relation[s][k];
                    }
                }
            }
        }

        return relation;

    }

}