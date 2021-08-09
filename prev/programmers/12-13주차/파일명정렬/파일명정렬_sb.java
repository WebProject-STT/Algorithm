import java.util.*;

class P17686 {
    public String[] solution(String[] files) {
        String[] answer = {};

        // 조건에 따른 정렬을 하기 위해 Comparator 구현
        // compare 리턴값이 양수면 두 객체의 자리를 바꿔줌
        Arrays.sort(files, new Comparator<String>(){
            @Override
            public int compare(String o1, String o2) {
                // 숫자 앞부분을 잘라서 head 생성
                String head1 = o1.split("[0-9]")[0];
                String head2 = o2.split("[0-9]")[0];

                // compareTo를 사용한 비교를 위해서는 모두 소문자로 변경 후 비교
                int result = head1.toLowerCase().compareTo(head2.toLowerCase());

                if (result == 0) { // 같은 문자일 경우 숫자로 비교
                    result = convertNum(o1, head1) - convertNum(o2, head2);
                }

                return result;
            }
        });

        return files;
    }

    public int convertNum(String str, String head) {
        str = str.substring(head.length()); // head 길이만큼 잘라서 숫자부터 시작하게 만들어줌
        String result = "";
        for (char c : str.toCharArray()) {
            if (Character.isDigit(c) && result.length() < 5) // 숫자인지 그리고 result 길이가 5가 안 넘는지 확인
                result += c;
            else
                break;
        }
        return Integer.valueOf(result);
    }
}