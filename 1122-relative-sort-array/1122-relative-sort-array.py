class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        store = {}
        res = []
        num = []
        for i in arr1:
            if i not in arr2:
                num.append(i)
        for i in arr1:
            store[i] = store.get(i, 0)+1
        for i in arr2:
            res += [i]*store[i]
        num.sort()
        res += num
        return res