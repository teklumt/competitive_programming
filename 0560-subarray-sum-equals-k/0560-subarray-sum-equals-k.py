class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ=0
        result=0
        prefixSum={0:1}
        for n in nums:
            summ+=n
            deff=summ-k
            result+=prefixSum.get(deff,0)
            prefixSum[summ]=prefixSum.get(summ,0)+1
        return result