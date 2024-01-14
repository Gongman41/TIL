T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    odd_sum = 0 
    for j in range(len(numbers)):
        if numbers[j] % 2 == 1:
            odd_sum += numbers[j]
    print(f"#{i+1} {odd_sum}")
