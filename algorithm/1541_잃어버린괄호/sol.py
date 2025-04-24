import sys

input = sys.stdin.readline
#  +, - 기준으로 나눠서 - 나온 부분부터는 다 - 로. 그 전까지는 다 + 로.

tem = input().strip().split("-")
result = sum(map(int,tem[0].split("+")))
for temp in tem[1:]:
    result -= sum(map(int,temp.split("+")))

print(result)

