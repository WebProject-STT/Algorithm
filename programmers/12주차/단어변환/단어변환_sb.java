import java.util.*;

class P43163 { // 단어변환

    class Node { // word와 cnt 정보를 담기 위한 용도
        String word;
        int cnt;

        Node(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }

    public int solution(String begin, String target, String[] words) {

        Queue<Node> queue = new LinkedList<Node>();
        Node node = new Node(begin, 0);

        queue.add(node);

        int lenTarget = target.length();
        int lenWords = words.length;
        boolean[] isVisited = new boolean[lenWords]; // 한 번 방문한 문자에 재방문하지 않도록 하기 위해 생성

        while (!queue.isEmpty()) {
            node = queue.poll();

            if (node.word.equals(target)) // node에 저장된 단어와 target이 같은 경우 cnt 반환
                return node.cnt;

            for (int i = 0; i < lenWords; i++) {
                if (isVisited[i]) continue; // 이미 방문한 경우 진행 X

                int diffCnt = 0; // 다른 알파벳 수 기록
                for (int j = 0; j < lenTarget; j++) {
                    if (diffCnt > 1) break; // diffCnt가 1보다 커지면 단어 변경 불가하므로 지나감
                    if (words[i].charAt(j) != node.word.charAt(j))
                        diffCnt++;
                }

                if (diffCnt == 1) { // 다른 알파벳이 하나뿐인 경우 words 안에 있는 단어로 변경
                    isVisited[i] = true;
                    queue.add(new Node(words[i], node.cnt + 1));
                }
            }
        }

        return 0; // target과 같은 단어가 존재하지 않으므로 0 반환
    }
}

/*
두 단어의 각 자리에 대한 알파벳 비교
다른 알파벳이 1개만 존재하는 경우 변경
바꾼 결과 target과 동일한 경우, 최소 단계 출력
동일하지 않은 경우 0 출력
*/