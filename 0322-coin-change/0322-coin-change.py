class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins = set(coins)
        @cache

        def func(target):
            if target in coins:
                return 1

            ans = inf
            for i in coins:
                if i < target:
                    ans = min(ans, 1 + func(target - i))
            return ans
        ans = func(amount)
        return ans if ans != inf else -1