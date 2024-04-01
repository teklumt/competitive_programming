class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        for i in s:
            stack.append(i)
            if stack and stack[-len(part):] == part:
                stack = stack[:-len(part)]
        return "".join(stack)