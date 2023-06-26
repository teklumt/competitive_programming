class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        result.append(pref[0])
        num = pref[0]
        for n in range(1, len(pref)):
            dem = num ^ pref[n]
            result.append(dem)
            num = num ^ dem

        return result
