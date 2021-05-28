# 베스트 앨범
from functools import cmp_to_key
def compare(x, y):
	if(x < y): # x 값이 y값 보다 작으면
		return 1 # y 내용을 앞으로 보냄
	elif(x > y):
		return -1
	else: # x 값이 y값과 동일하면
		if(x < y): # x과 y을 비교해서 y이 크면
			return -1 # x 내용을 앞으로 보냄
		elif(x > y):
			return 1
		else:
			return 0

def solution(genres, plays):
    print(plays)
    answer = []
    # 1. 정리 - 장르
    genres_d = dict()
    for idx, g in enumerate(genres):
        if g not in genres_d.keys(): genres_d[g] = [idx]
        else: genres_d[g].append(idx)
    # 2. 장르 내 재생 수 + 고유 번호 순
    for k, v in genres_d.items():
        # plays를 기반으로 sort / 고유 번호 sort
        genres_d[k] = sorted(v, key= cmp_to_key(lambda i,j:compare(plays[i], plays[j])))
    # 장르 sort -> 많이 재생
    genres_d = sorted(genres_d.values(), key= cmp_to_key(
        lambda x,y : compare(sum([plays[i] for i in x]), sum([plays[j] for j in y]))
    )) 

    for g in genres_d:
        answer.append(g[0])
        if len(g) >= 2:
            answer.append(g[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))