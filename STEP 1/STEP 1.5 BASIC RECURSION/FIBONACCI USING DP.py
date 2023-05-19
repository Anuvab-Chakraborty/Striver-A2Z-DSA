"""
n = int(input())
l = [-1] * (n + 1)


def fib(n):
    if l[n] != -1:
        return l[n]
    else:
        if n <= 1:
            l[n] = n
            return l[n]
        else:
            l[n] = fib(n - 1) + fib(n - 2)
            return l[n]


print(fib(n))
print(*l)
"""
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:return n
        return self.fib(n-1) + self.fib(n-2)
