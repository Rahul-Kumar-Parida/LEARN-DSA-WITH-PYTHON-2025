
def factorial(n):
    if n==1 or n==0:
        return 1
    return n* factorial(n-1)

fact = factorial(0)
print(f"Factorial is  {fact}")

#TC - o(n)
#TC- o(n)  stack Space