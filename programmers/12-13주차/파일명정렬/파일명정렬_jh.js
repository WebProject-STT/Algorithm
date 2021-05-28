// 짜고나서 다른 사람이랑 너네 코드 보니까 그냥 sort할때 인덱스 찾고 확인해도 됐겠구나,,라는 생각이 듭니다
function solution(files) {
	const findNumber = /[0-9]/;
	const findNonNumber = /[^0-9]/;
	const filesSplit = files.map((file) => {
		// Number가 나오는 인덱스 찾음
		const numIndex = file.search(findNumber);
		// head부분 제거
		const deleteHead = file.substring(numIndex);
		// Number+tail부분에서 tail 시작 인덱스 찾음
		const nonNumIndex = deleteHead.search(findNonNumber);
		// head, number, tail 저장
		const head = file.substring(0, numIndex);
		const number = nonNumIndex === -1 ? deleteHead : deleteHead.substring(0, nonNumIndex);
		const tail = nonNumIndex === -1 ? '' : deleteHead.substring(nonNumIndex);
		return [head, number, tail];
	});
	let answer = [];

	filesSplit.sort(function (a, b) {
		const firstHead = a[0].toUpperCase();
		const secondHead = b[0].toUpperCase();
		if (firstHead < secondHead) {
			return -1;
		}
		if (firstHead === secondHead) {
			return Number(a[1]) - Number(b[1]);
		}
		return 1;
	});

	filesSplit.forEach((fileSplit) => {
		answer.push(`${fileSplit[0]}${fileSplit[1]}${fileSplit[2]}`);
	});

	return answer;
}
