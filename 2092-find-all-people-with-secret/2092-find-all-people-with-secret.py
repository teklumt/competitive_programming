class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        res = set([0, firstPerson])
        
        store = {}
        for per1, per2 , time in meetings:
            if time not in store:
                store[time] = defaultdict(list)
            store[time][per1].append(per2)
            store[time][per2].append(per1)


        def dfs(node, graph):
            if node in seen:
                return
            seen.add(node)
            res.add(node)
            for i in graph:
                dfs(i, store[time][i])

        for time in sorted(store.keys()):
            seen = set()
            for From in store[time]:
                if From in res:
                    dfs(From, store[time][From])
            
        return res