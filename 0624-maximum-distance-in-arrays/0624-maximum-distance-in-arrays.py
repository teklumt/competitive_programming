class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minLeft = [min(arrays[0])]
        minRight = [min(arrays[-1])]

        maxx = 0

        for i in range(1, len(arrays)):
            minLeft.append(min(minLeft[-1], min(arrays[i])))
        for i in range(len(arrays) - 2, -1 ,-1):
            minRight.append(min(minRight[-1], min(arrays[i])))
        minRight = minRight[::-1]

        for i in range(len(arrays)):
            one, two = inf, inf
            if i  > 0:
                one = minLeft[i - 1]
            if i < len(arrays) - 1:
                two = minRight[i + 1]
            maxx = max(maxx, abs(max(arrays[i]) - min(one, two)))
        return maxx