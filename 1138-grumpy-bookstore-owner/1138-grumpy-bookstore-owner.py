class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        preSum = [0]
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                preSum.append(preSum[-1])
            else:
                preSum.append(customers[i] + preSum[-1])
        maxi = 0
        for i in range(len(preSum) - minutes):
            maxi = max(maxi, preSum[i + minutes]  -  preSum[i])
        return res + maxi
