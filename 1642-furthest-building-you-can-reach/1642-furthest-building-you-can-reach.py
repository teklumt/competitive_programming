class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        Heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1]  - heights[i]

            if diff <= 0 :
                continue 
            if bricks >= diff:
                heappush(Heap, -diff)
                bricks -= diff
            elif ladders:
                if Heap:
                    if -Heap[0] > diff:
                        bricks += -heappop(Heap) - diff
                        heappush(Heap, -diff)    
                ladders -= 1              
            else:return i
        return len(heights) - 1
               