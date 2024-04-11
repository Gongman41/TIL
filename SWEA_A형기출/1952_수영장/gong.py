T= int(input())
def dfs(money,month):
    global min_n
    if month > 12:
        min_n = min(money,min_n)
        return
    if plan[month]:
        dfs(money+one_day*plan[month],month+1)
        dfs(money+one_month,month+1)
        dfs(money+three_month,month+3)
    else:
        dfs(money,month+1)
for tc in range(1,T+1):
    one_day,one_month,three_month,one_year = map(int,input().split())
    plan = [0]+list(map(int,input().split()))
    # 계획이 있다면 1일권으로 계산하고 넘어가는 거,한달권으로 계산하고 넘어가는 거, 3달권으로 계산하고 넘어가는 거. 다 하고
    # 비교해서 1년권이 싸면 1년권으로
    min_n = one_year
    dfs(0,1)
    print(f'#{tc} {min_n}')
    
    
    