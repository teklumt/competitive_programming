class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=set()
        cur_color=image[sr][sc]
        def dfs(sr,sc,visited):
            if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc]==cur_color and (sr,sc) not in visited:
                image[sr][sc]=color
                visited.add((sr,sc))
                dfs(sr,sc-1,visited)
                dfs(sr,sc+1,visited)
                dfs(sr-1,sc,visited)
                dfs(sr+1,sc,visited)
        dfs(sr,sc,visited)
        return image
