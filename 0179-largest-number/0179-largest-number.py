class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num = []
        for i in range(len(nums)):
            str_num.append(str(nums[i]))
        for i in range(len(str_num)-1):
            for j in range(i+1,len(str_num)):
                if int(str_num[i]+str_num[j])<int(str_num[j]+str_num[i]):
                    str_num[i],str_num[j]=str_num[j],str_num[i]
        return "0" if int("".join(str_num))==0 else "".join(str_num) 