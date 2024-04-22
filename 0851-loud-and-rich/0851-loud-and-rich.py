class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
    
        res = [[] for _ in range(len(quiet))]
        check = [set() for _ in range(len(quiet)) ]
      
        for From , to in richer:
            graph[to].append(From)
        
        for i in range(len(quiet)):
            queue = deque([i])
            heappush(res[i], (-quiet[i], i))
            check[i].add(i)
            while queue:
                node = queue.popleft()

                for j in graph[node]:
                    if j not in check[i]:
                        check[i].add(j)
                        if res[i]:
                            heappushpop(res[i], (-quiet[j], j))
                        else:
                            heappush(res[i], (-quiet[j], j))
                        queue.append(j)
       

        return [i[0][1] for i in res]