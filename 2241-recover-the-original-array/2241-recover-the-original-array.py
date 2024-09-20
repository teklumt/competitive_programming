class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        nn = nums[0]
        k = 0
        rr = []
        for i in range(1, len(nums)):
            if (nums[i] - nn) != 0 and (nums[i] - nn)  % 2 == 0:
                mmm = (nums[i] - nn) // 2
                rr.append(mmm)
                # break
        def func(k):
            count = Counter(nums)
            res = []
            # print(k)
            for i in nums:
                if count[i]:
                    
                    cur = (i + k)
                    res.append(cur)
                    count[i] -= 1
                    count[cur + k] -= 1
            return res
        for i in rr:
            if len(func(i)) == len(nums) // 2:
                return func(i)
                
