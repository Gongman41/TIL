import sys

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 끝나는 시간을 기준으로 정렬 (끝나는 시간이 같으면 시작 시간 기준 정렬)
meetings.sort(key=lambda x: (x[1], x[0]))

# 2. 그리디 알고리즘 적용
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:  # 현재 회의의 시작 시간이 이전 회의의 끝나는 시간 이후라면
        count += 1
        end_time = end  # 회의 종료 시간을 갱신

# 3. 최대 사용할 수 있는 회의 개수 출력
print(count)
