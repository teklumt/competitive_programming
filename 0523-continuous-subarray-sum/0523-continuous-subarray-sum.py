class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums = [0] + nums
        hashMap = {}
        prefixSum = 0

        for i, num in enumerate(nums):
            
            prefixSum  += num
            r = prefixSum % k

            if r not in hashMap:
                hashMap[r] = i
            else:
                if i - hashMap[r] > 1:
                    return True
        
        return False