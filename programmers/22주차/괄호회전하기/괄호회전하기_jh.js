// 괄호의 쌍이 맞는지 확인하는 함수
function isCorrect(current, top) {
    // 스택이 비어있다면 올바른 괄호열이 아니므로 false 리턴
    if(top === undefined) {
        return false;
    }
    // current와 top이 쌍이 맞는지 확인해서 결과 리턴
    if(current === "]") {
        return top === "[";
    }
    if(current === ")") {
        return top === "(";
    }
    if(current === "}") {
        return top === "{";
    }
}

function solution(s) {
    const length = s.length;
    let answer = 0;
    // start는 회전에 따른 문자열의 시작 인덱스
    // 1번 회전하면 시작 인덱스는 1번이니께
    for (let start = 0; start < length; start++) {
        // 문자열 길이만큼 확인하기 위한 end 변수
        const end = start + length;
        const stack = [];
        // 문자열이 올바른 괄호 문자열인지 확인하는 flag
        let flag = true;
        for (let index = start; index < end; index++) {
            // 현재 원소
            const current = s[index % length];
            // 현재 원소가 열린 괄호열이면 스택에 push
            if(current === "[" || current === "(" || current === "{") {
                stack.push(current);
            }
            // 괄호열의 쌍이 맞지 않으면 flag 바꾸고 break
            else if(!isCorrect(current, stack.pop())) {
                flag = false;
                break;
            }
        }
        // 올바른 괄호 문자열일 경우 answer 증가
        if(stack.length === 0 && flag) {
            answer++;
        }
    }
    
    return answer;
}