class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        result = list(permutations(nums))
        for i in result:
            solutions.append(list(i))
        return solutions