class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        first = nums[0]
        possibleK = []
        for i in range(1, len(nums)):
            if (nums[i] - first) != 0 and (nums[i] - first)  % 2 == 0:
                cur = (nums[i] - first) // 2
                possibleK.append(cur)

        def func(k):
            count = Counter(nums)
            res = []
            for i in nums:
                if count[i]:
                    
                    cur = (i + k)
                    res.append(cur)
                    count[i] -= 1
                    count[cur + k] -= 1
            return res
        for i in possibleK:
            if len(func(i)) == len(nums) // 2:
                return func(i)
                
