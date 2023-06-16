class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hum = list(set(nums1) & set(nums2))
        n = len(nums1)
        m = len(nums2)
        if n > m:
            for j in hum:
                k = min(nums2.count(j), nums1.count(j))
                result += [j]*k
        else:
            for j in hum:
                k = min(nums2.count(j), nums1.count(j))
                result += [j]*k
        return result