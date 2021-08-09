// 구명보트 갯수의 최소값을 구하는 문제
// => 구조 횟수를 최소한으로 해야된다는건 한번 사람을 실을 때 최대한 많이 실어야된다는 것
function solution(people, limit) {
	const peopleSize = people.length;
	let answer = 0,
		// 두 사람을 태운 횟수
		cnt = 0,
		// 무거운 사람 인덱스
		heavyIndex = 0,
		// 가벼운 사람 인덱스
		lightIndex = peopleSize - 1;
	// 사람 몸무게 내림차순으로 정렬
	people.sort(function (a, b) {
		return b - a;
	});
	// 두 인덱스가 같아질때까지 실행
	// => 인덱스 같다는건 구출이 끝났다는 것
	while (heavyIndex < lightIndex) {
		// 무거운 사람과 가벼운 사람 무게 합쳤을때 제한 무게보다 같거나 작다면
		if (people[heavyIndex] + people[lightIndex] <= limit) {
			// 가벼운 사람 인덱스 감소
			lightIndex--;
			// 두명 태운 횟수 증가
			cnt++;
		}
		// 무거운 사람 인덱스 증가
		heavyIndex++;
	}
	// 사람 수에서 두명 태운 횟수 빼면 정답
	answer = peopleSize - cnt;

	return answer;
}
