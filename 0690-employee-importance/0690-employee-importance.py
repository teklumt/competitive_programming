"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {emp.id :[emp.importance, emp.subordinates] for emp in employees }

        stack = graph[id][-1]
        res = graph[id][0]
  

        seen = set()
        while stack:
            currId = stack.pop()
            if currId not in seen:
                res += graph[currId][0]

            for i in graph[currId][-1]:
                
                if i not in seen:
                    res += graph[i][0]
                    seen.add(i)
                    stack+=graph[i][-1]
        return res



     