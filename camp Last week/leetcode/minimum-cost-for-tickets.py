class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}
        def dp(ind):
            if ind >= len(days):
                return 0
            
            if ind not in memo:
                first = dp(ind + 1) + costs[0]
                second = dp(bisect_left(days, days[ind]  + 7)) + costs[1]
                third = dp(bisect_left(days, days[ind]  + 30)) + costs[2]
                memo[ind] = min(first, second, third)
            return memo[ind]
        return dp(0)
        


