class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left="[{("
        right="]})"
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if right.index(i)!=left.index(stack.pop()):
                    return False
        return len(stack)==0