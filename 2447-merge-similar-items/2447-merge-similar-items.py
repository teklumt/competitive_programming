class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)
        for i ,j in items1 + items2:
            store[i] += j
        res  = []
        for j in store:
            res.append([j, store[j]])
        return sorted(res)

        