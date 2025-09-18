import sys

sys.setrecursionlimit(1004)

def recursive(start=0, end=4):
    print(start, end)
    
    if start >= end:
        return end
    
    
    start += 1
    return recursive(start, end)


print(recursive(0, 1000))


def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))