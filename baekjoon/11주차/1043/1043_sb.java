import java.io.*;
import java.util.*;

/** 백준 1043 거짓말
 *
 * 진실을 말하는 사람과 각 파티별 참가자, 모든 사람의 파티 참가에 대해 기록
 * 진실을 말하고 있는 사람이 속한 파티를 true 로 표시하며,
 * true 인 파티의 참가자가 속한 모든 파티를 true 로 변경하기
 *
 * 입력 : 사람 수 N과 파티 수 M, 진실의 아는 사람 수와 번호, M개 파티에 오는 사람 수와 번호
 * 출력 : 지민이가 거짓말쟁이로 알려지지 않으면서 과장된 이야기를 할 수 있는 파티 개수 최댓값
 * */

class B1043 {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 사람 수
        int M = Integer.parseInt(st.nextToken()); // 파티 수
        boolean[] isParty = new boolean[M]; // 진실을 말해야하는 파티인지 아닌지 기록
        ArrayList<Integer>[] partyAttend = new ArrayList[N+1]; // 사람별 파티참가 기록
        for (int i = 1; i <= N; i++) partyAttend[i] = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        int knowNum = Integer.parseInt(st.nextToken()); // 진실을 알고있는 사람 수
        if (knowNum == 0) { // 진실을 알고있는 사람이 없는 경우
            bw.write(String.valueOf(M)); // 모든 파티에 과장된 이야기 가능
        }
        else { // 진실을 알고있는 사람이 있는 경우
            int[] know = new int[knowNum]; // 진실을 말하는 사람 기록
            for (int i = 0; i < knowNum; i++) {
                know[i] = Integer.parseInt(st.nextToken());
            }

            int[][] party = new int[M][]; // 파티별 참가자 기록
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int partyAttendNum = Integer.parseInt(st.nextToken()); // 파티별 참가자 수
                party[i] = new int[partyAttendNum]; // 파티별 참가자 기록
                for (int j = 0; j < partyAttendNum; j++) {
                    int temp = Integer.parseInt(st.nextToken());
                    party[i][j] = temp; // 파티에 참가하는 사람 기록
                    partyAttend[temp].add(i); // 사람별 참가한 파티 기록
                }
            }
            bfs(N, isParty, knowNum, know, party, partyAttend);

            int cnt = 0;
            for (int i = 0; i < M; i++) {
                if (!isParty[i]) cnt++;
            }
            bw.write(String.valueOf(cnt));
        }

        bw.flush();
        bw.close();
        br.close();

    }

    /** bfs
     *
     * @param N 사람 수
     * @param isParty 파티에 진실을 아는 사람이 있는지 체크
     * @param knowNum 진실을 아는 사람 수
     * @param know 진실을 아는 사람들
     * @param party 파티별 참가자
     * @param partyAttend 사람들의 파티 참가 기록
     * @return isParty 의 파티 참가 기록 결과
     */
    public static boolean[] bfs(int N, boolean[] isParty, int knowNum, int[] know, int[][] party, ArrayList<Integer>[] partyAttend) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] isVisited = new boolean[N+1]; // 진실을 아는 사람에 대해 수행했는지 확인용

        for (int i = 0; i < knowNum; i++) { // 진실을 아는 사람을 큐에 추가
            queue.add(know[i]);
        }

        while(!queue.isEmpty()) {
            int truePeople = queue.poll(); // 진실을 아는 사람
            isVisited[truePeople] = true;
            for (int i = 0; i < partyAttend[truePeople].size(); i++) {
                int attendPartyNum = partyAttend[truePeople].get(i); // 진실을 아는 사람이 참가한 파티
                isParty[attendPartyNum] = true;
                for (int j = 0; j < party[attendPartyNum].length; j++) { // 진실을 아는 사람이 참여한 파티의 참가자들에 대해
                    if (!isVisited[party[attendPartyNum][j]]){ // 아직 확인하지 않은 사람인 경우
                        queue.add(party[attendPartyNum][j]);
                    }
                }
            }

        }

        return isParty;
    }

}