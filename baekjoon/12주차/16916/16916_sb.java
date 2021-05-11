import java.io.*;

/** 백준 16916 부분 문자열
 *
 * KMP 알고리즘을 응용해서 풀어야 함
 * KMP 알고리즘은 일치 여부를 이용해 확인해 볼 필요가 없는 중간단계를 뛰어넘는 알고리즘
 *
 * 입력 : 문자열 S, 문자열 P
 * 출력 : P가 S의 부분 문자열이면 1, 아니면 0 출력
 * */

class B16916 {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static int answer = 0;

    public static int[] getPi(String P) { // P 내에서 반복적으로 나오는 문자가 있는지 확인
        int lenP = P.length();
        int[] pi = new int[lenP]; // P 문자열의 각각의 문자에 대한 기록
        int idx = 0; // 0부터 비교
        for (int i = 1; i < lenP; i++) { // 1부터 확인
            while(idx > 0 && P.charAt(i) != P.charAt(idx)) {
                idx = pi[idx-1]; // 해당 인덱스 위치 값을 찾아 앞의 글자와 비교하도록 함
            }
            if (P.charAt(i) == P.charAt(idx))
                pi[i] = ++idx; // 같은 경우에 대해 기록
        }
        return pi;
    }

    public static void KMP(String S, String P) throws IOException { // S 내에서 P와 동일한 문자가 있는지 확인
        int[] pi = getPi(P); // P의 동일한 문자 인덱스에 대한 기록
        int idx = 0; // P 기준
        for (int i = 0; i < S.length(); i++) { // S 기준
            while(idx > 0 && S.charAt(i) != P.charAt(idx)) {
                idx = pi[idx - 1];
            }
            if (S.charAt(i) == P.charAt(idx)) {
                if (idx == P.length() - 1) { // P가 S의 부분문자열인 경우
                    answer = 1;
                    break;
                }
                else
                    idx++;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        String S = br.readLine();
        String P = br.readLine();

        KMP(S, P);
        System.out.println(answer);
        br.close();
    }

}