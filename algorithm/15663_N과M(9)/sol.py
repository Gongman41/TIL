# import sys

# def backtrack(n, m, numbers, path, visited):
#     # 길이가 M이면 결과 출력
#     if len(path) == m:
#         print(" ".join(map(str, path)))
#         return
    
#     prev = -1  # 이전에 사용한 숫자 기록 (중복 방지)
#     for i in range(n):
#         if not visited[i] and numbers[i] != prev:
#             visited[i] = True
#             backtrack(n, m, numbers, path + [numbers[i]], visited)
#             visited[i] = False
#             prev = numbers[i]  # 같은 깊이에서 같은 숫자가 중복 선택되지 않도록 방지

# # 입력 처리
# N, M = map(int, sys.stdin.readline().split())
# numbers = sorted(map(int, sys.stdin.readline().split()))  # 정렬하여 사전순 보장

# visited = [False] * N  # 방문 여부 체크 리스트

# # 백트래킹 시작
# backtrack(N, M, numbers, [], visited)


def backtrack(n, m, numbers, path, used):
    # 길이가 M이면 결과 출력
    if len(path) == m:
        result = tuple(path)  # 튜플로 변환하여 중복 체크
        if result not in used:
            used.add(result)
            print(" ".join(map(str, path)))
        return
    
    for i in range(n):
        if i > 0 and numbers[i] == numbers[i - 1] and not visited[i - 1]:
            continue
        if not visited[i]:  # 방문하지 않은 숫자 선택
            visited[i] = True
            backtrack(n, m, numbers, path + [numbers[i]], used)
            visited[i] = False

# 입력 처리
N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))  # 정렬하여 사전순 보장

visited = [False] * N  # 방문 여부 체크 리스트
used = set()  # 중복 결과 저장용 집합

# 백트래킹 시작
backtrack(N, M, numbers, [], used)
