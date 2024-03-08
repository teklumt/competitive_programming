class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == 1 : 
            if nums[0] == k : 
                return 1 
            return -1 
        queue = deque()
        prefix_sums = [0]
        for num in nums :
            prefix_sums.append(prefix_sums[-1] + num)
        min_size = N + 1 
        for index, value in enumerate(prefix_sums) : 
            while queue and value <= prefix_sums[queue[-1]] : 
                queue.pop()
            while queue and value - prefix_sums[queue[0]] >= k : 
                min_size = min(min_size, index - queue.popleft())
            queue.append(index)
        if min_size != N + 1 : 
            return min_size
        return -1 