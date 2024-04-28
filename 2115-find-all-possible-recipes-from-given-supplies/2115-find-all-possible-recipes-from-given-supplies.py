class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        res = []
        supp = set(supplies)
        reci = set(recipes)
        dead = set()
        countIndig = Counter()


        for i in range(len(ingredients)):
            
            for j  in ingredients[i]:
                if j not in supp and  j not in reci:
                    dead.add(recipes[i])

                if j in reci:
                    graph[j].append(recipes[i])
                    countIndig[recipes[i]] += 1

        queue = deque()
        for i in recipes:
            if i not in countIndig and i not in dead:
                queue.append(i)
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                countIndig[i] -= 1
                if countIndig[i] == 0 and i not in dead:
                    queue.append(i)      

        return res

            
        
        
        


