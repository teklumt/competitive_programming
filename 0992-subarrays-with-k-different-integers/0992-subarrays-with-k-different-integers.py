class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
            def function(nums,k):
                Hash={}
                l=0
                r=0
                ans=[]
                while r<len(nums):
                    Hash[nums[r]]=Hash.get(nums[r],0)+1
                    while len(Hash)>k:
                        Hash[nums[l]]-=1
                        if Hash[nums[l]]==0:
                            del Hash[nums[l]]
                        l+=1
                    ans.append(r-l+1)
                    r+=1
                return sum(ans)
            
            return function(nums,k)-function(nums,k-1)