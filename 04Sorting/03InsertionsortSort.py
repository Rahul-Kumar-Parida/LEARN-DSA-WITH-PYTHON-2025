#insertion sort

lst=[4,7,2,7,8,1,9]

n=len(lst)

for i in range(1,n):
    key=lst[i]
    j=i-1

    while j>=0 and lst[j]>key:
        lst[j+1]=lst[j]
        j-=1
    lst[j+1]=key

print(lst)