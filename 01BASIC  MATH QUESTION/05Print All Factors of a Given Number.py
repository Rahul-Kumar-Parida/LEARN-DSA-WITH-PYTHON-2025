from math import isqrt


n=int(input())

result=[]
for i in range(1,isqrt(n)+1):
    if n%i==0:
        result.append(i)
        if i!=n/i:
            result.append(n//i)

result.sort()
print(result)