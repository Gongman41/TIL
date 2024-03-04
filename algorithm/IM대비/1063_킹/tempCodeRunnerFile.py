king, doll, N = map(str,input().split())
king = [int(king[1]),ord(king[0])-64]
doll = [int(doll[1]),ord(doll[0])-64]
N = int(N)
order_form = {'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],'RT':[1,1],'LT':[-1,1],'RB':[1,-1],'LB':[-1,-1]}
for _ in range(N):
    order = input()
    if 1<= king[0] + order_form[order][0] <= 8 and 1<= king[1] + order_form[order][1] <= 8:
        if [king[0] + order_form[order][0],king[1] + order_form[order][1]] == doll:
            if 1<= doll[0] + order_form[order][0] <= 8 and 1<= doll[1] + order_form[order][1] <= 8:
                king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
                doll = [doll[0] + order_form[order][0],doll[1] + order_form[order][1]]
        else:
            king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
print(chr(king[1]+64)+str(king[0]))

print(chr(doll[1]+64)+str(doll[0]))
