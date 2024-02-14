import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    queue = [0]*(N+1)
    piz = list(map(int,input().split()))
    front = rear = 0
    
    def enqueue(val):
        global front
        global rear
        if (rear+1)%(N+1) == front:
            return
        else:
            rear = (rear+1)%(N+1)
            queue[rear] = val

    def dequeue():
        
        global front
        global rear
        if rear == front:
            return 0 
        else:
            front = (front+1)%(N+1)
            enqueue(queue[front])
    for _ in range(M):
        dequeue()

    print(f'#{tc} {queue[(front+1)%(N+1)]}')
'''
요소들의 값 감소
dequeue 위치
front rear 사이 순회하다가
count로 해서 이하면 dequeue, 피자 남아있으면 그거 enqueue
두번째로 오는 애들은 enqueue할 때 값을 더하면 되겠네
abs(front=rear) ==1일때까지 순회
'''