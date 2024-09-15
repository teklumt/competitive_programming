class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        seen = set([start])
        while stack:
            ind = stack.pop()
            if arr[ind] == 0:
                return True
            one, two = ind + arr[ind], ind - arr[ind]
            if one < len(arr) and one not in seen:
                seen.add(one)
                stack.append(one)
            if two >= 0 and two not in seen:
                seen.add(two)
                stack.append(two)

        return False