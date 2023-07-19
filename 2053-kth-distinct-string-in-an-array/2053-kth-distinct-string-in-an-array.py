class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        nn = []
        for i in arr:
            if (i not in nn) and (arr.count(i) == 1):
                nn.append(i)
        return nn[k-1] if (k-1)<len(nn)else ""