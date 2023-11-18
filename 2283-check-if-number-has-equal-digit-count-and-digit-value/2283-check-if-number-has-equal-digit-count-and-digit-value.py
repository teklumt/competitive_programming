class Solution:
    def digitCount(self, num: str) -> bool:
        count=Counter(list(num))
        bo=True
        for i in range(len(num)):
            if count[str(i)]!=int(num[i]):
                bo=False
                break
        return bo