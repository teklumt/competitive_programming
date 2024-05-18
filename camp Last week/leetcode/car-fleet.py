class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(store)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)