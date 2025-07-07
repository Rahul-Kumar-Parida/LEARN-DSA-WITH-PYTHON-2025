#Find the Fibonacci Number


def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)
fibonacci=fibo(6)
print(fibonacci)

#TC -> o(2^n)
#SC -> o(2^n)