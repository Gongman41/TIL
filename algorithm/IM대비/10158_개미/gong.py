import sys
sys.stdin = open('input.txt')



w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())
gogo = 'right_up'
while t:
    tem = 0
    if gogo == 'right_up':
        if w-p > h-q:
            if t >= h-q:
                tem = h - q
                p += h-q
                q = h
                gogo = 'right_down'

            else:
                p += t
                q += t
                tem = t
        elif w-p < h - q:
            if t >= w-p:
                tem = w - p
                q += w-p
                p = w
                gogo = 'left_up'

            else:
                p += t
                q += t
                tem = t
        else:
            tem = h-q
            p = w
            q = h
            gogo = 'left_down'
    elif gogo == 'right_down':
        if w - p > q:
            if t >= q:
                tem = q
                p += q
                q = 0
                gogo = 'right_up'
            else:
                tem = t
                p += t
                q -= t
        elif w - p < q:
            if t >= w - p:
                tem = w-p
                q -= w - p
                p = w
                gogo = 'left_down'
            else:
                tem = t
                p += t
                q -= t
        else:
            tem = w-p
            p = w
            q = 0
            gogo = 'left_up'


    elif gogo == 'left_up':
        if p > h - q:
            if t >= h - q:
                tem = h-q
                p -= h - q
                q = h
                gogo = 'left_down'
            else:
                tem = t
                p -= t
                q += t
        elif p < h - q:
            if t >= p:
                tem = p
                q += p
                p = 0
                gogo = 'right_up'
            else:
                tem =t
                p -= t
                q += t
        else:
            tem = h-q
            p = 0
            q = h
    elif gogo == 'left_down':
        if p > q:
            if t >= q:
                tem =q
                p -= q
                q = 0
                gogo = 'left_up'
            else:
                tem = t
                p -= t
                q -= t
        elif p < q:
            if t >= w-p:
                tem = p
                q -= p
                p = 0
                gogo = 'right_down'
            else:
                tem = t
                p -= t
                q -= t
        else:
            tem = p
            p = 0
            q = 0
            gogo = 'right_up'
    t -= tem
print(p,q)