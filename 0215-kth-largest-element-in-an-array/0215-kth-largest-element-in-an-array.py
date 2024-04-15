class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = []
        heapify(num)
        for i  in nums:
            if len(num) < k:
                heappush(num, i)
            else:
                heappushpop(num, i)
      
        return num[0]
        