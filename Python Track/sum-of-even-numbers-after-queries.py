class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        even=0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even += nums[i]

        for qu in queries:
            num= nums[qu[1]]
            if num %2 == 0:
                even-=num
            num+=qu[0]
            if num%2==0:
                even+=num
            res.append(even)

            nums[qu[1]]=num
        return res