def backtrack(n, m, numbers, bitmask, path):
    # 길이가 M이면 출력
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    
    for i in range(n):
        if not (bitmask & (1 << i)):  # i번째 숫자가 아직 선택되지 않았다면
            backtrack(n, m, numbers, bitmask | (1 << i), path + [numbers[i]])

# 입력 처리
N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))  # 정렬하여 사전순 보장

# 백트래킹 시작
backtrack(N, M, numbers, 0, [])
