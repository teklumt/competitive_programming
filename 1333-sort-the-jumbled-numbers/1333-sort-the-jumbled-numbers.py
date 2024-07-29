class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):
            num = list(str(nums[i]))
            for j in range(len(num)):
                ind  = mapping[int(num[j])]
                num[j] = str(ind)
            res.append([int("".join(num)), i])
        res.sort()
        return [nums[j] for i, j in res]