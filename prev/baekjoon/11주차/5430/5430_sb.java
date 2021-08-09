import java.io.*;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

/** 백준 5430 AC (문자열, 파싱, 덱)
 * R은 배열 숫자 순서 뒤집는 함수, D는 첫 번째 숫자를 버리는 함수
 * 배열이 비어있는데 D를 사용한 경우 error 발생
 *
 * R 수행 후 D를 수행하면 마지막 숫자를 버리는 형태로 만들면 됨 => R에 따라 D 수행 위치 변화
 * R 상태에 따른 출력 순서 변경 필요
 *
 * 입력 : 테스트 케이스 수 T, 수행할 함수 p, 배열 길이 n,  숫자가 들어간 배열
 * 출력 : 주어진 정수 배열에 함수 수행 결과 출력, 에러 발생 시 error 출력
 */

class B5430 {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        StringTokenizer st;
        ArrayDeque<Integer> deque;

        int T = Integer.parseInt(br.readLine()); // 테스트케이스 수

        while(T-- > 0) {
            String p = br.readLine(); // 수행할 함수
            int n = Integer.parseInt(br.readLine()); // 배열의 길이
            st = new StringTokenizer(br.readLine(), "[],"); // 특정 문자열을 기준으로 나누어 st에 저장

            deque = new ArrayDeque<Integer>(); // 덱 초기화
            for (int i = 0; i < n; i++) { // 덱 생성
                deque.add(Integer.parseInt(st.nextToken()));
            }

            AC(p, deque);

        }

        bw.flush();
        bw.close();
        br.close();

    }

    /** AC 함수
     *
     * @param command AC 함수 수행 명령어 (ex. 'RDD')
     * @param deque 숫자를 저장한 deque
     * @throws IOException
     */
    public static void AC(String command, ArrayDeque<Integer> deque) throws IOException {
        boolean isReverse = false; // 순서 변경 여부 (default : 순서 변경 X의 의미로 false)
        for(char cmd : command.toCharArray()) {
            if (cmd == 'R') {
                isReverse = !isReverse; // 순서 뒤집기
                continue;
            }

            if (cmd == 'D') {
                if (deque.isEmpty()) { // 길이가 0인 경우 수행이 불가능하므로 error 반환
                    bw.write("error\n");
                    return;
                }
                if (isReverse) { // 순서를 뒤집어야 하는 경우
                    deque.pollLast();
                } else { // 순서를 뒤집을 필요가 없는 경우
                    deque.pollFirst();
                }
            }
        }

        // 모든 함수에 대해 정상적으로 수행한 경우 출력문을 만들어야 함

        makePrint(deque, isReverse);

    }

    /** 출력 상태를 만들어주는 함수
     *
     * @param deque 숫자를 저장한 deque
     * @param isReverse Reverse 상태 변수 (true인 경우 reverse 시켜서, false인 경우 원상태로 출력)
     * @throws IOException
     */
    public static void makePrint(ArrayDeque<Integer> deque,  boolean isReverse) throws IOException {

        bw.write("[");

        if (!deque.isEmpty()) { // deque에 원소가 존재하는 경우

            if (isReverse) { // 순서를 뒤집은 경우
                bw.write(String.valueOf(deque.pollLast()));
                while (!deque.isEmpty()){
                    bw.write("," + String.valueOf(deque.pollLast()));
                }
            }
            else { // 순서를 뒤집지 않은 경우
                bw.write(String.valueOf(deque.pollFirst()));
                while(!deque.isEmpty()) {
                    bw.write("," + String.valueOf(deque.pollFirst()));
                }
            }

        }

        bw.write("]\n");
    }
}