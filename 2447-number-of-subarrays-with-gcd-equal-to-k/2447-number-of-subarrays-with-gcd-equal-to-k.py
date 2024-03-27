class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count =  0
        for i in range(len(nums)):
            temp = nums[i]
            if temp == k:
                count += 1
            for j in range(i + 1 ,len(nums)):
                temp = gcd(temp, nums[j])
                if temp == k:
                    count += 1
        return count