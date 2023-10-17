class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(root,path):
            if root == len(graph) - 1:
                ans.append(path)
                return

            for v in graph[root]:
                dfs(v, path + [v])

        dfs(0, [0])
        return ans