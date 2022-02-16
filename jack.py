N,M = map(int, input().split())
cards = list(map(int, input().split()))
after = 0
before = 0
firsttry = 0
result = 0

def isNearer(after, result):
    if M-result > M-after and M>=after: # 더 가까운 합이다
        return 1
    
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if firsttry == 0:
                before = cards[a]+cards[b]+cards[c]
                firsttry = 1
                if before <= M:
                    result = before
            else:
                after = cards[a]+cards[b]+cards[c]
                if isNearer(after, result)==1:
                    result = after
               # before = after
print(result)