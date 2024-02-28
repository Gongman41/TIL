import sys
sys.stdin = open('input.txt')


pattern = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 16진수를 4비트 2진수로 변환하여 데이터를 받음.
    data = [''.join(map(lambda x: f'{int(x, base=16):04b}', input().strip())) for _ in range(N)]
    result = 0
    print(f'#{tc}', end=' ')
    for x in range(N):
        if len(set(data[x])) == 2:
            y = 0
            tmp = []
            while y != M*4:
                if (x == 0 and data[x][y] == '1') or (data[x][y] == '1' and data[x - 1][y] == '0'):
                    c = {0: 0, 1: 0, 2: 0, 3: 0}
                    for k in range(4):
                        while data[x][y] == str(k % 2):
                            c[k] += 1
                            y += 1
                    '''
                        단순 2진 암호코드와 차이는, 비율이 달라진다는 점
                        비율은 3:1:1:2 였다면 -> 6:2:2:4 -> 9:3:3:6 처럼 바뀔 수 있다.
                        이때, 가장 작은 수를 기준으로 모두를 나눈 몫만 구한다면
                        min(3:1:1:2) -> 1  3//1 : 1//1 : 1//1 : 2//1
                        min(6:2:2:4) -> 1  6//2 : 2//2 : 2//2 : 4//2
                        min(9:3:3:6) -> 1  9//3 : 3//3 : 3//3 : 6//3
                        
                        모두 결과는 동일하게 3:1:1:2 가 된다.
                    '''
                    p_key = min(c[1], c[2], c[3])
                    tmp.append(pattern[(c[1]//p_key, c[2]//p_key, c[3]//p_key)])
                    answer = 0
                    if len(tmp) == 8:
                        for i in range(8):
                            if i % 2:
                                answer += tmp[i]
                            else:
                                answer += tmp[i] * 3
                        if answer % 10:
                            pass
                        else:
                            result += sum(tmp)
                        tmp = []
                y += 1

    print(result)