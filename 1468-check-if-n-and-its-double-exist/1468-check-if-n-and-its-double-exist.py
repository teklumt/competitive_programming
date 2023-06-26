class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        bol=False
        for n in range(len(arr)):
            for m in range(len(arr)):
                if m!=n:
                    if arr[n]==2*arr[m]:
                        bol=True
        return bol