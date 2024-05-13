class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = Counter()
        for i, j in edges:
            count[i] += 1
            count[j] += 1
            if count[i] > 1:
                return i
            if count[j] > 1:
                return j
        