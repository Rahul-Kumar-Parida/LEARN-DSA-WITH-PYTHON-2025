n=int(input())
num=n
check=n
count=0

while n>0:
    count=count+1
    n=n//10

sum=0
while num>0:
    d=num%10
    sum=sum+pow(d,count)
    num=num//10

if check==sum:
    print(f"{check} is a armstrong number")
else:
    print(f"{check} is not a armstrong number")