class P77485 { // 행렬 테두리 회전하기

    // matrix 생성 (숫자 넣어서 matrix를 완성시켜줌)
    public void createMatrix(int[][] matrix, int rows, int columns) {
        int num = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = num++;
            }
        }
    }

    // matrix 회전 및 가장 작은 값 찾아내기
    public int rotateMatrix(int[][] matrix, int x1, int y1, int x2, int y2){
        int temp = matrix[x1][y1]; // 제일 왼쪽 위의 값 저장
        int min_ = temp; // 가장 작은 값을 임의로 지정
        // y1열에 대한 이동
        for (int i = x1; i < x2; i++) {
            matrix[i][y1] = matrix[i+1][y1];
            min_ = Math.min(min_, matrix[i][y1]);
        }

        // x2행에 대한 이동
        for (int i = y1; i < y2; i++) {
            matrix[x2][i] = matrix[x2][i+1];
            min_ = Math.min(min_, matrix[x2][i]);
        }

        // y2열에 대한 이동
        for (int i = x2; i > x1; i--) {
            matrix[i][y2] = matrix[i-1][y2];
            min_ = Math.min(min_, matrix[i-1][y2]);
        }

        // x1행에 대한 이동
        for (int i = y2; i > y1 + 1; i--) {
            matrix[x1][i] = matrix[x1][i-1];
            min_ = Math.min(min_, matrix[x1][i-1]);
        }

        // 처음에 저장해둔 (x1, y1) 자리의 값을 (x1, y1+1) 자리에 넣어줌
        matrix[x1][y1+1] = temp;
        return min_;
    }

    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] matrix = new int[rows][columns];
        int queryLen = queries.length;
        int[] answer = new int[queryLen];

        createMatrix(matrix, rows, columns);

        for (int i = 0; i < queryLen; i++) {
            int x1 = queries[i][0] - 1, y1 = queries[i][1] - 1, x2 = queries[i][2] - 1, y2 = queries[i][3] - 1; // 실제 인덱스 위치에 맞게 -1 시켜줌
            answer[i] = rotateMatrix(matrix, x1, y1, x2, y2);
        }

        return answer;
    }
}