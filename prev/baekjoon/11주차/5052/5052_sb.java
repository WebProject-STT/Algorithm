/** 백준 5052 전화번호 목록 (문자열, 정렬)
 * 한 번호가 다른 번호의 접두어인 경우가 없어야 함 (startWith() 사용)
 * 전화번호를 정렬하여 한쪽이 다른 한쪽 안에 속하는지 확인하는 과정을 거칠 필요가 있음
 * 두 전화번호가 같은 경우가 없으므로, 두 전화번호의 길이가 같을 때 확인할 필요가 없음
 *
 * 입력 : 테스트 케이스 t, 전화번호 수 n, n개의 전화번호
 * 출력 : 한 번호가 다른 번호의 접두어인 경우 NO, 아닌 경우 YES
 *
 * ---
 * Scanner와 System.out.println이 아닌 BufferedReader와 BufferedWriter를 사용한 이유는
 * 메모리와 시간이 더 적게 걸리기 때문 (메모리 3배, 시간 2배 차이남)
 * */

import java.io.*;
import java.util.Arrays;

class B5052 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine()); // 테스트케이스 수

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine()); // 전화번호 수
            String[] phoneNumber = new String[n]; // 전화번호를 담은 배열

            // 전화번호부 생성
            for (int j = 0; j < n; j++) {
                phoneNumber[j] = br.readLine();
            }

            Arrays.sort(phoneNumber);

            if (isStart(n, phoneNumber)) {
                bw.write("YES\n");
            }
            else {
                bw.write("NO\n");
            }

        }

        bw.flush();
        bw.close();
        br.close();

    }

    /** isStart
     *
     * @param n 전화번호 목록 수
     * @param phoneNumber 전화번호 목록
     * @return 결과에 따른 boolean 값
     */
    public static boolean isStart(int n, String[] phoneNumber) {

        for (int k = 0; k < n - 1; k++) {
            if (phoneNumber[k].length() == phoneNumber[k+1].length()) // 길이가 같은 경우 비교할 필요 X
                continue;
            if (phoneNumber[k+1].startsWith(phoneNumber[k])) { // 접두어인 경우 false 반환
                return false;
            }
        }

        return true; // 접두어가 아닌 경우이므로 true 반환

    }

}