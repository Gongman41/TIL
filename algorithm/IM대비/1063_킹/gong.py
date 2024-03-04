'''
8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 
알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

킹은 다음과 같이 움직일 수 있다.

R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로
체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.
'''
king, doll, N = map(str,input().split())
king = [int(king[1]),ord(king[0])-64] # 보기편하게 x축 y축으로 설정
doll = [int(doll[1]),ord(doll[0])-64]
N = int(N)
order_form = {'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1]}
#이동 커맨드 딕셔너리로 저장
for _ in range(N):
    order = input()
    if 1<= king[0] + order_form[order][0] <= 8 and 1<= king[1] + order_form[order][1] <= 8: #범위안일때 이동
        if [king[0] + order_form[order][0],king[1] + order_form[order][1]] == doll:#이동했는데 돌이랑 같고 돌 이동한거 범위 안이다
            if 1<= doll[0] + order_form[order][0] <= 8 and 1<= doll[1] + order_form[order][1] <= 8:
                king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
                doll = [doll[0] + order_form[order][0],doll[1] + order_form[order][1]]
        else:# 돌이랑 안겹칠때
            king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
print(chr(king[1]+64)+str(king[0])) # 다시 원래대로 변환
print(chr(doll[1]+64)+str(doll[0]))
