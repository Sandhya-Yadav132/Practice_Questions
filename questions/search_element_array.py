# Ques. search an element in array
#In this program learn new concept or thing "single line input"
      #  with slicing  [:N] :- jb extra input ko ignore krna ho
      # with set jb multiple element search krna ho

arr_size,num=map(int,input().split())
arr=list(map(int,input().split()))
if len(arr)!=arr_size:
    print("Invalid Input")
else:
    print('YES' if num in arr else 'NO') 
