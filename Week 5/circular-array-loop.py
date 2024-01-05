class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            seen=set()
            j=i
            while True:
                curr=(j+nums[j])%len(nums)
                if j==i:
                    seen.add(i)
                    if curr==j:
                        break
                    else:
                        if nums[curr]*nums[j]<0:
                            break
                        else:
                            j=curr
                            seen.add(j)
                else:
                    if curr==j:
                        break
                    if curr in seen:
                        return True
                    else:
                        if nums[curr]*nums[j]<0:
                            break
                        else:
                            j=curr
                            seen.add(j)
        return False