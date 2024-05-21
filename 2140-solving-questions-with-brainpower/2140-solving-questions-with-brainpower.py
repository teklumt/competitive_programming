class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def func(i):
            if i >= len(questions):
                return 0
            
            if i not in memo:
                memo[i] = max(func(i + questions[i][1] + 1 ) + questions[i][0], func(i + 1))
            return memo[i]
        return func(0)