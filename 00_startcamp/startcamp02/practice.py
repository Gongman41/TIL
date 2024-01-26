import sys

N = int(sys.stdin.readline().rstrip())
n_list = [0] * 10001

for m in range(N):
    num = int(sys.stdin.readline().rstrip())
    n_list[int(num)] += 1

for n in range(len(n_list)):
    if n_list[n] != 0:
        for i in range(n_list[n]):
            print(n)