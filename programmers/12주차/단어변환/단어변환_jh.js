// bfs로 품
function solution(begin, target, words) {
	const wordsLength = words.length,
		wordLength = words[0].length;
	let answer = 0;
	let nextVisit = [];
	let visited = new Array(wordsLength).fill(false);
	nextVisit.push([begin, 0]);
	while (nextVisit.length !== 0) {
		const [currentWord, currentCnt] = nextVisit[0];
		nextVisit.shift();
		if (currentWord === target) {
			answer = currentCnt;
			break;
		}
		for (let i = 0; i < wordsLength; i++) {
			if (!visited[i]) {
				let check = 0;
				// 다른 알파벳 개수 구함
				for (let j = 0; j < wordLength; j++) {
					if (currentWord[j] !== words[i][j]) {
						check++;
					}
				}
				// 알파벳 개수가 1개만 다르다면 큐에 해당 단어와 현재 변환 횟수 + 1 넣음
				if (check === 1) {
					visited[i] = true;
					nextVisit.push([words[i], currentCnt + 1]);
				}
			}
		}
	}

	return answer;
}
