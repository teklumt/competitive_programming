class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            seen=set()
            j=i
            while True:
                if j==i:
                    curr=(j+nums[j])%len(nums)
                    seen.add(i)
                    if curr==j:
                        break
                    else:
                        if nums[curr]>0 and nums[j]<0 or nums[curr]<0 and nums[j]>0:
                            break
                        else:
                            j=curr
                            seen.add(j)
                else:
                    curr=(j+nums[j])%len(nums)

                    if curr==j:
                        break
                    if curr in seen:
                        return True
                    else:
                        if nums[curr]>0 and nums[j]<0 or nums[curr]<0 and nums[j]>0:
                            break
                        else:
                            j=curr
                            seen.add(j)
        return False
