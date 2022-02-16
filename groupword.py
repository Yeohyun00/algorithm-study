n = int(input())
strings = []
for i in range(n):
    string = input()
    strings.append(string)
#strings = ['happy','new','year']


def successive(string):
    for b in range(len(string)):
        start = string.find(string[b])
        end = string.rfind(string[b])
        for x in range(start, end+1):
            if string[x]!=string[b]:
                return 1
                
count = 0
for a in range(len(strings)):
    length=0
    string = strings[a]
    successive(string)
    for b in range(len(string)):
        # 글자 한 번씩 나오면/글자 한번 아니어도 연속되면
        letter = string[b]
        if string.count(letter) != 1 and successive(string) == 1:
            break
        else:
            length+=1
    if length==len(string):
        count+=1
print(count)
