import sys


def fibonazzi(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1;
    for i in range(1,n):
        a,b = b, a+b
        return a;
n = int(sys.stdin.readline());
print(fibonazzi(n));