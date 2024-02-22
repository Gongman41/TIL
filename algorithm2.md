```py
N = int(input())
lst = [[0]*7 for _ in range(2)]
for n in range(4)
  lst[0][n] = N+n
  lst[1][7-n] = N-n
lst = str(lst)
print(*lst)
```
O log n
알고리즘에서 log의 밑수는 2
2의 몇 승이 되는 지 추정. 올림함  .
O(1) 보단 느리지만 유사한 성능
O(NlogN)_sort 은 O(logN)_이진탐색보다는 느리지만 비슷한 성능

16진수. 2진수를 더 가독성 있게 사용
2진수를 10진수로 변환시 연산 오래걸림
2진수를 16진수로 변환시 연산속도 매우빠름

윈도우 + r + calc
HEX 16진수
DEC 10진수
OCT 8진수
BIN 2진수

10진수 2로 나눈 나머지 거꾸로하면 2진수

2진수 16진수 변환은 연산이 없음. 라이브러리 사용이나 단순 암기