function solution(record) {
    let answer = []
    // 유저의 아이디와 닉네임 저장하는 딕셔너리,
    // 유저 아이디와 액션을 저장하는 이차원 배열
    let userRecord = {}, temp = [];
  
    record.forEach(x => {
        const [action, userId, userName] = x.split(" ");
        if (action === "Enter") {
            // 사용자가 처음 들어오거나 닉네임을 새로 바꿔서 들어왔다면
            if (userRecord[userId] !== userName) {
                // 사용자 아이디에 맞는 닉네임 갱신
                userRecord[userId] = userName;
            }
            // 유저 아이디와 Enter에 맞는 액션 문구 저장
            temp.push([userId, "님이 들어왔습니다."]);
        }
        else if (action === "Leave") {
            temp.push([userId, "님이 나갔습니다."]);
        }
        // 사용자가 도중에 닉네임을 바꿨다면
        else if (action === "Change") {
            // 닉네임 변경해줌
            userRecord[userId] = userName;
        }
    })
  
    temp.forEach(x => {
        // 최종 닉네임과 액션을 answer에 저장
        answer.push(`${userRecord[x[0]]}${x[1]}`);
    })

  return answer;
}