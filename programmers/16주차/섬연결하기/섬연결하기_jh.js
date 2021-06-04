// union-find 알고리즘 사용해서 풀이
// 최소 비용으로 다리 건설하려면 그래프에서 사이클이 생기면 안됨
// 사이클 생성 여부를 union-find를 통해 확인하며 비용 더해줌

// 부모 노드를 반환하는 함수
function getParent(a, parent) {
    if(a == parent[a]) {
        return a;
    }
    else {
        return parent[a] = getParent(parent[a], parent);
    }
}
// 서로의 부모노드를 합치는 함수
function unionParent(a, b, parent) {
    const parentA = getParent(a, parent);
    const parentB = getParent(b, parent);
    if(parentA < parentB) {
        parent[parentB] = parentA;
    }
    else {
        parent[parentA] = parentB;
    }
}

function solution(n, costs) {
    let parent = [];
    let answer = 0;
    // 초기에 자신의 부모노드는 자기자신
    for(let i=0; i<n; i++) {
        parent.push(i);
    }
    // 건설 비용 오름차순으로 정렬
    costs.sort(function(a, b) {
       return a[2] - b[2]; 
    });
    
    costs.forEach(x => {
        const [start, end, cost] = x;
        // 부모노드가 같지않으면 => 사이클이 형성되지 않는다면
        if (getParent(start, parent) != getParent(end, parent)) {
            // 비용 더함
            answer += cost;
            // 둘이 연결되니 부모노드 합쳐준다
            unionParent(start, end, parent);
        }
    });
    
    return answer;
}