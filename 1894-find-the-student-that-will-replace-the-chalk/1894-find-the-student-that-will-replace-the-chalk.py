class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ=sum(chalk)
        k=k-(k//summ)*summ
        for i in range(len(chalk)):
            if chalk[i]>k:
                return i
            else:
                k-=chalk[i]
        