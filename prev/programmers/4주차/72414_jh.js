// 다른 사람 풀이 보고 따라했는데 틀렸다..

// 초 단위 시간을 문자열로 변환
function timeToString(num) {
	const hour = Math.floor(num / 3600);
	num %= 3600;
	const minute = Math.floor(num / 60);
	const second = num % 60;
	return `${hour}:${minute}:${second}`;
}
// 시간을 초단위로 변환
function hourToSecond(time) {
	return parseInt(time[0]) * 3600 + parseInt(time[1]) * 60 + parseInt(time[2]);
}
// 동영상 재생 구간 시간을 시간, 분, 초 단위로 분할한 후 초 단위로 변환해서 반환
function getTime(time) {
	const timeSplit = time.split('-');
	const startTime = timeSplit[0].split(':');
	const endTime = timeSplit[1].split(':');
	return [hourToSecond(startTime), hourToSecond(endTime)];
}

function solution(play_time, adv_time, logs) {
	const playTime = hourToSecond(play_time.split(':'));
	const advTime = hourToSecond(adv_time.split(':'));
	// 초 별 광고를 시청중인 사용자의 수를 저장할 배열
	const viewerCnt = new Array(360000);
	let answer = '',
		maxSumCnt = 0,
		sumCnt;

	if (playTime === advTime) {
		return '00:00:00';
	}
	// 배열 초기화
	for (let i = 0; i < 360000; i++) {
		viewerCnt[i] = 0;
	}

	logs.forEach((log) => {
		const time = getTime(log);
		// 시청자 수 누적
		for (let i = time[0]; i < time[1]; i++) {
			viewerCnt[i] = +1;
		}
	});
	// 0 ~ advTime-1의 누적 시청자 수 더함
	for (let i = 0; i < advTime; i++) {
		sumCnt += viewerCnt[i];
	}
	maxSumCnt = sumCnt;

	for (let i = advTime; i < playTime; i++) {
		// 1 ~ advTime의 누적 시청자 수는 sumCnt에 - viewerCnt[0] + viewerCnt[advTime]
		// 이를 식으로 표현하면 다음과 같음
		sumCnt = sumCnt - viewerCnt[i - advTime] + viewerCnt[i];
		// 누적 재생시간이 더 큰 구간이 있다면
		if (sumCnt > maxSumCnt) {
			// 재생 시작시간 문자열로 변환
			answer = timeToString(i - advTime + 1);
			// 최댓값 갱신
			maxSumCnt = sumCnt;
		}
	}

	return answer;
}
