function solution(genres, plays) {
    const genresLength = genres.length;
    // 각 장르별 총 (장르 이름, 장르 번호, 총 재생 횟수) (2차원)
    // 장르별(노래 재생 횟수, 노래 고유번호) 저장(3차원)하는 배열
    // => genresPlays[i] => i번 장르의 노래 정보들이 저장되어 있음
    let totalPlays = [], genresPlays = [];
    // 정답 배열, genresPlays 배열 길이 => 배열에 값을 새로 넣을 때 이용
    let answer = [], genresPlaysLength = 0;
    for(let i=0; i<genresLength; i++) {
        const genre = genres[i], play = plays[i];
        const index = totalPlays.findIndex(play => play[0] === genre);
        // 현재 장르가 처음 보는 장르라면
        if (index === -1) {
            totalPlays.push([genre, genresPlaysLength, play]);
            // genresPlays에 2차원 배열 형태로 재생횟수와 고유번호 넣음
            // => 배열 새로 생성해주는 것
            genresPlays.push([[play, i]]);
            genresPlaysLength++;
        }
        // 현재 장르 저장되어 있다면
        else {
            // 총 재생횟수 더해주고
            totalPlays[index][2] += play;
            // 노래 정보 저장
            genresPlays[index].push([play, i]);
        }
    }
    // 총 재생횟수를 기준으로 내림차순 정렬
    totalPlays.sort(function(a, b) {
        return b[2] - a[2];
    })
    genresPlays.forEach(arr => {
        // 각 장르내에서 조건대로 정렬
        arr.sort(function(a, b) {
            if(a[0] == b[0]) {
                return a[1] - b[1];
            }
            return b[0] - a[0];
        });
    });
    for (let i = 0; i < genresPlaysLength; i++) {
        // 속한 노래가 많이 재생된 장르 먼저 확인
        const index = totalPlays[i][1];
        // 현재 장르에 수록된 곡이 1개라면 해당 곡의 번호만 answer에 push
        if(genresPlays[index].length < 2) {
            answer.push(genresPlays[index][0][1]);
        }
        // 수록곡 2개 이상이면
        else {
            // 2개만 answer에 push
            for(let j=0; j<2; j++) {
                answer.push(genresPlays[index][j][1]);
            }
        }
    }
    return answer;
}