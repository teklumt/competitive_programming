class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, temp  = [], []

        def backtrack(open , close):
            if open == n and close == n:
                res.append("".join(temp.copy()))
                return
            
            if open < n:
                temp.append('(')
                backtrack(open + 1 ,close)
                temp.pop()

            if close < n and close < open:
                temp.append(')')
                backtrack(open ,close + 1)
                temp.pop()
        
        backtrack(0, 0)
        return res