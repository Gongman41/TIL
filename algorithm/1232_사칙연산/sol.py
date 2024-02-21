
def midorder(cur):
    if type(mom[cur]) == str:
        left = midorder(baby[cur][0])
        
        right = midorder(baby[cur][1])
        temp_yon = mom[cur] #피연산자 받고 연산자 받기. 후위로 안하면 꼬이더라
        if temp_yon == '-':
            return left - right
        elif temp_yon == '+':
            return left + right
        elif temp_yon == '/':
            return left // right
        elif temp_yon == '*':
            return left * right
        
    else:
        return mom[cur]
        




for tc in range(1,11):
    N = int(input())
    baby = [[0,0] for _ in range(N+1)] #리프노드 위치저장
    mom = [0]*(N+1)
    for _ in range(N):
        c,s,*a = map(str,input().split()) #패킹인지 언패킹인지 사용. 없으면 빈리스트로 들어오더라
        if a: #빈 리스트면_연산자랑 리프노드 인덱스가 있으면
            mom[int(c)] = s
            baby[int(c)] = list(map(int,a)) #리스트로 갖다박기
        else:
            mom[int(c)] = int(s) #피연산자만 있으면
    print(f'#{tc} {midorder(1)}') #루트에서 시작



        