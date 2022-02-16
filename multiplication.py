num1 = input()
num2 = input()

result = []

for i in range(len(num2), 0, -1):
  result.append(int(num1) * int(num2[i-1]))

print(result[0], result[1], result[2], sep='\n')
print(result[0]+(result[1]*10)+result[2]*100)
    
    
    
            




