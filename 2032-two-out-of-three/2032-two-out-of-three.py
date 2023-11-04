class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        num = list(set1.intersection(set2))+list(set1.intersection(set3))+list(set2.intersection(set3))+list(set1.intersection(set2,set3))
        return list(set(num))