T = int(input())
for t in range(T):
    numbers = list(map(int,input().split()))
    A_number = numbers[0]
    B_number = numbers[1]
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    real_max_number = 0
    max_number = 0
    if A_number <= B_number:
        for i in range(B_number - A_number + 1):
            prev_max_number = real_max_number
            max_number = 0  

            for j in range(A_number):
                max_number += A[j] * B[j+i]
            if max_number >= prev_max_number:
                real_max_number = max_number
            else:
                real_max_number = prev_max_number
    else:
        for i in range(A_number - B_number + 1):
            prev_max_number = real_max_number
            max_number = 0

            for j in range(B_number):
                max_number += A[j+i] * B[j]
            if max_number >= prev_max_number:
                real_max_number = max_number
            else:
                real_max_number = prev_max_number

    print(f"#{t+1} {real_max_number}")