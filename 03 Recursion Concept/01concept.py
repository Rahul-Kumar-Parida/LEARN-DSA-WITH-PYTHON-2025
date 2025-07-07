#Recursion Theory
#when a function calls itself.

# def greet():
#     print("Anirudha")

# greet()
"""
count=0

def fun():
    global count
    if count==4:
        return
    print("ani")
    count+=1
    fun()

fun()

#1)head recursion (1st print, then function call)
#2)tail recursion (1st Function call, then print) (back tracking)

#3) Time Complexity o(n+1) -> o(n)
#4) Space Complexity o(n+1) -> o(n)

"""


###Recursion Using Parameters

def printx(x,n):
    if n==0:
        return
    print(x)
    printx(x,n-1)


printx(15,5)