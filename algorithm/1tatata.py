##############################
# 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
#
# 모든 수신값은 gameData에 들어갑니다.
#   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
#   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
#     예) gameData.balls[0][0]: 흰 공의 X좌표
#         gameData.balls[0][1]: 흰 공의 Y좌표
#         gameData.balls[1][0]: 1번 공의 X좌표
#         gameData.balls[4][0]: 4번 공의 X좌표
#         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

# 여기서부터 코드를 작성하세요.
# 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

# Vector 구현
'''
일타싸피 거리 d 구하는법 아래 공식이 더 정확합니다.
자료에 있는 거리 d는 주황색 선분의 전체 길이입니다

d = sqrt(a^2 + (b+2r)^2 - 2a(b+2r)cos(다))
( r은 공의 반지름 입니다.)
'''
import math


TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = int(input())
HOLES = [[0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130]]
balls = [list(map(int,input().split())) for _ in range(NUMBER_OF_BALLS)]
angle = 0
power = 100
r = 2.5
for i in range(1,len(balls)):
    target = []
    b = 10e10
    for j in range(len(HOLES)):
        if math.sqrt((balls[i][0]-HOLES[j][0])**2 +(balls[i][1]- HOLES[j][1])**2) < b:
            b = math.sqrt((balls[i][0]-HOLES[j][0])**2 +(balls[i][1]- HOLES[j][1])**2)
            target = HOLES[j]
    print(target)
    x = abs(balls[0][0]-target[0])
    y = abs(balls[0][1]-target[1])
    a = math.sqrt(x**2+y**2)
    c = math.sqrt((balls[0][0]-balls[i][0])**2+(balls[0][1]-balls[i][1])**2)
    ga = math.atan2(y,x)
    
    if -1 > (a**2+b**2-c**2)/2*a*b or 1 < (a**2+b**2-c**2)/2*a*b:
        print(math.degrees(ga))
    else:
        da = math.acos((a**2+b**2-c**2)/2*a*b)
        d = math.sqrt(a**2 + (b+2*r)**2 - 2*a*(b+2*r)*math.cos(da))
        na = math.acos((a**2+d**2-(b+2*r)**2)/2*a*d)
        theta = math.degrees(ga + na)
        print(theta)

    
            
        
        
    

#                 if balls[1][0] != 0 and balls[1][1] != 0:
#                     power = 110
#                     dx = balls[1][0] - balls[0][0]
#                     dy = balls[1][1] - balls[0][1]
#                     각도 = math.atan2(dy, dx)
#                     각도 = math.degrees(각도)
#                     angle = 90 - 각도
                

#                 merged_data = str(angle) + "/" + str(power)
#                 s.sendall(merged_data.encode())
#                 print("Data Sent:", merged_data)
#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
#     main()

# '''

# '''