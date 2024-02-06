'''

코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

'''

'''
def binary_search(start, end, target, cnt):
    # 중간 위치 인덱스 번호
    middle = (start + end) // 2
    # 언제까지? 중간지점이 내가 찾는 대상이면
    if middle == target:
        return cnt
    else:   # 아니면 조사
        if middle > target:
            return binary_search(start, middle, target, cnt+1)
        else:
            return binary_search(middle, end, target, cnt+1)

''' #그냥 갖다 박아도 되나. 재귀가 아니라 while문으로도 가능
T = int(input())
for tc in range(1,T+1):
    P, A, B = map(int,input().split())
    def binarySearch(a,key):
        start = a[0]
        end = a[-1]
        count = 0
        if len(a) < key:
            return count
        while start <= end:
            middle = (start+end)//2


            count += 1
            if a[middle-1] == key:
                return count
            elif a[middle-1] > key:
                end = middle
            else:
                start = middle
        return count

    a_count = binarySearch(list(range(1,P+1)),A)
    b_count = binarySearch(list(range(1,P+1)),B)
    if a_count > b_count:
        print(f"#{tc} B")
    elif a_count == b_count:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} A")