class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1] * len(graph)
        
        for i in range(len(graph)):
            
            if color[i] == -1:
                
                color[i] = 0
                
                stack = [i]
                while stack:
                    curNode = stack.pop()
                    
                    for neighbor in graph[curNode]:
                        if color[neighbor] == -1:
                            
                            color[neighbor] = 1 ^ color[curNode]
                            stack.append(neighbor)
                            
                        elif color[neighbor] == color[curNode]:
                            return False
        return True