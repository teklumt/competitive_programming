class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        new_ = temp = []
    
        
        for i in range(len(nums)):
            if temp:
                if nums[i] == temp[-1]:
                    temp.append(nums[i])
                else:
                    new_.append(temp)
                    temp = [nums[i]]
            else:
                temp = [nums[i]]
        if temp:
            new_.append(temp)
            
        res = 1
        maxx = new_[0][0]
        for i in range(len(new_)):
            if new_[i][0] > maxx:
                res = len(new_[i])
                maxx = new_[i][0]
            elif new_[i][0] == maxx:
                res = max(res , len(new_[i]))
        return res
        