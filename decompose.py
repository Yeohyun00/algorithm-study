#num = int(input())
num = 216
sum = 0
stat = 'unfound'

#자릿수 분해하여 더하는 함수 구현
def decompose(i):
    sum = int(i)
    for a in range(len(i)):
        sum+=int(i[a])
    print(sum)
    return sum

#생성자 탐색하는 함수 구현
def search(num):
    global stat
    for i in range(num):
        i = str(i)
        print('hihi')
        if decompose(i)==num:
            stat = 'found'
            return i
    if stat=='unfound':
        return 0
        
print(search(num))