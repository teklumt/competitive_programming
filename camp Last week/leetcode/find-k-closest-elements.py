class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort()
        ind = bisect_left(arr, x)
        queue = deque(arr[max(0,ind - k): ind] + arr[ind :ind + k])
        while len(queue) > k:
            if abs(queue[-1] - x ) >= abs(queue[0] - x):
                queue.pop()
            else:
                queue.popleft()
        return queue

        
        
        # return sorted(sorted(arr, key = lambda j:abs(x - j))[:k])
