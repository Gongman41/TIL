def longest_fruit_tanghulu(n, fruits):
    from collections import defaultdict

    left = 0
    fruit_count = defaultdict(int)
    max_length = 0

    for right in range(n):
        fruit_count[fruits[right]] += 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length

# 입력 예시
n = int(input())
fruits = list(map(int, input().split()))

# 함수 호출
print(longest_fruit_tanghulu(n, fruits))  # 출력: 4
