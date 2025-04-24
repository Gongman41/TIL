import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 누적 합 배열 만들기 (Prefix Sum)
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + lst[i - 1]

# 구간 합 계산 (O(1)로 빠르게 처리)
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])  # 누적합 활용
