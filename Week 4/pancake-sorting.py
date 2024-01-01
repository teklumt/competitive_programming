class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n):
            maxx = max(arr[:n-i])
            maxx_ind = arr.index(maxx)+1
            arr[:maxx_ind] = reversed(arr[:maxx_ind])
            result.append(maxx_ind)

            arr[:n-i] = reversed(arr[:n-i])
            result.append(n-i)
        return result
