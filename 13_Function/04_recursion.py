def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(10))

def sum(n):
    if n==1:
        return n
    return n+sum(n-1)
print(sum(5))

def ne(n):
    if n==1:
        return n
    return n-ne(n-1)
print(ne(5))

'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6........
fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fin(1)+fib(2)
fib(n)=fib(n-1)+fib(n-1)
'''

def fib(n):
    if (n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)
print(fib(13))


def fib(n):
    if (n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)

print(fib(8))