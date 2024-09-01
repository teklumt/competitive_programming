class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = []
        for i in arrays:
            res.append([min(i), max(i)])
        ans = -inf

        after = [res[-1][1]]
        before = [res[0][1]]
        for i in range(1 , len(res)):
            before.append(max(before[-1], res[i][1]))
        for i in range(len(res) - 2, -1, -1):
            after.append(max(after[-1], res[i][-1]))
        after = after[::-1]

        for i in range(len(res)):
            if i == 0:
                ans = max(ans, after[i + 1] - res[i][0])
            elif i == len(res) - 1:
                ans = max(ans , before[i - 1] - res[i][0])
            else:
                ans = max(ans ,after[i + 1] - res[i][0], before[i - 1] - res[i][0] )
        return ans
            

