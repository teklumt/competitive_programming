class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        summ = sum(arr[:k])
        minPossible = k * threshold
        
        left = 0
        count += 1 if summ >= minPossible else 0
        
        for i in range(k, len(arr)):
            summ = summ -  arr[left] + arr[i]
            left += 1
            if summ >= minPossible:
                count += 1
        return count
