T=10
for _ in range(T):
    tc = int(input())
    queue = [0]*9
    cycle = [1,2,3,4,5]
    front = rear = 0
    min_c = -1
    def enqueue(val):
        global front
        global rear
        if (rear+1)%9 == front:
            return
        else:
            rear = (rear+1)%9
            queue[rear] = val

    def dequeue():
        
        global front
        global rear
        global min_c
        min_c += 1
        min_c %= 5
        if rear == front:
            return 0 
        else:
            front = (front+1)%9
            if queue[front] - cycle[min_c] <= 0:
                enqueue(0)
                return 0
            else: 
                enqueue(queue[front]-cycle[min_c])
                return 1
    for n in list(map(int,input().split())):
        enqueue(n)

    while dequeue():
        pass
    result = []
    if front <= rear:
        result = queue[front+1:rear+1]
    else:
        result +=queue[front+1:]
        result += queue[:rear+1]
    print(f'#{tc}',*result)


