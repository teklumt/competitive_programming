class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        Red = defaultdict(list)
        Blue = defaultdict(list)

        for s, d in redEdges:
            Red[s].append(d)
        for s, d in blueEdges:
            Blue[s].append(d)
        
        res = [-1] * n
        queue = deque([[0, 0, None]])
        seen = set((0, None))
        while queue:
            currNode, length, currColor = queue.popleft()
            if res[currNode] == -1:
                res[currNode] = length
            if currColor != 'BLUE':
                for i in Blue[currNode]:
                    if (i, 'BLUE') not in seen:
                        queue.append([i, length + 1, 'BLUE'])
                        seen.add((i, 'BLUE'))

            if currColor != 'RED':
                for i in Red[currNode]:
                    if (i, 'RED') not in seen:
                        queue.append([i, length + 1, 'RED'])
                        seen.add((i, 'RED'))
        return res



        