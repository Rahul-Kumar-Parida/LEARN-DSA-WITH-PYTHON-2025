#bubble sort
lst=[4,7,2,7,8,1,9]

n=len(lst)

for i in range(n-1):
    for j in range(n-i-1):
        if lst[j]>lst[j+1]:  #for descending its <
            lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)