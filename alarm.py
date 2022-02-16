a,b = input().split()
hour,minu = int(a),int(b)
alarm = []

if 0<=minu<45:
    if hour == 0:
        alarm.append(23)
    else:
        alarm.append(hour-1)
    alarm.append(minu+60-45)
elif 45<=minu<=59:
    alarm.append(hour)
    alarm.append(minu-45)
    
print(str(alarm[0])+ ' ' + str((alarm[1])))
