let relationArr;
let visited = [],
	candidateKey = [];
let answer = 0,
	columnSize,
	relationSize;

function findCandidateKey(key) {
	// 현재 키의 유일성을 확인하기 위한 배열
	// => 릴레이션에서 현재 키(열)에 해당하는 행의 원소들을 문자열로 합쳐서 넣음
	let temp = [];
	for (let i = 0; i < relationSize; i++) {
		let str = '';
		for (let j = 0; j < columnSize; j++) {
			if (visited[j]) {
				str += relationArr[i][j];
			}
		}
		// 유일성 체크
		if (temp.includes(str)) {
			return;
		}
		temp.push(str);
	}
	// 최소성 체크
	for (let i = 0; i < candidateKey.length; i++) {
		let flag = true;
		// 후보키 중에 현재 키의 부분집합이 있는지 확인
		for (let j = 0; j < candidateKey[i].length; j++) {
			if (!key.includes(candidateKey[i][j])) {
				flag = false;
				break;
			}
		}
		if (flag) {
			return;
		}
	}
	candidateKey.push(key);
	answer++;
}

function dfs(current, currentKey, totalCnt) {
	if (currentKey.length === totalCnt) {
		findCandidateKey(currentKey);
		return;
	}
	for (let i = current; i < columnSize; i++) {
		if (!visited[i]) {
			visited[i] = true;
			dfs(i, `${currentKey}${i}`, totalCnt);
			visited[i] = false;
		}
	}
}
function solution(relation) {
	relationArr = relation;
	relationSize = relation.length;
	columnSize = relation[0].length;
	// 조합을 위한 방문배열 초기화
	for (let i = 0; i < columnSize; i++) {
		visited.push(false);
	}
	// 하나의 후보키에 들어갈 수 있는 키의 개수는 1 ~ column 개수
	for (let i = 1; i <= columnSize; i++) {
		dfs(0, '', i);
	}
	return answer;
}
