import java.util.*;
/* 후보키
후보키를 만들기 위해서는 유일성과 최소성이 만족되어야 함
조합을 만들어 set에 저장하고 해당 set이 튜플 수와 같은지 확인
만약 같은 경우 1로 표시 후 unique에 저장
=> 학번이 유일성을 만족하면 학번,이름,전공,학년에 대해 1000으로 기록
=> unique에 이미 저장되어 있는 정보가 부분집합으로 들어가는 경우 저장을 해서는 안됨
*/

class P42890 {
    public int solution(String[][] relation) {
        int row = relation.length;
        int col = relation[0].length;
        ArrayList<Integer> candidateKey = new ArrayList<>(); // 후보키를 저장하기 위한 리스트

        // 칼럼을 이용해 만들 수 있는 조합을 비트마스킹을 이용해 표현
        for (int set = 1; set < (1 << col); set++) {
            // 유일성 검사
            if (!isUnique(set, row, col, candidateKey, relation)) continue;
            // 최소성 검사
            if (!isMinimal(set, candidateKey)) continue;

            candidateKey.add(set);
        }

        return candidateKey.size();
    }

    public boolean isUnique(int set, int row, int col, ArrayList<Integer> candidateKey, String[][] relation) {
        HashMap<String, String> map = new HashMap<>();

        for (int r = 0; r < row; r++) {
            String temp = "";
            for (int c = 0; c < col; c++) {
                if ((set & (1 << c)) != 0) {
                    temp += relation[r][c];
                }
            }
            if (map.containsKey(temp)) return false; // 유일성 만족X
            else map.put(temp, temp); // 중복되지 않는 값 추가
        }

        // 모든 값에 대해 유일성을 만족하면 true 반환
        return true;

    }

    public boolean isMinimal(int set, ArrayList<Integer> candidateKey) {

        for (int key : candidateKey) { // 후보키의 부분집합에 대해
            if ((key & set) == key) return false; // key가 1로 가지고 있는 값을 set이 1로 가지고 있는 경우 => key & set의 결과가 key와 동일하게 나옴
        }

        // 최소성을 만족하므로 true 반환
        return true;
    }

}
