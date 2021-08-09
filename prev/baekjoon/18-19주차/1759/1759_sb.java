import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

/** 백준 1759 암호 만들기
 *
 * 주어진 C개의 문자를 L개의 암호로 만들기 => 브루트포스
 * 암호 조건 : 최소 한 개의 모음, 최소 두 개의 자음, 정렬된 형태
 *
 * 입력 : 두 정수 L, C 및 C개의 문자
 * 출력 : 사전식으로 만들 수 있는 암호 모두 출력
 * */
class B1759 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int L;
    static int C;
    static char[] alpha;
    static boolean[] visited;

    static void printPassowrd() throws Exception {
        String answer = "";
        for (int i = 0; i < C; i++)
            if (visited[i])
                answer += alpha[i];
        System.out.println(answer);
    }

    /** checkVowel
     *
     * @param alpha 확인하려는 문자
     * @return 모음인지 확인 결과 반환
     */
    static boolean checkVowel(char alpha) {
        if (alpha == 'a' || alpha == 'e' || alpha == 'i' || alpha == 'o' || alpha == 'u')
            return true;
        else
            return false;
    }

    /** createPassword
     *
     * @param len 암호 길이
     * @param idx for문 시작할 idx 번호
     * @param vowel 모음 수
     * @param consonants 자음 수
     */
    static void createPassword(int len, int idx, int vowel, int consonants) throws Exception {
        // 조건 만족 시 출력
        if (len == L) {
            if (vowel < 1 || consonants < 2) // 조건에 해당하지 않은 경우 반환
                return;
            printPassowrd();
            return;
        }

        for (int i = idx; i < C; i++) {
            if (!visited[i]) {
                visited[i] = true; // 방문한 알파벳 번호
                if (checkVowel(alpha[i]))
                    createPassword(len + 1, i + 1, vowel + 1, consonants);
                else
                    createPassword(len + 1, i + 1, vowel, consonants + 1);
                visited[i] = false; // 방문 표시 제거
            }
        }
    }

    public static void main(String[] args) throws Exception {

        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        alpha = new char[C]; // 입력 받은 문자 저장
        visited = new boolean[C]; // 방문 여부 표시

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++)
            alpha[i] = st.nextToken().charAt(0); // 한글자씩 받아와서 char로 변경

        Arrays.sort(alpha); // 사전순으로 만들기 위해 sort 시킴
        createPassword(0, 0, 0, 0);

        br.close();
    }
}
