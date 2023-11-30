class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        num=sum(salary[1:-1])
        m=len(salary)-2
        return num/m