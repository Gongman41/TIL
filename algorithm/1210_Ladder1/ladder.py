import sys
sys.stdin = open("input.txt")

def searching(arr,row,line):
    if (row == 99 and arr[row][line] == 1) or arr[row][line] == 0:
        return False
    elif arr[row][line] == 2:
        return True


    if line>= 1 and arr[row][line-1] == 1:
        return left_move(arr,row,line-1)
    elif line <= 98 and arr[row][line+1] == 1:
        return right_move(arr, row , line+1)
    elif arr[row+1][line] == 1 or arr[row+1][line] == 2:
        return searching(arr,row+1,line)
def left_move(arr,row,line):
    if line>= 1 and arr[row][line-1] == 1:
        return left_move(arr,row,line-1)
    elif arr[row + 1][line] == 1 or arr[row+1][line] == 2:
        return searching(arr, row + 1, line)

def right_move(arr,row,line):
    if line <= 98 and arr[row][line+1] == 1:
        return right_move(arr, row , line+1)
    elif arr[row+1][line] == 1 or arr[row+1][line] == 2:
        return searching(arr,row+1,line)
T = 10
for t in range(1,T+1):
    tc = int(input())
    ladder = [0]*100
    for n in range(100):
        ladder[n] = list(map(int,input().split()))

    r = 0
    l = 0
    while searching(ladder,r,l) == False:
        l += 1
    print(f"#{tc} {l}")




