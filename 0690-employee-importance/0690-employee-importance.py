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
        mydict = {employee.id: employee for employee in employees}
        def dfs(employee):
            res=mydict[employee].importance
            for i in mydict[employee].subordinates:
                res+=dfs(i)
            return res
        return dfs(id)