class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        num = []
        result = list(permutations(nums))
        for i in result:
            if list(i) not in num:
                num.append(list(i))
        return num