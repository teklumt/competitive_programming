class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        seen = set()
        res = []
        notSeen = []
        for i in arr2:
            res += [i] * count[i]
            seen.add(i)
        for i in count:
            if i not in seen:
                notSeen += [i] * count[i]
        return res + sorted(notSeen)

