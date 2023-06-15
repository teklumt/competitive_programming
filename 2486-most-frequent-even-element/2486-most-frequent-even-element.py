class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        result = []
        red = []
        gol = []
        for n in nums:
            if n % 2 == 0 and n not in red:
                result.append([nums.count(n), n])
                gol.append(nums.count(n))
                red.append(n)
        k = len(result)
        final = []
        if k == 0:
            return -1
        else:
            m = max(gol)
            for i in range(k-1, -1, -1):
                if result[i][0] == m:
                    final.append(result[i][1])
            return min(final)