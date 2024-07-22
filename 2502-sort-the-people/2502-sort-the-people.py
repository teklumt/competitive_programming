class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        return [ j[1] for j in sorted([[heights[i],names[i]] for i in range(len(names))])[::-1]]

