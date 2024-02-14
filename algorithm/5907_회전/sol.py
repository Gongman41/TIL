import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    queue = [0]
    queue += list(map(int,input().split()))
    front = 0
    rear = N
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
