class Solution:
    def fib(self, n: int) -> int:
        res = {}
        def func(n):
            if n==0 or  n == 1:
                return n
            if n not in res:
                res[n] = func(n - 1)  + func(n - 2)
            return res[n]
        return func(n)
