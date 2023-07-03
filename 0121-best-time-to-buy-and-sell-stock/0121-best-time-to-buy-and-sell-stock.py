class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxx=0
        for r in range(1,len(prices)):
            if prices[l]< prices[r]:
                maxx=max(maxx,prices[r]-prices[l])
            else:
                l=r
        return maxx
