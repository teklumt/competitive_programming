
class MedianFinder:

    def __init__(self):

        self.minHeapRight = []
        self.maxHeapLeft = []
        heapify(self.minHeapRight)
        heapify(self.maxHeapLeft)
        
    def addNum(self, num: int) -> None:

        heappush(self.maxHeapLeft, -num)
        
        if len(self.maxHeapLeft) -  len(self.minHeapRight) > 1 or (self.maxHeapLeft and self.minHeapRight and -self.maxHeapLeft[0] > self.minHeapRight[0]):
            heappush(self.minHeapRight, -heappop(self.maxHeapLeft))
        if -len(self.maxHeapLeft) +  len(self.minHeapRight) > 1:
            heappush(self.maxHeapLeft, -heappop(self.minHeapRight))

       
    def findMedian(self) -> float:
        n = heappop(self.minHeapRight) if self.minHeapRight else inf
        m = -heappop(self.maxHeapLeft) if self.maxHeapLeft else inf
        if n != inf:
            heappush(self.minHeapRight, n)
        if m != inf:
            heappush(self.maxHeapLeft, -m)
       
        if (len(self.minHeapRight) + len(self.maxHeapLeft))% 2:
            if (len(self.minHeapRight) + len(self.maxHeapLeft)) == 1:
                return min(n, m)
            elif len(self.minHeapRight) > len(self.maxHeapLeft):
                return self.minHeapRight[0]
            return -self.maxHeapLeft[0]
        return ( n + m) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()