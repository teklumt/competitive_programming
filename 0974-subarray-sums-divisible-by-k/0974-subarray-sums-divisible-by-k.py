class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store={0:1}
        res=summ=0
        for i in nums:
            summ+=i
            res+=store.get(summ%k,0)
            store[summ%k]=store.get(summ%k,0)+1
        return res