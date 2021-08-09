function solution(n) {
    var answer = [];
    var triangle = new Array(n);
    // 각 방향에 따라 숫자를 채우는 시작점의 x, y 좌표
    var up_x = n-2, up_y = n-2, down_x = 0, down_y = 0, right_x = n-1, right_y = 1;
    var direction = 0, num = 1;
    
    for(var i = 0; i < n; i++) {
        triangle[i] = new Array(i + 1);
    }
    
    // 예시대로 맨 위 꼭짓점부터 반시계 방향으로 숫자를 채울 거임
    // 꼭짓점부터 밑에까지 채울 때 숫자 n개, 방향 바뀔때마다 채우는 숫자
    // 1개씩 줄어든다고 생각
    // 바깥부터 삼각형 하나 그리고 또 안에 들어가서 삼각형 채우고 이런 너낌
    for(var k = n; k >= 1; k--) {
        var temp = direction % 3;
        // temp 
        // 0 => 아래쪽
        // 1 => 오른쪽
        // 2 => 위쪽
        switch(temp) {
            case 0:
                for(var i = down_x; i <= down_x + k - 1; i++) {
                    triangle[i][down_y] = num++;
                }
                // 다음 시작점으로 변경
                down_x += 2;
                down_y++;
                break;
            case 1:
                for(var j = right_y; j <= right_y + k - 1; j++) {
                    triangle[right_x][j] = num++;
                }
                right_x--;
                right_y++;
                break;
            case 2:
                var j = up_y;
                for(var i = up_x; i >= up_x - k + 1; i--) {
                        triangle[i][j--] = num++;
                }
                up_x--;
                up_y -= 2;
        }
        direction++;
    }
    
    for(var i = 0; i < n; i++) {
        for(var j = 0; j <= i; j++) {
            answer.push(triangle[i][j]);
        }
    }
    
    return answer;
}