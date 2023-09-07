class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        myhash = {}
        for i in range(len(edges)):
            if edges[i][0] in myhash:
                myhash[edges[i][0]] += 1
            else:
                myhash[edges[i][0]] = 1

            if edges[i][1] in myhash:
                myhash[edges[i][1]] += 1
            else:
                myhash[edges[i][1]] = 1
        n = len(myhash)

        result = []
        for i in myhash:
            result.append([myhash[i], i])
        result.sort()
        return result[-1][1]