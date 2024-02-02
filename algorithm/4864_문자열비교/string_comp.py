import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1,T+1):
    n_st = input()
    m_st = input()
    count = 0
    for i in range(len(m_st)-len(n_st)+1):
        if n_st == m_st[i:i+len(n_st)]:
            count=1
            break
    print(f"#{tc} {count}")
