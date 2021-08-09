// 시간을 분단위로 변경하는 함수
function convert(time) {
	const result = time.split(':');
	return parseInt(result[0]) * 60 + parseInt(result[1]);
}
function solution(m, musicinfos) {
	const musicinfosArr = musicinfos.map((musicinfo) => musicinfo.split(','));
	// 네오가 찾는 음악의 제목과 재생시간을 저장
	let answer = '',
		playTime = 0;
	// m에서 #이 붙어있는 음들은 모두 소문자형태로 변경
	// (C# => c)
	m = m.replace(/\w#/g, (x) => x[0].toLowerCase());
	musicinfosArr.forEach((musicinfo) => {
		// 노래 재생시간 저장
		const currentPlayTime = convert(musicinfo[1]) - convert(musicinfo[0]);
		// 악보에서 #이 붙어있는 음들은 모두 소문자형태로 변경
		const melody = musicinfo[3].replace(/\w#/g, (x) => x[0].toLowerCase());
		// 반복횟수 구함
		const repeatCnt = Math.floor(currentPlayTime / melody.length);
		// 실제로 노래가 재생된 구간의 악보를 구함
		let extendMelody = melody.repeat(repeatCnt);
		extendMelody += melody.substr(0, currentPlayTime % melody.length);
		// 재생구간에 네오가 기억하는 멜로디가 담겨져 있고 현재 노래 재생시간이
		// 정답으로 저장되어 있는 악보의 재생시간보다 길다면
		if (extendMelody.includes(m) && playTime < currentPlayTime) {
			// 정답 변경
			answer = musicinfo[2];
			playTime = currentPlayTime;
		}
	});
	// 일치하는 노래가 없다면
	if (answer === '') {
		answer = '(None)';
	}
	return answer;
}
