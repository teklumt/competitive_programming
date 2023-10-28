class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num=[]
        for i in nums:
            str_num.append(str(i))
        def compre(num1 , num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1
        str_num=sorted(str_num,key=functools.cmp_to_key(compre));

        return str(int("".join(str_num))) 
    