class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        store=Counter(s)
        stack=[]
        seen=set()
        for i in s:
            store[i]-=1
            if i in seen:
                continue
            while stack and stack[-1]>i and store[stack[-1]]>0:
                removed=stack.pop()
                seen.remove(removed)
            stack.append(i)
            seen.add(i)
        return "".join(stack)