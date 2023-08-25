class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        for l in range(len(nums)):
            k=l
            flag=False
            for i in range(l+1,len(nums)):
                if nums[k]<nums[i]:
                    result.append(nums[i])
                    flag=True
                    break
            if flag==False:
                for i in range(0,k):
                    if nums[k]<nums[i]:
                        result.append(nums[i])
                        flag=True
                        break
            if flag==False:
                result.append(-1)
        return result
        