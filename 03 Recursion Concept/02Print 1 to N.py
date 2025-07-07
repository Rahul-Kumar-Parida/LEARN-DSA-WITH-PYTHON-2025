#head print 1 to N using Recursion
"""
def myfun(i,n):
    if i>n:
        return 
    
    print(i)
    myfun(i+1,n)

myfun(1,5)

#Tail print 1 to N using Recursion
def myfunc(n):
    if n==0:
        return 
    myfunc(n-1)
    print(n)

myfunc(5)

"""


#Head print N to 1 using Recursion
"""
def myfun2(n):
    if n==0:
        return 
    print(n)
    myfun2(n-1)

myfun2(5)
#Tail print N to 1 using Recursion

def myfun(i,n):
    if i>n:
        return 
    myfun(i+1,n)
    print(i)
    

myfun(1,5)
"""




###Functional Recursion

def sumfun(sum,i,n):
    if i>n:
        print(sum)
        return
    sumfun(sum+i,i+1,n)

sumfun(0,1,5)


def sumfun2(n):
    if n==1:
        return 1
    return n+sumfun2(n-1)

hii = sumfun2(5)
print("hii  ",hii)