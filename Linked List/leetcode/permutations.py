class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res ,temp = [], []
        seen = set()


        def backTrack(i):
            if len(temp) == len(nums):
                res.append(temp.copy())
               
            
            for ind in range(len(nums)):
                
                if nums[ind] in seen:
                    continue

                temp.append(nums[ind])
                seen.add(nums[ind])
                backTrack(ind + 1)

                seen.remove(temp.pop())

        backTrack(0)
        return res