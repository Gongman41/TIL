import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    d = {}

    for _ in range(n):
        item, menu = input().split()
        if menu not in d:
            d[menu] = [item]  # 리스트로 저장
        else:
            d[menu].append(item)

    result = 1
    for key in d:
        result *= (len(d[key]) + 1)  # 의상을 안 입는 경우 포함

    print(result - 1)  # 아무것도 안 입는 경우 제외
