# Ques: find maximum in array
# In this program I have did minor operator mistake ==


t=int(input())
for _ in range(t):
    arr_size=int(input())
    arr=list(map(int,input().split()))[:arr_size]
    maximum=arr[0]
    for i in range(1,len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
    print(maximum)
