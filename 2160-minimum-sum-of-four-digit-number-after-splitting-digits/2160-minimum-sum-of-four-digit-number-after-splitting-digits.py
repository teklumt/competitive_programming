class Solution:
    def minimumSum(self, num: int) -> int:
        temp=num
        new=list(str(num))
        new.sort()
        i=new[0]+new[-1]
        j=new[1]+new[2]
        return int(i)+int(j)
