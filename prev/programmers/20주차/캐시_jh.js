/*
    LRU 알고리즘: 가장 오랫동안 사용되지 않은 페이지(도시)를 교체하는 알고리즘
    cache hit: CPU가 참고하려는 메모리가 캐시에 존재할 경우
    cache miss: CPU가 참고하려는 메모리가 캐시에 존재하지 않을 경우
*/
function solution(cacheSize, cities) {
    let answer = 0;
    // 캐시된 도시를 저장할 배열 
    let cache = [];
    // 캐시크기가 0일 경우 어떤 도시도 저장할 수 없기 때문에 cache miss가 
    // 도시의 개수만큼 발생
    if(cacheSize === 0) {
        return cities.length * 5;
    }
    
    cities.forEach(city => {
        // 도시의 이름은 대소문자를 구별하지 않기에 그냥 다 소문자로 만듬
        city = city.toLowerCase();
        // 현재 도시가 캐시 배열 내에 있는지 검사
        const index = cache.indexOf(city);
        // 현재 도시 캐시 배열에 있으면
        if (index >= 0) {
            // cache hit 발생
            answer += 1;
            // 그 위치에 있는 도시 삭제
            cache.splice(index, 1);
        }
        // 현재 도시 캐시 배열에 없으면
        else {
            // 캐시 배열 크기가 주어진 캐시크기와 같다면
            if (cache.length === cacheSize) {
                // 앞의 원소 제거 (LRU 알고리즘에 의거해)
                cache.shift();
            }
            // cache miss 발생
            answer += 5;
        }
        // 마지막에 현재 도시 넣어줌
        cache.push(city);
    })
    
    return answer;
}