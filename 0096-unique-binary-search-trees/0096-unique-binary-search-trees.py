class Solution:
    def numTrees(self, n: int) -> int:
        res = [1] * (n + 1)
        for i in range(2 , n + 1):
            tot = 0
            for j in range(1 , i + 1):
                left = j - 1
                right = i - j
                tot += res[left] * res[right]
            res[i] = tot
            
        return res[n]