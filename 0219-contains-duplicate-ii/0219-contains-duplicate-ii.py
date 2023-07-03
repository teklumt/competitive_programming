class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        answer=set()
        for j in range(len(nums)):
            if j-i>k:
                answer.remove(nums[i])
                i=i+1
            if nums[j] in answer:
                return True
            answer.add(nums[j])
        return False
