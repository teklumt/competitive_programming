class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        res = [[inf] * n for i in range(n)]
        for u , v, w in edges:
            res[u][u] = res[v][v] = 0
            res[u][v] = res[v][u] = w
        
        for via in range(n):

            for  u in range(n):
                for v in range(n):
                    res[u][v] = min(res[u][v] , res[u][via] + res[via][v])

        ans = 0
        minn = inf
        for i in  range(n):
            count = 0
            for j in range(n):
                if res[i][j] <= distanceThreshold:
                    count += 1
            if count < minn:
                ans, minn = i, count
            elif count == minn:
                ans = max(ans, i)
                
                
        return ans

        
