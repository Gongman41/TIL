from itertools import combinations

N, M = map(int, input().split())

# 1부터 N까지의 숫자 중에서 M개를 선택하는 조합을 비트마스크로 표현
for bitmask in combinations(range(1,N+1), M):
    # print(bitmask)
    # 0부터 시작하는 index를 1부터 시작하는 값으로 변환
    print(" ".join(str(i) for i in bitmask))


# def backtrack(n, m, start, path):
#     # 길이가 M이 되면 출력
#     if len(path) == m:
#         print(" ".join(map(str, path)))
#         return
    
#     # start부터 N까지 반복하며 숫자 선택
#     for i in range(start, n + 1):
#         backtrack(n, m, i + 1, path + [i])

# # 입력
# N, M = map(int, input().split())

# # 백트래킹 실행
# backtrack(N, M, 1, [])
