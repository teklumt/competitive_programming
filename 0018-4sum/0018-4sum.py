class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        if len(nums)<4:
            return []
        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                c=b+1
                d=len(nums)-1
                while c<d:
                    summ=nums[a]+nums[b]+nums[c]+nums[d]
                    if summ<target:
                        c+=1
                    elif summ>target:
                        d-=1
                    else:
                        if [nums[a],nums[b],nums[c],nums[d]] not in result:
                            result.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
        return result
