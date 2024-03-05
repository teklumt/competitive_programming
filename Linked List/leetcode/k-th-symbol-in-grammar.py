class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def func(n,k):
            if n==0:
                return 0
            if k%2:
                return func(n-1,(k+1)//2)==1
            else:
                return func(n-1,k//2)==0
        return int(func(n,k))





        res=False
        n=2**(n-1)

        while n!=1:
            n=n//2
            if k>n:
                k-=n  
                res=not res
        return 0 if not res else 1





        # def rec(n):
        #     if n==0:
        #         return 0
        #     val=rec(n-1)
        #     temp=""
        #     for i in val:
        #         if i=='0':
        #             temp+='01'
        #         else:
        #             temp+='10'
        #     return temp
        # return int(rec(n)[k-1])
