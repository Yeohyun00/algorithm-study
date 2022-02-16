string = 'OOXXOOXXOO'
sum = 0
count = 0
for i in range(len(string)):
    if i==0 and string[i]=='O':
        sum+=1
        count = 1
    else:
        if string[i]=='O' and string[i-1]=='O':
            count+=1
        elif string[i]=='O' and string[i-1]!=0:
            count+=1
        else:
            count=0
        sum+=count
print(sum)