let zeroCnt = 0, oneCnt = 0;

function compression(arr, x, y, size) {
    // 첫번째 원소 저장
    const first = arr[x][y];
    const endX = x + size, endY = y + size;
    // 분할된 영역 내 원소값이 모두 같지 않다면 false 리턴
    for(let i=x; i<endX; i++) {
        for(let j=y; j<endY; j++) {
            if(arr[i][j] != first) {
                return false;
            }
        }
    }
    // 원소값 모두 같으면 원소값에 따라 0 or 1 개수 증가
    first === 0 ? zeroCnt++ : oneCnt++;
    return true;
}
// 배열의 영역을 계속 4분할하여 압축
function checkArea(arr, x, y, size) {
    const division = size / 2;
    // 더 이상 4분할을 할 수 없으면 리턴
    if(division === 0) {
        return;
    }
    // 해당 영역 내 원소 값이 모두 같지 않다면
    if (!compression(arr, x, y, division)) {
        // 해당 영역을 또 4분할 하기 위해 함수 호출
        checkArea(arr, x, y, division);
    }
    if(!compression(arr, x, y+division, division)) {
        checkArea(arr, x, y+division, division);
    }
    if(!compression(arr, x+division, y, division)) {
        checkArea(arr, x+division, y, division);
    }
    if(!compression(arr, x+division, y+division, division)) {
        checkArea(arr, x+division, y+division, division);
    }
}
 
function solution(arr) {
    const length = arr.length;
    let answer = [];
    // 배열 전체 값이 달라서 영역을 나눠야 할 경우
    if (!compression(arr, 0, 0, length)) {
        // 영역 쪼개기
        checkArea(arr, 0, 0, length);
    }
    answer.push(zeroCnt);
    answer.push(oneCnt);
    
    return answer;
}