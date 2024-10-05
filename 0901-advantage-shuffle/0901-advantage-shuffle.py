class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        temp = [(nums2[i], i) for i in range(len(nums2))]
        temp.sort()

        left = len(nums1) - 1
        mapp = {}
        for m in range(len(temp) - 1, -1, -1):
            val, i = temp[m]
            if val < nums1[left]:
                mapp[i] = nums1[left]
                left -= 1
        res = [-1] * len(nums1)
        for i in mapp:
            res[i] = mapp[i]
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = nums1[left]
                left -= 1
        return res 