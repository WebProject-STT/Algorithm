/*
    f(1) = 2
    0 0 0 1
    0 0 1 0
    f(2) = 3
    0 0 1 0
    0 0 1 1
    f(3) = 5
    0 0 1 1
    0 1 0 1
    f(4) = 5
    0 1 0 0
    0 1 0 1
    f(5) = 6
    0 1 0 1
    0 1 1 0
    f(6) = 7
    0 1 1 0
    0 1 1 1
    f(7) = 11
    0 1 1 1
    1 0 1 1 
    => 짝수일 경우에는 마지막 비트를 1로 변경해주면 되고,
       홀수일 경우에는 맨 뒤에 있는 0과 1의 위치를 교환해주면 됨
       (0 다음에 1이 바로 나올 경우)
*/

// 제일 작은 수를 구하는 함수
function getMinBit(number) {
    const bits = [];
    let mul = 1, answer = 0, length;
    // number의 이진수를 구함
    while (number) {
        bits.push(number % 2);
        number = Math.floor(number / 2);
    }
    length = bits.length;
    // 모든 비트가 1일 경우 마지막에 0을 추가
    if(bits[length - 1] === 1) {
        bits.push(0);
        length++;
    }
    for (let i = 1; i < length; i++) {
        // 제일 처음으로 0과 1이 붙어있는 지점을 구함
        if (bits[i] === 0 && bits[i - 1] === 1) {
            // 두 비트 교환
            bits[i] = 1;
            bits[i - 1] = 0;
            break;
        }
    }
    // 이진수를 다시 십진수로 변환
    bits.forEach(bit => {
        answer += bit * mul;
        mul *= 2;
    })
    return answer;
}

function solution(numbers) {
    let answer = [];
    numbers.forEach(number => {
        // 짝수일 경우에는 해당 숫자의 1을 더하면 됨
        if (number % 2 === 0) {
            answer.push(number + 1);
        }
        else {
            answer.push(getMinBit(number));
        }
    })
    return answer;
}