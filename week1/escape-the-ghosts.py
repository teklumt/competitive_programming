class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        def distance_calc(arr1, arr2):
            
            return abs(arr1[0] - arr2[0]) + abs(arr1[1] - arr2[1])

        play_d = distance_calc([0, 0], target)

        for go in ghosts:
            
            go_D = distance_calc(go, target)
            if go_D <= play_d:
                return False
        return True