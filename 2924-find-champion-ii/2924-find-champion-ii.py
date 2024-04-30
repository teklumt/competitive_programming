class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        count  = Counter()
        for i, j in edges:
            graph[i].append(j)
            count[j] += 1
        place = [i for i in range(n) if i not in count]
        return place[0] if len(place) == 1 else -1 
