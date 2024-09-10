class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if not num: return 0
        memo = {}
        def func(i , summ):
            if summ == 0:
                return 0
            if i > num or summ < 0:
                return inf
            state = (i , summ)
            if state not in memo:
                sec = inf
                if i != 0:
                    sec = func(i , summ - i) + 1
                memo[state] = min(func(i + 10, summ - i) + 1, sec , func(i + 10, summ))
            return memo[state]
        res = func(k, num) 
        return res if res != inf else -1 