class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ=inf
        diff=inf
        for i in range(len(nums)):
            j=i+1
            r=len(nums)-1
            while j<r:
                curr=nums[i]+nums[j]+nums[r]
                if abs(target-curr)==0:
                    return curr
                elif abs(target-curr)<abs(target-summ):
                    summ=curr
                    if target-curr > 0:
                        j+=1
                    else:
                        r-=1
                else:
                    if target-curr > 0:
                        j+=1
                    else:
                        r-=1
        return summ