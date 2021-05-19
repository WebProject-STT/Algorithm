function solution(msg) {
    const length = msg.length;
    let answer = [], index = 0;
    // 알파벳 인덱스번호 딕셔너리 형태로 저장
    let indexNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").reduce((indexNum, current, index) => {indexNum[current] = index + 1; return indexNum;}, {});
    while (true) {
        // 현재 입력 단어와 처리되지 않은 단어가 남았는지 확인하는 변수
        let currentWord = "", check = false;
        for (let i = index; i < length; i++) {
            // 현재 단어가 딕셔너리에 저장되어 있지 않다면
            if (!(currentWord + msg[i] in indexNum)) {
                // 정답 배열에 이전 단어의 인덱스 번호 추가
                answer.push(indexNum[currentWord]);
                // 현재 단어 딕셔너리에 추가
                indexNum[currentWord + msg[i]] = Object.keys(indexNum).length + 1;
                // index 변수 갱신
                index = i;
                // 처리할 단어 남았음
                check = true;
                break;
            }
            // 단어 추가해줌
            currentWord += msg[i];
        }
        // 처리할 단어가 이제 없다면
        if (!check) {
            // 정답 배열에 인덱스 번호 추가
            answer.push(indexNum[currentWord]);
            break;
        }
    }
    return answer;
}