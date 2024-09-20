class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count  = Counter(arr)
        arr.sort(key=lambda x:abs(x))
        # print(count, arr)
        for i in range(len(arr)):
            if count[arr[i]]:
                if count[2 * arr[i]]:
                    count[2 * arr[i]] -= 1
                    count[arr[i]] -= 1
                else:
                    return False
        return True
            