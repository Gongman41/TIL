# from collections import deque
# N = int(input())
# target_lst = [int(input()) for _ in range(N)] 
# target_deq = deque(target_lst)
# target_deq.append(-1)#미리 popleft하는 코드로 짜서 이렇게 안하면 인덱스 에러 or 값 잘못나옴
# n_lst = []#12345678...
# result = []#결과
# a = target_deq.popleft()
# for n in range(1,N+1):# n은 append할 정수

# # a에 순열 첫번째 값 저장, n_lst에 오름차순으로 정수 넣으면서 n_lst 마지막 값이랑 비교

    
#     n_lst.append(n)
#     result.append('+')
#     while n_lst and n_lst[-1] >= a:#빈 리스트이면 맨 밑 if문으로 no 출력
#         if not a in n_lst:#이놈이랑 뒤에놈은 순열 못만드는 경우 체크용
#             print('no')
#             break
#         if n_lst[-1] == a:#같을때 순열 다음번째 값으로 이동
#             a = target_deq.popleft()
        
#         n_lst.pop() #얘는 같거나 클 때 일단 빼기
#         result.append('-')
        
        
#         if not target_deq:#얘가 결과 출력용
#             for i in range(len(result)):
#                 print(result[i])
#             break
    

from collections import deque

N = int(input())
target_lst = [int(input()) for _ in range(N)]
target_deq = deque(target_lst)
target_deq.append(-1)  # 미리 popleft하는 코드로 짜서 이렇게 안하면 인덱스 에러 or 값 잘못나옴
n_lst = []  # 12345678...
result = []  # 결과
a = target_deq.popleft()
flag = 0
for n in range(1, N + 1):  # n은 append할 정수

    # a에 순열 첫번째 값 저장, n_lst에 오름차순으로 정수 넣으면서 n_lst 마지막 값이랑 비교

    n_lst.append(n)
    result.append('+')
    while n_lst and n_lst[-1] >= a:  # 빈 리스트이면 맨 밑 if문으로 no 출력
        if n_lst[-1] > a:  # 이놈이랑 뒤에놈은 순열 못만드는 경우 체크용
            flag = 1
            break
        elif n_lst[-1] == a:  # 같을때 순열 다음번째 값으로 이동
            a = target_deq.popleft()

        n_lst.pop()  # 얘는 같거나 클 때 일단 빼기
        result.append('-')

        if not target_deq:  # 얘가 결과 출력용
            for i in range(len(result)):
                print(result[i])
            break
    if flag:
        print('NO')
        break
    # if not n_lst and target_deq:  # 이놈
    #     print('no')
    #     break
