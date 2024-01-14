N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = [0] * N 
sorted_numbers[0] = numbers[0]

for i in range(1, N):
    if i == 0:
        sorted_numbers[0] = numbers[0]
    elif i > 0:
        for j in range(i-1, -1, -1): 
            if sorted_numbers[j] > numbers[i]:
                sorted_numbers[j+1] = sorted_numbers[j]
                if j == 0:
                    sorted_numbers[j] = numbers[i]
            else:
                sorted_numbers[j+1] = numbers[i]
                break

medium_number = sorted_numbers[N // 2] 

print(medium_number)

                
             
    
        
         
        
        
        