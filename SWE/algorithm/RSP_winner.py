who_what = list(map(int,input().split()))
A = who_what[0]
B = who_what[1]

if (A==3 and B==2) or (A == 2 and B ==1) or (A == 1 and B ==3):
    print("A")
elif (B==3 and A==2) or (B == 2 and A == 1) or (B == 1 and A ==3):
    print("B")