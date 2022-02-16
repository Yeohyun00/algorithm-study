#fixed, change, sell = map(int, input().split())
fixed, change, sell = 2100000000, 9, 10
volume = 1
expense = fixed+change*volume
income = sell*volume
#총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.
#손익분기점이 언제 나오지 않는가?: 총 수입이 총 비용보다 많아질 수 없는 경우

if change >= sell:
    print('-1')
else:
    print(fixed//(sell-change)+1)
    