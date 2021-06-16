import java.util.*;

// 카카오프렌즈 컬러링북
class P1829 {
    class Node {
        int r;
        int c;
        int info; // 색칠 영역에 대한 정보
        Node(int r, int c, int info) {
            this.r = r;
            this.c = c;
            this.info = info;
        }
    }
    public int bfs(int m, int n, int i, int j, int[][] picture, boolean[][] isVisited) {
        int sizeOfOneArea = 1;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        Queue<Node> queue = new LinkedList<>();
        Node node;
        
        isVisited[i][j] = true;
        queue.offer(new Node(i, j, picture[i][j]));
        
        while (!queue.isEmpty()) {
            node = queue.poll();
            for (int idx = 0; idx < 4; idx++) {
                int nr = node.r + dx[idx];
                int nc = node.c + dy[idx];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && picture[nr][nc] == node.info && !isVisited[nr][nc]) {
                    isVisited[nr][nc] = true;
                    sizeOfOneArea++;
                    queue.offer(new Node(nr, nc, node.info));
                }
            }
        }
        
        return sizeOfOneArea;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] isVisited = new boolean[m][n]; // 방문 여부 표시
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !isVisited[i][j]) { // 그림 영역이면서 방문하지 않은 곳
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(m, n, i, j, picture, isVisited));
                    numberOfArea++;
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
}
