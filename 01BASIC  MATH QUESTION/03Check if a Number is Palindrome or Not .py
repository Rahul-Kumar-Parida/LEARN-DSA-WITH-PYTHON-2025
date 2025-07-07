num=int(input())
check=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10

if rev==check:
    print(f"{check} is Palindrome")
else:
    print(f"{check} is not Palindrome")
