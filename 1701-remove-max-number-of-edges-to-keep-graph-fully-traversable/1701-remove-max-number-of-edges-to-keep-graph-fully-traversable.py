class UnionFind:
    def __init__(self,size):
        self.root = {i:i for i in range(1,size + 1)}
        self.size = [1]*(size + 1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty: 
            if self.size[rootx] < self.size[rooty]:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            else:
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
    def IsConnected(self,x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        edges.sort(reverse =True)
        res = 0
        for types, x, y in edges:
            if types == 3:
                if alice.IsConnected(x, y):
                    res += 1
                else:
                    bob.union(x, y)
                    alice.union(x, y)
            elif types == 2:
                if bob.IsConnected(x, y):
                    res += 1
                else:
                    bob.union(x, y)
            else:
                if alice.IsConnected(x,y):
                    res += 1
                else: alice.union(x, y)
  
        return res if bob.size[bob.find(1)] == n and alice.size[alice.find(1)] == n else -1








        