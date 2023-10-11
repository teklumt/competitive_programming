class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mydict=collections.defaultdict(list)
        for src,des in edges:
            mydict[des].append(src)
        result=[]
        for i in range(n):
            if not mydict[i]:
                result.append(i)
        return result