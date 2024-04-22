class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1

        queue = deque([["0000", 0]])
        
        seen = set(deadends)

        while queue:
            currComb , count  = queue.popleft()

            if currComb == target:
                return count
            # if currComb in seen: continue
        
            nextComb = []
            for i in range(4):
                num = str((int(currComb[i]) + 1) % 10)
                num1 = currComb[:i] + num + currComb[i + 1:]
                nextComb.append(num1)
                
                num = str((int(currComb[i])  -  1) if int(currComb[i]) > 0 else 9)
                num2 = currComb[:i] + num + currComb[i + 1:]
                nextComb.append(num2)
            for comb in nextComb:
                if comb not in seen:
                    queue.append([comb, count + 1])
                    seen.add(comb)
        return -1

