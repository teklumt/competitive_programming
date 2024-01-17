class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        prefixSum={0:1}
        summ=0
        for i in nums:
            summ+=i
            ans+=prefixSum.get(summ-k,0)
            prefixSum[summ]=prefixSum.get(summ,0)+1
        return ans