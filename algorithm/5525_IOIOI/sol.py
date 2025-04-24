import sys

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())  # Pn의 N값
M = int(input().strip())  # 문자열 S의 길이
S = input().strip()       # 문자열 S

count = 0  # Pn이 등장하는 개수
i = 0      # 문자열 탐색 인덱스
pattern_length = 0  # 연속된 "IOI" 패턴 개수

while i < M - 1:
    if S[i:i+3] == "IOI":  # "IOI" 패턴 찾기
        pattern_length += 1  # 연속된 "IOI" 개수 증가
        if pattern_length >= N:
            count += 1  # "Pn" 패턴이 등장했으므로 카운트 증가
        i += 2  # "IOI"의 마지막 'I'부터 다시 검사
    else:
        pattern_length = 0  # 연속 패턴 깨짐 -> 초기화
        i += 1

print(count)
