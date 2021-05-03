# 파일명 정렬
import re
def solution(files):
    # 1. 가운데 숫자를 기준으로 split해야함
    files = [re.split("([0-9]+)", f) for f in files]
    # 2. head 기준 -> number 기준
    files = sorted(files, key = lambda x: (x[0].lower(), int(x[1])))
    
    return ["".join(f) for f in files]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

"""
파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현
파일명 - 영어, 숫자 ,공백, 마침표, -로만 이루어짐(영문자로 시작하고 숫자 하나 이상 포함)

파일명 - head, number, tail 세부분 => [foo] [010] [bar020.zip]
head => 숫자 x 문자(최소 한글자 이상)
number => 한글자~5글자 연속된 숫자(앞쪽에 0이 올 수 있음 -> 0101도 가능)
tail => 나머지 부분 -> 여기에 숫자가 오거나 아무것도 안올 수 도 있음

파일명 정렬
[1] head 사전 순 (이때, 대소문자 구분 x => MUZI==muzi==MuZi)
[2] number 숫자 순 (9 < 10 < 0011 < 012 < 13 < 014) 순 [숫자 앞 0 무시]
[3] 원래 입력에 주어진 순서 유지 -> 만약에 MUZI01.zip, muzi1.png가 들어오면 이 순서 유지
"""