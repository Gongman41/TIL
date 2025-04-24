import sys
input = sys.stdin.readline

N, M = map(int, input().split())
real_mat = [[0] * (N + 1) for _ in range(N + 1)]

# 누적 합 배열 만들기
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        real_mat[i][j] = row[j - 1] + real_mat[i - 1][j] + real_mat[i][j - 1] - real_mat[i - 1][j - 1]

# 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = real_mat[x2][y2] - real_mat[x1 - 1][y2] - real_mat[x2][y1 - 1] + real_mat[x1 - 1][y1 - 1]
    print(result)
