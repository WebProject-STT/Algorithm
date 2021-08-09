import java.util.*;

class P42579 { // 베스트앨범
    public int[] solution(String[] genres, int[] plays) {
        int num = plays.length; // 노래 수
        int[] answer = {}; // 장르별 최대 2개
        ArrayList<Song> songInfo = new ArrayList<Song>(); // 각 노래에 대한 정보를 담음
        HashMap<String, Integer> genreNum = new HashMap<String, Integer>(); // 장르별 재생 횟수
        ArrayList<Integer> album = new ArrayList<Integer>();

        for (int i = 0; i < num; i++) {
            String genre = genres[i];
            int play = plays[i];
            songInfo.add(new Song(i, genre, play)); // 노래 정보 생성
            // 장르별 재생 횟수 기록
            if (genreNum.containsKey(genre)) // 장르가 이미 존재하는 경우
                genreNum.put(genre, genreNum.get(genre) + play);
            else // 존재하지 않는 경우
                genreNum.put(genre, play);
        }

        // 조건에 맞춰 정렬 진행
        Collections.sort(songInfo, new Comparator<Song>(){
            @Override
            public int compare(Song s1, Song s2) {
                if (s1.genre.equals(s2.genre)) {
                    return s2.play - s1.play;
                } else {
                    return genreNum.get(s2.genre) - genreNum.get(s1.genre);
                }
            }
        });

        // answer[0] = songInfo.get(0).idx;
        album.add(songInfo.get(0).idx);
        int cnt = 1; // 앨범에 genre별로 넣은 횟수 확인을 위한 변수
        for (int i = 1; i < songInfo.size(); i++){
            Song pre = songInfo.get(i-1);
            Song cur = songInfo.get(i);
            if (!pre.genre.equals(cur.genre)) {
                album.add(cur.idx);
                cnt = 1;
            }
            else {
                if (cnt < 2) {
                    album.add(cur.idx);
                    cnt++;
                }
            }

        }

        int albumLen = album.size();
        answer = new int[albumLen];
        for (int i = 0; i < albumLen; i++) {
            answer[i] = album.get(i);
        }

        return answer;
    }
}

class Song {
    int idx;
    String genre;
    int play;

    Song (int idx, String genre, int play) {
        this.idx = idx;
        this.genre = genre;
        this.play = play;
    }
}