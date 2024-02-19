import math

TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = int(input())
HOLES = [[0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130]]
balls = [list(map(int,input().split())) for _ in range(NUMBER_OF_BALLS)]
angle = 0
power = 100
r = 2.5

for i in range(1, len(balls)):
    target = []
    b = 10e10
    for j in range(len(HOLES)):
        dist = math.sqrt((balls[i][0] - HOLES[j][0])**2 + (balls[i][1] - HOLES[j][1])**2)
        if dist < b:
            b = dist
            target = HOLES[j]
    print(target)
    
    x = abs(balls[0][0] - target[0])
    y = abs(balls[0][1] - target[1])
    a = math.sqrt(x**2 + y**2)
    c = math.sqrt((balls[0][0] - balls[i][0])**2 + (balls[0][1] - balls[i][1])**2)
    ga = math.atan2(y, x)
    
    cos_value = (a**2 + b**2 - c**2) / (2 * a * b)
    
    if cos_value <= -1:
        print("180")
    elif cos_value >= 1:
        print("0")
    else:
        # atan2 함수를 사용하여 각도를 계산합니다.
        theta = math.degrees(math.atan2(y, x))
        print(theta)
