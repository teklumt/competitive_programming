class unionfind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = [1] * (n + 1)

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
            self.parent[x] = self.parent[self.parent[x]]  
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] < self.size[rooty]:
              self.parent[rootx] = rooty
              self.size[rooty] += self.size[rootx]
            else:
              self.parent[rooty] = rootx
              self.size[rootx] += self.size[rooty]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        res = []
        one = unionfind(n)
        two = unionfind(n)
        for i, j in requests:
            bol = True
            two.union(i , j)
            for l, m in restrictions:
                if two.isConnected(l, m):
                    bol = False
                    break
            if bol:
                one.union(i , j)
                res.append(True)
            else:
                two = copy.deepcopy(one)
                res.append(False)
        return res
