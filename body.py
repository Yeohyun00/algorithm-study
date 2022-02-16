n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    #weight.append(arr[i][0])
    #height.append(arr[i][1])

#weight = [55,58,88,60,46]
#height = [185,183,186,175,155]
num = []
for i in range(n):
    num.append('1') #초기화
#modified_arr = [[55,185],[58,183],1,[60,175],[46,155]]
#x>p, y>q이면 덩치큰 것

#arr에서 꺼내어 비교 시작
k=0
for a in range(len(arr)):
    for b in range(len(arr)-1,-1,-1):
        if a!=b and arr[a][0]<arr[b][0] and arr[a][1]<arr[b][1]: #자신보다 덩치 큰 상대 발견
            k+=1 
    num[a]=k+1
    k=0
for c in range(len(num)):
    print(num[c],end=' ')