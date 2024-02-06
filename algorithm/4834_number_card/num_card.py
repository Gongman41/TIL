'''

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


'''
import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    n_list = list(input())
    temp = [0]*10
    same_c = []
    for n in n_list:
        temp[int(n)] += 1
    max_n = 0
    max_c = max(temp)
    for t in range(len(temp)):
        if temp[t] == max_c:
            same_c.append(t)
    same_c.sort()
    max_n = same_c[len(same_c)-1]

    print(f"#{test_case} {max_n} {max_c}")
#그냥 카운팅 정렬. 

'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 문자열 -> iterable | 순회하며 정수로 변환
    ai = list(map(int, input()))
    print(ai)
    # 각 정수가 나온 횟수를 세기 위한 리스트
    counting_list = [0 for _ in range(10)]

    # 데이터 전체 순회하며 카운팅
    for num in ai:
        counting_list[num] += 1
    print(counting_list)
    max_count = 0   # 보유 개수
    result = 0      # 카드 번호
    # 0~9 전부 순회
    for i in range(10):
        # 보유 개수가 많거나 같다면
        # 같다면 -> 카드 번호가 더 큰 것
        if max_count <= counting_list[i]:
            max_count = counting_list[i]
            result = i

    print(f'#{tc} {result} {max_count}')'''
    #비슷. 근데 애초에 오름차순으로 정렬돼있어 그대로 가면 카드번호 더 큰거임
    
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    num_of_cards = int(input())     # 카드의 장수
    str_cards = input()          # 카드 입력
    # 어떤 숫자가 몇번 나오는지 카운트하기 위한 리스트
    card_count = [0] * 10

    # 카드가 0으로 시작하는 경우 처리
    i = 0
    while str_cards[i] == '0':
        card_count[0] += 1
        i += 1

    cards = int(str_cards)

    # 카드의 1의 자리의 숫자가 몇번 나오는지 세서 card_list 를 갱신함
    while cards > 0:
        card_count[cards % 10] += 1
        cards //= 10

    max_card = max(card_count)  # 가장 많이 나온 숫자가 몇 번 나왔는지 저장
    max_card_num = 0    # 가장 많이 나온 숫자가 무엇인지 찾기 위한 변수

    for i in range(len(card_count)):
        # 가장 많이 나온 숫자를 찾기 위함.
        # 가장 많이 나온 숫자가 두개 이상이라면 더 큰 숫자로 갱신됨
        if card_count[i] == max_card:
            max_card_num = i


    print(f'#{testcase} {max_card_num} {max_card}')
    ''' #//로 자릿수별 계산하는 법