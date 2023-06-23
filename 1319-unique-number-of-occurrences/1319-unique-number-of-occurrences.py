class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = []
        bol = True
        for n in set(arr):
            if arr.count(n) not in result:
                result.append(arr.count(n))
            else:
                bol = False
                break
        return bol
