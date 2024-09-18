class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([(x , 0)])
        seen = set([x])
        while queue:
            n , opp  = queue.popleft()
            if n == y:return opp
            eleven = (n // 11)
            five = (n // 5)
            if n % 11 == 0 and eleven not in seen:
                queue.append((eleven, opp + 1))
                seen.add(eleven)
            if n % 5 == 0 and five not in seen:
                queue.append((five, opp + 1))
                seen.add(five)
            if (n + 1) not in seen:
                queue.append((n + 1, opp + 1))
                seen.add(n + 1)
            if (n - 1) not in seen:
                queue.append((n - 1, opp + 1))
                seen.add(n - 1)



