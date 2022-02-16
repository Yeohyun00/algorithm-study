num = int(input())
count = 0
newnum = -1
firsttry = 1

while newnum!=num:
    if firsttry == 1:
        if num < 10:
            tmpnum = int('0'+str(num))
            newnum = int(str(tmpnum%10) + str((tmpnum//10+tmpnum%10)%10))
        else:
            newnum = int(str(num%10) + str((num//10+num%10)%10))
        count+=1
        firsttry += 1
    else:
        if newnum < 10:
            tmpnum = int('0'+str(newnum))
            newnum = int(str(tmpnum%10) + str((tmpnum//10+tmpnum%10)%10))
        else:
            newnum = int(str(newnum%10) + str((newnum//10+newnum%10)%10))
        count+=1
print(count)