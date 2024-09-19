class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * len(cost)
        res[0] = cost[0]
        for i in range(1, len(cost)):
            one,  two = res[i - 1] , 0
            if i >= 2:
                two = res[i - 2]
            res[i] = min(one, two) + cost[i]
        return min(res[-1], res[-2])
            