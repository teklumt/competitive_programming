class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        curr = []
        maxHeap = []

        for i in range(len(capital)):
            curr.append([capital[i] ,profits[i]])
        curr.sort()
        left = 0
        while k > 0:
            while left < len(capital) and curr[left][0] <= w:
                heappush(maxHeap, -curr[left][1])
                left += 1
            if maxHeap:
                w += -heappop(maxHeap)
            k -= 1
        return w


