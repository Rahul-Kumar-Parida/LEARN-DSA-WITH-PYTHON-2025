#method 1
list =[4,5,6,7,8,1,2,3]

revList=[]
def reverse(n):
    if n==0:
        return
    revList.append(list[n-1])
    reverse(n-1)

reverse(len(list))
print(revList)


#method 2

arr =[1,2,3,4,5,6,7]

def rev(arr,st,end):
    if st>=end:
        return
    arr[st],arr[end]=arr[end],arr[st]
    rev(arr,st+1,end-1)

rev(arr,0,len(arr)-1)
print(arr)

#TC-> o(N/2) -> o(N)
#SC-> o(N/2) -> o(N) Stack Space