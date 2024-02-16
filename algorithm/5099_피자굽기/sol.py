import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    queue = [-1]*(N+1)
    piz = list(map(int,input().split()))
    front = rear = 0
    num = 0

    
    def enqueue(val,i): # nn은 버티기 횟수
        global front
        global rear
        if (rear+1)%(N+1) == front:
            return
        else:
            rear = (rear+1)%(N+1)
            nn = 0
            while True:
                nn += 1
                if 2**(nn-1)-1 < val <= 2**nn-1:
                    break


            queue[rear] = [nn,i]

    def just_enqueue(val): # nn은 버티기 횟수
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
        global num
        if rear == front:
            return 0 
        else:

            front = (front+1)%(N+1)
            if queue[front][0] != 0:
                just_enqueue(queue[front])
            else:
                if M != num:
                    enqueue(piz[num],num)
                    num += 1

    for n in range(N):
        enqueue(piz[n],n)
        num += 1
    while not ((front < rear and rear-front == 1) or (front > rear and (front+1)%(N+1) == rear)):
        queue[(front+1)%(N+1)][0] -= 1
        dequeue()


    print(f'#{tc} {queue[(front+1)%(N+1)][1]+1}')
'''
요소들의 값 감소
dequeue 위치, 발생 시 no rolling
front rear 사이 순회하다가
count로 해서 이하면 dequeue, 피자 남아있으면 그거 enqueue
두번째로 오는 애들은 enqueue할 때 값을 더하면 되겠네
abs(front=rear) ==1일때까지 순회
한바퀴돌면 //2. 라는건 1이 됐을 떄 거기서 나눠서 0이 되는 거.
1 한턴
2 3 두턴
4 5 6 7 세턴
8 9 10 11 12 13 14 15 네턴
16 17 18 19 20 다섯턴
2*(n-1)-1 < a <= 2*n-1
'''