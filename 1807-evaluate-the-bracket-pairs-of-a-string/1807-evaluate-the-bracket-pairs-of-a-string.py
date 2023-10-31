class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        stack = ""
        i = 0
        store = {}
        for j in knowledge:
            store[j[0]] = j[1]
        while i < len(s):
            if s[i] != '(':
                stack += s[i]
            else:
                check = ""
                i += 1
                while s[i] != ')':
                    check += s[i]
                    i += 1
                if check in store:
                    stack += store[check]
                else:
                    stack += '?'
            i += 1
        return stack