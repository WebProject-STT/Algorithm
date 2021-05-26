function solution(rows, columns, queries) {
    // 2차원 배열 생성
    let board = Array.from(Array(rows), () => Array(columns).fill(0));
    let answer = [];
    // board값 초기화
    for(let i=0; i<rows; i++) {
        for(let j=0; j<columns; j++) {
            board[i][j] = i * columns + j + 1;
        }
    }
    queries.forEach(query => {
        // query의 x, y는 1 이상이므로 배열 인덱스에 맞춰서 1씩 뺌
        const [firstX, firstY, secondX, secondY] = query.map(x => x - 1);
        const firstData = board[firstX][firstY];
        let minData = firstData;
        // 마지막 원소부터 하나씩 끌어당겨서 값 변경
        for(let i=firstX; i<secondX; i++) {
            board[i][firstY] = board[i+1][firstY];
            minData = Math.min(minData, board[i][firstY]);
        }
        for(let j=firstY; j<secondY; j++) {
            board[secondX][j] = board[secondX][j+1];
            minData = Math.min(minData, board[secondX][j]);
        }
        for(let i=secondX; i>firstX; i--) {
            board[i][secondY] = board[i-1][secondY];
            minData = Math.min(minData, board[i][secondY]);
        }
        for(let j=secondY; j>firstY+1; j--) {
            board[firstX][j] = board[firstX][j-1];
            minData = Math.min(minData, board[firstX][j]);
        }
        board[firstX][firstY+1] = firstData;
        answer.push(minData);
    });
    return answer;
}