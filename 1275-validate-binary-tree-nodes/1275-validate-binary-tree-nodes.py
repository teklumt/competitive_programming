class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {i : i for i in range(n)}
        res = True
        pp = [0] * n

        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x

        def union(x , y):
            nonlocal res
            parentX = find(x)
            parentY = find(y)
            if parentX == parentY:
                res = False
            else: 
                parent[parentX] = parentY
        for i in range(n):
            if leftChild[i] != -1:
                if pp[leftChild[i]]:
                    return False
                union(leftChild[i], i)
                pp[leftChild[i]] = 1
            if rightChild[i] != -1:
                if pp[rightChild[i]]:
                    return False
                union(rightChild[i], i)
                pp[rightChild[i]] = 1
        count = 0
        for i in parent:
            if i == find(i):
                count += 1
        return res and count == 1
